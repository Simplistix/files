from collections import MutableMapping
from .base import Base

class Dir(Base, MutableMapping):

    def list(self, key=None, reversed=False, files=True, dirs=True):
        return list_of_strings

    def read(self, path, encoding=None):
        return a_string

    def write(self, path, value, encoding=None, permissions=None):
        # path may be slash separated or sequence of segments
        # perms may be string or Permissions object
        return the_path

    def create(self, path, permissions=None):
        # perms may be string or Permissions object
        return the_path

    def __getitem__(self, name):
        # subclass KeyError to provide full path?
        return a_File_or_Dir_or_error

    def __setitem__(self, name, value):
        # move or copy from previous location?
        return
    
        
