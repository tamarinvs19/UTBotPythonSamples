import sys
sys.path.append(r'..')
import builtins
import isort
import unittest
import isort.format


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable isort.format.format_simplified
    
    # region FUZZER
    
    def test_format_simplified(self):
        """
        import_line = 'impor0t'
        """
        actual = isort.format.format_simplified("impor0t")
        
        self.assertEqual('impor0t', actual)
    
    def test_format_simplified1(self):
        """
        import_line = 'import e'
        """
        actual = isort.format.format_simplified("import e")
        
        self.assertEqual('e', actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable isort.format.format_natural
    
    # region FUZZER
    
    def test_format_natural(self):
        """
        import_line = 'py5tön'
        """
        actual = isort.format.format_natural("py5tön")
        
        self.assertEqual('import py5tön', actual)
    
    def test_format_natural1(self):
        """
        import_line = ';.'
        """
        actual = isort.format.format_natural(";.")
        
        self.assertEqual('from ; import ', actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable isort.format.ask_whether_to_apply_changes_to_file
    
    # region FUZZER
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_ask_whether_to_apply_changes_to_file_with_exception(self):
        """
        file_path = '6o'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        isort.format.ask_whether_to_apply_changes_to_file("6o")
    # endregion
    
    # endregion

