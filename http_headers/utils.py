""" Implementation of some helper classes/function used by various submodules. """

from abc     import ABCMeta
from typing  import Any
import json
import os

def readFile(pathToFile: str) -> Any:
    """ Generic txt/json reader """

    isjson = lambda x: x.endswith('.json')
    istxt  = lambda x: x.endswith('.txt')

    if os.path.isfile(pathToFile):
        with open(pathToFile, mode = 'r', encoding = 'utf-8') as f:

            if   isjson(pathToFile): contents = json.load(f)
            elif istxt(pathToFile) : contents = f.readlines()
            else: raise RuntimeError(f"{pathToFile} is not a .json or .txt file")

    else:
        raise FileNotFoundError(f"{pathToFile} does not exist.")

    return contents


class Singleton(ABCMeta):
    """ Singleton metaclass """
    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]
