""" Declaration of classes / datatypes used jointly by all modules """

from typing import Literal, get_args

HTTP_VERSION_TYPE   = Literal[1, 2]                                           # Supported http versions
GENERATOR_TYPE      = Literal['scrape', 'program', 'file']                    # Type of user agent generator to be used
INPUT_TYPE          = Literal['browser', 'device', 'domain']
BROWSER_TYPE        = Literal['chrome', 'edge', 'firefox', 'safari', 'opera'] # Available browsers
PARSER_TYPE         = Literal['browser', 'cpu', 'device', 'engine', 'os']     # Parser types (names) used in parser.py, generator.py
DEVICE_TYPE         = Literal['desktop', 'mobile']                            # Available device types
DOMAIN_TYPE         = Literal['com',  'jsp',  'edu', 'org', 'info', 'net',    # Available domains
                              'php3', 'aspx', 'biz', 'uk',  'it',   'is',  
                              'ua',   'cc',   'de',  'us',  'tv',   'eu',   
                              'ru',   'cn',   'jp',  'nl',  'be',   'fr',  
                              'ch',   'gr',   'se',  'dk',  'bg',   'cz',   
                              'hu',   'lt',   'pl',  'ro',  'sk',   'si',  
                              'br',   'pt',   'es',  'il',  'au',   'io',   
                              'no',   'ir',   'at']


UNKNOWN_NAME        = 'unknown'     # Unknown name token. Used for the initialisation of most properties
MAX_USER_AGENT_SIZE = 256           # Maximum num characters comprising a user agent
UNKNOWN_VERSION     = '0.0'         # Unknown version token. Used for the initialisation of most properties
EMPTY               = r''           # Empty pattern
CONSTANT_HEADERS    = {             # Headers with constant values regardless of browser/OS/device combination
    "Sec-Fetch-Site"            : "same-site",
    "Sec-Fetch-Mode"            : "navigate",
    "Sec-Fetch-User"            : "?1",
    "Sec-Fetch-Dest"            : "document",
    "Upgrade-Insecure-Requests" : "1",
    "Connection"                : "keep-alive"
}

# Extract some constants
HTTP_VERSIONS   = get_args(HTTP_VERSION_TYPE)
DEVICES         = get_args(DEVICE_TYPE)
DOMAINS         = get_args(DOMAIN_TYPE)
BROWSERS        = get_args(BROWSER_TYPE)
PARSERS         = get_args(PARSER_TYPE)