# -*- coding: utf-8 -*-
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.contrib.humanize.templatetags.humanize import ordinal
from django.contrib.auth.decorators import login_required
from django.db.models import Count, F
from django.core.cache import cache

from common.decorators import render_to
from common.pagination import paginate

from bill.models import Bill, BillType, BillStatus, BillTerm, TermType
from bill.search import bill_search_manager, parse_bill_number
from bill.title import get_secondary_bill_title
from committee.util import sort_members
from person.models import Person
from events.models import Feed

from settings import CURRENT_CONGRESS

from us import get_congress_dates

import urllib, urllib2, json, datetime, os.path
from registration.helpers import json_response

@render_to('bill/bill_details.html')
def bill_details(request, congress, type_slug, number):
    if type_slug.isdigit():
        bill_type = type_slug
    else:
        try:
            bill_type = BillType.by_slug(type_slug)
        except BillType.NotFound:
            raise Http404("Invalid bill type: " + type_slug)
    
    bill = get_object_or_404(Bill, congress=congress, bill_type=bill_type, number=number)
    
    def get_reintroductions():
        reintro_prev = None
        reintro_next = None
        for reintro in bill.find_reintroductions():
            if reintro.congress < bill.congress: reintro_prev = reintro
            if reintro.congress > bill.congress and not reintro_next: reintro_next = reintro
        return reintro_prev, reintro_next
        
    def get_market():
        m = bill.get_open_market(request.user)
        if m: m.name = m.name.replace(bill.display_number, "it")
        return m
        
    return {
        'bill': bill,
        "congressdates": get_congress_dates(bill.congress),
        "subtitle": get_secondary_bill_title(bill, bill.titles),
        "reintros": get_reintroductions, # defer so we can use template caching
        "market": get_market,
        "current": bill.congress == CURRENT_CONGRESS,
        "dead": bill.congress != CURRENT_CONGRESS and bill.current_status not in BillStatus.final_status_obvious,
        'feed': Feed.BillFeed(bill),
    }

@json_response
@login_required
def market_test_vote(request):
    bill = get_object_or_404(Bill, id = request.POST.get("bill", "0"))
    prediction = int(request.POST.get("prediction", "0"))
    market = bill.get_open_market(request.user)
    if not market: return { }
    
    from predictionmarket.models import Trade, TradingAccount
    account = TradingAccount.get(request.user)
    if prediction != 0:
        # Buy shares in one of the outcomes.
        try:
            t = Trade.place(account, market.outcomes.get(owner_key = 1 if prediction == 1 else 0), 10)
        except ValueError as e:
            return { "error": str(e) }
            
    else:
        # Sell shares.
        positions, pl = account.position_in_market(market)
        for outcome in positions:
            Trade.place(account, outcome, -positions[outcome]["shares"])
    
    return { "vote": prediction }

@render_to('bill/bill_text.html')
def bill_text(request, congress, type_slug, number, version=None):
    if version == "":
        version = None
    
    try:
        bill_type = BillType.by_slug(type_slug)
    except BillType.NotFound:
        raise Http404("Invalid bill type: " + type_slug)
    bill = get_object_or_404(Bill, congress=congress, bill_type=bill_type, number=number)
    
    from billtext import load_bill_text, bill_gpo_status_codes
    try:
        textdata = load_bill_text(bill, version)
    except IOError:
        textdata = None

    # Get a list of the alternate versions of this bill.
    alternates = None
    if textdata:
        alternates = []
        for v in bill_gpo_status_codes:
            fn = "data/us/bills.text/%s/%s/%s%d%s.mods.xml" % (bill.congress, BillType.by_value(bill.bill_type).xml_code, BillType.by_value(bill.bill_type).xml_code, bill.number, v)
            if os.path.exists(fn):
                alternates.append(load_bill_text(bill, v, mods_only=True))
        alternates.sort(key = lambda mods : mods["docdate"])

    return {
        'bill': bill,
        "congressdates": get_congress_dates(bill.congress),
        "textdata": textdata,
        "version": version,
        "alternates": alternates,
        "related_bills": list(bill.find_reintroductions()) + [r.related_bill for r in bill.get_related_bills()],
    }

@json_response
def bill_text_ajax(request):
    for p in ("left_bill", "left_version", "right_bill", "right_version", "mode"):
        if not p in request.GET:
            raise Http404()
    
    from billtext import load_bill_text, compare_xml_text
    import lxml
    
    left_bill = Bill.objects.get(id = request.GET["left_bill"])
    left = load_bill_text(left_bill, request.GET["left_version"], mods_only=True)
    
    right_bill = Bill.objects.get(id = request.GET["right_bill"])
    right = load_bill_text(right_bill, request.GET["right_version"], mods_only=True)
    
    doc1 = lxml.etree.parse(left["basename"] + ".html")
    doc2 = lxml.etree.parse(right["basename"] + ".html")
    compare_xml_text(doc1, doc2) # revises DOMs in-place
    
    # dates aren't JSON serializable
    left["docdate"] = left["docdate"].strftime("%x")
    right["docdate"] = right["docdate"].strftime("%x")
    
    return {
        "left_meta": left,
        "right_meta": right,
        "left_text": lxml.etree.tostring(doc1),
        "right_text": lxml.etree.tostring(doc2),
    }

