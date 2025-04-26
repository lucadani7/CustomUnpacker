import struct
from collections import namedtuple

"""Constants that we will use in the program, using namedtuple data structure. See more here: https://docs.python.org/3/library/collections.html#collections.namedtuple"""

Constants = namedtuple('Constants', ['HEADER_FORMAT', 'HEADER_SIZE'])
"""HEADER_FORMAT: 256s is a string with exactly 256 bytes for file name storage;
    I from 256sI represents an elem which is an instance of unsigned int on 4 bytes for file size storage
    
    HEADER_SIZE: compute dinamically the header size
"""
constants = Constants('256sI', struct.calcsize('256sI'))
