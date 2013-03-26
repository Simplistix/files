# all should be getable and setable

def set_permissions(self, value):
    print(self, value)
        
class Base(object):

    def __init__(self, path):
        self.path = path
    
    def _permissions(self):
        # setable and getable
        # setable with string or permissions object
        return Permissions(self.path)

    permissions = property(_permissions, set_permissions)
    
    @property
    def atime(self):
        return datetime

    @property
    def mtime(self):
        return datetime

    @property
    def ctime(self):
        return datetime

    
