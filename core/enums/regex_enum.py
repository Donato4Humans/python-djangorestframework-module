from enum import Enum


class RegexEnum(Enum):
    NAME = (# we can add more variables and choose what we need
        r'^[A-Z][a-z]{,19}$', # this part will go into pattern arg of class constructor
        'Only alpha characters are allowed.', # and this into msg arg
    )

    def __init__(self, pattern:str, msg:str):
        self.pattern = pattern
        self.msg = msg