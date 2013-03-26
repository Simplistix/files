from testfixtures import TempDirectory
from unittest import TestCase

class Tests(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_getitem_dir(self):
        pass

    def test_getitem_file(self):
        pass

    def test_setitem_file(self):
        pass

    def test_setitem_dir(self):
        pass

    def test_setitem_new_file(self):
        pass

    def test_setitem_new_dir(self):
        pass

    def test_move_dir(self):
        pass

    def test_move_file(self):
        pass
    
class ListTests(TestCase):

    def test_default(self):
        # unordered by default
        pass

    def test_order_by_name(self):
        # ordered by name by default
        pass

    def test_order_by_atime(self):
        pass

    def test_order_by_mtime(self):
        pass

    def test_order_by_ctime(self):
        pass

    def test_order_by_junk(self):
        pass

    def test_order_reversed(self):
        pass

    def test_files_only(self):
        pass

    def test_dirs_only(self):
        pass
    
class WriteTests(TestCase):

    def test_bytes(self):
        pass

    def test_string(self):
        pass

    def test_slash_separate(self):
        # make intermediaries
        pass
    
    def test_path_segments(self):
        pass
    
    def test_permissions(self):
        # make sure intermediaries are created the same?
        pass

class CreateTests(TestCase):

    def test_string(self):
        pass

    def test_slash_separated(self):
        # make intermediaries
        pass
    
    def test_path_segments(self):
        pass
    
    def test_permissions(self):
        pass
