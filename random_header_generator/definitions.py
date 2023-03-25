""" Declaration of classes / datatypes used jointly by all modules """

from typing import Literal, get_args

HTTP_VERSION_TYPE   = Literal[1, 2]                                           # Supported http versions
GENERATOR_TYPE      = Literal['scrape', 'program', 'file']                    # Type of user agent generator to be used
INPUT_TYPE          = Literal['browser', 'device', 'country']                 # Input names expected by the user
BROWSER_TYPE        = Literal['chrome', 'edge', 'firefox', 'safari', 'opera'] # Available browsers
PARSER_TYPE         = Literal['browser', 'cpu', 'device', 'engine', 'os']     # Parser types (names) used in parser.py, generator.py
DEVICE_TYPE         = Literal['desktop', 'mobile']                            # Available device types
COUNTRY_TYPE        = Literal[                                                # Availabel countries' A2 - codes
    'ad', 'ae', 'af', 'ag', 'al', 'am', 'ao', 'ar', 'as', 'at', 'au', 'az', 
    'ba', 'bb', 'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bo', 'br', 'bs', 
    'bt', 'bw', 'by', 'bz', 'ca', 'cd', 'ch', 'cl', 'cm', 'cn', 'co', 'cr', 
    'cu', 'cy', 'cz', 'de', 'dj', 'dk', 'dm', 'do', 'dz', 'ec', 'ee', 'eg', 
    'er', 'es', 'et', 'fi', 'fj', 'fr', 'ga', 'gb', 'gd', 'ge', 'gh', 'gm', 
    'gn', 'gq', 'gr', 'gt', 'gw', 'gy', 'hn', 'hr', 'ht', 'hu', 'id', 'ie', 
    'il', 'in', 'iq', 'ir', 'is', 'it', 'jm', 'jo', 'jp', 'ke', 'kg', 'kh', 
    'ki', 'km', 'kn', 'kw', 'kz', 'lb', 'lc', 'li', 'lk', 'lr', 'ls', 'lt', 
    'lu', 'lv', 'ly', 'ma', 'mc', 'md', 'me', 'mg', 'mh', 'ml', 'mn', 'mr', 
    'mt', 'mu', 'mw', 'mx', 'my', 'mz', 'ne', 'ng', 'ni', 'nl', 'no', 'np', 
    'nr', 'nu', 'nz', 'om', 'pa', 'pe', 'pg', 'ph', 'pk', 'pl', 'ps', 'pt', 
    'py', 'qa', 'ro', 'rs', 'ru', 'rw', 'sa', 'sb', 'sc', 'sd', 'se', 'sg', 
    'si', 'sk', 'sl', 'sm', 'sn', 'so', 'sr', 'ss', 'sv', 'sz', 'td', 'tg', 
    'th', 'tj', 'tm', 'tn', 'to', 'tr', 'tt', 'tv', 'tw', 'tz', 'ua', 'ug', 
    'us', 'uy', 'uz', 'vc', 've', 'vn', 'vu', 'ye', 'za', 'zm', 'zw']


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
COUNTRIES       = get_args(COUNTRY_TYPE)
BROWSERS        = get_args(BROWSER_TYPE)
PARSERS         = get_args(PARSER_TYPE)