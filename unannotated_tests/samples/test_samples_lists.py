import sys
sys.path.append(r'../..')
import builtins
import samples.lists
import datetime
import samples
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable samples.lists.find_articles_with_author
    
    # region FUZZER
    
    def test_find_articles_with_author(self):
        """
        articles = builtins.list[samples.lists.Article]
        author = 'Spythön'
        """
        article = samples.lists.Article("€", "pythön", "pythön", datetime.datetime(1, 4, 1, 2))
        
        actual = samples.lists.find_articles_with_author([article], "Spythön")
        
        self.assertEqual([], actual)
    # endregion
    
    # endregion

