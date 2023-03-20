""" This module implements the user agent parser, which extracts information from a
    user agent string regarding the browser, operating system, device and engine.
    
    Based on the ua_parser_py repo: https://github.com/vitalibo/ua-parser-py. 
"""

from dataclasses    import fields
from ..utils        import Singleton
from .              import regexes as r
from .              import datatypes as dtypes
from typing         import Tuple, Union, Callable, List, Type, cast
from ..definitions  import UNKNOWN_NAME, UNKNOWN_VERSION, PARSER_TYPE, PARSERS
import re


class GenericParser():
    """ Generic parser class. Parses a user agent string to extract information about 
        one of the following:
        * Browser : name, version, major version
        * CPU     : architecture
        * Device  : vendor, model, type
        * Engine  : name, version
        * OS      : name, version
    """

    def __init__(self, 
        regexes: List[r.REGEXDICT],   # List of regexes to use for property matching 
        cls    : Type[dtypes.Dataclass] # Dataclass that will be given as output
        ):
        """ Initialisation method """

        self.regexes   = regexes 
        self.className = cls     

        return 

    
    def _getMatch(self, userAgent: str) -> \
        Tuple[Union[re.Match[str], None], r.REGEXDICT]:
        """ Tries to match the user agent string with the regex list.
            It returns the match, and the dictionary that will map its 
            keys to the corresponding matching values.
        """
        
        matches, dict_ = None, cast(r.REGEXDICT, {})

        for dict_ in self.regexes:
            matches = dict_['regex'].search(userAgent)
            if matches: break
        
        return matches, dict_


    @staticmethod
    def _makeDict(matches: Union[re.Match[str], None], dict_ : r.REGEXDICT) -> dict:
        """ Makes dictionary with all properties that match """

        d = {} # Output dictionary
        if matches:
            for i, (key, value) in enumerate(dict_['props'].items()):
                try:               match = matches.group(i + 1)
                except IndexError: match = None

                d[key] = GenericParser._map(match, key, value)

        return d

    
    @staticmethod
    def _map(match: Union[str, None], key:str, value: Union[str, Callable, None] = None) -> str:
        """ Mapper function. Processes a substring returned as the result of re.group function.
            The returned function modifies <m> (= a regex match object) according to the type of the 
            specified <value>. 
            In particular, if a match for the property <key> has been found: 
                * If value is None, it returns the corresponding match,
                * if the value is a string, the match is ignored, and the value itself is returned,
                * if the value is a callable (function) it is being applied to the match, and the
                result of that operation is returned.

            If no match is found for the property <key>:
                * If value is a string, the value itself is returned (similar to the above)
                * If the value is None or a callable, a property-dependent unknown token is returned
        """

        if match:
            if   not value                  : out = match
            elif isinstance(value, str)     : out = value
            elif isinstance(value, Callable): out = value(match)

        else:
            if isinstance(value, str) : out = value
            else                      : out = GenericParser._UNKtoken(key)
        
        return out

    
    @staticmethod
    def _UNKtoken(key:str) -> str:
        """ Returns the unknown token corresponding to the input key """
        return  UNKNOWN_VERSION if key == 'version' else UNKNOWN_NAME


    def _dataClassFromDict(self, argDict: dict, filter = False):
        """ Populates the appropriate dataclass from a dictionary """

        # Get fields that exist in the class
        fieldSet = {f.name for f in fields(self.className) if f.init}

        # Remove additional args from the argDict that do not appear in the dataclass if needed
        if filter:
            filteredArgDict = {k : v for k, v in argDict.items() if k in fieldSet}
        else:
            filteredArgDict = argDict
            
        # make dataclasss
        return self.className(**filteredArgDict)

    
    def __call__(self, userAgent: str) -> dtypes.Dataclass:
        """ Searches the regex list (see regexes.py) for a match with the user
            agent string, and extracts the information needed from a user agent 
            string by the substrings returned by a regex match. Then it generates
            the appropriate data class
        """

        matches, dict_ = self._getMatch(userAgent)
        d = self._makeDict(matches, dict_)
        c = self._dataClassFromDict(d)
        
        return c


def parserFactory(name: PARSER_TYPE) -> GenericParser:
    """ Makes a GenericParser object according to the specified type (name). """

    if   name == 'browser': return GenericParser(r.BROWSER, dtypes.Browser)
    elif name == 'cpu'    : return GenericParser(r.CPU,     dtypes.CPU)
    elif name == 'device' : return GenericParser(r.DEVICE,  dtypes.Device)
    elif name == 'engine' : return GenericParser(r.ENGINE,  dtypes.Engine)
    elif name == 'os'     : return GenericParser(r.OS,      dtypes.OS)
    else: raise ValueError(f" Parser {name} is not implemented.")


class Parser(metaclass = Singleton):
    """ User agent string parser. It extracts the following information:
        Browser : name, version, major version
        CPU     : architecture
        Device  : vendor, model, type
        Engine  : name, version
        OS      : name, version
    """

    def __init__(self):
        """ Initialisation method. Instantiates required parsers. 
            The format of the input lists can be found on regexes.py
        """

        # Dictionary of parser names and corresponding objects
        self.parsers = {key: parserFactory(key) for key in PARSERS}

        return


    def __call__(self, userAgent: str) -> \
        Tuple[dtypes.Dataclass, dtypes.Dataclass, dtypes.Dataclass, dtypes.Dataclass, dtypes.Dataclass]:
        """ Parses a user agent string, returning the following classes (in order of appearance):
            browser, cpu, device, engine, os
        """
        return tuple(self.parsers[key](userAgent) for key in PARSERS)

    
    def get(self,
        userAgent : str,                     # User agent string
        attribute : Tuple[PARSER_TYPE, str], # Property whose value will be returned.
        ) -> str:
        """ Returns a specific property of the user agent string.
            The full list of properties can be found on templates.py, in the classes
            Browser, CPU, Device, Engine, OS.
        """

        parserName, propertyName = attribute     # Parser's name and key that the parser should look for        
        parser = self.parsers.get(parserName)    # Get the parser that will provide the key's value

        if parser:
            dClass = parser(userAgent)           # Get object from the corresponding generic parser
            return getattr(dClass, propertyName) # Extract the corresponding key (=property). Raises AttributeError if not found

        else: 
            raise KeyError(f'Parser {parserName} does not exist')
