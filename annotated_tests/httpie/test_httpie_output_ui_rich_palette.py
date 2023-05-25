import sys
sys.path.append(r'../..')
import types
import builtins
import httpie
import unittest
import httpie.output.ui.rich_palette


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable httpie.output.ui.rich_palette._make_rich_color_theme

    # region FUZZER

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception(self):
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme()

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception1(self):
        """
        style_name = None
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme(None)

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception2(self):
        """
        style_name = 'o¥o'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("o¥o")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception3(self):
        """
        style_name = '€⁽'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("€⁽")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception4(self):
        """
        style_name = ''
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception5(self):
        """
        style_name = ''
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception6(self):
        """
        style_name = '?foo'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("?foo")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception7(self):
        """
        style_name = 'abcdefgijklmnopqrst'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("abcdefgijklmnopqrst")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception8(self):
        """
        style_name = 'fo2o'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("fo2o")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception9(self):
        """
        style_name = 'pybthön'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("pybthön")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception10(self):
        """
        style_name = 'abdefghi5jklmnopqrst'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("abdefghi5jklmnopqrst")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception11(self):
        """
        style_name = '€₱'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("€₱")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception12(self):
        """
        style_name = '€'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("€")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception13(self):
        """
        style_name = 'foo'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("foo")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception14(self):
        """
        style_name = 'pythön'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("pythön")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception15(self):
        """
        style_name = 'abcdefghijklmnopqrst'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("abcdefghijklmnopqrst")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception16(self):
        """
        style_name = 'abcdefghijklmPnopqrst'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("abcdefghijklmPnopqrst")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception17(self):
        """
        style_name = 'fo'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("fo")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception18(self):
        """
        style_name = 'f¤oo'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("f¤oo")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception19(self):
        """
        style_name = 'afoo'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("afoo")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception20(self):
        """
        style_name = 'oo'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("oo")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception21(self):
        """
        style_name = 'abcdefghijklmnopqrst'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("abcdefghijklmnopqrst")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception22(self):
        """
        style_name = 'pythn'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("pythn")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception23(self):
        """
        style_name = 'D'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("D")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception24(self):
        """
        style_name = 'pythönð'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("pythönð")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception25(self):
        """
        style_name = 'abcdefghijfklmnopqrst'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("abcdefghijfklmnopqrst")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception26(self):
        """
        style_name = 'abcdefghjklmnopqrst'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("abcdefghjklmnopqrst")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception27(self):
        """
        style_name = 'abcdefghiklmnopqrst'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("abcdefghiklmnopqrst")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception28(self):
        """
        style_name = 'abcdefghijklnopqrst'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("abcdefghijklnopqrst")
    # endregion

    # endregion

