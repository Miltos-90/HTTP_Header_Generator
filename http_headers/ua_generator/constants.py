""" Holds the necessary data for the generation of randomized user agents (see programmer.py) """

from typing         import Literal, Tuple, Dict, Union, Set, get_args
from ..definitions  import BROWSER_TYPE
from dataclasses    import dataclass


""" Datatypes declaration for the dictionaries below. """
BRAND_TYPE          = Literal['nexus', 'pixel', 'samsung']                     # Generic Android OS systems for mobile devices
OS_TYPE             = Literal['windows', 'linux', 'android', 'macos', 'ios']   # Generic OS
SOFTWARE_TYPE       = Union[BROWSER_TYPE, OS_TYPE, BRAND_TYPE]                 # Generic software name
ANDROID_DEVKEY_TYPE = Dict[BRAND_TYPE, Tuple]                                  # Android devices
ANDROID_VERKEY_TYPE = Dict[BRAND_TYPE, Dict[str, Dict]]                        # Android versions
OS_NAMES            = get_args(OS_TYPE)

@dataclass
class Software():           # Software object
    name    : SOFTWARE_TYPE # Software name
    details : dict          # Additional software details
    version : str           # Software version


""" Dictionaries definitions """
# User agent templates for each operating system and browser: https://www.whatismybrowser.com/guides/the-latest-user-agent/
TEMPLATES: Dict[Tuple[OS_TYPE, BROWSER_TYPE], Tuple] = {
    ('windows', 'chrome') : (
        'Mozilla/5.0 (Windows NT {windows}; Win64; x64) AppleWebKit/{webkit} (KHTML, like Gecko) Chrome/{chrome} Safari/{webkit}',
        'Mozilla/5.0 (Windows NT {windows}; WOW64) AppleWebKit/{webkit} (KHTML, like Gecko) Chrome/{chrome} Safari/{webkit}',
    ),

    ('windows', 'edge') : (
        'Mozilla/5.0 (Windows NT {windows}; Win64; x64) AppleWebKit/{webkit} (KHTML, like Gecko) Chrome/{chrome} Safari/{webkit} Edg/{chrome}',
    ),

    ('windows', 'firefox') : (
        'Mozilla/5.0 (Windows NT {windows}; Win64; x64; rv:{firefox}) Gecko/20100101 Firefox/{firefox}',
        'Mozilla/5.0 (Windows NT {windows}; WOW64; rv:{firefox}) Gecko/20100101 Firefox/{firefox}',
    ),
    
    ('windows', 'opera') : (
        'Mozilla/5.0 (Windows NT {windows}; Win64; x64) AppleWebKit/{webkit} (KHTML, like Gecko) Chrome/{chromium} Safari/{webkit} OPR/{opera}',
        'Mozilla/5.0 (Windows NT {windows}; WOW64) AppleWebKit/{webkit} (KHTML, like Gecko) Chrome/{chromium} Safari/{webkit} OPR/{opera}',
    ),

    ('linux', 'chrome') : (
        'Mozilla/5.0 (X11; Linux i686) AppleWebKit/{webkit} (KHTML, like Gecko) Ubuntu Chromium/{chrome} Chrome/{chrome} Safari/{webkit}',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/{webkit} (KHTML, like Gecko) Chrome/{chrome} Safari/{webkit}',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/{webkit} (KHTML, like Gecko) Chrome/{chrome} Safari/{webkit}',
    ),

    ('linux', 'edge') : (
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/{webkit} (KHTML, like Gecko) Chrome/{chrome} Safari/{webkit} Edg/{chrome}',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/{webkit} (KHTML, like Gecko) Chrome/{chrome} Safari/{webkit} Edg/{chrome}',
    ),

    ('linux', 'firefox') : (
        'Mozilla/5.0 (X11; Linux x86_64; rv:{firefox}) Gecko/20100101 Firefox/{firefox}',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:{firefox}) Gecko/20100101 Firefox/{firefox}',
    ),

    ('linux', 'opera') : (
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/{webkit} (KHTML, like Gecko) Chrome/{chromium} Safari/{webkit} OPR/{opera}',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/{webkit} (KHTML, like Gecko) Chrome/{chromium} Safari/{webkit} OPR/{opera}',
    ),

    ('android', 'chrome') : (
        'Mozilla/5.0 (Linux; Android {android}{device}{build}) AppleWebKit/{webkit} (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/{webkit}',
    ),

    ('android', 'edge') : (
        'Mozilla/5.0 (Linux; Android {android}{device}{build}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/{webkit} EdgA/{chrome}',
    ),

    ('android', 'firefox') : (
        'Mozilla/5.0 (Android {android}; Mobile; rv:{firefox}) Gecko/{firefox} Firefox/{firefox}',
    ),

    ('android', 'opera') : (
        'Mozilla/5.0 (Linux; Android {android}; {device}) AppleWebKit/{webkit} (KHTML, like Gecko) Chrome/{chromium} Mobile Safari/{webkit} OPR/{opera}',
    ),

    ('macos', 'chrome') : (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X {macos}) AppleWebKit/{webkit} (KHTML, like Gecko) Chrome/{chrome} Safari/{webkit}',
    ),

    ('macos', 'edge') : (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X {macos}) AppleWebKit/{webkit} (KHTML, like Gecko) Chrome/{chrome} Safari/{webkit} Edg/{chrome}',
    ),

    ('macos', 'safari') : (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X {macos}) AppleWebKit/{webkit} (KHTML, like Gecko) Version/{safari} Safari/{webkit}',
    ),

    ('macos', 'firefox') : (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X {macos}; rv:{firefox}) Gecko/20100101 Firefox/{firefox}',
    ),

    ('macos', 'opera') : (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X {macos}) AppleWebKit/{webkit} (KHTML, like Gecko) Chrome/{chromium} Safari/{webkit} OPR/{opera}',
    ),

    ('ios', 'chrome') : (
        'Mozilla/5.0 (iPhone; CPU iPhone OS {ios} like Mac OS X) AppleWebKit/{webkit} (KHTML, like Gecko) CriOS/{chrome} Mobile/15E148 Safari/{webkit}',
    ),

    ('ios', 'edge') : (
        'Mozilla/5.0 (iPhone; CPU iPhone OS {ios} like Mac OS X) AppleWebKit/{webkit} (KHTML, like Gecko) Version/15.0 EdgiOS/{chrome} Mobile/15E148 Safari/{webkit}',
    ),

    ('ios', 'safari') : (
        'Mozilla/5.0 (iPhone; CPU iPhone OS {ios} like Mac OS X) AppleWebKit/{webkit} (KHTML, like Gecko) Version/{safari} Mobile/15E148 Safari/{webkit}',
    ),

    ('ios', 'firefox') : (
        'Mozilla/5.0 (iPhone; CPU iPhone OS {ios} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/{firefox} Mobile/15E148 Safari/605.1.15',
    ),

}


