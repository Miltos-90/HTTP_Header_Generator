""" This module declares all constants and regexes needed for the Parser object (see parser.py).
    Based on the ua_parser_py repo (see https://github.com/vitalibo/ua-parser-py)
"""

from ..utils        import readFile
from ..definitions  import EMPTY
from typing         import TypedDict, List, Union, Dict
import re

# Read constants
WINDOWS_VERSIONS = readFile('windows_versions.json')
SAFARI_VERSIONS  = readFile('safari_versions.json')


def strMapper(
    str_: str,              # String to be mapped to the value of the corresponding key of the map_ dict 
    map_: Dict[str, str],   # Mapper dictionary (either WINDOWS_VERSIONS or SAFARI_VERSIONS)
    UNK : str  = '?',       # Token used as unknown key (returned value is None)
    ) -> Union[str, None]:
    """ Maps a string to the corresponding value of a dictionary. 
    Used in some regex lists below
    """

    for key, value in map_.items():

        if key.lower() in str_.lower():

            if value == UNK : return None
            else            : return value
    
    return str_ # If you reach this point (str_ is not a key of the mapper dict), return the input string


""" Regex lists """

# Regex list class
class REGEXDICT(TypedDict):
    regex: re.Pattern
    props: dict

BROWSER: List[REGEXDICT] = [
    {   # Chrome for Android/iOS
        'regex' : re.compile(r'\b(?:crmo|crios)\/([\w\.]+)', re.I),                           
        'props' : {'version': None, 'name': 'Chrome'}
    },{ # Microsoft Edge
        'regex' : re.compile(r'edg(?:e|ios|a)?\/([\w\.]+)', re.I),
        'props' : {'version': None, 'name': 'Edge'}
    },{ # Opera Mini
        'regex' : re.compile(r'(opera mini)\/([-\w\.]+)', re.I),
        'props' : {'name': None, 'version': None}
    },{ # Opera Mobi/Tablet
        'regex' : re.compile(r'(opera [mobiletab]{3,6})\b.+version\/([-\w\.]+)', re.I),       
        'props' : {'name': None, 'version': None}
    },{ # Opera
        'regex' : re.compile(r'(opera)(?:.+version\/|[\/ ]+)([\w\.]+)', re.I),                
        'props' : {'name': None, 'version': None}

    # Presto based

    },{ # Opera mini on iphone >= 8.0
        'regex' : re.compile(r'opios[\/ ]+([\w\.]+)', re.I),                                  
        'props' : {'version': None, 'name': 'Opera Mini'}
    },{ # Opera Webkit
        'regex' : re.compile(r'\bopr\/([\w\.]+)', re.I),                                      
        'props' : {'version': None, 'name': 'Opera'}
    
    # Mixed 
    
    },{ # Kindle
        'regex' : re.compile(r'(kindle)\/([\w\.]+)', re.I),                                 
        'props' : {'name': None, 'version': None}
    },{ # Lunascape/Maxthon/Netfront/Jasmine/Blazer
        'regex' : re.compile(r'(lunascape|maxthon|netfront|jasmine|blazer)[\/ ]?([\w\.]*)', re.I),  
        'props' : {'name': None, 'version': None}

    # Trident based

    },{ # Avant/IEMobile/SlimBrowser
        'regex' : re.compile(r'(avant |iemobile|slim)(?:browser)?[\/ ]?([\w\.]*)', re.I),           
        'props' : {'name': None, 'version': None}
    },{ # Baidu Browser
        'regex' : re.compile(r'(ba?idubrowser)[\/ ]?([\w\.]+)', re.I),
        'props' : {'name': None, 'version': None}
    },{ # Internet Explorer
        'regex' : re.compile(r'(?:ms|\()(ie) ([\w\.]+)', re.I),
        'props' : {'name': None, 'version': None}

    # Webkit/KHTML based

    },{ # Flock/RockMelt/Midori/Epiphany/Silk/Skyfire/Bolt/Iron/Iridium/PhantomJS/Bowser/QupZilla/Falkon/Rekonq/Puffin/Brave/Whale/QQBrowserLite/QQ, aka ShouQ
        'regex' : re.compile(r'(flock|rockmelt|midori|epiphany|silk|skyfire|ovibrowser|bolt|iron|vivaldi|iridium|phantomjs|bowser|quark|qupzilla|falkon|rekonq|puffin|brave|whale|qqbrowserlite|qq)\/([-\w\.]+)', re.I),  
        'props' : {'name': None, 'version': None}
    },{ # Weibo
        'regex' : re.compile(r'(weibo)__([\d\.]+)', re.I),
        'props' : {'name': None, 'version': None}
    },{ # UCBrowser
        'regex' : re.compile(r'(?:\buc? ?browser|(?:juc.+)ucweb)[\/ ]?([\w\.]+)', re.I),
        'props' : {'version': None, 'name': 'UCBrowser'}, 
    },{ # WeChat Desktop for Windows Built-in Browser
        'regex' : re.compile(r'\bqbcore\/([\w\.]+)', re.I),
        'props' : {'version': None, 'name': 'WeChat(Win) Desktop'}, 
    },{ # WeChat
        'regex' : re.compile(r'micromessenger\/([\w\.]+)', re.I),
        'props' : {'version': None, 'name': 'WeChat'}, 
    },{ # Konqueror
        'regex' : re.compile(r'konqueror\/([\w\.]+)', re.I),
        'props' : {'version': None, 'name': 'Konqueror'}, 
    },{ # IE11
        'regex' : re.compile(r'trident.+rv[: ]([\w\.]{1,9})\b.+like gecko', re.I),
        'props' : {'version': None, 'name': 'IE'} 
    },{ # Yandex
        'regex' : re.compile(r'yabrowser\/([\w\.]+)', re.I),
        'props' : {'version': None, 'name': 'Yandex'}, 
    },{ # Avast/AVG Secure Browser
        'regex' : re.compile(r'(avast|avg)\/([\w\.]+)', re.I),
        'props' : {
            'name'   : lambda s: re.sub(r'(.+)', '\\1 Secure Browser', s),
            'version': None
            }
    },{ # Firefox Focus
        'regex' : re.compile(r'\bfocus\/([\w\.]+)', re.I),                                  
        'props' : {'version': None, 'name': 'Firefox Focus'}, 
    },{ # Opera Touch
        'regex' : re.compile(r'\bopt\/([\w\.]+)', re.I),                                    
        'props' : {'version': None, 'name': 'Opera Touch'}, 
    },{ # Coc Coc Browser 
        'regex' : re.compile( r'coc_coc\w+\/([\w\.]+)', re.I),                              
        'props' : {'version': None, 'name': 'Coc Coc'},
    },{ # Dolphin
        'regex' : re.compile(r'dolfin\/([\w\.]+)', re.I),                                   
        'props' : {'version': None, 'name': 'Dolphin'}, 
    },{ # Opera Coast
        'regex' : re.compile(r'coast\/([\w\.]+)', re.I),                                    
        'props' : {'version': None, 'name': 'Opera Coast'}, 
    },{ # MIUI Browser
        'regex' : re.compile(r'miuibrowser\/([\w\.]+)', re.I),                              
        'props' : {'version': None, 'name': 'MIUI Browser'}, 
    },{ # Firefox for iOS
        'regex' : re.compile(r'fxios\/([-\w\.]+)', re.I),                                   
        'props' : {'version': None, 'name': 'Firefox'}, 
    },{ # 360
        'regex' : re.compile(r'\bqihu|(qi?ho?o?|360)browser', re.I),                        
        'props' : {'name': '360 Browser'},  
    },{ # Oculus/Samsung/Sailfish Browser 
        'regex' : re.compile(r'(oculus|samsung|sailfish)browser\/([\w\.]+)', re.I),
        'props' : {
            'name'   : lambda s: re.sub(r'(.+)', '\\1 Browser', s),
            'version': None
            },
    },{ # Comodo Dragon
        'regex' : re.compile(r'(comodo_dragon)\/([\w\.]+)', re.I),
        'props' : {
            'name'   : lambda s: re.sub(r'_', ' ', s),
            'version': None
            }, 
    },{ # Electron-based App
        'regex' : re.compile(r'(electron)\/([\w\.]+) safari', re.I),
        'props' : {'name': None, 'version': None}
    },{ # Tesla
        'regex' : re.compile(r'(tesla)(?: qtcarbrowser|\/(20\d\d\.[-\w\.]+))', re.I),
        'props' : {'name': None, 'version': None}
    },{ # QQBrowser/Baidu App/2345 Browser
        'regex' : re.compile(r'm?(qqbrowser|baiduboxapp|2345Explorer)[\/ ]?([\w\.]+)', re.I),
        'props' : {'name': None, 'version': None}
    },{ # SouGouBrowser
        'regex' : re.compile(r'(metasr)[\/ ]?([\w\.]+)', re.I),
        'props' : {'name': None} 
    },{ # LieBao Browser
        'regex' : re.compile(r'(lbbrowser)', re.I),
        'props' : {'name': None},
    },{ # LinkedIn App for iOS & Android
        'regex' : re.compile(r'\[(linkedin)app\]', re.I), 
        'props' : {'name': 'None'}, 
    
    # WebView

    },{ # Facebook App for iOS & Android
        'regex' : re.compile(r'((?:fban\/fbios|fb_iab\/fb4a)(?!.+fbav)|;fbav\/([\w\.]+);)', re.I), 
        'props' : {'name': 'Facebook', 'version': None},
    },{ # Kakao App
        'regex' : re.compile(r'(kakao(?:talk|story))[\/ ]([\w\.]+)', re.I),
        'props' : {'name': None, 'version': None}, 
    },{ # Naver App
        'regex' : re.compile(r'(naver)\(.*?(\d+\.[\w\.]+).*\)', re.I),
        'props' : {'name': None, 'version': None}, 
    },{ # Line App for iOS
        'regex' : re.compile(r'safari (line)\/([\w\.]+)', re.I),
        'props' : {'name': None, 'version': None}, 
    },{ # Line App for Android
        'regex' : re.compile(r'\b(line)\/([\w\.]+)\/iab', re.I),
        'props' : {'name': None, 'version': None}, 
    },{ # Chromium/Instagram
        'regex' : re.compile(r'(chromium|instagram)[\/ ]([-\w\.]+)', re.I),
        'props' : {'name': None, 'version': None}, 
    },{ # Google Search Appliance on iOS
        'regex' : re.compile(r'\bgsa\/([\w\.]+) .*safari\/', re.I),
        'props' : {'version': None, 'name': 'GSA'},                             
    },{ # Chrome Headless
        'regex' : re.compile(r'headlesschrome(?:\/([\w\.]+)| )', re.I),
        'props' : {'version': None, 'name': 'Chrome Headless'},            
    },{ # Chrome WebView
        'regex' : re.compile(r' wv\).+(chrome)\/([\w\.]+)', re.I),
        'props' : {'name': 'Chrome WebView', 'version': None},             
    },{ # Android Browser
        'regex' : re.compile(r'droid.+ version\/([\w\.]+)\b.+(?:mobile safari|safari)', re.I),
        'props' : {'version': None, 'name': 'Android Browser'},            
    },{ # Chrome/OmniWeb/Arora/Tizen/Nokia
        'regex' : re.compile(r'(chrome|omniweb|arora|[tizenoka]{5} ?browser)\/v?([\w\.]+)', re.I),
        'props' : {'name': None, 'version': None},                                      
    },{ # Mobile Safari
        'regex' : re.compile(r'version\/([\w\.]+) .*mobile\/\w+ (safari)', re.I),
        'props' : {'version': None, 'name': 'Mobile Safari'},                   
    },{ # Safari & Safari Mobile
        'regex' : re.compile(r'version\/([\w\.]+) .*(mobile ?safari|safari)', re.I),
        'props' : {'version': None, 'name': None},                                      
    },{ # Safari < 3.0 
        'regex' : re.compile(r'webkit.+?(mobile ?safari|safari)(\/[\w\.]+)', re.I),
        'props' : {
            'name'   : None,                                                           
            'version': lambda s: strMapper(s, SAFARI_VERSIONS)
            },        
    },{
        'regex' : re.compile(r'(webkit|khtml)\/([\w\.]+)', re.I), 
        'props' : {'name': None, 'version': None},

    # Gecko based

    },{ # Netscape 
        'regex' : re.compile(r'(navigator|netscape\d?)\/([-\w\.]+)', re.I),                           
        'props' : {'name': 'Netscape', 'version': None},
    },{ # Firefox Reality
        'regex' : re.compile(r'mobile vr; rv:([\w\.]+)\).+firefox', re.I),                            
        'props' : {'version': None, 'name': 'Firefox Reality'},            
    },{ # Flow
        'regex' : re.compile(r'ekiohf.+(flow)\/([\w\.]+)', re.I),                                   
        'props' : {'name': None, 'version': None}
    },{ # Swiftfox
        'regex' : re.compile(r'(swiftfox)', re.I),
        'props' : {'name': None, 'version': None}
    },{ # IceDragon/Iceweasel/Camino/Chimera/Fennec/Maemo/Minimo/Conkeror/Klar
        'regex' : re.compile(r'(icedragon|iceweasel|camino|chimera|fennec|maemo browser|minimo|conkeror|klar)[\/ ]?([\w\.\+]+)', re.I),                         
        'props' : {'name': None, 'version': None}
    },{ # Firefox/SeaMonkey/K-Meleon/IceCat/IceApe/Firebird/Phoenix
        'regex' : re.compile(r'(seamonkey|k-meleon|icecat|iceape|firebird|phoenix|palemoon|basilisk|waterfox)\/([-\w\.]+)$', re.I),                             
        'props' : {'name': None, 'version': None}
    },{ # Other Firefox-based
        'regex' : re.compile(r'(firefox)\/([\w\.]+)', re.I),                                        
        'props' : {'name': None, 'version': None}
    },{ # Mozilla
        'regex' : re.compile(r'(mozilla)\/([\w\.]+) .+rv\:.+gecko\/\d+', re.I),                     
        'props' : {'name': None, 'version': None}
    },{ # Polaris/Lynx/Dillo/iCab/Doris/Amaya/w3m/NetSurf/Sleipnir/Obigo/Mosaic/Go/ICE/UP.Browser
        'regex' : re.compile(r'(polaris|lynx|dillo|icab|doris|amaya|w3m|netsurf|sleipnir|obigo|mosaic|(?:go|ice|up)[\. ]?browser)[-\/ ]?v?([\w\.]+)', re.I),
        'props' : {'name': None, 'version': None}
    },{ # Links
        'regex' : re.compile(r'(links) \(([\w\.]+)', re.I),
        'props' : {'name': None, 'version': None}
    },{ # Panasonic Viera
        'regex' : re.compile(r'panasonic;(viera)', re.I),
        'props' : {'name': None, 'version': None}
    },{ # Cobalt
        'regex' : re.compile(r'(cobalt)\/([\w\.]+)', re.I),
        'props' : {
            'name'   : None, 
            'version': lambda s: re.sub(r'[^\d\.]+.', EMPTY, s)
            }
    }
]

