# this file was automatically generated by prognosis.py
congress = 111
pop_title_prefixes = [u'A bill to extend the temporary suspension of duty',
 u'To amend the Internal Revenue Code of 1986 to',
 u'A bill to suspend temporarily the duty on certain',
 u'Expressing the sense of the House of Representatives that',
 u'To designate the facility of the United States Postal',
 u'Providing for consideration of the bill (H.R.',
 u'A bill to amend the Internal Revenue Code of',
 u'For the relief of',
 u'A resolution recognizing the',
 u'To amend title 38, United States Code, to',
 u'A bill to extend temporarily the suspension of duty',
 u'Supporting the goals and ideals of National',
 u'To direct the Secretary of',
 u'Expressing the sense of Congress that',
 u'To suspend temporarily the duty on',
 u'Reserved for the Speaker.',
 u'Proposing an amendment to the Constitution of the United',
 u'Expressing support for the',
 u'A bill for the relief of',
 u'Amending the Rules of the House of Representatives to',
 u'To provide for the',
 u'To amend title 10, United States Code, to',
 u'A resolution supporting the goals and ideals of',
 u'A bill to provide for the',
 u'A resolution congratulating the',
 u'Expressing support for designation of the',
 u'A resolution honoring the',
 u'A resolution expressing support for',
 u'To authorize the Secretary of',
 u'A resolution expressing the sense of the Senate that',
 u'A bill to authorize',
 u'A resolution designating the week',
 u'A bill to require the',
 u'A bill to amend title 38, United States Code,',
 u'A resolution commemorating the',
 u'A bill to designate the',
 u'A bill to extend and',
 u'Expressing the sense of the Congress',
 u'A bill to reduce temporarily the',
 u'Providing for consideration of the Senate']