BROWSERS: Dict[BROWSER_TYPE, Dict[str, Dict]] = { 
    # browser name: major version : {additional key/value pairs for minor versions and additional properties}
    'chrome' : {
        '76.0.3809' :   {'minor_range': (0, 255), 'webkit': '537.36'},
        '77.0.3865' :   {'minor_range': (0, 255), 'webkit': '537.36'},
        '78.0.3904' :   {'minor_range': (0, 255), 'webkit': '537.36'},
        '79.0.3945' :   {'minor_range': (0, 255), 'webkit': '537.36'},
        '80.0.3987' :   {'minor_range': (0, 255), 'webkit': '537.36'},
        '81.0.4044' :   {'minor_range': (0, 255), 'webkit': '537.36'},
        '83.0.4103' :   {'minor_range': (0, 255), 'webkit': '537.36'},
        '84.0.4147' :   {'minor_range': (0, 255), 'webkit': '537.36'},
        '85.0.4183' :   {'minor_range': (0, 255), 'webkit': '537.36'},
        '86.0.4240' :   {'minor_range': (0, 255), 'webkit': '537.36'},
        '87.0.4280' :   {'minor_range': (0, 255), 'webkit': '537.36'},
        '88.0.4324' :   {'minor_range': (0, 255), 'webkit': '537.36'},
        '89.0.4389' :   {'minor_range': (0, 255), 'webkit': '537.36'},
        '90.0.4430' :   {'minor_range': (0, 255), 'webkit': '537.36'},
        '91.0.4472' :   {'minor_range': (0, 255), 'webkit': '537.36'},
        '92.0.4515' :   {'minor_range': (0, 255), 'webkit': '537.36'},
        '93.0.4577' :   {'minor_range': (0, 255), 'webkit': '537.36'},
        '94.0.4606' :   {'minor_range': (0, 255), 'webkit': '537.36'},
        '95.0.4638' :   {'minor_range': (0, 255), 'webkit': '537.36'},
        '96.0.4664' :   {'minor_range': (0, 255), 'webkit': '537.36'},
        '97.0.4692' :   {'minor_range': (0, 255), 'webkit': '537.36'},
        '98.0.4758' :   {'minor_range': (0, 255), 'webkit': '537.36'},
        '99.0.4844' :   {'minor_range': (0, 255), 'webkit': '537.36'},
        '100.0.4896':   {'minor_range': (0, 255), 'webkit': '537.36'},
        '101.0.4951':   {'minor_range': (0, 255), 'webkit': '537.36'},
        '102.0.5005':   {'minor_range': (0, 255), 'webkit': '537.36'},
        '103.0.5060':   {'minor_range': (0, 255), 'webkit': '537.36'},
        '104.0.5112':   {'minor_range': (0, 255), 'webkit': '537.36'},
        '105.0.5195':   {'minor_range': (0, 255), 'webkit': '537.36'},
        '106.0.5249':   {'minor_range': (0, 255), 'webkit': '537.36'},
        '107.0.5304':   {'minor_range': (0, 255), 'webkit': '537.36'},
        '108.0.5359':   {'minor_range': (0, 255), 'webkit': '537.36'},
        '109.0.5414':   {'minor_range': (0, 255), 'webkit': '537.36'},
        '110.0.5481':   {'minor_range': (0, 255), 'webkit': '537.36'},
        '111.0.5563':   {'minor_range': (0, 255), 'webkit': '537.36'}
        },
        
    'edge': { 
        '88.0.705'  :   {'minor_range': (0, 99), 'webkit': '537.36'},
        '89.0.774'  :   {'minor_range': (0, 99), 'webkit': '537.36'},
        '90.0.818'  :   {'minor_range': (0, 99), 'webkit': '537.36'},
        '91.0.864'  :   {'minor_range': (0, 99), 'webkit': '537.36'},
        '92.0.902'  :   {'minor_range': (0, 99), 'webkit': '537.36'},
        '93.0.961'  :   {'minor_range': (0, 99), 'webkit': '537.36'},
        '94.0.992'  :   {'minor_range': (0, 99), 'webkit': '537.36'},
        '95.0.1020' :   {'minor_range': (0, 99), 'webkit': '537.36'},
        '96.0.1054' :   {'minor_range': (0, 99), 'webkit': '537.36'},
        '97.0.1072' :   {'minor_range': (0, 99), 'webkit': '537.36'},
        '98.0.1108' :   {'minor_range': (0, 99), 'webkit': '537.36'},
        '99.0.1141' :   {'minor_range': (0, 99), 'webkit': '537.36'},
        '99.0.1146' :   {'minor_range': (0, 99), 'webkit': '537.36'},
        '100.0.1185':   {'minor_range': (0, 99), 'webkit': '537.36'},
        '101.0.1210':   {'minor_range': (0, 99), 'webkit': '537.36'},
        '102.0.1245':   {'minor_range': (0, 99), 'webkit': '537.36'},
        '103.0.1264':   {'minor_range': (0, 99), 'webkit': '537.36'},
        '104.0.1293':   {'minor_range': (0, 99), 'webkit': '537.36'},
        '105.0.1146':   {'minor_range': (0, 99), 'webkit': '537.36'},
        '106.0.1146':   {'minor_range': (0, 99), 'webkit': '537.36'},
        '107.0.1418':   {'minor_range': (0, 99), 'webkit': '537.36'},
        '108.0.1462':   {'minor_range': (0, 99), 'webkit': '537.36'},
        '109.0.1518':   {'minor_range': (0, 99), 'webkit': '537.36'},
        '110.0.1587':   {'minor_range': (0, 99), 'webkit': '537.36'},
        '111.0.1661':   {'minor_range': (0, 99), 'webkit': '537.36'}
        },
        
    'firefox': { 
        '78'   :   {'minor_range': (0, 15)},
        '79'   :   {'minor_range': (0, 0)},
        '80'   :   {'minor_range': (0, 1)},
        '81'   :   {'minor_range': (0, 2)},
        '82'   :   {'minor_range': (0, 3)},
        '83'   :   {'minor_range': (0, 0)},
        '84'   :   {'minor_range': (0, 2)},
        '85'   :   {'minor_range': (0, 2)},
        '86'   :   {'minor_range': (0, 1)},
        '87'   :   {'minor_range': (0, 0)},
        '88'   :   {'minor_range': (0, 1)},
        '89'   :   {'minor_range': (0, 2)},
        '90'   :   {'minor_range': (0, 2)},
        '91.0' :   {'minor_range': (0, 13)},
        '92.0' :   {'minor_range': (0, 1)},
        '93.0' :   {'minor_range': (0, 0)},
        '94.0' :   {'minor_range': (0, 2)},
        '95.0' :   {'minor_range': (0, 2)},
        '96.0' :   {'minor_range': (0, 3)},
        '97.0' :   {'minor_range': (0, 2)},
        '98.0' :   {'minor_range': (0, 2)},
        '99.0' :   {'minor_range': (0, 1)},
        '100.0':   {'minor_range': (0, 2)},
        '101.0':   {'minor_range': (0, 1)},
        '102.0':   {'minor_range': (0, 6)},
        '103.0':   {'minor_range': (0, 2)},
        '104.0':   {'minor_range': (0, 2)},
        '105.0':   {'minor_range': (0, 3)},
        '106.0':   {'minor_range': (0, 5)},
        '107.0':   {'minor_range': (0, 1)},
        '108.0':   {'minor_range': (0, 2)},
        '109.0':   {'minor_range': (0, 1)},
        '110.0':   {'minor_range': (0, 1)}
        },
        
    'safari' : {
        '8' :   {'minor_range': (0, 0), 'webkit': '600.7.12'},
        '9' :   {'minor_range': (0, 0), 'webkit': '601.4.4'},
        '10':   {'minor_range': (0, 0), 'webkit': '603.1.30'},
        '11':   {'minor_range': (0, 0), 'webkit': '605.1.33'},
        '12':   {'minor_range': (0, 1), 'webkit': '607.1.40'},
        '13':   {'minor_range': (0, 1), 'webkit': '608.2.11'},
        '14':   {'minor_range': (0, 1), 'webkit': '610.3.7.1.9'},
        '15':   {'minor_range': (0, 6), 'webkit': '612.3.6'},
        '16':   {'minor_range': (0, 3), 'webkit': '614.3.7.1.5'},
        },
    
    'opera' : {
        '66.0.3515.27'  : {'chromium': '79.0.3946',  'webkit': '537.36'},
        '66.0.3515.36'  : {'chromium': '79.0.3947',  'webkit': '537.36'},
        '66.0.3515.44'  : {'chromium': '79.0.3948',  'webkit': '537.36'},
        '66.0.3515.60'  : {'chromium': '79.0.3949',  'webkit': '537.36'},
        '66.0.3515.72'  : {'chromium': '79.0.3950',  'webkit': '537.36'},
        '66.0.3515.95'  : {'chromium': '80.0.3987',  'webkit': '537.36'},
        '66.0.3515.103' : {'chromium': '79.0.3945',  'webkit': '537.36'},
        '66.0.3515.115' : {'chromium': '79.0.3945',  'webkit': '537.36'},
        '67.0.3575.31'  : {'chromium': '79.0.3950',  'webkit': '537.36'},
        '67.0.3575.53'  : {'chromium': '80.0.3987',  'webkit': '537.36'},
        '67.0.3575.79'  : {'chromium': '80.0.3987',  'webkit': '537.36'},
        '67.0.3575.97'  : {'chromium': '80.0.3987',  'webkit': '537.36'},
        '67.0.3575.115' : {'chromium': '80.0.3987',  'webkit': '537.36'},
        '67.0.3575.137' : {'chromium': '81.0.4044',  'webkit': '537.36'},
        '68.0.3618.46'  : {'chromium': '81.0.4044',  'webkit': '537.36'},
        '68.0.3618.56'  : {'chromium': '81.0.4044',  'webkit': '537.36'},
        '68.0.3618.63'  : {'chromium': '81.0.4044',  'webkit': '537.36'},
        '68.0.3618.91'  : {'chromium': '83.0.4103',  'webkit': '537.36'},
        '68.0.3618.104' : {'chromium': '83.0.4103',  'webkit': '537.36'},
        '68.0.3618.125' : {'chromium': '83.0.4103',  'webkit': '537.36'},
        '68.0.3618.165' : {'chromium': '83.0.4103',  'webkit': '537.36'},
        '68.0.3618.173' : {'chromium': '83.0.4103',  'webkit': '537.36'},
        '69.0.3686.36'  : {'chromium': '83.0.4103',  'webkit': '537.36'},
        '69.0.3686.49'  : {'chromium': '83.0.4103',  'webkit': '537.36'},
        '69.0.3686.57'  : {'chromium': '83.0.4103',  'webkit': '537.36'},
        '69.0.3686.77'  : {'chromium': '84.0.4147',  'webkit': '537.36'},
        '69.0.3686.95'  : {'chromium': '84.0.4147',  'webkit': '537.36'},
        '70.0.3728.71'  : {'chromium': '84.0.4147',  'webkit': '537.36'},
        '70.0.3728.95'  : {'chromium': '84.0.4147',  'webkit': '537.36'},
        '70.0.3728.106' : {'chromium': '84.0.4147',  'webkit': '537.36'},
        '70.0.3728.119' : {'chromium': '84.0.4147',  'webkit': '537.36'},
        '70.0.3728.133' : {'chromium': '85.0.4183',  'webkit': '537.36'},
        '70.0.3728.144' : {'chromium': '85.0.4183',  'webkit': '537.36'},
        '70.0.3728.154' : {'chromium': '85.0.4183',  'webkit': '537.36'},
        '70.0.3728.178' : {'chromium': '85.0.4183',  'webkit': '537.36'},
        '70.0.3728.189' : {'chromium': '85.0.4183',  'webkit': '537.36'},
        '71.0.3770.148' : {'chromium': '85.0.4183',  'webkit': '537.36'},
        '71.0.3770.171' : {'chromium': '85.0.4183',  'webkit': '537.36'},
        '71.0.3770.198' : {'chromium': '85.0.4183',  'webkit': '537.36'},
        '71.0.3770.228' : {'chromium': '86.0.4240',  'webkit': '537.36'},
        '71.0.3770.271' : {'chromium': '86.0.4240',  'webkit': '537.36'},
        '71.0.3770.284' : {'chromium': '86.0.4240',  'webkit': '537.36'},
        '72.0.3815.148' : {'chromium': '86.0.4240',  'webkit': '537.36'},
        '72.0.3815.178' : {'chromium': '86.0.4240',  'webkit': '537.36'},
        '72.0.3815.186' : {'chromium': '86.0.4240',  'webkit': '537.36'},
        '72.0.3815.200' : {'chromium': '86.0.4240',  'webkit': '537.36'},
        '72.0.3815.207' : {'chromium': '86.0.4240',  'webkit': '537.36'},
        '72.0.3815.211' : {'chromium': '86.0.4240',  'webkit': '537.36'},
        '72.0.3815.320' : {'chromium': '86.0.4240',  'webkit': '537.36'},
        '72.0.3815.371' : {'chromium': '87.0.4280',  'webkit': '537.36'},
        '72.0.3815.378' : {'chromium': '87.0.4280',  'webkit': '537.36'},
        '72.0.3815.400' : {'chromium': '87.0.4280',  'webkit': '537.36'},
        '72.0.3815.355' : {'chromium': '87.0.4280',  'webkit': '537.36'},
        '72.0.3815.354' : {'chromium': '87.0.4280',  'webkit': '537.36'},
        '73.0.3856.257' : {'chromium': '87.0.4280',  'webkit': '537.36'},
        '73.0.3856.284' : {'chromium': '87.0.4280',  'webkit': '537.36'},
        '73.0.3856.329' : {'chromium': '87.0.4280',  'webkit': '537.36'},
        '73.0.3856.344' : {'chromium': '87.0.4280',  'webkit': '537.36'},
        '74.0.3911.75'  : {'chromium': '88.0.4324',  'webkit': '537.36'},
        '74.0.3911.107' : {'chromium': '88.0.4324',  'webkit': '537.36'},
        '74.0.3911.139' : {'chromium': '88.0.4324',  'webkit': '537.36'},
        '74.0.3911.144' : {'chromium': '88.0.4324',  'webkit': '537.36'},
        '74.0.3911.154' : {'chromium': '88.0.4324',  'webkit': '537.36'},
        '74.0.3911.160' : {'chromium': '88.0.4324',  'webkit': '537.36'},
        '74.0.3911.203' : {'chromium': '89.0.4389',  'webkit': '537.36'},
        '74.0.3911.218' : {'chromium': '89.0.4389',  'webkit': '537.36'},
        '74.0.3911.232' : {'chromium': '89.0.4389',  'webkit': '537.36'},
        '75.0.3969.93'  : {'chromium': '89.0.4389',  'webkit': '537.36'},
        '75.0.3969.141' : {'chromium': '89.0.4389',  'webkit': '537.36'},
        '75.0.3969.149' : {'chromium': '89.0.4389',  'webkit': '537.36'},
        '75.0.3969.171' : {'chromium': '89.0.4389',  'webkit': '537.36'},
        '75.0.3969.218' : {'chromium': '90.0.4430',  'webkit': '537.36'},
        '75.0.3969.243' : {'chromium': '90.0.4430',  'webkit': '537.36'},
        '75.0.3969.250' : {'chromium': '90.0.4430',  'webkit': '537.36'},
        '76.0.4017.94'  : {'chromium': '90.0.4430',  'webkit': '537.36'},
        '76.0.4017.107' : {'chromium': '90.0.4430',  'webkit': '537.36'},
        '76.0.4017.123' : {'chromium': '90.0.4430',  'webkit': '537.36'},
        '76.0.4017.137' : {'chromium': '90.0.4430',  'webkit': '537.36'},
        '76.0.4017.154' : {'chromium': '91.0.4472',  'webkit': '537.36'},
        '76.0.4017.175' : {'chromium': '91.0.4472',  'webkit': '537.36'},
        '76.0.4017.177' : {'chromium': '91.0.4472',  'webkit': '537.36'},
        '77.0.4054.60'  : {'chromium': '91.0.4472',  'webkit': '537.36'},
        '77.0.4054.64'  : {'chromium': '91.0.4472',  'webkit': '537.36'},
        '77.0.4054.80'  : {'chromium': '91.0.4472',  'webkit': '537.36'},
        '77.0.4054.90'  : {'chromium': '91.0.4472',  'webkit': '537.36'},
        '77.0.4054.146' : {'chromium': '91.0.4472',  'webkit': '537.36'},
        '77.0.4054.172' : {'chromium': '91.0.4472',  'webkit': '537.36'},
        '77.0.4054.203' : {'chromium': '91.0.4472',  'webkit': '537.36'},
        '77.0.4054.254' : {'chromium': '91.0.4472',  'webkit': '537.36'},
        '77.0.4054.277' : {'chromium': '92.0.4515',  'webkit': '537.36'},
        '78.0.4093.112' : {'chromium': '92.0.4515',  'webkit': '537.36'},
        '78.0.4093.147' : {'chromium': '92.0.4515',  'webkit': '537.36'},
        '78.0.4093.184' : {'chromium': '92.0.4515',  'webkit': '537.36'},
        '78.0.4093.231' : {'chromium': '92.0.4515',  'webkit': '537.36'},
        '79.0.4143.22'  : {'chromium': '92.0.4515',  'webkit': '537.36'},
        '79.0.4143.50'  : {'chromium': '94.0.4606',  'webkit': '537.36'},
        '79.0.4143.56'  : {'chromium': '94.0.4606',  'webkit': '537.36'},
        '79.0.4143.66'  : {'chromium': '94.0.4606',  'webkit': '537.36'},
        '79.0.4143.72'  : {'chromium': '94.0.4606',  'webkit': '537.36'},
        '80.0.4170.16'  : {'chromium': '94.0.4606',  'webkit': '537.36'},
        '80.0.4170.40'  : {'chromium': '94.0.4606',  'webkit': '537.36'},
        '80.0.4170.63'  : {'chromium': '95.0.4638',  'webkit': '537.36'},
        '80.0.4170.72'  : {'chromium': '95.0.4638',  'webkit': '537.36'},
        '81.0.4196.31'  : {'chromium': '95.0.4638',  'webkit': '537.36'},
        '81.0.4196.37'  : {'chromium': '95.0.4638',  'webkit': '537.36'},
        '81.0.4196.54'  : {'chromium': '96.0.4664',  'webkit': '537.36'},
        '81.0.4196.60'  : {'chromium': '96.0.4664',  'webkit': '537.36'},
        '82.0.4227.23'  : {'chromium': '96.0.4664',  'webkit': '537.36'},
        '82.0.4227.33'  : {'chromium': '96.0.4664',  'webkit': '537.36'},
        '82.0.4227.43'  : {'chromium': '96.0.4664',  'webkit': '537.36'},
        '82.0.4227.58'  : {'chromium': '97.0.4692',  'webkit': '537.36'},
        '83.0.4254.19'  : {'chromium': '97.0.4692',  'webkit': '537.36'},
        '83.0.4254.27'  : {'chromium': '97.0.4692',  'webkit': '537.36'},
        '83.0.4254.54'  : {'chromium': '98.0.4758',  'webkit': '537.36'},
        '83.0.4254.62'  : {'chromium': '98.0.4758',  'webkit': '537.36'},
        '84.0.4316.14'  : {'chromium': '98.0.4758',  'webkit': '537.36'},
        '84.0.4316.21'  : {'chromium': '98.0.4758',  'webkit': '537.36'},
        '84.0.4316.31'  : {'chromium': '99.0.4844',  'webkit': '537.36'},
        '84.0.4316.42'  : {'chromium': '99.0.4844',  'webkit': '537.36'},
        '85.0.4341.18'  : {'chromium': '99.0.4844',  'webkit': '537.36'},
        '85.0.4341.28'  : {'chromium': '100.0.4896', 'webkit': '537.36'},
        '85.0.4341.39'  : {'chromium': '100.0.4896', 'webkit': '537.36'},
        '85.0.4341.47'  : {'chromium': '100.0.4896', 'webkit': '537.36'},
        '85.0.4341.60'  : {'chromium': '100.0.4896', 'webkit': '537.36'},
        '85.0.4341.75'  : {'chromium': '100.0.4896', 'webkit': '537.36'},
        '86.0.4363.23'  : {'chromium': '100.0.4896', 'webkit': '537.36'},
        '86.0.4363.32'  : {'chromium': '101.0.4951', 'webkit': '537.36'},
        '86.0.4363.50'  : {'chromium': '101.0.4951', 'webkit': '537.36'},
        '86.0.4363.59'  : {'chromium': '101.0.4951', 'webkit': '537.36'},
        '87.0.4390.25'  : {'chromium': '101.0.4951', 'webkit': '537.36'},
        '87.0.4390.26'  : {'chromium': '101.0.4951', 'webkit': '537.36'},
        '87.0.4390.31'  : {'chromium': '102.0.5005', 'webkit': '537.36'},
        '87.0.4390.36'  : {'chromium': '102.0.5005', 'webkit': '537.36'},
        '87.0.4390.45'  : {'chromium': '102.0.5005', 'webkit': '537.36'},
        '88.0.4412.27'  : {'chromium': '102.0.5005', 'webkit': '537.36'},
        '88.0.4412.34'  : {'chromium': '102.0.5005', 'webkit': '537.36'},
        '88.0.4412.40'  : {'chromium': '102.0.5005', 'webkit': '537.36'},
        '88.0.4412.53'  : {'chromium': '103.0.5060', 'webkit': '537.36'},
        '88.0.4412.74'  : {'chromium': '103.0.5060', 'webkit': '537.36'},
        '89.0.4447.38'  : {'chromium': '103.0.5060', 'webkit': '537.36'},
        '89.0.4447.48'  : {'chromium': '103.0.5060', 'webkit': '537.36'},
        '89.0.4447.51'  : {'chromium': '103.0.5060', 'webkit': '537.36'},
        '89.0.4447.71'  : {'chromium': '103.0.5060', 'webkit': '537.36'},
        '89.0.4447.56'  : {'chromium': '104.0.5112', 'webkit': '537.36'},
        '89.0.4447.62'  : {'chromium': '104.0.5112', 'webkit': '537.36'},
        '89.0.4447.63'  : {'chromium': '104.0.5112', 'webkit': '537.36'},
        '89.0.4447.83'  : {'chromium': '104.0.5112', 'webkit': '537.36'},
        '89.0.4447.91'  : {'chromium': '104.0.5112', 'webkit': '537.36'},
        '89.0.4447.101' : {'chromium': '104.0.5112', 'webkit': '537.36'},
        '90.0.4480.48'  : {'chromium': '104.0.5112', 'webkit': '537.36'},
        '90.0.4480.54'  : {'chromium': '104.0.5112', 'webkit': '537.36'},
        '90.0.4480.80'  : {'chromium': '105.0.5195', 'webkit': '537.36'},
        '90.0.4480.84'  : {'chromium': '105.0.5195', 'webkit': '537.36'},
        '90.0.4480.107' : {'chromium': '105.0.5195', 'webkit': '537.36'},
        '91.0.4516.16'  : {'chromium': '105.0.5195', 'webkit': '537.36'},
        '91.0.4516.20'  : {'chromium': '105.0.5195', 'webkit': '537.36'},
        '91.0.4516.65'  : {'chromium': '106.0.5249', 'webkit': '537.36'},
        '91.0.4516.77'  : {'chromium': '106.0.5249', 'webkit': '537.36'},
        '91.0.4516.70'  : {'chromium': '106.0.5249', 'webkit': '537.36'},
        '91.0.4516.80'  : {'chromium': '106.0.5249', 'webkit': '537.36'},
        '92.0.4561.21'  : {'chromium': '106.0.5249', 'webkit': '537.36'},
        '92.0.4561.30'  : {'chromium': '107.0.5304', 'webkit': '537.36'},
        '92.0.4561.33'  : {'chromium': '107.0.5304', 'webkit': '537.36'},
        '92.0.4561.43'  : {'chromium': '107.0.5304', 'webkit': '537.36'},
        '92.0.4561.47'  : {'chromium': '107.0.5304', 'webkit': '537.36'},
        '92.0.4561.50'  : {'chromium': '107.0.5304', 'webkit': '537.36'},
        '92.0.4561.61'  : {'chromium': '107.0.5304', 'webkit': '537.36'},
        '93.0.4585.11'  : {'chromium': '107.0.5304', 'webkit': '537.36'},
        '93.0.4585.21'  : {'chromium': '107.0.5304', 'webkit': '537.36'},
        '93.0.4585.37'  : {'chromium': '108.0.5359', 'webkit': '537.36'},
        '93.0.4585.39'  : {'chromium': '108.0.5359', 'webkit': '537.36'},
        '93.0.4585.64'  : {'chromium': '108.0.5359', 'webkit': '537.36'},
        '93.0.4585.70'  : {'chromium': '108.0.5359', 'webkit': '537.36'},
        '94.0.4606.26'  : {'chromium': '108.0.5359', 'webkit': '537.36'},
        '94.0.4606.38'  : {'chromium': '108.0.5359', 'webkit': '537.36'},
        '94.0.4606.54'  : {'chromium': '108.0.5359', 'webkit': '537.36'},
        '94.0.4606.65'  : {'chromium': '109.0.5414', 'webkit': '537.36'},
        '94.0.4606.76'  : {'chromium': '109.0.5414', 'webkit': '537.36'},
        '95.0.4635.25'  : {'chromium': '109.0.5414', 'webkit': '537.36'},
        '95.0.4635.37'  : {'chromium': '109.0.5414', 'webkit': '537.36'},
        '95.0.4635.46'  : {'chromium': '109.0.5414', 'webkit': '537.36'},
        '96.0.4693.20'  : {'chromium': '109.0.5414', 'webkit': '537.36'},
        '96.0.4693.31'  : {'chromium': '110.0.5481', 'webkit': '537.36'},
        '96.0.4693.50'  : {'chromium': '111.0.5563', 'webkit': '537.36'},
        }
    }