CPU: List[REGEXDICT] = [
    {   # AMD64 (x64)
        'regex' : re.compile(r'(?:(amd|x(?:(?:86|64)[-_])?|wow|win)64)[;\)]', re.I),
        'props' : {'architecture': 'amd64'},                              
    },{ # IA32 (quicktime)
        'regex' : re.compile(r'(ia32(?=;))', re.I),                                         
        'props' : {'architecture': lambda s: s.lower()},                       
    },{ # IA32 (x86)
        'regex' : re.compile(r'((?:i[346]|x)86)[;\)]', re.I),                               
        'props' : {'architecture': 'ia32'}, 
    },{ # ARM64
        'regex' : re.compile(r'\b(aarch64|arm(v?8e?l?|_?64))\b', re.I),                     
        'props' : {'architecture': 'arm64'}, 
    },{ # ARMHF
        'regex' : re.compile(r'\b(arm(?:v[67])?ht?n?[fl]p?)\b', re.I),                      
        'props' : {'architecture': 'armhf'}, 
    },{ # PocketPC mistakenly identified as PowerPC
        'regex' : re.compile(r'windows (ce|mobile); ppc;', re.I),                           
        'props' : {'architecture': 'arm'},  
    },{ # PowerPC
        'regex' : re.compile(r'((?:ppc|powerpc)(?:64)?)(?: mac|;|\))', re.I),               
        'props' : {'architecture': lambda s: re.sub(r'ower', EMPTY, s).lower()},
    },{ # SPARC
        'regex' : re.compile(r'(sun4\w)[;\)]', re.I),                                       
        'props' : {'architecture': 'sparc'}, 
    },{ # IA64, 68K, ARM/64, AVR/32, IRIX/64, MIPS/64, SPARC/64, PA-RISC
        'regex' : re.compile(r'((?:avr32|ia64(?=;))|68k(?=\))|\barm(?=v(?:[1-7]|[5-7]1)l?|;|eabi)|(?=atmel )avr|(?:irix|mips|sparc)(?:64)?\b|pa-risc)', re.I),  
        'props' : {'architecture': lambda s: s.lower()}                              
    }
]

