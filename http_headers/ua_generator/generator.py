""" This module implements an abstract user agent extractor class as a template
    for the concrete user agent scraper and reader classes.
    The reader class Reader class generates user agents read from an input file.
    The scraper class retrieves user agents from the website http://www.useragentstring.com/.
    The programmes class generates user agents for the browsers and operating systems defined in 
    the constants.py file. It is based on the repo: https://github.com/iamdual/ua-generator/
"""

from ..definitions  import BROWSER_TYPE, DEVICE_TYPE, GENERATOR_TYPE
from ..definitions  import DEVICES, BROWSERS, MAX_USER_AGENT_SIZE as UA_SIZE
from .proxies       import ParserToGeneratorProxy as Parser
from typing         import Dict, List, Tuple
from collections    import defaultdict
from random         import choice
from .helpers       import getAgent
import warnings


class Generator():
    """ User agent generator. """


    def __init__(self, by: GENERATOR_TYPE, **kwargs):

        """ Initialisation method. Additional properties (browsers[list] 
            and userAgents[dict]) are populated in the concrete implementations.
        """

        self.userAgents: Dict[Tuple[str, str], List[str]] = defaultdict(list) # Empty user agent dict
        self.Parser = Parser()      # Adapter (user agent parser)
        self._import(by, **kwargs)  # Import user agents

        return


    def __call__(self,
        browser      : BROWSER_TYPE,   # Browser name
        device       : DEVICE_TYPE,    # Device type
        otherDevices : tuple = DEVICES # Other device types to choose from
        ) -> Tuple[BROWSER_TYPE, DEVICE_TYPE, str]:
        """ 
            Returns a randomly selected user agent from the given device type and browser names. 
            This is the default implementation, which applies to the Scraper and the Reader.
            If no user agent for the given browser/device combination is found, the following logic
            is implemented:
            - Get another user agent from a different browser (randomly chosen) from the same device type
            - If this fails, get another user agent from a different browser (randomly chosen) from a different device type
            The two above steps are repeated until we run out of possible device choices. If this happens
            a ValueError is raised
        """

        if not any(otherDevices):
            # No more devices are available to choose from. Raise error
            raise ValueError('No valid user agent was found.')

        else:
            
            # Get a randomly selected user agent string for the selected browser and device type (if one exists)
            applicableAgents = self.userAgents.get( (browser, device), [] )

            if applicableAgents: 
                # Valid user agent found. Exit
                return browser, device, choice(applicableAgents)
            
            else: 
                # No user agent is found (due to invalid browser name/ device type combination).
                # Get all user agents for this device type, even from different browsers
                applicableAgents = self._getDeviceCompatible(device)

                if bool(applicableAgents):                              # Valid user agent found from other browsers. Exit
                    browser   = choice(list(applicableAgents.keys()))   # Choose one of the browsers
                    userAgent = choice(applicableAgents[browser])       # Choose an agent from the selected browser

                    return browser, device, userAgent
                
                else:
                    # Agents for this device type are not found (for none of the available browsers).
                    # Update available (remaining) devices to choose an agent from
                    otherDevices = tuple([d for d in otherDevices if d != device])

                    # Choose another device type and re-run procedure with the remaining types for the same browser
                    device = choice(otherDevices)

                    return self.__call__(browser, device, otherDevices) # Recurse


    def _getDeviceCompatible(self, deviceType: DEVICE_TYPE) -> Dict[BROWSER_TYPE, List[str]]:
        """ Get all available user agents for a given device type """

        applicableAgents = {} # Dict containing a list of all device-compatible user agents (values) for all browsers (keys)
        for (curBrowser, curDevice), uaStringList in self.userAgents.items():
            
            if curDevice == deviceType: applicableAgents[curBrowser] = uaStringList

        return applicableAgents

    
    def _getAttribute(self, userAgent: str, attribute: tuple) -> str:
        """ Get an attribute of the user agent string. """

        return self.Parser.get(userAgent, attribute).lower()


    def _import(self, by: GENERATOR_TYPE, **kwargs):
        """ Adds a user agent to the dictionary """
        
        # Counters for stats
        succesfulImports, unsuccesfulImports = 0, 0

        for userAgent in getAgent(by, **kwargs):

            browser   = self._getAttribute(userAgent, ('browser', 'name'))
            device    = self._getAttribute(userAgent, ('device', 'type'))
            browserOK = browser in BROWSERS               # Is valid browser
            deviceOK  = device  in DEVICES                # Is valid device
            sizeOK    = len(userAgent.strip()) <= UA_SIZE # Has valid size

            if browserOK and deviceOK and sizeOK: # Valid user agent. Add to dict
                self.userAgents[browser, device].append(userAgent)
                succesfulImports += 1
            
            else: # Ignore user agent
                unsuccesfulImports += 1
            
        self._check(succesfulImports, unsuccesfulImports) # Check how many user agents were imported

        return
    

    @staticmethod
    def _check(successes: int, failures: int):
        """ Checks for succesfully imported user agents. Will raise error or warning. """

        if successes == 0: 
            # Zero user agents imported -> raise error
            raise ValueError(f'No valid user agents have been succesfully imported.')
        
        elif failures != 0: 
            # Not all user agents imported succesfully -> print warning
            ratio  = successes / (failures + successes) * 100
            msg    = f'Succesfully imported {successes} user agents ({round(ratio, 1)} % of all).'

            warnings.warn(msg)
        
        # else -> failures = 0 and successes != 0 (i.e. every single user agent is valid and succesfully imported)
        return 