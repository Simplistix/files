from unittest import TestCase

from ..dir import Dir
from ..file import File

class Base(object):

    def test_expand_user(self):
        # expand ~
        pass

    def test_read_permissions(self):
        pass

    def test_write_permissions(self):
        pass

    def test_write_partial_permissions(self):
        pass

    def test_read_atime(self):
        pass

    def test_write_atime(self):
        pass

    def test_read_mtime(self):
        pass

    def test_write_mtime(self):
        pass
    
    def test_read_ctime(self):
        pass

    def test_write_ctime(self):
        pass
    
class TestDir(Base, TestCase):

    def make_one(self):
        # create
        # set perms
        # set atime
        # set mtime
        # set ctime
        self.thing = Dir()

class TestFile(Base, TestCase):

    def make_one(self):
        # create
        # set perms
        # set atime
        # set mtime
        # set ctime
        self.thing = File()