DEVICE: List[REGEXDICT] = [
    # Mobiles & Tablets

        # Samsung devices 
    {   
        'regex' : re.compile(r'\b(sch-i[89]0\d|shw-m380s|sm-[pt]\w{2,4}|gt-[pn]\d{2,4}|sgh-t8[56]9|nexus 10)', re.I),   
        'props' : {'model': None, 'vendor': 'Samsung', 'type': 'tablet'}, 
    },{
        'regex' : re.compile(r'\b((?:s[cgp]h|gt|sm)-\w+|galaxy nexus)', re.I), 
        'props' : {'model': None, 'vendor': 'Samsung', 'type': 'mobile'}, 
        },{
        'regex' : re.compile(r'samsung[- ]([-\w]+)', re.I), 
        'props' : {'model': None, 'vendor': 'Samsung', 'type': 'mobile'},  
        },{
        'regex' : re.compile(r'sec-(sgh\w+)', re.I), 
        'props' : {'model': None, 'vendor': 'Samsung', 'type': 'mobile'},
    
        # Apple

    },{ # iPod/iPhone
        'regex' : re.compile(r'\((ip(?:hone|od)[\w ]*);', re.I),
        'props' : {'model': None, 'vendor': 'Apple', 'type': 'mobile'}, 
    },{ # iPad
        'regex' : re.compile(r'\((ipad);[-\w\),; ]+apple', re.I),
        'props' : {'model': None, 'vendor': 'Apple', 'type': 'tablet'}, 
    },{
        'regex' : re.compile(r'applecoremedia\/[\w\.]+ \((ipad)', re.I), 
        'props' : {'model': None, 'vendor': 'Apple', 'type': 'tablet'}, 
    },{
        'regex' : re.compile(r'\b(ipad)\d\d?,\d\d?[;\]].+ios', re.I), 
        'props' : {'model': None, 'vendor': 'Apple', 'type': 'tablet'},
    },{
        'regex' : re.compile(r'(macintosh);', re.I), 
        'props' : {'model': None, 'vendor': 'Apple'},
    },{ # Sharp
        'regex' : re.compile(r'\b(sh-?[altvz]?\d\d[a-ekm]?)', re.I), 
        'props' : {'model': None, 'vendor': 'Sharp', 'type': 'mobile'},
    },{ # Huawei
        'regex' : re.compile(r'\b((?:ag[rs][23]?|bah2?|sht?|btv)-a?[lw]\d{2})\b(?!.+d\/s)', re.I),
        'props' : {'model': None, 'vendor': 'Huawei', 'type': 'tablet'}, 
    },{
        'regex' : re.compile(r'(?:huawei|honor)([-\w ]+)[;\)]', re.I), 
        'props' : {'model': None, 'vendor': 'Huawei', 'type': 'tablet'}, 
    },{
        'regex' : re.compile(r'\b(nexus 6p|\w{2,4}-[atu]?[ln][01259x][012359][an]?)\b(?!.+d\/s)', re.I), 
        'props' : {'model': None, 'vendor': 'Huawei', 'type': 'mobile'}, 
    },{ # Xiaomi POCO
        'regex' : re.compile(r'\b(poco[\w ]+)(?: bui|\))', re.I),
        'props' : {
            'model'  : lambda s: re.sub('_', ' ', s), 
            'vendor' : 'Xiaomi', 
            'type'   : 'mobile'
            }, 
    },{ # Xiaomi Hongmi 'numeric' models
        'regex' : re.compile(r'\b; (\w+) build\/hm\1', re.I), 
        'props' : {
            'model'  : lambda s: re.sub('_', ' ', s), 
            'vendor' : 'Xiaomi', 
            'type'   : 'mobile'
            }, 
    },{ # Xiaomi Hongmi
        'regex' : re.compile(r'\b(hm[-_ ]?note?[_ ]?(?:\d\w)?) bui', re.I),
        'props' : {
            'model'  : lambda s: re.sub('_', ' ', s), 
            'vendor' : 'Xiaomi', 
            'type'   : 'mobile'
            }, 
    },{ # Xiaomi Redmi
        'regex' : re.compile(r'\b(redmi[\-_ ]?(?:note|k)?[\w_ ]+)(?: bui|\))', re.I),
        'props' : {
            'model'  : lambda s: re.sub('_', ' ', s), 
            'vendor' : 'Xiaomi', 
            'type'   : 'mobile'
            }, 
    },{ # Xiaomi Mi
        'regex' : re.compile(r'\b(mi[-_ ]?(?:a\d|one|one[_ ]plus|note lte|max)?[_ ]?(?:\d?\w?)[_ ]?(?:plus|se|lite)?)(?: bui|\))', re.I),
        'props' : {
            'model'  : lambda s: re.sub('_', ' ', s), 
            'vendor' : 'Xiaomi', 
            'type'   : 'mobile'
            }, 
    },{ # Mi Pad tablets
        'regex' : re.compile(r'\b(mi[-_ ]?(?:pad)(?:[\w_ ]+))(?: bui|\))', re.I),
        'props' : {
            'model'  : lambda s: re.sub('_', ' ', s), 
            'vendor' : 'Xiaomi', 
            'type'   : 'tablet'
            }, 
    },{ # OPPO
        'regex' : re.compile(r'; (\w+) bui.+ oppo', re.I),
        'props' : {'model': None, 'vendor': 'OPPO', 'type': 'mobile'}
    },{
        'regex' : re.compile(r'\b(cph[12]\d{3}|p(?:af|c[al]|d\w|e[ar])[mt]\d0|x9007|a101op)\b', re.I), 
        'props' : {'model': None, 'vendor': 'OPPO', 'type': 'mobile'}
    },{ # Vivo
        'regex' : re.compile(r'vivo (\w+)(?: bui|\))', re.I), 
        'props' : {'model': None, 'vendor': 'Vivo', 'type': 'mobile'}
    },{ 
        'regex' : re.compile(r'\b(v[12]\d{3}\w?[at])(?: bui|;)', re.I), 
        'props' : {'model': None, 'vendor': 'Vivo', 'type': 'mobile'}
    },{ # Realme
        'regex' : re.compile(r'\b(rmx[12]\d{3})(?: bui|;|\))', re.I), 
        'props' : {'model': None, 'vendor': 'Realme', 'type': 'mobile'}
    },{ # Motorola
        'regex' : re.compile(r'\b(milestone|droid(?:[2-4x]| (?:bionic|x2|pro|razr))?:?( 4g)?)\b[\w ]+build\/', re.I), 
        'props' : {'model': None, 'vendor': 'Motorola', 'type': 'mobile'}, 
    },{ 
        'regex' : re.compile(r'\bmot(?:orola)?[- ](\w*)', re.I), 
        'props' : {'model': None, 'vendor': 'Motorola', 'type': 'mobile'}, 
    },{ 
        'regex' : re.compile(r'((?:moto[\w\(\) ]+|xt\d{3,4}|nexus 6)(?= bui|\)))', re.I), 
        'props' : {'model': None, 'vendor': 'Motorola', 'type': 'mobile'}, 
    },{
        'regex' : re.compile(r'\b(mz60\d|xoom[2 ]{0,2}) build\/', re.I), 
        'props' : {'model': None, 'vendor': 'Motorola', 'type': 'tablet'},  
    },{  # LG
        'regex' : re.compile(r'((?=lg)?[vl]k\-?\d{3}) bui| 3\.[-\w; ]{10}lg?-([06cv9]{3,4})', re.I), 
        'props' : {'model': None, 'vendor': 'LG', 'type': 'tablet'},  
    },{
        'regex' : re.compile(r'(lm(?:-?f100[nv]?|-[\w\.]+)(?= bui|\))|nexus [45])', re.I), 
        'props' : {'model': None, 'vendor': 'LG', 'type': 'mobile'},  
    },{
        'regex' : re.compile(r'\blg[-e;\/ ]+((?!browser|netcast|android tv)\w+)', re.I), 
        'props' : {'model': None, 'vendor': 'LG', 'type': 'mobile'},  
    },{
        'regex' : re.compile(r'\blg-?([\d\w]+) bui',  re.I), 
        'props' : {'model': None, 'vendor': 'LG', 'type': 'mobile'},  
    },{ # Lenovo 
        'regex' : re.compile(r'(ideatab[-\w ]+)', re.I), 
        'props' : {'model': None, 'vendor': 'Lenovo', 'type': 'tablet'},  
    },{
        'regex' : re.compile(r'lenovo ?(s[56]000[-\w]+|tab(?:[\w ]+)|yt[-\d\w]{6}|tb[-\d\w]{6})', re.I), 
        'props' : {'model': None, 'vendor': 'Lenovo', 'type': 'tablet'},  
    },{ # Nokia
        'regex' : re.compile(r'(?:maemo|nokia).*(n900|lumia \d+)', re.I), 
        'props' : {
            'model'  : lambda s: re.sub('_', ' ', s), 
            'vendor' : 'Nokia', 
            'type'   : 'mobile'
            }, 
    },{
        'regex' : re.compile(r'nokia[-_ ]?([-\w\.]*)', re.I), 
        'props' : {
            'model'  : lambda s: re.sub('_', ' ', s), 
            'vendor' : 'Nokia', 
            'type'   : 'mobile'
            }, 
    },{ # Google Pixel C
        'regex' : re.compile(r'(pixel c)\b',  re.I), 
        'props' : {'model': None, 'vendor': 'Google', 'type': 'tablet'},
    },{ # Google Pixel
        'regex' : re.compile(r'droid.+; (pixel[\daxl ]{0,6})(?: bui|\))',  re.I), 
        'props' : {'model': None, 'vendor': 'Google', 'type': 'mobile'},
    },{ # Sony
        'regex' : re.compile(r'droid.+ ([c-g]\d{4}|so[-gl]\w+|xq-a\w[4-7][12])(?= bui|\).+chrome\/(?![1-6]{0,1}\d\.))',  re.I), 
        'props' : {'model': None, 'vendor': 'Sony', 'type': 'mobile'},
    },{
        'regex' : re.compile(r'sony tablet [ps]',  re.I), 
        'props' : {'model': 'Xperia Tablet', 'vendor': 'Sony', 'type': 'tablet'}, 
    },{
        'regex' : re.compile(r'\b(?:sony)?sgp\w+(?: bui|\))',  re.I), 
        'props' : {'model': 'Xperia Tablet', 'vendor': 'Sony', 'type': 'tablet'}, 
    },{ # OnePlus
        'regex' : re.compile(r' (kb2005|in20[12]5|be20[12][59])\b', re.I), 
        'props' : {'model': None, 'vendor': 'OnePlus', 'type': 'mobile'}, 
    },{
        'regex' : re.compile(r'(?:one)?(?:plus)? (a\d0\d\d)(?: b|\))',  re.I), 
        'props' : {'model': None, 'vendor': 'OnePlus', 'type': 'mobile'}, 
    },{ # Amazon
        'regex' : re.compile(r'(alexa)webm', re.I), 
        'props' : {'model': None, 'vendor': 'Amazon', 'type': 'tablet'}, 
    },{ # Kindle Fire without Silk
        'regex' : re.compile(r'(kf[a-z]{2}wi)( bui|\))', re.I), 
        'props' : {'model': None, 'vendor': 'Amazon', 'type': 'tablet'}, 
    },{ # Kindle Fire HD
        'regex' : re.compile(r'(kf[a-z]+)( bui|\)).+silk\/', re.I), 
        'props' : {'model': None, 'vendor': 'Amazon', 'type': 'tablet'}, 
    },{ # Fire Phone
        'regex' : re.compile(r'((?:sd|kf)[0349hijorstuw]+)( bui|\)).+silk\/', re.I), 
        'props' : {
            'model'  : lambda s: re.sub(r'(.+)', 'Fire Phone \\1', s), 
            'vendor' : 'Amazon', 
            'type'   : 'mobile'
            }, 
    },{ # BlackBerry PlayBook
        'regex' : re.compile(r'(playbook);[-\w\),; ]+(rim)', re.I), 
        'props' : {'model': None, 'vendor' : None, 'type': 'tablet'},
    },{ # BlackBerry 10
        'regex' : re.compile(r'\b((?:bb[a-f]|st[hv])100-\d)', re.I), 
        'props' : {'model': None, 'vendor': 'BlackBerry', 'type': 'mobile'}, 
    },{ # BlackBerry 10
        'regex' : re.compile(r'\(bb10; (\w+)', re.I), 
        'props' : {'model': None, 'vendor': 'BlackBerry', 'type': 'mobile'}, 
    },{ # Asus
        'regex' : re.compile(r'(?:\b|asus_)(transfo[prime ]{4,10} \w+|eeepc|slider \w+|nexus 7|padfone|p00[cj])', re.I), 
        'props' : {'model': None, 'vendor': 'ASUS', 'type': 'tablet'}, 
    },{
        'regex' : re.compile(r' (z[bes]6[027][012][km][ls]|zenfone \d\w?)\b', re.I), 
        'props' : {'model': None, 'vendor': 'ASUS', 'type': 'mobile'}, 
    },{ # HTC Nexus 9
        'regex' : re.compile(r'(nexus 9)', re.I), 
        'props' : {'model': None, 'vendor': 'HTC', 'type': 'tablet'}, 
    },{ # HTC
        'regex' : re.compile(r'(htc)[-;_ ]{1,2}([\w ]+(?=\)| bui)|\w+)', re.I), 
        'props' : {
            'vendor': None, 
            'model' : lambda s: re.sub('_', ' ', s), 
            'type'  : 'mobile'
            },
    },{ # ZTE
        'regex' : re.compile(r'(zte)[- ]([\w ]+?)(?: bui|\/|\))', re.I), 
        'props' : {
            'vendor': None, 
            'model' : lambda s: re.sub('_', ' ', s),
            'type'  : 'mobile'}
    },{ # Alcatel/GeeksPhone/Nexian/Panasonic/Sony
        'regex' : re.compile(r'(alcatel|geeksphone|nexian|panasonic|sony)[-_ ]?([-\w]*)', re.I), 
        'props' : {
            'vendor': None, 
            'model' : lambda s: re.sub('_', ' ', s),
            'type'  : 'mobile'}
    },{ # Acer
        'regex' : re.compile(r'droid.+; ([ab][1-7]-?[0178a]\d\d?)', re.I), 
        'props' : {'model': None, 'vendor': 'Acer', 'type': 'tablet'}, 
    },{ # Meizu
        'regex' : re.compile(r'\bmz-([-\w]{2,})', re.I), 
        'props' : {'model': None, 'vendor': 'Meizu', 'type': 'mobile'}, 
    },{
        'regex' : re.compile(r'droid.+; (m[1-5] note) bui', re.I), 
        'props' : {'model': None, 'vendor': 'Meizu', 'type': 'mobile'}, 
    },{ # BlackBerry/BenQ/Palm/Sony-Ericsson/Acer/Asus/Dell/Meizu/Motorola/Polytron
        'regex' : re.compile(r'(blackberry|benq|palm(?=\-)|sonyericsson|acer|asus|dell|meizu|motorola|polytron)[-_ ]?([-\w]*)', re.I), 
        'props' : {'vendor': None, 'model': None, 'type': 'mobile'}, 
    },{ # HP iPAQ
        'regex' : re.compile(r'(hp) ([\w ]+\w)', re.I), 
        'props' : {'vendor': None, 'model': None, 'type': 'mobile'},  
    },{  # Asus
        'regex' : re.compile(r'(asus)-?(\w+)', re.I), 
        'props' : {'vendor': None, 'model': None, 'type': 'mobile'}, 
    },{ # Microsoft Lumia
        'regex' : re.compile(r'(microsoft); (lumia[\w ]+)', re.I), 
        'props' : {'vendor': None, 'model': None, 'type': 'mobile'}, 
    },{ # Lenovo
        'regex' : re.compile(r'(lenovo)[-_ ]?([-\w]+)', re.I), 
        'props' : {'vendor': None, 'model': None, 'type': 'mobile'}, 
    },{ # Jolla
        'regex' : re.compile(r'(jolla)', re.I), 
        'props' : {'vendor': None, 'model': None, 'type': 'mobile'}, 
    },{ # OPPO
        'regex' : re.compile(r'(oppo) ?([\w ]+) bui', re.I), 
        'props' : {'vendor': None, 'model': None, 'type': 'mobile'}, 
    },{ # Archos
        'regex' : re.compile(r'(archos) (gamepad2?)',  re.I),                                        
        'props' : {'vendor': None, 'model': None, 'type': 'tablet'},
    },{ # KOBO
        'regex' : re.compile(r'(kobo)\s(ereader|touch)',  re.I),                                        
        'props' : {'vendor': None, 'model': None, 'type': 'tablet'}, 
    },{ # HP TouchPad
        'regex' : re.compile(r'(hp).+(touchpad(?!.+tablet)|tablet)', re.I),                                
        'props' : {'vendor': None, 'model': None, 'type': 'tablet'}, 
    },{ # Kindle
        'regex' : re.compile(r'(kindle)\/([\w\.]+)', re.I), 
        'props' : {'vendor': None, 'model': None, 'type': 'tablet'}, 
    },{ # Nook
        'regex' : re.compile(r'(nook)[\w ]+build\/(\w+)', re.I),                                            
        'props' : {'vendor': None, 'model': None, 'type': 'tablet'}, 
    },{ # Dell Streak
        'regex' : re.compile(r'(dell) (strea[kpr\d ]*[\dko])', re.I), 
        'props' : {'vendor': None, 'model': None, 'type': 'tablet'}, 
    },{ # Le Pan Tablets
        'regex' : re.compile(r'(le[- ]+pan)[- ]+(\w{1,9}) bui', re.I), 
        'props' : {'vendor': None, 'model': None, 'type': 'tablet'}, 
    },{ # Trinity Tablets
        'regex' : re.compile(r'(trinity)[- ]*(t\d{3}) bui', re.I), 
        'props' : {'vendor': None, 'model': None, 'type': 'tablet'}, 
    },{ # Gigaset Tablets
        'regex' : re.compile(r'(gigaset)[- ]+(q\w{1,9}) bui', re.I), 
        'props' : {'vendor': None, 'model': None, 'type': 'tablet'}, 
    },{ # Vodafone
        'regex' : re.compile(r'(vodafone) ([\w ]+)(?:\)| bui)', re.I), 
        'props' : {'vendor': None, 'model': None, 'type': 'tablet'}, 
    },{ # Surface Duo
        'regex' : re.compile(r'(surface duo)', re.I), 
        'props' : {'model': None, 'vendor': 'Microsoft', 'type': 'tablet'}, 
    },{ # Fairphone
        'regex' : re.compile(r'droid [\d\.]+; (fp\du?)(?: b|\))', re.I), 
        'props' : {'model': None, 'vendor': 'Fairphone', 'type': 'mobile'}, 
    },{ # AT&T
        'regex' : re.compile(r'(u304aa)', re.I),                                                     
        'props' : {'model': None, 'vendor': 'AT&T', 'type': 'mobile'},  
    },{ # Siemens
        'regex' : re.compile(r'\bsie-(\w*)', re.I),                                                  
        'props' : {'model': None, 'vendor': 'Siemens', 'type': 'mobile'}, 
    },{ # RCA Tablets
        'regex' : re.compile(r'\b(rct\w+) b', re.I),                                                 
        'props' : {'model': None, 'vendor': 'RCA', 'type': 'tablet'}, 
    },{ # Dell Venue Tablets
        'regex' : re.compile(r'\b(venue[\d ]{2,7}) b', re.I),                                        
        'props' : {'model': None, 'vendor': 'Dell', 'type': 'tablet'}, 
    },{ # Verizon Tablet
        'regex' : re.compile(r'\b(q(?:mv|ta)\w+) b', re.I),                                         
        'props' : {'model': None, 'vendor': 'Verizon', 'type': 'tablet'}, 
    },{ # Barnes & Noble Tablet
        'regex' : re.compile(r'\b(?:barnes[& ]+noble |bn[rt])([\w\+ ]*) b', re.I),                   
        'props' : {'model': None, 'vendor': 'Barnes & Noble', 'type': 'tablet'}, 
    },{
        'regex' : re.compile(r'\b(tm\d{3}\w+) b', re.I), 
        'props' : {'model': None, 'vendor': 'NuVision', 'type': 'tablet'}, 
    },{ # ZTE K Series Tablet
        'regex' : re.compile(r'\b(k88) b', re.I),                                                    
        'props' : {'model': None, 'vendor': 'ZTE', 'type': 'tablet'}, 
    },{ # ZTE Nubia
        'regex' : re.compile(r'\b(nx\d{3}j) b',  re.I),                                              
        'props' : {'model': None, 'vendor': 'ZTE', 'type': 'mobile'},  
    },{ # Swiss GEN Mobile
        'regex' : re.compile(r'\b(gen\d{3}) b.+49h', re.I),                                          
        'props' : {'model': None, 'vendor': 'Swiss', 'type': 'mobile'},  
    },{ # Swiss ZUR Tablet
        'regex' : re.compile(r'\b(zur\d{3}) b', re.I),                                               
        'props' : {'model': None, 'vendor': 'Swiss', 'type': 'tablet'}, 
    },{ # Zeki Tablets
        'regex' : re.compile(r'\b((zeki)?tb.*\b) b', re.I),                                          
        'props' : {'model': None, 'vendor': 'Zeki', 'type': 'tablet'}, 
    },{ # Dragon Touch Tablet
        'regex' : re.compile(r'\b([yr]\d{2}) b', re.I),                                             
        'props' : {'vendor': 'Dragon Touch', 'model': None, 'type': 'tablet'}, 
    },{ # Dragon Touch Tablet
        'regex' : re.compile(r'\b(dragon[- ]+touch |dt)(\w{5}) b', re.I),                            
        'props' : {'vendor': 'Dragon Touch', 'model': None, 'type': 'tablet'}, 
    },{ # Insignia Tablets
        'regex' : re.compile(r'\b(ns-?\w{0,9}) b', re.I),                                            
        'props' : {'model': None, 'vendor': 'Insignia', 'type': 'tablet'}, 
    },{ # NextBook Tablets
        'regex' : re.compile(r'\b((nxa|next)-?\w{0,9}) b', re.I),                                    
        'props' : {'model': None, 'vendor': 'NextBook', 'type': 'tablet'}, 
    },{ # Voice Xtreme Phones
        'regex' : re.compile(r'\b(xtreme\_)?(v(1[045]|2[015]|[3469]0|7[05])) b', re.I),              
        'props' : {'vendor': 'Voice', 'model': None, 'type': 'mobile'}, 
    },{ # LvTel Phones
        'regex' : re.compile(r'\b(lvtel\-)?(v1[12]) b', re.I),                                       
        'props' : {'vendor': 'LvTel', 'model': None, 'type': 'mobile'}, 
    },{ # Essential PH-1
        'regex' : re.compile(r'\b(ph-1) ', re.I),                                                    
        'props' : {'model': None, 'vendor': 'Essential', 'type': 'mobile'}, 
    },{ # Envizen Tablets
        'regex' : re.compile(r'\b(v(100md|700na|7011|917g).*\b) b', re.I),                          
        'props' : {'model': None, 'vendor': 'Envizen', 'type': 'tablet'}, 
    },{ # MachSpeed Tablets
        'regex' : re.compile(r'\b(trio[-\w\. ]+) b', re.I),                                   
        'props' : {'model': None, 'vendor': 'MachSpeed', 'type': 'tablet'}, 
    },{ # Rotor Tablets
        'regex' : re.compile(r'\btu_(1491) b', re.I), 
        'props' : {'model': None, 'vendor': 'Rotor', 'type': 'tablet'}, 
    },{ # Nvidia Shield Tablets
        'regex' : re.compile(r'(shield[\w ]+) b', re.I),                                        
        'props' : {'model': None, 'vendor': 'Nvidia', 'type': 'tablet'}, 
    },{ # Sprint Phones
        'regex' : re.compile(r'(sprint) (\w+)', re.I), 
        'props' : {'vendor': None, 'model': None, 'type': 'mobile'}, 
    },{ # Microsoft Kin
        'regex' : re.compile(r'(kin\.[onetw]{3})', re.I), 
        'props' : {
            'model' : lambda s: re.sub(r'\.', r' ', s),
            'vendor': 'Microsoft',
            'type'  : 'mobile'}
    },{ # Zebra
        'regex' : re.compile(r'droid.+; ([c6]+|et5[16]|mc[239][23]x?|vc8[03]x?)\)', re.I), 
        'props' : {'model': None, 'vendor': 'Zebra', 'type': 'tablet'}, 
    },{
        'regex' : re.compile(r'droid.+; (ec30|ps20|tc[2-8]\d[kx])\)',  re.I), 
        'props' : {'model': None, 'vendor': 'Zebra', 'type': 'mobile'},

    # Smart TVs

    },{ # Samsung SmartTV
        'regex' : re.compile(r'smart-tv.+(samsung)', re.I), 
        'props' : {'vendor': None, 'type': 'smarttv'}, 
    },{
        'regex' : re.compile(r'hbbtv.+maple;(\d+)', re.I), 
        'props' : {
            'model' : lambda s: re.sub(r'^', 'SmartTV', s),
            'vendor': 'Samsung',
            'type'  : 'smarttv'}
    },{ # LG SmartTV
        'regex' : re.compile(r'(nux; netcast.+smarttv|lg (netcast\.tv-201\d|android tv))', re.I), 
        'props' : {'vendor': 'LG', 'type': 'smarttv'},  
    },{ # Apple TV
        'regex' : re.compile(r'(apple) ?tv', re.I), 
        'props' : {'vendor': None, 'model': 'Apple TV', 'type': 'smarttv'},  
    },{ # Google Chromecast
        'regex' : re.compile(r'crkey', re.I), 
        'props' : {'model': 'Chromecast', 'vendor': 'Google', 'type': 'smarttv'},  
    },{ # Fire TV
        'regex' : re.compile(r'droid.+aft(\w)( bui|\))', re.I), 
        'props' : {'model': None, 'vendor': 'Amazon', 'type': 'smarttv'},  
    },{ # Sharp
        'regex' : re.compile(r'\(dtv[\);].+(aquos)', re.I), 
        'props' : {'model': None, 'vendor': 'Sharp', 'type': 'smarttv'},  
    },{
        'regex' : re.compile(r'(aquos-tv[\w ]+)\)', re.I), 
        'props' : {'model': None, 'vendor': 'Sharp', 'type': 'smarttv'},
    },{ # Sony
        'regex' : re.compile(r'(bravia[\w ]+)( bui|\))', re.I), 
        'props' : {'model': None, 'vendor': 'Sony', 'type': 'smarttv'},
    },{ # Xiaomi
        'regex' : re.compile(r'(mitv-\w{5}) bui', re.I), 
        'props' : {'model': None, 'vendor': 'Xiaomi', 'type': 'smarttv'},
    },{ # TechniSAT
        'regex' : re.compile(r'Hbbtv.*(technisat) (.*);', re.I), 
        'props' : {'model': None, 'vendor': None, 'type': 'smarttv'},  
    },{ # Roku
        'regex' : re.compile(r'\b(roku)[\dx]*[\)\/]((?:dvp-)?[\d\.]*)', re.I), 
        'props' : {
            'vendor': lambda s: re.sub(r'\s\s*$', EMPTY, re.sub(r'^\s\s*', EMPTY, s)), 
            'model' : lambda s: re.sub(r'\s\s*$', EMPTY, re.sub(r'^\s\s*', EMPTY, s)),  
            'type'  : 'smarttv'
            },  
    },{ # HbbTV devices
        'regex' : re.compile(r'hbbtv\/\d+\.\d+\.\d+ +\([\w ]*; *(\w[^;]*);([^;]*)', re.I), 
        'props' : {
            'vendor': lambda s: re.sub(r'\s\s*$', EMPTY, re.sub(r'^\s\s*', EMPTY, s)), 
            'model' : lambda s: re.sub(r'\s\s*$', EMPTY, re.sub(r'^\s\s*', EMPTY, s)), 
            'type'  : 'smarttv'
            },  
    },{ # SmartTV from Unidentified Vendors
        'regex' : re.compile(r'\b(android tv|smart[- ]?tv|opera tv|tv; rv:)\b', re.I),               
        'props' : {'type': 'smarttv'}, 

    # Consoles
    
    },{ # Ouya
        'regex' : re.compile(r'(ouya)', re.I), 
        'props' : {'vendor': None, 'model': None, 'type': 'console'},  
    },{ # Nintendo
        'regex' : re.compile(r'(nintendo) (\w+)', re.I), 
        'props' : {'vendor': None, 'model': None, 'type': 'console'},  
    },{ # Nvidia
        'regex' : re.compile(r'droid.+; (shield) bui', re.I), 
        'props' : {'model': None, 'vendor': 'Nvidia', 'type': 'console'}, 
    },{ # Playstation
        'regex' : re.compile(r'(playstation \w+)', re.I), 
        'props' : {'model': None, 'vendor': 'Sony', 'type': 'console'}, 
    },{ # Microsoft Xbox
        'regex' : re.compile(r'\b(xbox(?: one)?(?!; xbox))[\); ]', re.I), 
        'props' : {'model': None, 'vendor': 'Microsoft', 'type': 'console'},  
 
    # Wearables

    },{ # Pebble
        'regex' : re.compile(r'((pebble))app',  re.I),                                               
        'props' : {'vendor': None, 'model': None, 'type': 'wearable'}, 
    },{ # Apple Watch
        'regex' : re.compile(r'(watch)(?: ?os[,\/]|\d,\d\/)[\d\.]+',  re.I),                                               
        'props' : {'model': None, 'vendor': 'Apple', 'type': 'wearable'}, 
    },{ # Google Glass
        'regex' : re.compile(r'droid.+; (glass) \d', re.I),                                          
        'props' : {'model': None, 'vendor': 'Google', 'type': 'wearable'},  
    },{
        'regex' : re.compile(r'droid.+; (wt63?0{2,3})\)', re.I), 
        'props' : {'model': None, 'vendor': 'Zebra', 'type': 'wearable'},  
    },{ # Oculus Quest
        'regex' : re.compile(r'(quest( 2)?)', re.I),                                                 
        'props' : {'model': None, 'vendor': 'Facebook', 'type': 'wearable'}, 

    # Embedded 
     
    },{ # Tesla
        'regex' : re.compile(r'(tesla)(?: qtcarbrowser|\/[-\w\.]+)', re.I),                          
        'props' : {'vendor': None, 'type': 'embedded'},

    # Mixed (Generic)

    },{ # Android Phones from Unidentified Vendors
        'regex' : re.compile(r'droid .+?; ([^;]+?)(?: bui|\) applew).+? mobile safari',  re.I),      
        'props' : {'model': None, 'type': 'mobile'},  
    },{ # Android Tablets from Unidentified Vendors
        'regex' : re.compile(r'droid .+?; ([^;]+?)(?: bui|\) applew).+?(?! mobile) safari', re.I),   
        'props' : {'model': None, 'type': 'tablet'},  
    },{ # Unidentifiable Tablet
        'regex' : re.compile(r'\b((tablet|tab)[;\/]|focus\/\d(?!.+mobile))',  re.I),                 
        'props' : {'type': 'tablet'},  
    },{ # Unidentifiable Mobile
        'regex' : re.compile(r'(phone|mobile(?:[;\/]| safari)|pda(?=.+windows ce))', re.I),          
        'props' : {'type': 'mobile'},  
    },{ # Generic Android Device
        'regex' : re.compile(r'(android[-\w\. ]{0,9});.+buil', re.I),                                 
        'props' : {'model': None, 'vendor': 'Generic'}
    }
]