factors = {(1, False): {'count': 931,
              'factors': {'cosponsor_chair': {'count': 139,
                                              'regression_beta': 0.47766329911543881,
                                              'success_rate': 98.56115107913669},
                          'cosponsor_committeemember_3-5': {'count': 142,
                                                            'regression_beta': 0.17301584501754039,
                                                            'success_rate': 98.59154929577464},
                          'cosponsor_leader_majority': {'count': 337,
                                                        'regression_beta': -0.20155053957660046,
                                                        'success_rate': 98.81305637982196},
                          'cosponsor_leader_minority': {'count': 253,
                                                        'regression_beta': -0.10184855782016052,
                                                        'success_rate': 98.02371541501977},
                          'cosponsors_crosspartisan': {'count': 500,
                                                       'regression_beta': 3.6611333921241331,
                                                       'success_rate': 99.4},
                          'sponsor_committee_rankingmember': {'count': 24,
                                                              'regression_beta': -3.0642982140933888,
                                                              'success_rate': 58.333333333333336},
                          'sponsor_majority': {'count': 666,
                                               'regression_beta': 1.5710652623241372,
                                               'success_rate': 97.74774774774775},
                          'sponsor_minority': {'count': 265,
                                               'regression_beta': -0.1026987861920185,
                                               'success_rate': 90.56603773584905},
                          u'startswith:Expressing support for designation of the': {'count': 16,
                                                                                    'regression_beta': 32.258821310483441,
                                                                                    'success_rate': 100.0},
                          u'startswith:Expressing support for the': {'count': 17,
                                                                     'regression_beta': 32.765547678952672,
                                                                     'success_rate': 100.0},
                          u'startswith:Providing for consideration of the Senate': {'count': 24,
                                                                                    'regression_beta': 34.167059371491398,
                                                                                    'success_rate': 100.0}},
              'regression_beta': [1.4707073328632727,
                                  0.17301584501754039,
                                  -3.0642982140933888,
                                  -0.10184855782016052,
                                  1.5710652623241372,
                                  34.167059371491398,
                                  -0.20155053957660046,
                                  -0.1026987861920185,
                                  0.47766329911543881,
                                  3.6611333921241331,
                                  32.765547678952672,
                                  32.258821310483441],
              'regression_predictors_map': {'cosponsor_chair': 7,
                                            'cosponsor_committeemember_3-5': 0,
                                            'cosponsor_leader_majority': 5,
                                            'cosponsor_leader_minority': 2,
                                            'cosponsors_crosspartisan': 8,
                                            'sponsor_committee_rankingmember': 1,
                                            'sponsor_majority': 3,
                                            'sponsor_minority': 6,
                                            u'startswith:Expressing support for designation of the': 10,
                                            u'startswith:Expressing support for the': 9,
                                            u'startswith:Providing for consideration of the Senate': 4},
              'success_name': 'agreed to',
              'success_rate': 95.70354457572503},
 (1, True): {'count': 1784,
             'factors': {'cosponsor_chair': {'count': 178,
                                             'regression_beta': 0.91622705794005743,
                                             'success_rate': 76.96629213483146},
                         'cosponsor_leader_majority': {'count': 525,
                                                       'regression_beta': 0.28934241472917538,
                                                       'success_rate': 63.42857142857143},
                         'cosponsor_leader_minority': {'count': 388,
                                                       'regression_beta': 0.53553312734378478,
                                                       'success_rate': 63.91752577319588},
                         'cosponsor_rankingmember': {'count': 217,
                                                     'regression_beta': 0.19093747552721249,
                                                     'success_rate': 64.97695852534562},
                         'cosponsors_crosspartisan': {'count': 812,
                                                      'regression_beta': 0.89381109874990539,
                                                      'success_rate': 61.206896551724135},
                         'sponsor_committee_chair': {'count': 56,
                                                     'regression_beta': 1.8359719093863394,
                                                     'success_rate': 83.92857142857143},
                         'sponsor_committee_member_majority': {'count': 373,
                                                               'regression_beta': 0.81693859083819731,
                                                               'success_rate': 69.97319034852546},
                         'sponsor_majority': {'count': 1171,
                                              'regression_beta': -0.25350455935888283,
                                              'success_rate': 55.5935098206661},
                         'sponsor_minority': {'count': 613,
                                              'regression_beta': -0.43867662783703654,
                                              'success_rate': 39.151712887438826},
                         u'startswith:Amending the Rules of the House of Representatives to': {'count': 40,
                                                                                               'regression_beta': -2.9148950437005952,
                                                                                               'success_rate': 2.5},
                         u'startswith:Expressing the sense of the House of Representatives that': {'count': 110,
                                                                                                   'regression_beta': -1.6882374833900649,
                                                                                                   'success_rate': 16.363636363636363},
                         u'startswith:Providing for consideration of the Senate': {'count': 24,
                                                                                   'regression_beta': 34.097012377682944,
                                                                                   'success_rate': 100.0},
                         u'startswith:Providing for consideration of the bill (H.R.': {'count': 88,
                                                                                       'regression_beta': 3.405267005039752,
                                                                                       'success_rate': 96.5909090909091}},
             'regression_beta': [-0.6322462704536681,
                                 1.8359719093863394,
                                 -0.25350455935888283,
                                 34.097012377682944,
                                 -2.9148950437005952,
                                 0.28934241472917538,
                                 -0.43867662783703654,
                                 3.405267005039752,
                                 -1.6882374833900649,
                                 0.91622705794005743,
                                 0.89381109874990539,
                                 0.81693859083819731,
                                 0.53553312734378478,
                                 0.19093747552721249],
             'regression_predictors_map': {'cosponsor_chair': 8,
                                           'cosponsor_leader_majority': 4,
                                           'cosponsor_leader_minority': 11,
                                           'cosponsor_rankingmember': 12,
                                           'cosponsors_crosspartisan': 9,
                                           'sponsor_committee_chair': 0,
                                           'sponsor_committee_member_majority': 10,
                                           'sponsor_majority': 1,
                                           'sponsor_minority': 5,
                                           u'startswith:Amending the Rules of the House of Representatives to': 3,
                                           u'startswith:Expressing the sense of the House of Representatives that': 7,
                                           u'startswith:Providing for consideration of the Senate': 2,
                                           u'startswith:Providing for consideration of the bill (H.R.': 6},
             'success_name': 'agreed to',
             'success_rate': 49.94394618834081},
 (2, False): {'count': 523,
              'factors': {'reintroduced': {'count': 106,
                                           'regression_beta': -0.8007186030458443,
                                           'success_rate': 12.264150943396226}},
              'regression_beta': [-1.1669315326455869, -0.8007186030458443],
              'regression_predictors_map': {'reintroduced': 0},
              'success_name': 'enacted',
              'success_rate': 21.414913957934992},
 (2, True): {'count': 4059,
             'factors': {'cosponsor_chair': {'count': 202,
                                             'regression_beta': 0.94298112361446917,
                                             'success_rate': 9.405940594059405},
                         'cosponsor_committeemember_3-5': {'count': 425,
                                                           'regression_beta': -0.15279349842961057,
                                                           'success_rate': 4.705882352941177},
                         'cosponsor_leader_majority': {'count': 68,
                                                       'regression_beta': 0.26004541279893922,
                                                       'success_rate': 7.352941176470588},
                         'cosponsor_rankingmember': {'count': 165,
                                                     'regression_beta': 1.0684475831530904,
                                                     'success_rate': 13.333333333333334},
                         'cosponsors_bipartisan': {'count': 162,
                                                   'regression_beta': 0.72645162635488869,
                                                   'success_rate': 6.790123456790123},
                         'cosponsors_crosspartisan': {'count': 942,
                                                      'regression_beta': 0.70199668023832462,
                                                      'success_rate': 5.201698513800425},
                         'sponsor_committee_chair': {'count': 273,
                                                     'regression_beta': 0.67416061825066842,
                                                     'success_rate': 7.6923076923076925},
                         'sponsor_leader_majority': {'count': 116,
                                                     'regression_beta': 0.42405511342156443,
                                                     'success_rate': 6.0344827586206895},
                         'sponsor_minority': {'count': 1108,
                                              'regression_beta': -0.6847286796404537,
                                              'success_rate': 1.1732851985559567},
                         u'startswith:A bill to authorize': {'count': 30,
                                                             'regression_beta': 1.6151195478497253,
                                                             'success_rate': 10.0},
                         u'startswith:A bill to designate the': {'count': 25,
                                                                 'regression_beta': 2.7564180535787752,
                                                                 'success_rate': 24.0},
                         u'startswith:A bill to extend the temporary suspension of duty': {'count': 250,
                                                                                           'regression_beta': -34.06190486156629,
                                                                                           'success_rate': 0.0},
                         u'startswith:A bill to suspend temporarily the duty on certain': {'count': 150,
                                                                                           'regression_beta': -32.895885094235901,
                                                                                           'success_rate': 0.0}},
             'regression_beta': [-3.9934475371211056,
                                 0.67416061825066842,
                                 -32.895885094235901,
                                 2.7564180535787752,
                                 -0.15279349842961057,
                                 0.26004541279893922,
                                 -0.6847286796404537,
                                 -34.06190486156629,
                                 1.6151195478497253,
                                 0.42405511342156443,
                                 0.94298112361446917,
                                 0.72645162635488869,
                                 0.70199668023832462,
                                 1.0684475831530904],
             'regression_predictors_map': {'cosponsor_chair': 9,
                                           'cosponsor_committeemember_3-5': 3,
                                           'cosponsor_leader_majority': 4,
                                           'cosponsor_rankingmember': 12,
                                           'cosponsors_bipartisan': 10,
                                           'cosponsors_crosspartisan': 11,
                                           'sponsor_committee_chair': 0,
                                           'sponsor_leader_majority': 8,
                                           'sponsor_minority': 5,
                                           u'startswith:A bill to authorize': 7,
                                           u'startswith:A bill to designate the': 2,
                                           u'startswith:A bill to extend the temporary suspension of duty': 6,
                                           u'startswith:A bill to suspend temporarily the duty on certain': 1},
             'success_name': 'enacted',
             'success_rate': 2.75930032027593},
 (3, False): {'count': 867,
              'factors': {'cosponsor_leader_minority': {'count': 122,
                                                        'regression_beta': 0.37673231368291943,
                                                        'success_rate': 37.704918032786885},
                          'cosponsors_bipartisan': {'count': 72,
                                                    'regression_beta': 0.67260273023092298,
                                                    'success_rate': 55.55555555555556},
                          'reintroduced': {'count': 203,
                                           'regression_beta': -1.092855020110167,
                                           'success_rate': 14.77832512315271},
                          u'startswith:To designate the facility of the United States Postal': {'count': 75,
                                                                                                'regression_beta': 2.5004574515221685,
                                                                                                'success_rate': 82.66666666666667}},
              'regression_beta': [-1.0246571231935162,
                                  -1.092855020110167,
                                  0.37673231368291943,
                                  2.5004574515221685,
                                  0.67260273023092298],
              'regression_predictors_map': {'cosponsor_leader_minority': 1,
                                            'cosponsors_bipartisan': 3,
                                            'reintroduced': 0,
                                            u'startswith:To designate the facility of the United States Postal': 2},
              'success_name': 'enacted',
              'success_rate': 29.296424452133795},
 (3, True): {'count': 6570,
             'factors': {'cosponsor_chair': {'count': 477,
                                             'regression_beta': 1.4485847439302257,
                                             'success_rate': 11.949685534591195},
                         'cosponsor_committeemember_3-5': {'count': 907,
                                                           'regression_beta': 0.071617147484627719,
                                                           'success_rate': 5.843439911797134},
                         'cosponsor_leader_minority': {'count': 696,
                                                       'regression_beta': 0.265872196665004,
                                                       'success_rate': 6.609195402298851},
                         'cosponsor_rankingmember': {'count': 363,
                                                     'regression_beta': 0.78016654720144185,
                                                     'success_rate': 12.947658402203857},
                         'cosponsors_bipartisan': {'count': 328,
                                                   'regression_beta': 0.64577900031963109,
                                                   'success_rate': 12.195121951219512},
                         'cosponsors_crosspartisan': {'count': 1993,
                                                      'regression_beta': 0.32575037701799248,
                                                      'success_rate': 5.4189663823381835},
                         'reintroduced': {'count': 1811,
                                          'regression_beta': -1.060026856452579,
                                          'success_rate': 1.6565433462175594},
                         'sponsor_committee_chair': {'count': 254,
                                                     'regression_beta': 2.089795981060905,
                                                     'success_rate': 20.078740157480315},
                         'sponsor_majority': {'count': 4616,
                                              'regression_beta': -1.0903142343700745,
                                              'success_rate': 4.614384748700173},
                         'sponsor_minority': {'count': 1954,
                                              'regression_beta': -1.6934178905264767,
                                              'success_rate': 2.0982599795291708},
                         u'startswith:To amend the Internal Revenue Code of 1986 to': {'count': 236,
                                                                                       'regression_beta': -33.462582343317258,
                                                                                       'success_rate': 0.0},
                         u'startswith:To designate the facility of the United States Postal': {'count': 101,
                                                                                               'regression_beta': 4.186748107917702,
                                                                                               'success_rate': 61.386138613861384}},
             'regression_beta': [-2.7799570246307903,
                                 2.089795981060905,
                                 -1.0903142343700745,
                                 -33.462582343317258,
                                 0.071617147484627719,
                                 -1.6934178905264767,
                                 -1.060026856452579,
                                 1.4485847439302257,
                                 0.64577900031963109,
                                 0.32575037701799248,
                                 4.186748107917702,
                                 0.265872196665004,
                                 0.78016654720144185],
             'regression_predictors_map': {'cosponsor_chair': 6,
                                           'cosponsor_committeemember_3-5': 3,
                                           'cosponsor_leader_minority': 10,
                                           'cosponsor_rankingmember': 11,
                                           'cosponsors_bipartisan': 7,
                                           'cosponsors_crosspartisan': 8,
                                           'reintroduced': 5,
                                           'sponsor_committee_chair': 0,
                                           'sponsor_majority': 1,
                                           'sponsor_minority': 4,
                                           u'startswith:To amend the Internal Revenue Code of 1986 to': 2,
                                           u'startswith:To designate the facility of the United States Postal': 9},
             'success_name': 'enacted',
             'success_rate': 3.8660578386605784},
 (4, False): {'count': 499,
              'factors': {'cosponsor_chair': {'count': 23,
                                              'regression_beta': -37.207764117692371,
                                              'success_rate': 86.95652173913044},
                          'cosponsor_leader_majority': {'count': 32,
                                                        'regression_beta': 36.342066313720352,
                                                        'success_rate': 100.0},
                          'cosponsor_rankingmember': {'count': 20,
                                                      'regression_beta': 74.681352696352405,
                                                      'success_rate': 100.0},
                          'cosponsors_bipartisan': {'count': 62,
                                                    'regression_beta': 35.919064516585095,
                                                    'success_rate': 100.0},
                          'reintroduced': {'count': 24,
                                           'regression_beta': 35.968182929971938,
                                           'success_rate': 100.0},
                          'sponsor_committee_chair': {'count': 10,
                                                      'regression_beta': -75.411739927695251,
                                                      'success_rate': 60.0},
                          'sponsor_leader_majority': {'count': 59,
                                                      'regression_beta': 0.71396219101476999,
                                                      'success_rate': 100.0},
                          u'startswith:A resolution congratulating the': {'count': 21,
                                                                          'regression_beta': 0.18414450468269122,
                                                                          'success_rate': 100.0},
                          u'startswith:A resolution designating the week': {'count': 28,
                                                                            'regression_beta': 0.93271251450299664,
                                                                            'success_rate': 100.0},
                          u'startswith:A resolution expressing support for': {'count': 26,
                                                                              'regression_beta': 0.84329896349804134,
                                                                              'success_rate': 100.0},
                          u'startswith:A resolution honoring the': {'count': 24,
                                                                    'regression_beta': 0.12100634407223858,
                                                                    'success_rate': 100.0},
                          u'startswith:A resolution recognizing the': {'count': 39,
                                                                       'regression_beta': 36.564714246397955,
                                                                       'success_rate': 100.0}},
              'regression_beta': [37.718589741458359,
                                  0.93271251450299664,
                                  36.564714246397955,
                                  36.342066313720352,
                                  -75.411739927695251,
                                  35.968182929971938,
                                  0.71396219101476999,
                                  -37.207764117692371,
                                  35.919064516585095,
                                  0.12100634407223858,
                                  0.84329896349804134,
                                  0.18414450468269122,
                                  74.681352696352405],
              'regression_predictors_map': {'cosponsor_chair': 6,
                                            'cosponsor_leader_majority': 2,
                                            'cosponsor_rankingmember': 11,
                                            'cosponsors_bipartisan': 7,
                                            'reintroduced': 4,
                                            'sponsor_committee_chair': 3,
                                            'sponsor_leader_majority': 5,
                                            u'startswith:A resolution congratulating the': 10,
                                            u'startswith:A resolution designating the week': 0,
                                            u'startswith:A resolution expressing support for': 9,
                                            u'startswith:A resolution honoring the': 8,
                                            u'startswith:A resolution recognizing the': 1},
              'success_name': 'agreed to',
              'success_rate': 98.59719438877755},
 (4, True): {'count': 707,
             'factors': {'cosponsor_leader_majority': {'count': 38,
                                                       'regression_beta': 0.055771752097075952,
                                                       'success_rate': 84.21052631578948},
                         'cosponsors_bipartisan': {'count': 65,
                                                   'regression_beta': 3.266267151982897,
                                                   'success_rate': 95.38461538461539},
                         'cosponsors_crosspartisan': {'count': 252,
                                                      'regression_beta': 1.6522207939888578,
                                                      'success_rate': 82.53968253968254},
                         'sponsor_committee_chair': {'count': 29,
                                                     'regression_beta': -2.5544447610433361,
                                                     'success_rate': 20.689655172413794},
                         'sponsor_committee_member_majority': {'count': 74,
                                                               'regression_beta': -1.6058000523371516,
                                                               'success_rate': 41.891891891891895},
                         'sponsor_leader_majority': {'count': 63,
                                                     'regression_beta': 2.0132128784782251,
                                                     'success_rate': 93.65079365079364},
                         u'startswith:A resolution designating the week': {'count': 30,
                                                                           'regression_beta': 1.7996987541726834,
                                                                           'success_rate': 93.33333333333333},
                         u'startswith:A resolution expressing support for': {'count': 30,
                                                                             'regression_beta': 0.90364939539057243,
                                                                             'success_rate': 86.66666666666667},
                         u'startswith:A resolution expressing the sense of the Senate that': {'count': 31,
                                                                                              'regression_beta': -2.5383179642932654,
                                                                                              'success_rate': 22.580645161290324}},
             'regression_beta': [0.38387395706305982,
                                 1.7996987541726834,
                                 -2.5544447610433361,
                                 -1.6058000523371516,
                                 0.055771752097075952,
                                 2.0132128784782251,
                                 3.266267151982897,
                                 1.6522207939888578,
                                 -2.5383179642932654,
                                 0.90364939539057243],
             'regression_predictors_map': {'cosponsor_leader_majority': 3,
                                           'cosponsors_bipartisan': 5,
                                           'cosponsors_crosspartisan': 6,
                                           'sponsor_committee_chair': 1,
                                           'sponsor_committee_member_majority': 2,
                                           'sponsor_leader_majority': 4,
                                           u'startswith:A resolution designating the week': 0,
                                           u'startswith:A resolution expressing support for': 8,
                                           u'startswith:A resolution expressing the sense of the Senate that': 7},
             'success_name': 'agreed to',
             'success_rate': 69.58981612446959},
 (5, False): {'count': 121,
              'factors': {'cosponsor_leader_majority': {'count': 47,
                                                        'regression_beta': -1.3174240099759083,
                                                        'success_rate': 31.914893617021278},
                          'cosponsors_crosspartisan': {'count': 67,
                                                       'regression_beta': -0.5545577274483946,
                                                       'success_rate': 38.80597014925373},
                          'sponsor_minority': {'count': 24,
                                               'regression_beta': -1.1583091945831081,
                                               'success_rate': 29.166666666666668}},
              'regression_beta': [1.1709538621720259,
                                  -1.1583091945831081,
                                  -0.5545577274483946,
                                  -1.3174240099759083],
              'regression_predictors_map': {'cosponsor_leader_majority': 2,
                                            'cosponsors_crosspartisan': 1,
                                            'sponsor_minority': 0},
              'success_name': 'agreed to',
              'success_rate': 52.892561983471076},
 (5, True): {'count': 336,
             'factors': {'sponsor_majority': {'count': 235,
                                              'regression_beta': 0.24434967703546062,
                                              'success_rate': 24.25531914893617},
                         'sponsor_minority': {'count': 101,
                                              'regression_beta': -1.2741915725355906,
                                              'success_rate': 6.930693069306931},
                         u'startswith:Expressing the sense of Congress that': {'count': 52,
                                                                               'regression_beta': -2.9020215987646596,
                                                                               'success_rate': 1.9230769230769231},
                         u'startswith:Expressing the sense of the Congress': {'count': 24,
                                                                              'regression_beta': -34.936981396658872,
                                                                              'success_rate': 0.0}},
             'regression_beta': [-1.0534944152250385,
                                 -1.2741915725355906,
                                 -34.936981396658872,
                                 0.24434967703546062,
                                 -2.9020215987646596],
             'regression_predictors_map': {'sponsor_majority': 2,
                                           'sponsor_minority': 0,
                                           u'startswith:Expressing the sense of Congress that': 3,
                                           u'startswith:Expressing the sense of the Congress': 1},
             'success_name': 'agreed to',
             'success_rate': 19.047619047619047},
 (6, False): {'count': 37,
              'factors': {},
              'regression_beta': None,
              'regression_predictors_map': None,
              'success_name': 'agreed to',
              'success_rate': 45.945945945945944},
 (6, True): {'count': 78,
             'factors': {},
             'regression_beta': None,
             'regression_predictors_map': None,
             'success_name': 'agreed to',
             'success_rate': 21.794871794871796},
 (7, False): {'count': 16,
              'factors': {},
              'regression_beta': None,
              'regression_predictors_map': None,
              'success_name': 'enacted or passed',
              'success_rate': 68.75},
 (7, True): {'count': 107,
             'factors': {'sponsor_minority': {'count': 49,
                                              'regression_beta': -37.281921015388235,
                                              'success_rate': 0.0},
                         u'startswith:Proposing an amendment to the Constitution of the United': {'count': 47,
                                                                                                  'regression_beta': -37.215975245573354,
                                                                                                  'success_rate': 0.0}},
             'regression_beta': [-0.8979415932059589,
                                 -37.281921015388235,
                                 -37.215975245573354],
             'regression_predictors_map': {'sponsor_minority': 0,
                                           u'startswith:Proposing an amendment to the Constitution of the United': 1},
             'success_name': 'enacted or passed',
             'success_rate': 10.280373831775702},
 (8, False): {'count': 22,
              'factors': {},
              'regression_beta': None,
              'regression_predictors_map': None,
              'success_name': 'enacted or passed',
              'success_rate': 36.36363636363637},
 (8, True): {'count': 42,
             'factors': {'sponsor_majority': {'count': 18,
                                              'regression_beta': 2.6835090921646256,
                                              'success_rate': 38.888888888888886}},
             'regression_beta': [-3.1354942159076828, 2.6835090921646256],
             'regression_predictors_map': {'sponsor_majority': 0},
             'success_name': 'enacted or passed',
             'success_rate': 19.047619047619047}}