def bill_list(request):
    if request.POST.get("allow_redirect", "") == "true":
        bill = parse_bill_number(request.POST.get("text", ""), congress=request.POST.get("congress", ""))
        if bill:
            @json_response
            def get_redirect_response():
                return { "redirect": bill.get_absolute_url() }
            return get_redirect_response()
    
    ix1 = None
    ix2 = None
    if "subject" in request.GET:
        ix = BillTerm.objects.get(id=request.GET["subject"])
        if ix.parents.all().count() == 0:
            ix1 = ix
        else:
            ix1 = ix.parents.all()[0]
            ix2 = ix
    return show_bill_browse("bill/bill_list.html", request, ix1, ix2, { })

def show_bill_browse(template, request, ix1, ix2, context):
    return bill_search_manager().view(request, template,
        defaults={
            "congress": request.GET["congress"] if "congress" in request.GET else (CURRENT_CONGRESS if "sponsor" not in request.GET else Person.objects.get(id=request.GET["sponsor"]).most_recent_role_congress()),
            "sponsor": request.GET.get("sponsor", None),
            "terms": ix1.id if ix1 else None,
            "terms2": ix2.id if ix2 else None,
            "text": request.GET.get("text", None),
            "current_status": request.GET.get("status").split(",") if "status" in request.GET else None,
            "sort": request.GET.get("sort", None),
        },
        noun = ("bill", "bills"),
        context = context,
        )
 
def query_popvox(method, args):
    if isinstance(method, (list, tuple)):
        method = "/".join(method)
    
    _args = { }
    if args != None: _args.update(args)
    _args["api_key"] = settings.POPVOX_API_KEY
    
    url = "https://www.popvox.com/api/" + method + "?" + urllib.urlencode(_args).encode("utf8")
    
    req = urllib2.Request(url)
    resp = urllib2.urlopen(req)
    if resp.getcode() != 200:
        raise Exception("Failed to load page: " + url)
    ret = resp.read()
    encoding = resp.info().getparam("charset")
    ret = ret.decode(encoding)
    return json.loads(ret)

subject_choices_data = None
def subject_choices(include_legacy=True):
    global subject_choices_data
    if subject_choices_data == None:
        subject_choices_data = { }
        for t in BillTerm.objects.filter(term_type=TermType.new).exclude(parents__id__gt=0):
            x = []
            subject_choices_data[t] = x
            for tt in t.subterms.all():
                x.append(tt)
        subject_choices_data = sorted(subject_choices_data.items(), key = lambda x : x[0].name)
    return subject_choices_data

