import sys
sys.path.append(r'../..')
import builtins
import httpie.context
import types
import IPython.lib.pretty
import pathlib
import httpie
import unittest
import httpie.output.ui.man_pages


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable httpie.output.ui.man_pages.is_available

    # region FUZZER

    def test_is_available(self):
        """
        program = 'nt'
        """
        actual = httpie.output.ui.man_pages.is_available("nt")

        self.assertEqual(False, actual)
    # endregion

    # endregion

    # region Test suites for executable httpie.output.ui.man_pages.display_for

    # region FUZZER

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_display_for_with_exception(self):
        """
        env = httpie.context.Environment
        program = ''
        """
        env = httpie.context.Environment()
        c_unicode_i_o = IPython.lib.pretty.CUnicodeIO()
        c_unicode_i_o1 = IPython.lib.pretty.CUnicodeIO()
        env.stdin = None
        env.stdout = c_unicode_i_o
        env._orig_stderr = c_unicode_i_o1
        env.stderr_isatty = True

        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.man_pages.display_for(env, "")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_display_for_with_exception1(self):
        """
        env = httpie.context.Environment
        program = 'abcdefghijklmnopqrst'
        """
        env = httpie.context.Environment()
        path = pathlib.Path()
        c_unicode_i_o = IPython.lib.pretty.CUnicodeIO()
        env.is_windows = False
        env.config_dir = path
        env.show_displays = True
        env.stderr_isatty = True
        env._orig_stderr = c_unicode_i_o
        env.program_name = "pythön"

        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.man_pages.display_for(env, "abcdefghijklmnopqrst")
    # endregion

    # endregion