OS: Dict[OS_TYPE, Union[Set, Dict[str,Dict]]] = {
    # OS name: major version : {additional key/value pairs for minor versions and additional properties}
    'ios' : {
        '9' :   {'minor_range': (0, 3)},
        '10':   {'minor_range': (0, 3)},
        '11':   {'minor_range': (0, 4)},
        '12':   {'minor_range': (0, 5)},
        '13':   {'minor_range': (0, 7)},
        '14':   {'minor_range': (0, 8)},
        '15':   {'minor_range': (0, 7)},
        '16':   {'minor_range': (0, 4)}
    },
    
    'linux': {
        '5.0' : {'minor_range': (0, 21)},
        '5.1' : {'minor_range': (0, 21)},
        '5.2' : {'minor_range': (0, 20)},
        '5.3' : {'minor_range': (0, 18)},
        '5.4' : {'minor_range': (0, 184)},
        '5.5' : {'minor_range': (0, 19)},
        '5.6' : {'minor_range': (0, 19)},
        '5.7' : {'minor_range': (0, 19)},
        '5.8' : {'minor_range': (0, 18)},
        '5.9' : {'minor_range': (0, 16)},
        '5.10': {'minor_range': (0, 105)},
        '5.11': {'minor_range': (0, 22)},
        '5.12': {'minor_range': (0, 19)},
        '5.13': {'minor_range': (0, 19)},
        '5.14': {'minor_range': (0, 21)},
        '5.15': {'minor_range': (0, 28)},
        '5.16': {'minor_range': (0, 14)},
        '5.17': {'minor_range': (0, 11)},
        '5.18': {'minor_range': (0, 16)},
        '5.19': {'minor_range': (0, 17)},
        '6.0' : {'minor_range': (0, 19)},
        '6.1' : {'minor_range': (0, 14)},
        '6.2' : {'minor_range': (0, 1)},
    },
    
    'macos': {
        '10.8':  {'minor_range': (0, 8)},
        '10.9':  {'minor_range': (0, 5)},
        '10.10': {'minor_range': (0, 5)},
        '10.11': {'minor_range': (0, 6)},
        '10.12': {'minor_range': (0, 6)},
        '10.13': {'minor_range': (0, 6)},
        '10.14': {'minor_range': (0, 6)},
        '10.15': {'minor_range': (0, 7)},
        '11.0':  {'minor_range': (0, 0)},
        '11.2':  {'minor_range': (0, 3)},
        '11.3':  {'minor_range': (0, 1)},
        '11.5':  {'minor_range': (0, 2)},
        '11.6':  {'minor_range': (0, 6)},
        '12.0':  {'minor_range': (0, 2)},
        '12.2':  {'minor_range': (0, 2)},
        '12.3':  {'minor_range': (0, 2)},
        '12.4':  {'minor_range': (0, 1)},
        '12.5':  {'minor_range': (0, 2)},
        '12.6':  {'minor_range': (0, 5)},
        '13.0':  {'minor_range': (0, 1)},
        '13.1':  {'minor_range': (0, 1)},
        '13.2':  {'minor_range': (0, 2)},
    },
    
    'windows' : {
        '6.1',
        '6.2',
        '6.3',
        '10.0'
        # Windows 11: They can be differentiated from Windows 10 using only client hints.
        # The user agent string will not be updated. See
        #  https://51degrees.com/blog/windows-11-detectable-with-uach, https://learn.microsoft.com/en-us/microsoft-edge/web-platform/how-to-detect-win11
    }
}


