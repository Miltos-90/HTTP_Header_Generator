""" Implementation of the Header Generator class, along with and helper classes """

from abc           import ABC
from .ua_parser    import Parser
from collections   import OrderedDict
from typing        import Literal, Dict, Union, Any
from .ua_generator import CHParser, Generator as UAGenerator
from .             import definitions as defs
from .             import utils
import random      as rd
import warnings


""" Helper classes for use in the HeaderGenerator class. """
class GenericHeaderGenerator(ABC):
    """ Generic HTTP Header generator class """

    def __init__(self, pathToFile: str):
        """ Initialisation method. Reads necessary data. """
        
        self.data = utils.readFile(pathToFile)
        
        return


    def __call__(self, key: str, defaultKey: str) -> str:
        """ Randomly chooses an element from the dictionary <data>
            associated with the attribute <s>. If the attribute does not exist,
            return a randomly selected value from the ones of the <default> key
        """

        exists = key in self.data.keys()

        if exists: return rd.choice(self.data[key])
        else     : return rd.choice(self.data[defaultKey])


    @staticmethod
    def _addQFactors(l:list) -> list:
        """ Appends randomly generated relative quality factors (q-factors) 
            to the elements (strings) of the input list l.
        """
        
        num   = len(l)
        minq  = round(1.0 / num, 1)      # Minimum q value that can be set (maximum = 1.0)
        dq    = (1.0 - minq) / (num + 1) # Reduction rate between cosecutive q values
        qVals = [""]                     # To be populated with the q values
        q     = 1.0                      # Assume first q factor to be equal to 1

        for _ in range(1, num):
            q = rd.uniform(q - dq, q - 2 * dq) # Randomly select a continuously decreasing q factor
            q = max(0.1, round(q, 1))          # round to first decimal and set it to minimum 0.1
            qVals.append(f";q={q}")

        l = [e + q for e, q in zip(l, qVals)] # Append to the elements of the input list

        return l


class Accept(GenericHeaderGenerator):
    """ Generator of the 'Accept' header """

    def __call__(self, 
        name    : str,  # Browser name
        version : float # Browser major (significant) version
        ) -> str:
        """ Generate a randomized Accept Encoding header. """

        # Get header values corresponding to this browser, i.e.
        # a list of version-from and -to numbers [integers] and header contents
        list_ = self.data[name]

        # Loop over the list and get the header value according to the version range
        for dict_ in list_:
            if version >= dict_["version_from"] and version < dict_["version_to"]:
                return dict_["header"]
        
        # If this point is reached, the version was not found
        raise ValueError(f'{name} browser version {version} is not supported for the "Accept" header')


class AcceptEncoding(GenericHeaderGenerator):
    """ Generator of the 'Accept-Encoding' header """

    def __init__(self, pathToFile: str):
        """ Initialisation method. Reads necessary data. """

        super().__init__(pathToFile)

        # The file contains a dict of a single element. Unpack it
        self.data = self.data["Accept-Encoding"]

        return 


    def __call__(self, 
        addQFactors: Union[bool, None] = None # Indicates if relative quality factors should be included
        ) -> str:
        """ Generate a randomized Accept Encoding header. """
        
        if not addQFactors: 
            addQFactors = rd.random() >= 0.5      # Choose randomly if quality factors will be included if not specified
        
        numStr   = rd.randint(1, len(self.data))  # Choose a random number <num> of encoding strings to be included
        encoders = rd.sample(self.data, numStr)   # Make <k> unique random choices from the population of accepted encoders

        if '*' in encoders:     # Always set 'no preference' at the end
            encoders.pop(encoders.index('*')) 
            encoders.append('*')

        if 'gzip' in encoders:  # If 'gzip' is chosen, put it first  
            encoders.pop(encoders.index('gzip')) 
            encoders.insert(0, 'gzip')

        # Add relative quality factors
        if addQFactors: encoders = self._addQFactors(encoders)

        return ", ".join(encoders)