ENGINE: List[REGEXDICT] = [
    { # EdgeHTML
        'regex' : re.compile(r'windows.+ edge\/([\w\.]+)', re.I), 
        'props' : {'version': None, 'name': 'EdgeHTML'}, 
    },{ # Blink
        'regex' : re.compile(r'webkit\/537\.36.+chrome\/(?!27)([\w\.]+)', re.I), 
        'props' : {'version': None, 'name': 'Blink'}, 
    },{ # Presto
        'regex' : re.compile(r'(presto)\/([\w\.]+)',  re.I), 
        'props' : {'name': None, 'version': None}, 
    },{ # WebKit/Trident/NetFront/NetSurf/Amaya/Lynx/w3m/Goanna
        'regex' : re.compile(r'(webkit|trident|netfront|netsurf|amaya|lynx|w3m|goanna)\/([\w\.]+)', re.I), 
        'props' : {'name': None, 'version': None}, 
    },{ # Flow
        'regex' : re.compile(r'ekioh(flow)\/([\w\.]+)', re.I), 
        'props' : {'name': None, 'version': None}, 
    },{ # KHTML/Tasman/Links
        'regex' : re.compile(r'(khtml|tasman|links)[\/ ]\(?([\w\.]+)', re.I), 
        'props' : {'name': None, 'version': None}, 
    },{ # iCab 
        'regex' : re.compile(r'(icab)[\/ ]([23]\.[\d\.]+)', re.I), 
        'props' : {'name': None, 'version': None}, 
    },{ # Gecko
        'regex' : re.compile(r'rv\:([\w\.]{1,9})\b.+(gecko)', re.I), 
        'props' : {'version': None, 'name': None}, 
    }
]

