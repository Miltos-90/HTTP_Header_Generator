""" Implementation of some helper classes/function used by various submodules. """

from abc     import ABCMeta
from typing  import Any
import random as rd
import json
import os
import os

PATH  = os.path.dirname(__file__) # Absolute path of this file


def readFile(filename: str) -> Any:
    """ Generic txt/json reader """

    isjson   = lambda x: x.endswith('.json')
    istxt    = lambda x: x.endswith('.txt')
    filePath = os.path.join(PATH, 'data', filename)

    if os.path.isfile(filePath):
        with open(filePath, mode = 'r', encoding = 'utf-8') as f:

            if   isjson(filePath): contents = json.load(f)
            elif istxt(filePath) : contents = f.read().splitlines()
            else: raise RuntimeError(f"{filePath} is not a .json or .txt file")

    else:
        raise FileNotFoundError(f"{filePath} does not exist.")

    return contents


def addQFactors(l:list) -> list:
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


class Singleton(ABCMeta):
    """ Singleton metaclass """
    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]
