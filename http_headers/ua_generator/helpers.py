""" This module implements a set of functions responsible for generating  user agent strings 
    from various sources, as well as a Software Factory (& its derivatives), used within the 
    Programmer class (see generators.py)
"""

from ..definitions  import BROWSER_TYPE, UNKNOWN_NAME, GENERATOR_TYPE, BROWSERS
from typing         import Union, cast, Tuple
from random         import randint, choice
from .              import constants as c
from bs4            import BeautifulSoup
from ..utils        import readFile
import requests
import string
import os

class SoftwareFactory():
    """ Base software factory. It provides random software versions and their corresponding details """

    def __init__(self, versions: dict):
        
        self.versions = versions
        self.names    = list(versions.keys())
        return


    def __call__(self, name: c.SOFTWARE_TYPE) -> c.Software:
        """ Randomly chooses a software version and its associated details from its name"""
        
        versions = self.versions[name] # Get versions relevant to software <name>

        # if only keys are specified in the data (i.e. the structure is a set), convert to dict
        if isinstance(versions, set): versions = dict.fromkeys(versions, {})

        # Select version from those
        majorVersion   = choice(list(versions.keys())) # Randomly select major version number
        versionDetails = versions[majorVersion]        # Additional details associated with this version
        
        # Randomly select minor version number
        minorRange     = versionDetails.get('minor_range')
        minorVersion   = randint(minorRange[0], minorRange[1]) if minorRange else None
        
        return c.Software(
            name    = name,
            details = self._makeDetails(majorVersion, minorVersion, versionDetails),
            version = self._makeVersionString(majorVersion, minorVersion = minorVersion, name = name),
        )


    @staticmethod
    def _makeDetails(
        majorVersion      : str,              # Major version of the software 
        minorVersion      : Union[int, None], # Minor version of the software 
        versionProperties : dict              # Additional software details 
        ) -> dict:
        """ Generates all addditional details of a major version of a software """

        # Loop over all properties and populate dictionary
        d = {'major_version' : majorVersion}
        
        if minorVersion is not None:
            d['minor_version'] = str(minorVersion)
            
        for propKey, propValue in versionProperties.items():
            if propKey != 'minor_range':  d[propKey] = propValue

        return d


    @staticmethod
    def _makeVersionString(majorVersion: str, **kwargs) -> str:
        """ Makes version string for a software given its major version 
            and additional main properties. """
    
        minorVer = kwargs.get("minorVersion", 0)
        name     = cast(c.SOFTWARE_TYPE, kwargs.get("name", UNKNOWN_NAME))
        version  = majorVersion # Start with the major version

        # and add minor version if needed
        if minorVer and not SoftwareFactory._skipMinorVersion(name, minorVer): 
            version = version + '.' + str(minorVer)

        # Format version appropriately
        if name in ['macos', 'ios']: version = version.replace('.', '_')
        
        return version


    @staticmethod
    def _skipMinorVersion(
        name          :c.SOFTWARE_TYPE, # Software name
        minorVersion : int              # Minor version of the software
        ) -> bool:
        """ Evaluates whether or not the minor software version
            should be included in the version string
        """

        # Some software truncates the trailing '.0' pattern during versions
        l = ['macos', 'ios', 'firefox', 'opera']
        if name in l : stripZero = True
        else         : stripZero = False

        # Do not include minor version in the following cases
        return minorVersion == 0 and stripZero


class AndroidFactory(SoftwareFactory):
    """ Android OS factory. Produces Android platforms. """

    def __init__(self, 
        systems: dict # Dictionary containing the details of the system
        ):
        
        self.versions = systems['versions']
        self.devices  = systems['devices']
        self.names    = list(systems['versions'].keys())

        return
    

    def __call__(self, 
        brand: Union[c.BRAND_TYPE, None] = None # Android device brand (e.g. samsung, nexus, etc.) 
        ) -> c.Software:
        """ Generate a random Android OS """

        # Randomly select a brand of mobile phones operating on Android and make OS
        # Make new variable to ensure safe casting in super().__call__()
        if not brand: brand_ = choice(self.names)
        else        : brand_ = brand
        
        # Make os
        os = super(AndroidFactory, self).__call__(brand_)
        os.name                     = 'android' # overwrite with OS name
        os.details['brand']         = brand_
        os.details['device_name']   = choice(self.devices[brand_])
        os.details['build_number']  = self._formatBuildNumber(os.details['build_number'])
        
        return os


    @staticmethod
    def _formatBuildNumber(
        buildNumbers : tuple    # Avaliable build numbers to choose from
        ) -> str:
        """ Formats the buildnumber according to the mmanufacturer. 
            Supports nexus, samsung and pixel devices.
        """

        buildNum   = choice(buildNumbers)   # Choose a build number at random.
        formatters = (                      # Generate random formatters for the build number.
            {'from': '{s}', 'to' : '{}'.format(choice(string.ascii_uppercase))},
            {'from': '{d}', 'to' : '{:02d}{:02d}{:02d}'.format(randint(17, 22), randint(0, 12), randint(0, 29))},
            {'from': '{v}', 'to' : '{}'.format(randint(1, 255))}
        )

        for f in formatters: buildNum = buildNum.replace(f['from'], f['to'])

        return buildNum


    @staticmethod
    def _makeVersionString(majorVersion: str, **kwargs) -> str: 
        """ Makes version string for a software given its main properties. """
        return majorVersion.replace('.0', '')       