OS: List[REGEXDICT] = [
    # Windows 

    { # Windows (iTunes)
        'regex' : re.compile(r'microsoft (windows) (vista|xp)', re.I), 
        'props' : {'name': None, 'version': None}, 
    },{ # Windows RT
        'regex' : re.compile(r'(windows) nt 6\.2; (arm)', re.I), 
        'props' : {
            'name'   : None, 
            'version': lambda s: strMapper(s, WINDOWS_VERSIONS)
        }, 
    },{ # Windows Phone
        'regex' : re.compile(r'(windows (?:phone(?: os)?|mobile))[\/ ]?([\d\.\w ]*)', re.I), 
        'props' : {
            'name'   : None, 
            'version': lambda s: strMapper(s, WINDOWS_VERSIONS)
        },
    },{
        'regex' : re.compile(r'(windows)[\/ ]?([ntce\d\. ]+\w)(?!.+xbox)', re.I), 
        'props' : {
            'name'   : None, 
            'version': lambda s: strMapper(s, WINDOWS_VERSIONS)
        }, 
    },{
        'regex' : re.compile(r'(win(?=3|9|n)|win 9x )([nt\d\.]+)', re.I), 
        'props' : {
            'name'   : 'Windows', 
            'version': lambda s: strMapper(s, WINDOWS_VERSIONS)
        }, 
    
    # iOS / MacOS

    },{ # iOS
        'regex' : re.compile(r'ip[honead]{2,4}\b(?:.*os ([\w]+) like mac|; opera)', re.I), 
        'props' : {
            'version': lambda s: re.sub(r'_', r'.', s), 
            'name'   : 'iOS'
        }, 
    },{
        'regex' : re.compile(r'cfnetwork\/.+darwin', re.I), 
        'props' : {
            'version': lambda s: re.sub(r'_', r'.', s), 
            'name'   : 'iOS'
        },
    },{ # Mac OS
        'regex' : re.compile(r'(mac os x) ?([\w\. ]*)', re.I), 
        'props' : {
            'name'   : 'Mac OS',
            'version': lambda s: re.sub(r'_', r'.', s)
        },
    },{ #
        'regex' : re.compile(r'(macintosh|mac_powerpc\b)(?!.+haiku)', re.I), 
        'props' : {
            'name'   : 'Mac OS',
            'version': lambda s: re.sub(r'_', r'.', s)
        },
    
    # Mobile Operating systems

    },{ # Android-x86/HarmonyOS
        'regex' : re.compile(r'droid ([\w\.]+)\b.+(android[- ]x86|harmonyos)', re.I), 
        'props' : {'version': None, 'name': None}, 
    },{ # Android/WebOS/QNX/Bada/RIM/Maemo/MeeGo/Sailfish OS
        'regex' : re.compile(r'(android|webos|qnx|bada|rim tablet os|maemo|meego|sailfish)[-\/ ]?([\w\.]*)', re.I), 
        'props' : {'name': None, 'version': None}, 
    },{ # Blackberry
        'regex' : re.compile(r'(blackberry)\w*\/([\w\.]*)', re.I), 
        'props' : {'name': None, 'version': None}, 
    },{ # Tizen/KaiOS
        'regex' : re.compile(r'(tizen|kaios)[\/ ]([\w\.]+)', re.I), 
        'props' : {'name': None, 'version': None}, 
    },{ # Series 40
        'regex' : re.compile(r'\((series40);', re.I), 
        'props' : {'name': None, 'version': None},  
    },{ # BlackBerry 10
        'regex' : re.compile(r'\(bb(10);', re.I), 
        'props' : {'version': None, 'name': 'BlackBerry'}, 
    },{ # Symbian
        'regex' : re.compile(r'(?:symbian ?os|symbos|s60(?=;)|series60)[-\/ ]?([\w\.]*)', re.I), 
        'props' : {'version': None, 'name': 'Symbian'}, 
    },{ # Firefox OS
        'regex' : re.compile(r'mozilla\/[\d\.]+ \((?:mobile|tablet|tv|mobile; [\w ]+); rv:.+ gecko\/([\w\.]+)', re.I), 
        'props' : {'version': None, 'name': 'Firefox OS'}, 
    },{ # WebOS
        'regex' : re.compile(r'web0s;.+rt(tv)', re.I), 
        'props' : {'version': None, 'name': 'webOS'}, 
    },{
        'regex' : re.compile(r'\b(?:hp)?wos(?:browser)?\/([\w\.]+)', re.I), 
        'props' : {'version': None, 'name': 'webOS'},
    },{ # WatchOS
        'regex' : re.compile(r'watch(?: ?os[,\/]|\d,\d\/)([\d\.]+)', re.I), 
        'props' : {'version': None, 'name': 'watchOS'}, 
    
    # Google Chromcast 

    },{ # Google Chromecast
        'regex' : re.compile(r'crkey\/([\d\.]+)', re.I), 
        'props' : {'version': None, 'name': 'Chromecast'}, 
    },{ # Chromium OS
        'regex' : re.compile(r'(cros) [\w]+ ([\w\.]+\w)', re.I), 
        'props' : {'name': 'Chromium OS', 'version': None}, 

    # Smart TVs

    },{ # Panasonic Viera
        'regex' : re.compile(r'/panasonic;(viera)', re.I), 
        'props' : {'name': None, 'version': None},
    },{ # Net Range
        'regex' : re.compile(r'(netrange)mmh', re.I), 
        'props' : {'name': None, 'version': None},

    # Consoles

    },{ # Nintendo/Playstation
        'regex' : re.compile(r'(nintendo|playstation) (\w+)', re.I), 
        'props' : {'name': None, 'version': None},
    },{ # Microsoft Xbox (360, One, X, S, Series X, Series S)
        'regex' : re.compile(r'(xbox); +xbox ([^\);]+)', re.I), 
        'props' : {'name': None, 'version': None},

    # Others
    
    },{ # Joli/Palm
        'regex' : re.compile(r'\b(joli|palm)\b ?(?:os)?\/?([\w\.]*)', re.I), 
        'props' : {'name': None, 'version': None},
    },{ # Mint
        'regex' : re.compile(r'(mint)[\/\(\) ]?(\w*)', re.I), 
        'props' : {'name': None, 'version': None},
    },{ # Mageia/VectorLinux
        'regex' : re.compile(r'(mageia|vectorlinux)[; ]', re.I), 
        'props' : {'name': None, 'version': None},
    },{ # Ubuntu/Debian/SUSE/Gentoo/Arch/Slackware/Fedora/Mandriva/CentOS/PCLinuxOS/RedHat/Zenwalk/Linpus/Raspbian/Plan9/Minix/RISCOS/Contiki/Deepin/Manjaro/elementary/Sabayon/Linspire
        'regex' : re.compile(r'([kxln]?ubuntu|debian|suse|opensuse|gentoo|arch(?= linux)|slackware|fedora|mandriva|centos|pclinuxos|red ?hat|zenwalk|linpus|raspbian|plan 9|minix|risc os|contiki|deepin|manjaro|elementary os|sabayon|linspire)(?: gnu\/linux)?(?: enterprise)?(?:[- ]linux)?(?:-gnu)?[-\/ ]?(?!chrom|package)([-\w\.]*)', re.I), 
        'props' : {'name': None, 'version': None},
    },{ # Hurd/Linux
        'regex' : re.compile(r'(hurd|linux) ?([\w\.]*)', re.I), 
        'props' : {'name': None, 'version': None},
    },{ # GNU
        'regex' : re.compile(r'(gnu) ?([\w\.]*)', re.I),                                          
        'props' : {'name': None, 'version': None},
    },{ # FreeBSD/NetBSD/OpenBSD/PC-BSD/GhostBSD/DragonFly
        'regex' : re.compile(r'\b([-frentopcghs]{0,5}bsd|dragonfly)[\/ ]?(?!amd|[ix346]{1,2}86)([\w\.]*)',  re.I), 
        'props' : {'name': None, 'version': None},
    },{ # Haiku
        'regex' : re.compile(r'(haiku) (\w+)',  re.I), 
        'props' : {'name': None, 'version': None},
    },{ # Solaris
        'regex' : re.compile(r'(sunos) ?([\w\.\d]*)', re.I), 
        'props' : {'name': 'Solaris', 'version': None}, 
    },{ # Solaris
        'regex' : re.compile(r'((?:open)?solaris)[-\/ ]?([\w\.]*)', re.I), 
        'props' : {'name': None, 'version': None},
    },{ # AIX
        'regex' : re.compile(r'(aix) ((\d)(?=\.|\)| )[\w\.])*', re.I), 
        'props' : {'name': None, 'version': None},
    },{ # BeOS/OS2/AmigaOS/MorphOS/OpenVMS/Fuchsia/HP-UX
        'regex' : re.compile(r'\b(beos|os\/2|amigaos|morphos|openvms|fuchsia|hp-ux)', re.I), 
        'props' : {'name': None, 'version': None},
    },{ # UNIX
        'regex' : re.compile(r'(unix) ?([\w\.]*)', re.I), 
        'props' : {'name': None, 'version': None},
    }
]
