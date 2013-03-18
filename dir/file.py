
class File(object):

    def __init__(self, path):
        self.path = path
        pass

    def read(self, encoding=None):
        pass

    def write(self, value, encoding=None):
        pass
    
    @property
    def permissions(self):
        # setable and getable
        # setable with string or permissions object
        return Permissions(self.path)

    def open(self, mode='r', other_stuff_from_file):
        # maybe just document to use open(f.path)?
        return open(self.path)
