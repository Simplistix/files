from collections import MutableMapping

class Dir(MutableMapping):

    def __init__(self, path):
        pass

    def list(self, order_by, order_dir):
        return list_of_strings

    def read(self, path, encoding=None):
        return a_string

    def write(self, path, value, encoding=None, permissions=None):
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
    
        
