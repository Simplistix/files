from unittest import TestCase

from ..file import File

class Tests(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_read_bytes(self):
        pass

    def test_read_string(self):
        pass

    def test_write_bytes(self):
        pass

    def test_write_string(self):
        pass

    def test_size(self):
        pass

    def test_open(self):
        f = File('foo')
        with open(f.path) as file:
            file.read()
            pass
        
