""" Implementation of some helper classes/function used by various submodules. """

from abc     import ABCMeta
from typing  import Any
import json
import os
import os

PATH  = os.path.dirname(__file__) # Absolute path of this file

def readFile(filename: str) -> Any:
    """ Generic txt/json reader """

    isjson   = lambda x: x.endswith('.json')
    istxt    = lambda x: x.endswith('.txt')
    filePath = os.path.join(PATH, filename)

    if os.path.isfile(filePath):
        with open(filePath, mode = 'r', encoding = 'utf-8') as f:

            if   isjson(filePath): contents = json.load(f)
            elif istxt(filePath) : contents = f.read().splitlines()
            else: raise RuntimeError(f"{filePath} is not a .json or .txt file")

    else:
        raise FileNotFoundError(f"{filePath} does not exist.")

    return contents


class Singleton(ABCMeta):
    """ Singleton metaclass """
    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]