class AcceptLanguage(GenericHeaderGenerator):
    """ Generator of the 'Accept-Language' header """

    def __call__(self, 
        domain          : str,                              # Domain to relate languages to
        globalLanguages : list = ['en', 'en-GB', 'en-US'],  # Languages that are always accepted
        addQFactors     : Union[bool, None] = None          # Indicates if relative quality factors should be included
        ) -> str:
        """ Generate a randomized 'Accept-Language' header """

        # Get a language related to the input domain
        domainLanguage = super().__call__(domain, defaultKey = "eu")

        # Prevent the same language from appearing in both the domain-specific language and the universal languages
        dupe = domainLanguage in globalLanguages
        if not dupe : languages = [domainLanguage] + globalLanguages
        else        : languages = globalLanguages

        # Add relative quality factors
        if addQFactors: languages = self._addQFactors(languages)

        return ",".join(languages)


class Selector():
    """ Selects an os, device, and browser based on actual usage
        information obtained from https://gs.statcounter.com/
    """

    def __init__(self):
        """ Imports required data. """
        
        self.softwareData = utils.readFile('./data/software_market_share.json')
        domainData        = utils.readFile('./data/domain_market_share.json')
        
        # Extract weights for device and domain selection
        self.devWeights = [self.softwareData[d]["usage"] for d in defs.DEVICES]
        self.domWeights = [domainData.get(domain, 1e-9) for domain in defs.DOMAINS]
        # NOTE: If a domain is not available in the domain statistics file (./data/domain_market_share.json) 
        # it can still be selected with a low probability (=1e-9 - two orders of magnitude below the minimum on the file).
        
        return
    

    def __call__(self, 
        request: Literal['browser', 'device', 'domain'], **kwargs
        ) -> str:
        """ """

        if request == 'browser': return self._getBrowser(device = kwargs.get('device', 'desktop'))
        if request == 'device' : return self._getDevice()
        if request == 'domain' : return self._getDomain()


    def _getDevice(self) -> defs.DEVICE_TYPE:
        """ Selects a device """
        return rd.choices(population = defs.DEVICES, weights = self.devWeights)[0]


    def _getBrowser(self, device: defs.DEVICE_TYPE) -> defs.BROWSER_TYPE:
        """ Selects a browser """

        browser = rd.choices(
            population = list( self.softwareData[device]["browser"].keys() ),
            weights    = list( self.softwareData[device]["browser"].values() )
        )[0]
        
        return browser


    def _getDomain(self) -> defs.DOMAIN_TYPE:
        """ Selects a domain """
        return rd.choices(population = defs.DOMAINS, weights = self.domWeights)[0]