ANDROID: Dict[str, Union[ANDROID_DEVKEY_TYPE, ANDROID_VERKEY_TYPE]] = {
     "devices" : {
        "nexus"   : ('Nexus 5', 'Nexus 5X', 'Nexus 6', 'Nexus 6P', 'Nexus 9'),
        "pixel"   : ('Pixel 2', 'Pixel 2 XL', 'Pixel 3', 'Pixel 3a', 'Pixel 3a XL', 'Pixel 3 XL', 'Pixel 4',
                    'Pixel 4 XL', 'Pixel 4a (5G)', 'Pixel 5', 'Pixel 5a (5G)', 'Pixel 6', 'Pixel 6 Pro'),
        "samsung" : ('SM-G390Y', 'SM-G390Y', 'SM-G525F', 'SM-G9006W', 'SM-G9209K', 'SM-316U',
                    'SM-318ML', 'SM-318MZ', 'SM-318MZ', 'SM-360GY', 'SM-G110B', 'SM-G110H',
                    'SM-G110M', 'SM-G130BT', 'SM-G130BU', 'SM-G130E', 'SM-G130H', 'SM-G130HN',
                    'SM-G130M', 'SM-G130U', 'SM-G150N0', 'SM-G150NK', 'SM-G150NL', 'SM-G150NS',
                    'SM-G155S', 'SM-G1600', 'SM-G1600', 'SM-G160N', 'SM-G1650', 'SM-G165N',
                    'SM-G30HN', 'SM-G310H', 'SM-G310HN', 'SM-G310R', 'SM-G310R5', 'SM-G3139',
                    'SM-G3139D', 'SM-G313F', 'SM-G313H', 'SM-G313HN', 'SM-G313HU', 'SM-G313HY',
                    'SM-G313HZ', 'SM-G313M', 'SM-G313ML', 'SM-G313MU', 'SM-G313MY', 'SM-G313U',
                    'SM-G316F', 'SM-G316HU', 'SM-G316M', 'SM-G316ML', 'SM-G316MY', 'SM-G318',
                    'SM-G318H', 'SM-G318HZ', 'SM-G318M', 'SM-G318ML', 'SM-G318MZ', 'SM-G350',
                    'SM-G3502', 'SM-G3502C', 'SM-G3502I', 'SM-G3502L', 'SM-G3502T', 'SM-G3502U',
                    'SM-G3508', 'SM-G3508I', 'SM-G3508J', 'SM-G3509', 'SM-G3509I', 'SM-G350E',
                    'SM-G350L', 'SM-G350M', 'SM-G350X', 'SM-G3518', 'SM-G3556D', 'SM-G3558',
                    'SM-G3559', 'SM-G355H', 'SM-G355HN', 'SM-G355HQ', 'SM-G355M', 'SM-G3568V',
                    'SM-G357', 'SM-G357FZ', 'SM-G357FZ', 'SM-G357M', 'SM-G3586V', 'SM-G3588V',
                    'SM-G3589W', 'SM-G3606', 'SM-G3608', 'SM-G3609', 'SM-G360AZ', 'SM-G360BT',
                    'SM-G360F', 'SM-G360F', 'SM-G360FY', 'SM-G360G', 'SM-G360GY', 'SM-G360H',
                    'SM-G360HU', 'SM-G360M', 'SM-G360P', 'SM-G360T', 'SM-G360V', 'SM-G361F',
                    'SM-G361H', 'SM-G361HU', 'SM-G368T', 'SM-G3812', 'SM-G3812B', 'SM-G3815',
                    'SM-G3818', 'SM-G3818ZM', 'SM-G3819D', 'SM-G3858', 'SM-G386F', 'SM-G386T',
                    'SM-G386T1', 'SM-G386U', 'SM-G386W', 'SM-G388F', 'SM-G389F', 'SM-G390F',
                    'SM-G390W', 'SM-G390Y', 'SM-G398FN', 'SM-G5108', 'SM-G5108Q', 'SM-G5109',
                    'SM-G5306W', 'SM-G5308W', 'SM-G5309W', 'SM-G530A', 'SM-G530AZ', 'SM-G530BT',
                    'SM-G530F', 'SM-G530FQ', 'SM-G530FZ', 'SM-G530H', 'SM-G530M', 'SM-G530MU',
                    'SM-G530P', 'SM-G530R4', 'SM-G530R7', 'SM-G530T', 'SM-G530T1', 'SM-G530W',
                    'SM-G530Y', 'SM-G530YZ', 'SM-G531BT', 'SM-G531F', 'SM-G531H', 'SM-G531M',
                    'SM-G531Y', 'SM-G532F', 'SM-G532G', 'SM-G532M', 'SM-G532MT', 'SM-G5500',
                    'SM-G550FY', 'SM-G550T', 'SM-G550T1', 'SM-G550T2', 'SM-G5510', 'SM-G5520',
                    'SM-G5528', 'SM-G570', 'SM-G5700', 'SM-G570F', 'SM-G570M', 'SM-G570Y',
                    'SM-G6000', 'SM-G600F', 'SM-G600F', 'SM-G600FY', 'SM-G600S', 'SM-G6100',
                    'SM-G610F', 'SM-G610FD', 'SM-G610K', 'SM-G610L', 'SM-G610M', 'SM-G610S',
                    'SM-G610Y', 'SM-G611F', 'SM-G611FF', 'SM-G611FFDD', 'SM-G611K', 'SM-G611L',
                    'SM-G611M', 'SM-G611M/DS', 'SM-G611MT', 'SM-G611S', 'SM-G615F', 'SM-G615FU',
                    'SM-G6200', 'SM-G710', 'SM-G7102', 'SM-G7102T', 'SM-G7105', 'SM-G7105H',
                    'SM-G7105K', 'SM-G7105L', 'SM-G7106', 'SM-G7108', 'SM-G7108V', 'SM-G7109',
                    'SM-G710L', 'SM-G710S', 'SM-G710x', 'SM-G715F', 'SM-G715FN', 'SM-G715U',
                    'SM-G715U1', 'SM-G715W', 'SM-G715X', 'SM-G7200', 'SM-G7202', 'SM-G720AX',
                    'SM-G720N0', 'SM-G730A', 'SM-G730V', 'SM-G730W8', 'SM-G7508Q', 'SM-G7509',
                    'SM-G750A', 'SM-G750H', 'SM-G770F', 'SM-G770U1', 'SM-G780F', 'SM-G780G',
                    'SM-G780X', 'SM-G7810', 'SM-G781B', 'SM-G781BR', 'SM-G781N', 'SM-G781U1',
                    'SM-G781V', 'SM-G800A', 'SM-G800F', 'SM-G800H', 'SM-G800M', 'SM-G800R4',
                    'SM-G800Y', 'SM-G820A', 'SM-G8508S', 'SM-G850A', 'SM-G850F', 'SM-G850FQ',
                    'SM-G850K', 'SM-G850M', 'SM-G850S', 'SM-G850W', 'SM-G850X', 'SM-G850Y',
                    'SM-G860P', 'SM-G870A', 'SM-G870D', 'SM-G870F', 'SM-G870F0', 'SM-G870W',
                    'SM-G8750', 'SM-G8850', 'SM-G8858', 'SM-G885F', 'SM-G885K', 'SM-G885L',
                    'SM-G885S', 'SM-G885X', 'SM-G885Y', 'SM-G8870', 'SM-G887F', 'SM-G887N',
                    'SM-G888N0', 'SM-G889A', 'SM-G889G', 'SM-G890A', 'SM-G891', 'SM-G891A',
                    'SM-G892A', 'SM-G892A', 'SM-G892U', 'SM-G9006V', 'SM-G9008V', 'SM-G9009D',
                    'SM-G900A', 'SM-G900AZ', 'SM-G900F', 'SM-G900FD', 'SM-G900FQ', 'SM-G900H',
                    'SM-G900I', 'SM-G900J', 'SM-G900K', 'SM-G900L', 'SM-G900M', 'SM-G900MD',
                    'SM-G900P', 'SM-G900R4', 'SM-G900R6', 'SM-G900R7', 'SM-G900S', 'SM-G900T',
                    'SM-G900T1', 'SM-G900T3', 'SM-G900V', 'SM-G900W8', 'SM-G901F', 'SM-G903M',
                    'SM-G903W', 'SM-G906K', 'SM-G906L', 'SM-G906S', 'SM-G906SKL', 'SM-G9092',
                    'SM-G9098', 'SM-G9198', 'SM-G9200', 'SM-G9208', 'SM-G9209', 'SM-G9209',
                    'SM-G920A', 'SM-G920AZ', 'SM-G920F', 'SM-G920FQ', 'SM-G920G1', 'SM-G920I',
                    'SM-G920K', 'SM-G920L', 'SM-G920P', 'SM-G920R4', 'SM-G920R6', 'SM-G920R7',
                    'SM-G920S', 'SM-G920T', 'SM-G920T1', 'SM-G920V', 'SM-G920W8', 'SM-G920X',
                    'SM-G925', 'SM-G9250', 'SM-G925A', 'SM-G925F', 'SM-G925FQ', 'SM-G925I',
                    'SM-G925ID', 'SM-G925K', 'SM-G925L', 'SM-G925P', 'SM-G925R4', 'SM-G925R6',
                    'SM-G925R7', 'SM-G925S', 'SM-G925T', 'SM-G925V', 'SM-G925W8', 'SM-G925X',
                    'SM-G925X', 'SM-G925Z', 'SM-G9280', 'SM-G9287', 'SM-G9287C', 'SM-G928A',
                    'SM-G928C', 'SM-G928F', 'SM-G928G', 'SM-G928i', 'SM-G928K', 'SM-G928L',
                    'SM-G928N', 'SM-G928N0', 'SM-G928P', 'SM-G928R4', 'SM-G928S', 'SM-G928T',
                    'SM-G928V', 'SM-G928W8', 'SM-G928X', 'SM-G9298', 'SM-G9300', 'SM-G9308',
                    'SM-G930A', 'SM-G930AZ', 'SM-G930F', 'SM-G930FD', 'SM-G930K', 'SM-G930L',
                    'SM-G930P', 'SM-G930R4', 'SM-G930R6', 'SM-G930R7', 'SM-G930S', 'SM-G930SKL',
                    'SM-G930T', 'SM-G930T1', 'SM-G930U', 'SM-G930V', 'SM-G930VC', 'SM-G930VL',
                    'SM-G930W', 'SM-G930W8', 'SM-G930X', 'SM-G9350', 'SM-G935A', 'SM-G935AU',
                    'SM-G935D', 'SM-G935F', 'SM-G935FD', 'SM-G935J', 'SM-G935K', 'SM-G935L',
                    'SM-G935P', 'SM-G935R4', 'SM-G935R6', 'SM-G935R7', 'SM-G935S', 'SM-G935T',
                    'SM-G935T1', 'SM-G935U', 'SM-G935V', 'SM-G935VC', 'SM-G935W', 'SM-G935W8',
                    'SM-G935X', 'SM-G950', 'SM-G9500', 'SM-G9508', 'SM-G950D', 'SM-G950F',
                    'SM-G950FD', 'SM-G950J', 'SM-G950N', 'SM-G950U', 'SM-G950U1', 'SM-G950W',
                    'SM-G950X', 'SM-G950XC', 'SM-G955', 'SM-G9550', 'SM-G9558', 'SM-G955F',
                    'SM-G955FD', 'SM-G955J', 'SM-G955N', 'SM-G955U', 'SM-G955U1', 'SM-G955W',
                    'SM-G955X', 'SM-G955XU', 'SM-G9600', 'SM-G9608', 'SM-G960F', 'SM-G960FD',
                    'SM-G960L', 'SM-G960N', 'SM-G960U', 'SM-G960U1', 'SM-G960US', 'SM-G960UX',
                    'SM-G960W', 'SM-G960X', 'SM-G960XU', 'SM-G9650', 'SM-G965F', 'SM-G965FD',
                    'SM-G965J', 'SM-G965N', 'SM-G965U', 'SM-G965U1', 'SM-G965UX', 'SM-G965W',
                    'SM-G965X', 'SM-G965XU', 'SM-G9700', 'SM-G9708', 'SM-G970F', 'SM-G970FD',
                    'SM-G970N', 'SM-G970U', 'SM-G970U1', 'SM-G970W', 'SM-G970X', 'SM-G970XC',
                    'SM-G970XN', 'SM-G970XU', 'SM-G9730', 'SM-G9730Z', 'SM-G9738', 'SM-G973C',
                    'SM-G973D', 'SM-G973F', 'SM-G973J', 'SM-G973N', 'SM-G973U', 'SM-G973U1',
                    'SM-G973W', 'SM-G973XC', 'SM-G973XN', 'SM-G973XU', 'SM-G9750', 'SM-G9758',
                    'SM-G975F', 'SM-G975FD', 'SM-G975N', 'SM-G975U', 'SM-G975U1', 'SM-G975W',
                    'SM-G975XC', 'SM-G975XN', 'SM-G975XU', 'SM-G977B', 'SM-G977N', 'SM-G977P',
                    'SM-G977T', 'SM-G977U', 'SM-G97xF', 'SM-G980A', 'SM-G980F', 'SM-G9810',
                    'SM-G981A', 'SM-G981B', 'SM-G981C', 'SM-G981N', 'SM-G981U', 'SM-G981U1',
                    'SM-G981V', 'SM-G981W', 'SM-G985F', 'SM-G985X', 'SM-G9860', 'SM-G986B',
                    'SM-G986N', 'SM-G986U', 'SM-G986U1', 'SM-G986W', 'SM-G9880', 'SM-G988B',
                    'SM-G988BR', 'SM-G988N', 'SM-G988U', 'SM-G988W', 'SM-G990B', 'SM-G990E',
                    'SM-G990U', 'SM-G9910', 'SM-G991BR', 'SM-G991N', 'SM-G991XU', 'SM-G9960',
                    'SM-G9968', 'SM-G996BR', 'SM-G996N', 'SM-G996X', 'SM-G996XU', 'SM-G9980',
                    'SM-G9988', 'SM-G998N', 'SM-G998X', 'SM-G998XU', 'SM-J730F', 'SM-M017F')
    },

    "versions" : {
        "nexus": {
            '5.0': {
                'minor_range': (0, 3),
                'build_number': ('LRX21{s}', 'LRX22{s}')
            },
            '5.1': {
                'minor_range': (0, 1),
                'build_number': ('LMY47{s}', 'LMY48{s}', 'LYZ28{s}', 'LVY48{s}', 'LMY49{s}')
            },
            '6.0': {
                'minor_range': (0, 1),
                'build_number': ('MRA58{s}', 'MRA59{s}', 'MDA89{s}', 'MDB08{s}', 'MMB29{s}', 'MXC14{s}', 'MHC19{s}',
                                'MOB30{s}', 'M5C14{s}', 'MTC19{s}', 'MMB30{s}', 'MXC89{s}', 'MTC20{s}', 'MOB31{s}')
            },
            '7.0': {
                'minor_range': (0, 0),
                'build_number': ('NRD90{s}', 'NRD91{s}', 'NBD91{s}', 'N5D91{s}', 'NBD92{s}')
            },
            '7.1': {
                'minor_range': (0, 2),
                'build_number': ('NDE63{s}', 'NMF26{s}', 'NMF27{s}', 'N2G47{s}', 'NHG47{s}', 'NJH34{s}', 'NKG47{s}',
                                'NOF27{s}', 'N6F26{s}', 'N4F27{s}', 'N8I11{s}', 'NGI55{s}', 'N9F27{s}')
            },
            '8.0': {
                'minor_range': (0, 5),
                'build_number': ('OPR1.{d}.{v}', 'OPR2.{d}.{v}', 'OPR3.{d}.{v}', 'OPR4.{d}.{v}', 'OPR5.{d}.{v}',
                                'OPR6.{d}.{v}', 'OPD1.{d}.{v}', 'OPD2.{d}.{v}', 'OPD3.{d}.{v}')
            },
            '8.1': {
                'minor_range': (0, 7),
                'build_number': ('OPM1.{d}.{v}', 'OPM2.{d}.{v}', 'OPM3.{d}.{v}', 'OPM4.{d}.{v}', 'OPM5.{d}.{v}')
            }
        },

        "pixel" : {
            '8.0': {
                'minor_range': (0, 5),
                'build_number': ('OPR1.{d}.{v}', 'OPR2.{d}.{v}', 'OPR3.{d}.{v}', 'OPR4.{d}.{v}', 'OPR5.{d}.{v}',
                                'OPR6.{d}.{v}', 'OPD1.{d}.{v}', 'OPD2.{d}.{v}', 'OPD3.{d}.{v}')
            },
            '8.1': {
                'minor_range': (0, 7),
                'build_number': ('OPM1.{d}.{v}', 'OPM2.{d}.{v}', 'OPM3.{d}.{v}', 'OPM4.{d}.{v}', 'OPM5.{d}.{v}')
            },
            '9.0': {
                'minor_range': (0, 0),
                'build_number': ('PPR1.{d}.{v}', 'PPR2.{d}.{v}', 'PD1A.{d}.{v}', 'PQ1A.{d}.{v}', 'PQ2A.{d}.{v}',
                                'PQ3A.{d}.{v}', 'PQ3B.{d}.{v}', 'QQ2A.{d}.{v}')
            },
            '10.0': {
                'minor_range': (0, 0),
                'build_number': ('QD1A.{d}.{v}', 'QQ1B.{d}.{v}', 'QQ1C.{d}.{v}', 'QQ1D.{d}.{v}', 'QQ2A.{d}.{v}')
            },
            '11.0': {
                'minor_range': (0, 0),
                'build_number': ('RP1A.{d}.{v}', 'RP1B.{d}.{v}', 'RP1C.{d}.{v}', 'RP1D.{d}.{v}', 'RD1A.{d}.{v}',
                                'RD1B.{d}.{v}', 'RQAA.{d}.{v}', 'RQ3A.{d}.{v}', 'RQ1D.{d}.{v}')
            },
            '12.0': {
                'minor_range': (0, 0),
                'build_number': ('SP1A.{d}.{v}', 'SD1A.{d}.{v}', 'SQ1D.{d}.{v}', 'SQ1A.{d}.{v}', 'SQ1D.{d}.{v}')
            },
        },

        "samsung": {
            '5.0': {
                'minor_range': (0, 3),
                'build_number': ('LRX21{s}', 'LRX22{s}')
            },
            '5.1': {
                'minor_range': (0, 1),
                'build_number': ('LMY47{s}', 'LMY48{s}', 'LYZ28{s}', 'LVY48{s}', 'LMY49{s}')
            },
            '6.0': {
                'minor_range': (0, 1),
                'build_number': ('MRA58{s}', 'MRA59{s}', 'MDA89{s}', 'MDB08{s}', 'MMB29{s}', 'MXC14{s}', 'MHC19{s}',
                                'MOB30{s}', 'M5C14{s}', 'MTC19{s}', 'MMB30{s}', 'MXC89{s}', 'MTC20{s}', 'MOB31{s}')
            },
            '7.0': {
                'minor_range': (0, 0),
                'build_number': ('NRD90{s}', 'NRD91{s}', 'NBD91{s}', 'N5D91{s}', 'NBD92{s}')
            },
            '7.1': {
                'minor_range': (0, 2),
                'build_number': ('NDE63{s}', 'NMF26{s}', 'NMF27{s}', 'N2G47{s}', 'NHG47{s}', 'NJH34{s}', 'NKG47{s}',
                                'NOF27{s}', 'N6F26{s}', 'N4F27{s}', 'N8I11{s}', 'NGI55{s}', 'N9F27{s}')
            },
            '8.0': {
                'minor_range': (0, 5),
                'build_number': ('OPR6.{d}.{v}', 'OPR1.{d}.{v}', 'OPR4.{d}.{v}', 'OPR5.{d}.{v}', 'OPD1.{d}.{v}')
            },
            '8.1': {
                'minor_range': (0, 7),
                'build_number': ('OPM1.{d}.{v}', 'OPM2.{d}.{v}', 'OPM3.{d}.{v}', 'OPM5.{d}.{v}')
            },
            '9.0': {
                'minor_range': (0, 0),
                'build_number': ('PPR1.{d}.{v}', 'PPR2.{d}.{v}', 'PD1A.{d}.{v}', 'PQ1A.{d}.{v}', 'PQ2A.{d}.{v}', 'PQ3A.{d}.{v}')
            },
            '10.0': {
                'minor_range': (0, 0),
                'build_number': ('QP1A.{d}.{v}', 'QQ1A.{d}.{v}', 'QQ1B.{d}.{v}', 'QQ1C.{d}.{v}', 'PQ2A.{d}.{v}', 'QQ1D.{d}.{v}'
                                'QQ2A.{d}.{v}', 'QQ3A.{d}.{v}', 'QD4A.{d}.{v}')
            },
            '11.0': {
                'minor_range': (0, 0),
                'build_number': ('RP1A.{d}.{v}', 'RD1A.{d}.{v}', 'RQ1A.{d}.{v}', 'RQ1C.{d}.{v}', 'RQ1D.{d}.{v}', 'RQ2A.{d}.{v}',
                                'RQ3A.{d}.{v}', 'RD2A.{d}.{v}')
            },
            '12.0': {
                'minor_range': (0, 0),
                'build_number': ('SP1A.{d}.{v}', 'SD1A.{d}.{v}', 'SQ1A.{d}.{v}', 'SQ1D.{d}.{v}')
            },
    }
    }

    }