@render_to('bill/bill_docket.html')
def bill_docket(request):
    def build_info():
        groups0 = [
            ("Enacted Laws", "enacted bills and joint resolutions", " so far in this session of Congress",
                BillStatus.final_status_passed_bill), # 2
            ("Passed Resolutions", "passed resolutions", " so far in this session of Congress (for joint and concurrent resolutions, passed both chambers)",
                BillStatus.final_status_passed_resolution), # 3
            ("At the President", "bills", " that are awaiting the president's signature",
                (BillStatus.passed_bill,)), # 1
            ("Active Legislation", "bills and joint/concurrent resolutions", " that had a significant vote in one chamber and are likely to get a vote in the other chamber",
                (BillStatus.pass_over_house, BillStatus.pass_over_senate, BillStatus.pass_back_senate, BillStatus.pass_back_house)), # 4
            ("Inactive Legislation", "bills and resolutions", " that have been introduced, referred to committee, or reported by committee and await further action",
                (BillStatus.introduced, BillStatus.referred, BillStatus.reported)), # 3
            ("Failed Legislation", "bills and resolutions", " that failed a vote on passage and are now dead or failed a significant vote such as cloture, passage under suspension, or resolving differences", 
                (BillStatus.fail_originating_house, BillStatus.fail_originating_senate, BillStatus.fail_second_house, BillStatus.fail_second_senate, BillStatus.prov_kill_suspensionfailed, BillStatus.prov_kill_cloturefailed, BillStatus.prov_kill_pingpongfail)), # 7
            ("Vetoed Bills", "bills", " that were vetoed and the veto was not overridden by Congress",
                (BillStatus.prov_kill_veto, BillStatus.override_pass_over_house, BillStatus.override_pass_over_senate, BillStatus.vetoed_pocket, BillStatus.vetoed_override_fail_originating_house, BillStatus.vetoed_override_fail_originating_senate, BillStatus.vetoed_override_fail_second_house, BillStatus.vetoed_override_fail_second_senate)), # 8

        ]
        
        def loadgroupqs(statuses, congress=CURRENT_CONGRESS):
            return Bill.objects.filter(congress=congress, current_status__in=statuses)
        
        groups = [
            (   g[0], # title
                g[1], # text 1
                g[2], # text 2
                "/congress/bills/browse?status=" + ",".join(str(s) for s in g[3]), # link
               loadgroupqs(g[3]).count(), # count in category
               loadgroupqs(g[3]).order_by('-current_status_date')[0:6], # top 6 in this category
                )
            for g in groups0 ]
            
        dhg_bills = Bill.objects.filter(congress=CURRENT_CONGRESS, docs_house_gov_postdate__gt=datetime.datetime.now() - datetime.timedelta(days=10)).filter(docs_house_gov_postdate__gt=F('current_status_date'))
        sfs_bills = Bill.objects.filter(congress=CURRENT_CONGRESS, senate_floor_schedule_postdate__gt=datetime.datetime.now() - datetime.timedelta(days=5)).filter(senate_floor_schedule_postdate__gt=F('current_status_date'))
        coming_up = list(dhg_bills | sfs_bills)
        coming_up.sort(key = lambda b : b.docs_house_gov_postdate if (b.docs_house_gov_postdate and (not b.senate_floor_schedule_postdate or b.senate_floor_schedule_postdate < b.docs_house_gov_postdate)) else b.senate_floor_schedule_postdate, reverse=True)
        
        start, end = get_congress_dates(CURRENT_CONGRESS)
        end_year = end.year if end.month > 1 else end.year-1 # count January finishes as the prev year
        current_congress_years = '%d-%d' % (start.year, end.year)
        current_congress = ordinal(CURRENT_CONGRESS)
        
        # Get the count of bills by status and by Congress.
        counts_by_congress = []
        for c in xrange(96, CURRENT_CONGRESS+1):
            total = Bill.objects.filter(congress=c).count()
            counts_by_congress.append({
                "congress": c,
                "dates": get_congress_dates(c),
                "counts": [ ],
                "total": total,
            })
            for g in groups0:
                t = loadgroupqs(g[3], congress=c).count()
                counts_by_congress[-1]["counts"].append(
                    { "count": t,
                      "percent": "%0.0f" % float(100.0*t/total),
                      "link": "/congress/bills/browse?congress=%s&status=%s" % (c, ",".join(str(s) for s in g[3])),
                      } )
        counts_by_congress.reverse()
        
        # When does activity occur within the session cycle?
        from django.db import connection
        cursor = connection.cursor()
        def pull_time_stat(field, where, historical=True):
            cursor.execute("SELECT YEAR(%s) - congress*2 - 1787, MONTH(%s), COUNT(*) FROM bill_bill WHERE congress>=96 AND congress%s%d AND %s GROUP BY YEAR(%s) - congress*2, MONTH(%s)" % (field, field, "<" if historical else "=", CURRENT_CONGRESS, where, field, field))
            activity = [{ "x": r[0]*12 + (r[1]-1), "count": r[2], "year": r[0] } for r in cursor.fetchall()]
            total = sum(m["count"] for m in activity)
            for i, m in enumerate(activity): m["cumulative_count"] = m["count"]/float(total) + (0.0 if i==0 else activity[i-1]["cumulative_count"])
            for m in activity: m["count"] = round(m["count"] / (CURRENT_CONGRESS-96), 1)
            for m in activity: m["cumulative_count"] = round(m["cumulative_count"] * 100.0)
            return activity
        activity_introduced_by_month = pull_time_stat('introduced_date', "1")
        activity_enacted_by_month = pull_time_stat('current_status_date', "current_status IN (%d,%d)" % (int(BillStatus.enacted_signed), int(BillStatus.enacted_veto_override)))
    
        return {
            "total": Bill.objects.filter(congress=CURRENT_CONGRESS).count(),
            "current_congress_years": current_congress_years,
            "current_congress": current_congress,
            "groups": groups,
            "coming_up": coming_up,
            "subjects": subject_choices(),
            "BILL_STATUS_INTRO": (BillStatus.introduced, BillStatus.referred, BillStatus.reported),
            
            "groups2": groups0,
            "counts_by_congress": counts_by_congress,
            
            "activity": (("Bills and Resolutions Introduced", activity_introduced_by_month),
             ("Bills and Joint Resolutions Enacted", activity_enacted_by_month) )
        }
        
    ret = cache.get("bill_docket_info")    
    if not ret:
        ret = build_info()
        cache.set("bill_docket_info", ret, 60*60)
    
    return ret
    
def subject(request, sluggedname, termid):
    ix = BillTerm.objects.get(id=termid)
    if ix.parents.all().count() == 0:
        ix1 = ix
        ix2 = None
    else:
        ix1 = ix.parents.all()[0]
        ix2 = ix
    return show_bill_browse("bill/subject.html", request, ix1, ix2, { "term": ix, "feed": Feed.IssueFeed(ix) })
    
import django.contrib.sitemaps
class sitemap_current(django.contrib.sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 1.0
    def items(self):
        return Bill.objects.filter(congress=CURRENT_CONGRESS)
class sitemap_previous(django.contrib.sitemaps.Sitemap):
    changefreq = "yearly"
    priority = 0.25
    def items(self):
        return Bill.objects.filter(congress=CURRENT_CONGRESS-1)
class sitemap_archive(django.contrib.sitemaps.Sitemap):
    changefreq = "yearly"
    priority = 0.25
    def items(self):
        return Bill.objects.filter(congress__lt=CURRENT_CONGRESS-1)

