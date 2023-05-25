import sys
sys.path.append(r'..')
import builtins
import isort
import unittest
import isort.comments


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable isort.comments.parse
    
    # region FUZZER
    
    def test_parse(self):
        """
        line = ''
        """
        actual = isort.comments.parse("")
        
        self.assertEqual(('', ''), actual)
    
    def test_parse1(self):
        """
        line = '#￦'
        """
        actual = isort.comments.parse("#￦")
        
        self.assertEqual(('', '￦'), actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable isort.comments.add_to_line
    
    # region FUZZER
    
    def test_add_to_line(self):
        """
        comments = builtins.list[typing.Any]
        """
        actual = isort.comments.add_to_line([])
        
        self.assertEqual('', actual)
    
    def test_add_to_line1(self):
        """
        comments = builtins.list[typing.Any]
        original_string = '@'
        removed = min
        comment_prefix = '€'
        """
        actual = isort.comments.add_to_line([], "@", True, "€")
        
        self.assertEqual('@', actual)
    # endregion
    
    # endregion

