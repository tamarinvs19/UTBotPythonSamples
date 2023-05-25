import sys
sys.path.append(r'../..')
import rich.markdown
import builtins
import rich.rule
import rich.containers
import httpie
import unittest
import httpie.output.ui.rich_utils


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable httpie.output.ui.rich_utils.render_as_string

    # region FUZZER

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception(self):
        """
        renderable = rich.markdown.MarkdownElement
        """
        renderable = rich.markdown.MarkdownElement()

        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string(renderable)

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception1(self):
        """
        renderable = 'abcdefghijklmnopqrst'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("abcdefghijklmnopqrst")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception2(self):
        """
        renderable = 'pyhön'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("pyhön")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception3(self):
        """
        renderable = '€'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("€")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception4(self):
        """
        renderable = 'abcdefghiklmnopqrst'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("abcdefghiklmnopqrst")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception5(self):
        """
        renderable = rich.rule.Rule
        """
        renderable = rich.rule.Rule()

        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string(renderable)

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception6(self):
        """
        renderable = 'foo'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("foo")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception7(self):
        """
        renderable = rich.markdown.CodeBlock
        """
        renderable = rich.markdown.CodeBlock("ab¡cdefghijklmnopqrst", "abcdefghijklmnopqrst")

        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string(renderable)

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception8(self):
        """
        renderable = '€⁽'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("€⁽")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception9(self):
        """
        renderable = 'pythön'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("pythön")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception10(self):
        """
        renderable = 'foo['
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("foo[")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception11(self):
        """
        renderable = '€⃃'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("€⃃")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception12(self):
        """
        renderable = rich.markdown.Heading
        """
        renderable = rich.markdown.Heading("w")

        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string(renderable)

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception13(self):
        """
        renderable = 'w'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("w")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception14(self):
        """
        renderable = rich.markdown.ImageItem
        """
        renderable = rich.markdown.ImageItem("€⁽", False)

        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string(renderable)

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception15(self):
        """
        renderable = 'aGbcdfghijklmnopqrst'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("aGbcdfghijklmnopqrst")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception16(self):
        """
        renderable = 'w'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("w")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception17(self):
        """
        renderable = rich.containers.Renderables
        """
        renderable = rich.containers.Renderables()

        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string(renderable)

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception18(self):
        """
        renderable = rich.markdown.CodeBlock
        """
        renderable = rich.markdown.CodeBlock("foo", "€")

        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string(renderable)

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception19(self):
        """
        renderable = 'foo'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("foo")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception20(self):
        """
        renderable = ''
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception21(self):
        """
        renderable = '€⃕'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("€⃕")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_render_as_string_with_exception22(self):
        """
        renderable = 'B'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.rich_utils.render_as_string("B")
    # endregion

    # endregion

