import sys
sys.path.append(r'..')
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
        style_name = object()
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme(object())

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception2(self):
        """
        style_name = builtins.object
        """
        style_name = builtins.object()

        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme(style_name)

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception3(self):
        """
        style_name = 'oo6'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("oo6")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception4(self):
        """
        style_name = 'pythön'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("pythön")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception5(self):
        """
        style_name = 'pythöin'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("pythöin")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception6(self):
        """
        style_name = 'py>thön'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("py>thön")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception7(self):
        """
        style_name = 'abcdefghiklmnopqrDst'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("abcdefghiklmnopqrDst")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception8(self):
        """
        style_name = 'pyhön'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("pyhön")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception9(self):
        """
        style_name = 'abcdefg?hijklmnopqrst'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("abcdefg?hijklmnopqrst")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception10(self):
        """
        style_name = '₟€'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("₟€")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception11(self):
        """
        style_name = 'foo'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("foo")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception12(self):
        """
        style_name = ''
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception13(self):
        """
        style_name = 'abcdefghijkmnopSqrst'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("abcdefghijkmnopSqrst")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception14(self):
        """
        style_name = 'rythön'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("rythön")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception15(self):
        """
        style_name = '3'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("3")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception16(self):
        """
        style_name = 'abcdefgRhijklmnopqrst'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("abcdefgRhijklmnopqrst")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception17(self):
        """
        style_name = 'pyPthön'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("pyPthön")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception18(self):
        """
        style_name = 'pthönĝ'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("pthönĝ")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception19(self):
        """
        style_name = 'abcdefghijk:lmnopqrst'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("abcdefghijk:lmnopqrst")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception20(self):
        """
        style_name = '₥€'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("₥€")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception21(self):
        """
        style_name = 'pthönG'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("pthönG")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception22(self):
        """
        style_name = 'fo'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("fo")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test__make_rich_color_theme_with_exception23(self):
        """
        style_name = 'oo'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_palette._make_rich_color_theme("oo")
    # endregion

    # endregion

