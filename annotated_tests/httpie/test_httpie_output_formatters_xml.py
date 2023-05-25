import sys
sys.path.append(r'../..')
import builtins
import types
import httpie
import unittest
import httpie.output.formatters.xml


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable httpie.output.formatters.xml.parse_xml

    # region FUZZER

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_parse_xml_with_exception(self):
        """
        data = '€'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.formatters.xml.parse_xml("€")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_parse_xml_with_exception1(self):
        """
        data = 'abdefghijklmnopqrst'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.formatters.xml.parse_xml("abdefghijklmnopqrst")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_parse_xml_with_exception2(self):
        """
        data = 'fo'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.formatters.xml.parse_xml("fo")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_parse_xml_with_exception3(self):
        """
        data = 'pyhön'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.formatters.xml.parse_xml("pyhön")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_parse_xml_with_exception4(self):
        """
        data = 'abcdefhghijklmnopqrst'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.formatters.xml.parse_xml("abcdefhghijklmnopqrst")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_parse_xml_with_exception5(self):
        """
        data = 'abcdefghijklmnopqrst'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.formatters.xml.parse_xml("abcdefghijklmnopqrst")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_parse_xml_with_exception6(self):
        """
        data = 'abcdefghijklmnopqrst'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.formatters.xml.parse_xml("abcdefghijklmnopqrst")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_parse_xml_with_exception7(self):
        """
        data = 'fo'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.formatters.xml.parse_xml("fo")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_parse_xml_with_exception8(self):
        """
        data = 'Parse given XML `data` string into an appropriate :class:`~xml.dom.minidom.Document` object.'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.formatters.xml.parse_xml("Parse given XML `data` string into an appropriate :class:`~xml.dom.minidom.Document` object.")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_parse_xml_with_exception9(self):
        """
        data = 'abcdefghjklmnHopqrst'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.formatters.xml.parse_xml("abcdefghjklmnHopqrst")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_parse_xml_with_exception10(self):
        """
        data = 'pythöné'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.formatters.xml.parse_xml("pythöné")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_parse_xml_with_exception11(self):
        """
        data = 'Parse given XML `data` string into an appropriate :class:`~xml.dom.minidom.Document` oject.'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.formatters.xml.parse_xml("Parse given XML `data` string into an appropriate :class:`~xml.dom.minidom.Document` oject.")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_parse_xml_with_exception12(self):
        """
        data = 'foSo'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.formatters.xml.parse_xml("foSo")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_parse_xml_with_exception13(self):
        """
        data = 'foo'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.formatters.xml.parse_xml("foo")
    # endregion

    # endregion

    # region Test suites for executable httpie.output.formatters.xml.parse_declaration

    # region FUZZER

    def test_parse_declaration(self):
        """
        raw_body = 'oo6'
        """
        actual = httpie.output.formatters.xml.parse_declaration("oo6")

        self.assertEqual(None, actual)
    # endregion

    # endregion

