import sys
sys.path.append(r'..')
import builtins
import httpie
import unittest
import httpie.output.ui.rich_utils


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable httpie.output.ui.rich_utils.render_as_string

    # region FUZZER

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception(self):
        """
        renderable = object()
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string(object())

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception1(self):
        """
        renderable = builtins.object
        """
        renderable = builtins.object()

        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string(renderable)

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception2(self):
        """
        renderable = ''
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception3(self):
        """
        renderable = 'fo'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("fo")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception4(self):
        """
        renderable = 'pythöný'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("pythöný")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception5(self):
        """
        renderable = 'w'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("w")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception6(self):
        """
        renderable = 'pythön'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("pythön")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception7(self):
        """
        renderable = 'abcdefghjklmnHopqrst'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("abcdefghjklmnHopqrst")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception8(self):
        """
        renderable = 'jw'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("jw")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception9(self):
        """
        renderable = 'foo'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("foo")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception10(self):
        """
        renderable = 'abcdefghijklmGnopqrst'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("abcdefghijklmGnopqrst")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception11(self):
        """
        renderable = '­'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("­")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception12(self):
        """
        renderable = '€₶'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("€₶")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception13(self):
        """
        renderable = 'wfo'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("wfo")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception14(self):
        """
        renderable = 'abcdefghijklmnbopqrst'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("abcdefghijklmnbopqrst")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception15(self):
        """
        renderable = 'abcdefghijklmnopqrst'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("abcdefghijklmnopqrst")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception16(self):
        """
        renderable = 'pthönĝ'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("pthönĝ")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception17(self):
        """
        renderable = 'abcdefghijlmnopqrst'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("abcdefghijlmnopqrst")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception18(self):
        """
        renderable = 'pythön'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("pythön")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception19(self):
        """
        renderable = 'pythn'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("pythn")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception20(self):
        """
        renderable = 'foo['
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("foo[")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception21(self):
        """
        renderable = 'abcdefg2hijklmnopqrst'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("abcdefg2hijklmnopqrst")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception22(self):
        """
        renderable = '~oo'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("~oo")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception23(self):
        """
        renderable = 'pyth¦ön'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("pyth¦ön")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception24(self):
        """
        renderable = 'fooy'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("fooy")
    # endregion

    # endregion