class ClientHintGenerator():
    """ Derivation of user agent client hints based on a parsed user agent.
        See: https://github.com/WICG/ua-client-hints for definitions.
    """

    def __init__(self):
        """ Initialisation method. Reads data and instantiates classes. """

        self.cpuBitness = utils.readFile('./data/cpu_bitness.json')
        self.Parser     = CHParser()

        return


    def __call__(self, userAgent: str) -> Dict[str, str]:
        """ Generates client hints from a user agent, using the dictionaries
            resulting from the parsing operation.
        """

        # Parse user agent
        browser, cpu, device, _, os = self.Parser(userAgent)
        
        # Extract specific attributes needed
        bName     = getattr(browser, 'name')
        bVersion  = getattr(browser, 'version')
        bMajorVer = getattr(browser, 'majorVersion')
        cpuArch   = getattr(cpu,     'architecture')
        devType   = getattr(device,  'type')
        devModel  = getattr(device,  'model')
        osName    = getattr(os,      'name')
        osVersion = getattr(os,      'version')
        
        # Generate client hints dictionary
        return {
            "Sec-CH-UA"                   : self._UA(bName, bMajorVer),
            "Sec-CH-UA-Arch"              : self._UAGeneric(cpuArch),
            "Sec-CH-UA-Bitness"           : self._UABitness(cpuArch),
            "Sec-CH-UA-Full-Version-List" : self._UA(bName, bVersion, full = True),
            "Sec-CH-UA-Mobile"            : self._UAMobile(devType),
            "Sec-CH-UA-Model"             : self._UAGeneric(devModel),
            "Sec-CH-UA-Platform"          : self._UAPlatform(osName),
            "Sec-CH-UA-Platform-Version"  : self._UAGeneric(osVersion),
        }


    def _UABitness(self,
        name : str, # CPU architecture
        ) -> str:
        """ Generates the value of the Sec-CH-UA-Bitness header.
            See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-CH-UA-Bitness
        """
        
        return self._format(self.cpuBitness.get(name, defs.EMPTY))


    def _UAGeneric(self,
        architecture: str # CPU architecutre
        ) -> str:
        """ Generates the value of the Sec-CH-UA-Arch, Sec-CH-UA-Model, Sec-CH-UA-Platform-Version headers.
            See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-CH-UA-Arch
                https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-CH-UA-Model
                https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-CH-UA-Platform-Version
        """

        return self._format(architecture)


    @staticmethod
    def _UAMobile(
        s: str # Device type
        ) -> str:
        """ Generates the value of the Sec-CH-UA-Mobile header.
            See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-CH-UA-Mobile
        """
            
        if s == 'mobile': return '?1'
        else            : return '?0'


    def _UAPlatform(self,
        name # Name of the operating system
        ) -> str:
        """ Generates the value of the Sec-CH-UA-Platform header.
            See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-CH-UA-Platform
        """
        
        if name.lower() not in ['ios', 'mac os', 'macos']: 
            name = name.title()

        return self._format(name)


    def _UA(self,
        name    : str,  # Brand name
        version : str,  # Major (Significant) version of the browser
        full    : bool = False
        ) -> str: 
        """ Generates the value of the Sec-CH-UA and Sec-CH-UA-Full-Version-List headers.
            See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-CH-UA
            and  https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-CH-UA-Full-Version-List
        """

        brandList = []
        if name != defs.EMPTY: brandList.append({'brand': name, 'version': version})

        # Make  intentionally incorrect brand string
        if full : brandList.append({'brand': ' Not A;Brand', 'version': '99.0.0.0'})
        else    : brandList.append({'brand': ' Not A;Brand', 'version': '99'})

        # Convert to string
        return self._makeBrandString(brandList)


    @staticmethod
    def _makeBrandString(
        brandList: list # List of dicts {brand, version}
        ) -> str:
        """ Generates a string from the brand list of the user"""

        serial = []
        for d in brandList:
            brand   = d['brand']
            version = d['version']
            bLower  = brand.lower()

            if bLower == 'chrome':
                for name in ['Chromium', 'Google Chrome']:
                    serial.append(f'"{name}";v="{version}"')
            
            elif bLower == 'edge':
                for name in ['Chromium', 'Microsoft Edge']:
                    serial.append(f'"{name}";v="{version}"')

            else:
                # NOTE: If brand is not chrome or edge, this header is not supported (up until now, March 2023)
                # The following will simply append the brand name of the browser, but this header is 
                # going to be removed in the removeUnsupportedHeaders() function downstream.
                serial.append(f'"{brand}";v="{version}"')
        
        return ', '.join(serial)


    @staticmethod
    def _format(x: str) -> str:
        """ Generic string formatter for the client hints """
        
        return f'"{x}"'


