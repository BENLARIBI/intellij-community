# Stubs for mimetools (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
import rfc822

class Message(rfc822.Message):
    encodingheader = ...  # type: Any
    typeheader = ...  # type: Any
    def __init__(self, fp, seekable=1): ...
    plisttext = ...  # type: Any
    type = ...  # type: Any
    maintype = ...  # type: Any
    subtype = ...  # type: Any
    def parsetype(self): ...
    plist = ...  # type: Any
    def parseplist(self): ...
    def getplist(self): ...
    def getparam(self, name): ...
    def getparamnames(self): ...
    def getencoding(self): ...
    def gettype(self): ...
    def getmaintype(self): ...
    def getsubtype(self): ...

def choose_boundary(): ...
def decode(input, output, encoding): ...
def encode(input, output, encoding): ...
def copyliteral(input, output): ...
def copybinary(input, output): ...
