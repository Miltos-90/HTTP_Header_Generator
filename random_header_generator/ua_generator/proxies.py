""" Implementation of a proxy class that modifies the user agents' parser's values (see ua_parser)
    for compatibility with the user-agent-string generators.
"""

from ..definitions  import UNKNOWN_NAME, UNKNOWN_VERSION, PARSER_TYPE, PARSERS, EMPTY
from typing         import Dict, Tuple
from abc            import ABC, abstractmethod
from ..ua_parser    import Parser, Dataclass
from ..utils        import readFile
from dataclasses    import fields


class Proxy(ABC):
    """ Abstract proxy class. Defines methods. """

   
    def __init__(self): 
        """ Initialisation method. Instantiates objects and reads necessary data. """

        self.parser = Parser() # Parses an agent string (see ./ua_parser)

        # Dictionary that maps from returned parser value (key), to the value indicated here
        self.aliases: Dict[PARSER_TYPE, Dict[str, str]] = readFile('parser_adapter.json')

        self.aliases.update({"device": readFile('operating_systems.json')})

        return


    @abstractmethod
    def __call__(self, userAgent: str) -> \
        Tuple[Dataclass, Dataclass, Dataclass, Dataclass, Dataclass]: 
        """ Extracts all dataclasses from the parser and modifies 
            their values accordingly before returning them.
        """
        pass


    def _getOriginal(self, 
        userAgent : str,                     # Agent from which the attribute is needdd
        attribute : Tuple[PARSER_TYPE, str]  # Attribute whose value will be returned.
        ) -> str:
        """ Get the original attribute of the user agent string from the parser"""

        if attribute == ('device', 'type'):

            # Device type will be inferred from OS name.
            osName = self.get(userAgent, attribute = ('os', 'name'))
            attr   = self.aliases["device"].get(osName, UNKNOWN_NAME)
            
        else: # Get any other attributes from the parser directly
            attr = self.parser.get(userAgent, attribute).lower()

        return attr


    @abstractmethod
    def _modify(self, 
        attribute : Tuple[PARSER_TYPE, str],  # Attribute whose value will be adapted.
        value     : str                       # Corresponding value returned by the parser
        ) -> str:
        """ Adapts the original attribute's value that was returned from the parser """
        pass
    

    def get(self, 
        userAgent : str,                     # Agent from which the attribute is needdd
        attribute : Tuple[PARSER_TYPE, str], # Attribute whose value will be returned.
        ) -> str:
        """ Get an (adapted) attribute of the user agent string. """

        attr = self._getOriginal(userAgent, attribute)
        return self._modify(attribute, attr)


class ParserToGeneratorProxy(Proxy):
    """ Adapter for a subset of the attribute values returned by the parser.
        Used primarily to modify browser and OS names to be accepted from the extractors (extractors.py).
        Example modifications: "chrome webview" -> "chrome", "opera mini" -> "opera", etc.
    """

    
    def __call__(self, userAgent: str) -> \
        Tuple[Dataclass, Dataclass, Dataclass, Dataclass, Dataclass]:
        """ Extracts all dataclasses from the parser and modifies 
            their values accordingly before returning them.
        """

        dclasses = self.parser(userAgent) # Dataclasses that a Parser's call produces

        for pName, dclass in zip(PARSERS, dclasses):

            for field in fields(dclass):

                fName = field.name                          # Get field name
                value = self.get(userAgent, (pName, fName)) # Get modified value
                setattr(dclass, fName, value)               # Update attribute with new value

        return dclasses


    def _modify(self, 
        attribute : Tuple[PARSER_TYPE, str],  # Attribute whose value will be adapted.
        value     : str                       # Corresponding value returned by the parser
        ) -> str:
        """ Adapts the original attribute's value that was returned from the parser """

        parserName = attribute[0]                     # Get name of the parser to be used
        aliasDict  = self.aliases.get(parserName, {}) # Get the corresponding mod. dictionary (if it exists)

        if bool(aliasDict):
            # Grab the property's value if it exists in the modification dict
            newValue = aliasDict.get(value)
            if newValue: value = newValue # Set new if exists

        return value


class ParserToClientHintsProxy(Proxy):
    """ Adapter for a subset of attribute values returned by the parser. Used to modify names 
        and version numbers to be suitable for use with the client hints generator (client_hints.py). 
        It sets unknown versions and browser/OS names (identified by the corresponding tokens 
        in definitions.py) to None values.
    """


    def __call__(self, userAgent: str) -> Tuple[Dataclass, Dataclass, Dataclass, Dataclass, Dataclass]:
        """ Extracts all dataclasses from the parser and modifies 
            their values accordingly before returning them.
        """

        dclasses = self.parser(userAgent) # Dataclasses that a Parser's call produces

        for dclass in dclasses:
            for field in fields(dclass):

                # Get name and current value of the dataclass
                variable = field.name
                value    = getattr(dclass, variable)

                # Modify if needed
                if value in [UNKNOWN_NAME, UNKNOWN_VERSION]: setattr(dclass, variable, EMPTY)

        return dclasses
    

    def _getOriginal(self, 
        userAgent : str,                     # Agent from which the attribute is needdd
        attribute : Tuple[PARSER_TYPE, str]  # Attribute whose value will be returned.
        ) -> str:
        """ Get the original attribute of the user agent string from the parser"""

        return self.parser.get(userAgent, attribute).lower()


    def _modify(self, 
        attribute : Tuple[PARSER_TYPE, str],  # Attribute whose value will be adapted.
        value     : str                       # Corresponding value returned by the parser
        ) -> str:
        """ Adapts the original attribute's value that was returned from the parser """

        return EMPTY if value in [UNKNOWN_NAME, UNKNOWN_VERSION] else value
    

