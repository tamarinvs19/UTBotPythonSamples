import sys
sys.path.append(r'..')
import isort.setuptools_commands
import builtins
import isort
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable isort.setuptools_commands.initialize_options
    
    # region FUZZER
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_initialize_options_with_exception(self):
        """
        self = isort.setuptools_commands.ISortCommand
        """
        i_sort_command = isort.setuptools_commands.ISortCommand()
        i_sort_command.user_options = []
        i_sort_command.arguments = {}
        i_sort_command.description = "abcdefghijklmnopqrst"
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        i_sort_command.initialize_options()
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_initialize_options_with_exception1(self):
        """
        self = isort.setuptools_commands.ISortCommand
        """
        i_sort_command = isort.setuptools_commands.ISortCommand()
        i_sort_command.arguments = {}
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        i_sort_command.initialize_options()
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_initialize_options_with_exception2(self):
        """
        self = isort.setuptools_commands.ISortCommand
        """
        i_sort_command = isort.setuptools_commands.ISortCommand()
        i_sort_command.description = "foo"
        i_sort_command.arguments = {}
        i_sort_command.user_options = []
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        i_sort_command.initialize_options()
    # endregion
    
    # endregion
    
    # region Test suites for executable isort.setuptools_commands.distribution_files
    
    # region FUZZER
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_distribution_files_with_exception(self):
        """
        self = isort.setuptools_commands.ISortCommand
        """
        i_sort_command = isort.setuptools_commands.ISortCommand()
        i_sort_command.user_options = []
        i_sort_command.arguments = {}
        i_sort_command.description = "Find distribution packages."
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        i_sort_command.distribution_files()
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_distribution_files_with_exception1(self):
        """
        self = isort.setuptools_commands.ISortCommand
        """
        i_sort_command = isort.setuptools_commands.ISortCommand()
        i_sort_command.description = "setup.py"
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        i_sort_command.distribution_files()
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_distribution_files_with_exception2(self):
        """
        self = isort.setuptools_commands.ISortCommand
        """
        i_sort_command = isort.setuptools_commands.ISortCommand()
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        i_sort_command.distribution_files()
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_distribution_files_with_exception3(self):
        """
        self = isort.setuptools_commands.ISortCommand
        """
        i_sort_command = isort.setuptools_commands.ISortCommand()
        i_sort_command.user_options = []
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        i_sort_command.distribution_files()
    # endregion
    
    # endregion
    
    # region Test suites for executable isort.setuptools_commands.run
    
    # region FUZZER
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_run_with_exception(self):
        """
        self = isort.setuptools_commands.ISortCommand
        """
        i_sort_command = isort.setuptools_commands.ISortCommand()
        i_sort_command.description = "€"
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        i_sort_command.run()
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_run_with_exception1(self):
        """
        self = isort.setuptools_commands.ISortCommand
        """
        i_sort_command = isort.setuptools_commands.ISortCommand()
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        i_sort_command.run()
    # endregion
    
    # endregion