class SoftwareGenerator():
    """ Generic software factory. Convenience class that wraps the above implementations. 
        It produces software of any type: browsers, operating systems, and 
        Android platforms.
     """

    def __init__(self):

        self.osFactory      = SoftwareFactory(c.OS)
        self.androidFactory = AndroidFactory(c.ANDROID)
        self.browserFactory = SoftwareFactory(c.BROWSERS)

        return 

    def __call__(self, name: c.SOFTWARE_TYPE) -> c.Software:
        """ Generates the requested software object given its name. """

        if   name == 'android'  : return self.androidFactory()
        elif name in BROWSERS   : return self.browserFactory(name)
        elif name in c.OS_NAMES : return self.osFactory(name)
        else: raise ValueError(f'Software {name} is not a valid input.')


def getAgent(by: GENERATOR_TYPE, **kwargs):
    """ Creates and returns an appropriate function for user agent string generation 
        based on the provided type (<by> argument) and additional parameters.
    """

    """ Declaration of the various functions that can be returned """
    
    def read(filename: str):
        """ Reads a list of User-Agent strings from a given file. """

        exists = os.path.isfile(filename)
        istxt  = filename.endswith('.txt')

        if exists and istxt:
            with open(filename, mode = 'r', encoding = 'utf-8') as f:
                contents = f.read().splitlines()

            for agent in contents: yield agent

        elif not exists: raise FileNotFoundError(r'File {filename} does not exist.')
        elif not istxt : raise ValueError(r'File {filename} is not a .txt file.')


    def scrape( 
        limit   : int = 10,                       # Number of results to be returned (from most to least recent),
        browsers: Tuple[BROWSER_TYPE] = BROWSERS, # Names of browsers to be scraped (assumed lowercase)
        baseURL : str = 'http://www.useragentstring.com/pages/useragentstring.php?name={name}' # URL to scrape from
        ):
        """ Gathers a list of User-Agent strings from http://www.useragentstring.com for the given list of browsers """


        """ Helper functions """
        def _allAvailable(browsers: Tuple[BROWSER_TYPE]) -> bool: # Names of browsers to be scraped
            """ Checks if all input browsers are available for scraping from the URL """

            # Make set of all available browsers
            lines       = readFile('scraper_browsers.txt')
            allBrowsers = set( [b.rstrip('\n') for b in lines] )
            
            return not bool(set(browsers).difference(allBrowsers))


        def _scrapeURL( 
            session : requests.Session, # HTTP session
            browser : BROWSER_TYPE,     # Names of browsers to be scraped
            limit   : int,              # Number of results to be returned (from most to least recent),
            baseURL : str               # URL to scrape from
            ) -> list:
            """ Scrapes the latest User-Agent strings for the given browser """

            url      = baseURL.format(name = browser)
            response = session.get(url)
            soup     = BeautifulSoup(response.content, 'html.parser')
            texts    = [link.a.text for link in soup.findAll('li')]

            # Limit scraped results if needed
            if limit and len(texts) > limit: texts = texts[:limit]

            return texts


        """ Main body """
        if _allAvailable(browsers):
        
            session = requests.Session()
            for browser in browsers:
                agents = _scrapeURL(session, browser, limit, baseURL)
                for agent in agents: yield agent

        else:
            raise ValueError(f'User agent scraper: Non-supported browser detected. Aborting')


    def program(limit: int = 10): # Number of agents to be generated for each template (see constants.py)
        """ Generates programmatically a randomly-selected user agent according to a set type and browser. """

        make = SoftwareGenerator() # Instantiate software generator

        for osName, browserName in c.TEMPLATES.keys():

            # Generate a number of random agents for this browser/OS combination.
            for _ in range(limit):
                
                agent   = choice(c.TEMPLATES[(osName, browserName)]) # Select a template (if multiples exist)
                browser, os = make(browserName), make(osName)        # Make software objects
                
                # Replace version(s) details
                for name in c.OS_NAMES: agent = agent.replace(f'{{{name}}}', os.version)
                for name in BROWSERS  : agent = agent.replace(f'{{{name}}}', browser.version)
                
                agent = agent.replace('{webkit}', browser.details.get('webkit', '')).\
                            replace('{chromium}', browser.details.get('chromium', '')).\
                            replace('{device}', '; ' + os.details.get('device_name', '')).\
                            replace('{build}' , '; Build/' + os.details.get('build_number', ''))

                yield agent


    """ Main body """
    if   by == 'program': return program(**kwargs)
    elif by == 'scrape' : return scrape(**kwargs)
    elif by == 'file'   : return read(**kwargs)
    else: raise ValueError(f"User agent generation method {by} not implemented.")