""" Header generator """
class HeaderGenerator(metaclass = utils.Singleton):
    """ Generator of realistic, randomly-chosen HTTP headers.
        Extended from: https://github.com/MichaelTatarski/fake-http-header
    """

    def __init__(self, by: defs.GENERATOR_TYPE = 'program', **kwargs):
        """ Initialisation method. Instantiates necessary ojects. """

        self.Parser      = Parser()
        self.UserAgent   = UAGenerator(by = by, **kwargs)
        
        self.ClientHints = ClientHintGenerator()
        self.Referer     = GenericHeaderGenerator('./data/referers.json')
        self.Encoder     = AcceptEncoding('./data/acceptEncoding.json')
        self.Language    = AcceptLanguage('./data/languages.json')
        self.Accept      = Accept('./data/accept.json')
        self.Selector    = Selector()
        self.domains     = list(self.Referer.data.keys())

        # Header-browser-version compatibility tables
        self.compTable   = utils.readFile('./data/header_compatibility.json')

        # Browser-based header order
        self.headerOrder = utils.readFile('./data/header_order.json')

        return


    def _checkInput(self, 
        inputType: defs.INPUT_TYPE,  # Type of input to check or return
        value    : Union[None, str], # Corresponding value provided by the user
        **kwargs) -> Any:
        """ Checks user input if provided, otherwise it returns realistic randomly 
            selected values according to usage/market statistics data.
        """

        if not value: 
            # User did not supply a value for the input. Produce one.
            return self.Selector(inputType, **kwargs)

        else:         
            # Check if user input is valid.
            value  = value.lower()

            if   inputType not in ["browser", "device", "domain"]:      errMsg = "Invalid input type."
            elif inputType == "browser" and value not in defs.BROWSERS: errMsg = "Invalid browser name."
            elif inputType == "device"  and value not in defs.DEVICES:  errMsg = "Invalid device type."
            elif inputType == "domain"  and value not in self.domains:  errMsg = "Invalid domain."
            else:                                                       errMsg = None

            if errMsg: raise ValueError(errMsg)
            else     : return value


    @staticmethod
    def _warnOnOverwrite(
        inputType : defs.INPUT_TYPE,    # Type of input being checked (used to print warning)
        userValue : Union[None, str],   # Input value supplied by the user
        newValue  : str                 # Value used for the generation of the user agent
        ):
        """ Compares the values of the user inputs, and the values used for the genration of the user agent.
            If they do not match, a warning is printed.
        """

        if userValue and newValue != userValue.lower():
            msg = f'{inputType.title()} overwritten to find suitable user agent.'
            warnings.warn(message = msg)

        return


    @staticmethod
    def _makeCookieHeader(cookieDict: Dict[str, str]) -> str:
        """ Generates the <Cookie> header given a dict of cookies """

        # Convert dictionary of cookies to a list of {'name': <name>, 'value': <value>} dicts
        cookieList = [{'name': key, 'value': value} for key, value in cookieDict.items()]
        
        # Convert to string: Format first cookie
        cookie    = cookieList.pop()
        cookieStr = f"{cookie['name']}={cookie['value']}"

        # Format subsequent cookies
        for c in cookieList: cookieStr += f"; {c['name']}={c['value']}"

        return cookieStr


    def _removeIncompatible(self, 
        headers    : dict,              # Dict with all the headers
        browser    : defs.BROWSER_TYPE, # browser name
        device     : defs.DEVICE_TYPE,  # device type
        browserVer : float,             # browser version
        ) -> dict:
        """ Extracts compatible headers for a given browser (and version) and device"""

        # Get compatible header names (keys) and versions (values)
        compatibleTab = self.compTable[f'{browser}-{device}']
        
        headers_ = {} # Dict that contains the compatible headers only
        for hName, hValue in headers.items():

            # Version for which <browser> first supported <hName>
            minVersion  = compatibleTab[hName]

            # if header <hName> is supported for the given version, add it to the dict
            if browserVer >= minVersion: headers_[hName] = hValue 

        return headers_

    
    @staticmethod
    def _makeHTTPVersionCompatible(
        headers: dict, httpVersion: defs.HTTP_VERSION_TYPE) -> dict:
        """ Makes header dict compatible to HTTP version 2.0, i.e.
            it lowercases their names.
         """

        if httpVersion == 2:
            headers = {k.lower(): v for k, v in headers.items()}
        
        return headers


    def _order(self, 
        headers     : Dict[str, str],
        httpVersion : defs.HTTP_VERSION_TYPE, 
        browser     : defs.BROWSER_TYPE,
        ) -> OrderedDict:
        """ Converts the headers dictionary to an ordered dict based on the browser
            and http versions.
         """

        # Extract order for current http version and browser
        if httpVersion == 1: 
            orderedHeaderNames = self.headerOrder["http version 1.x"][browser]
        else: 
            orderedHeaderNames = self.headerOrder["http version 2.x"][browser]

        # Make ordered dictionary
        headersOrdered = OrderedDict()
        for hName in orderedHeaderNames:

            if hName in headers: # header might not exist for older versions
                headersOrdered[hName] = headers.pop(hName)
        
        # Add the remaining headers (in an unordered manner)
        for hName, hValue in headers.items():
            headersOrdered[hName] = hValue
        
        return headersOrdered
    

    def __call__(self,
        domain      : Union[None, defs.DOMAIN_TYPE]  = None, 
        device      : Union[None, defs.DEVICE_TYPE]  = None, 
        browser     : Union[None, defs.BROWSER_TYPE] = None,
        httpVersion : defs.HTTP_VERSION_TYPE = 1,
        cookies     : Dict[str, str] = {},
        ) -> OrderedDict[str, str]:

        """ Generates realistic, randomly-chosen HTTP headers.
        Inputs:
            * domain can be either:

                * str containing one of: 
                    com, jsp, edu, org, info, net, php3, aspx, biz, uk, it,
                    is,  ua,  cc,  de,  us,   tv,  eu,   ru,   cn,  jp, nl, be,  
                    fr,  ch,  gr,  se,  dk,   bg,  cz,   hu,   lt,  pl, ro, sk, 
                    si,  br,  pt,  es,  il,   au,  io,   no,   ir,  at
                * Empty: random selection among all
            * Browser can be either
                * str containing one of: chrome, edge, firefox, safari
                * Empty: random selection among all
            * Device (list) can be either
                * str containing one of: mobile, desktop
                * Empty: random selection among all
            * HTTP version (int), can be either 1 (supports both 1.0 and 1.1) 2, or
                empty which defaults to 1
            * Cookies: Dictionary of <name>, <value> pairs containing cookies, or empty.
        """

        # Sanity check on user supplied values
        browser_ = self._checkInput(inputType = 'browser', value = browser)
        device_  = self._checkInput(inputType = 'device',  value = device)
        domain_  = self._checkInput(inputType = 'domain',  value = domain)
        if httpVersion not in defs.HTTP_VERSIONS: 
            raise ValueError('Invalid http version.')
        
        # Get user agent client hints and browser version. NOTE: The User Agent can 
        # overwrite user inputs if an agent is not found for the user-supplied values.
        browser_, device_, userAgent = self.UserAgent(browser_, device_)
        brVersion   = float(self.UserAgent._getAttribute(userAgent, ('browser', 'majorVersion')))
        clientHints = self.ClientHints(userAgent)
        
        headers: dict[str, str] =  { # Make (partial) header dictionary
            "User-Agent"      : userAgent,
            "Referer"         : self.Referer(domain_, defaultKey = 'com'), 
            "Accept"          : self.Accept(browser_, brVersion),
            "Accept-Language" : self.Language(domain_),
            "Accept-Encoding" : self.Encoder(),
        }

        if bool(cookies):                     # Add cookies if needed
            headers['Cookie'] = self._makeCookieHeader(cookies)
        headers.update(clientHints)           # Add client hints
        headers.update(defs.CONSTANT_HEADERS) # Add constant-valued headers
        
        headers = self._removeIncompatible(headers, browser_, device_, brVersion)
        headers = self._makeHTTPVersionCompatible(headers, httpVersion)
        headers = self._order(headers, httpVersion, browser_)
        
        # Print a warning if the user-supplied values were overwritten
        self._warnOnOverwrite(inputType = 'browser', userValue = browser, newValue = browser_)
        self._warnOnOverwrite(inputType = 'device',  userValue = device,  newValue = device_)   
        self._warnOnOverwrite(inputType = 'domain',  userValue = domain,  newValue = domain_)       
        
        return headers
