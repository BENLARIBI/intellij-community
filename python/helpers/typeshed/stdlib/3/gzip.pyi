# Stubs for gzip (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
import _compression

def open(filename, mode='', compresslevel=9, encoding=None, errors=None, newline=None): ...

class _PaddedFile:
    file = ...  # type: Any
    def __init__(self, f, prepend=b''): ...
    def read(self, size): ...
    def prepend(self, prepend=b''): ...
    def seek(self, off): ...
    def seekable(self): ...

class GzipFile(_compression.BaseStream):
    myfileobj = ...  # type: Any
    mode = ...  # type: Any
    name = ...  # type: Any
    compress = ...  # type: Any
    fileobj = ...  # type: Any
    def __init__(self, filename=None, mode=None, compresslevel=9, fileobj=None, mtime=None): ...
    @property
    def filename(self): ...
    @property
    def mtime(self): ...
    crc = ...  # type: Any
    def write(self, data): ...
    def read(self, size=-1): ...
    def read1(self, size=-1): ...
    def peek(self, n): ...
    @property
    def closed(self): ...
    def close(self): ...
    def flush(self, zlib_mode=...): ...
    def fileno(self): ...
    def rewind(self): ...
    def readable(self): ...
    def writable(self): ...
    def seekable(self): ...
    def seek(self, offset, whence=...): ...
    def readline(self, size=-1): ...

class _GzipReader(_compression.DecompressReader):
    def __init__(self, fp): ...
    def read(self, size=-1): ...

def compress(data, compresslevel=9): ...
def decompress(data): ...
