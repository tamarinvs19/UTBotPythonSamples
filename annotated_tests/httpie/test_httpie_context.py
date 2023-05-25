import sys
sys.path.append(r'../..')
import httpie.context
import builtins
import argparse
import io
import IPython.lib.pretty
import pathlib
import httpie.config
import tempfile
import httpie
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable httpie.context.__repr__

    # region FUZZER

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test___repr___with_exception(self):
        """
        self = httpie.context.Environment
        """
        environment = httpie.context.Environment()
        namespace = argparse.Namespace()
        raw_i_o_base = io.RawIOBase()
        buffered_writer = io.BufferedWriter(raw_i_o_base)
        c_unicode_i_o = IPython.lib.pretty.CUnicodeIO()
        environment.is_windows = False
        environment.program_name = "foo"
        environment.stdin_isatty = False
        environment.args = namespace
        environment.colors = 170141183460469231731687303715884105727
        environment.stdout = buffered_writer
        environment.stderr_isatty = False
        environment.stdout_encoding = "foo"
        environment.stderr = c_unicode_i_o

        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        environment.__repr__()

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test___repr___with_exception1(self):
        """
        self = httpie.context.Environment
        """
        environment = httpie.context.Environment()
        path = pathlib.Path()
        raw_i_o_base = io.RawIOBase()
        buffered_random = io.BufferedRandom(raw_i_o_base)
        namespace = argparse.Namespace()
        c_unicode_i_o = IPython.lib.pretty.CUnicodeIO()
        config = httpie.config.Config()
        config.DEFAULTS = {"pythön": [], }
        config.FILENAME = "abcdefghijklmnopqrst"
        environment.config_dir = path
        environment.stdout = buffered_random
        environment.stdin_encoding = "€"
        environment.args = namespace
        environment.stdout_encoding = "pythön"
        environment.program_name = "pythön"
        environment.is_windows = False
        environment.stderr = c_unicode_i_o
        environment._config = config

        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        environment.__repr__()
    # endregion

    # endregion

    # region Test suites for executable httpie.context.apply_warnings_filter

    # region FUZZER

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_apply_warnings_filter_with_exception(self):
        """
        self = httpie.context.Environment
        """
        environment = httpie.context.Environment()
        namespace = argparse.Namespace()
        raw_i_o_base = io.RawIOBase()
        buffered_writer = io.BufferedWriter(raw_i_o_base)
        c_unicode_i_o = IPython.lib.pretty.CUnicodeIO()
        environment.is_windows = False
        environment.program_name = "foo"
        environment.stdin_isatty = False
        environment.args = namespace
        environment.colors = 170141183460469231731687303715884105727
        environment.stdout = buffered_writer
        environment.stderr_isatty = False
        environment.stdout_encoding = "pythön"
        environment.stderr = c_unicode_i_o

        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        environment.apply_warnings_filter()
    # endregion

    # endregion

    # region Test suites for executable httpie.context._make_rich_console

    # region FUZZER

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_console_with_exception(self):
        """
        self = httpie.context.Environment
        file = tempfile.SpooledTemporaryFile[typing.Any]
        force_terminal = min (mutated from zero)
        """
        environment = httpie.context.Environment()
        string_i_o = io.StringIO()
        config = httpie.config.Config()
        config.FILENAME = "pythön"
        config.DEFAULTS = {"pythön": [], }
        c_unicode_i_o = IPython.lib.pretty.CUnicodeIO()
        namespace = argparse.Namespace()
        path = pathlib.Path()
        environment.stderr = string_i_o
        environment._config = config
        environment.show_displays = True
        environment.stdout = c_unicode_i_o
        environment.args = namespace
        environment.stdin_isatty = True
        environment.config_dir = path
        environment.colors = 1
        file = tempfile.SpooledTemporaryFile()

        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        environment._make_rich_console(file, False)
    # endregion

    # endregion

