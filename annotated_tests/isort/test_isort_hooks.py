import sys
sys.path.append(r'..')
import builtins
import isort
import unittest
import isort.hooks


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable isort.hooks.get_output
    
    # region FUZZER
    
    def test_get_output_with_exception(self):
        """
        command = builtins.list[typing.Any]
        """
        # This test fails because function [isort.hooks.get_output] produces [OSError]
        isort.hooks.get_output([])
    # endregion
    
    # endregion
    
    # region Test suites for executable isort.hooks.get_lines
    
    # region FUZZER
    
    def test_get_lines_with_exception(self):
        """
        command = builtins.list[typing.Any]
        """
        # This test fails because function [isort.hooks.get_lines] produces [OSError]
        isort.hooks.get_lines([])
    # endregion
    
    # endregion
    
    # region Test suites for executable isort.hooks.git_hook
    
    # region FUZZER
    
    def test_git_hook_with_exception(self):
        # This test fails because function [isort.hooks.git_hook] produces [subprocess.CalledProcessError]
        isort.hooks.git_hook()
    
    def test_git_hook_with_exception1(self):
        """
        strict = min
        modify = min
        lazy = zero (mutated from min)
        settings_file = '--name-only'
        directories = builtins.list[typing.Any]
        """
        # This test fails because function [isort.hooks.git_hook] produces [subprocess.CalledProcessError]
        isort.hooks.git_hook(True, True, True, "--name-only", [])
    # endregion
    
    # endregion

