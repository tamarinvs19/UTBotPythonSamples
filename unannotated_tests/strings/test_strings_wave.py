import sys
sys.path.append(r'..\..\..')
import builtins
import strings
import unittest
import strings.wave


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.wave.wave
    
    # region FUZZER
    
    def test_wave(self):
        """
        txt = '€'
        """
        actual = strings.wave.wave("€")
        
        self.assertEqual([], actual)
    
    def test_wave1(self):
        """
        txt = 'abcdefBhijklmnopqrst'
        """
        actual = strings.wave.wave("abcdefBhijklmnopqrst")
        
        self.assertEqual(['AbcdefBhijklmnopqrst', 'aBcdefBhijklmnopqrst', 'abCdefBhijklmnopqrst', 'abcDefBhijklmnopqrst', 'abcdEfBhijklmnopqrst', 'abcdeFBhijklmnopqrst', 'abcdefBhijklmnopqrst', 'abcdefBHijklmnopqrst', 'abcdefBhIjklmnopqrst', 'abcdefBhiJklmnopqrst', 'abcdefBhijKlmnopqrst', 'abcdefBhijkLmnopqrst', 'abcdefBhijklMnopqrst', 'abcdefBhijklmNopqrst', 'abcdefBhijklmnOpqrst', 'abcdefBhijklmnoPqrst', 'abcdefBhijklmnopQrst', 'abcdefBhijklmnopqRst', 'abcdefBhijklmnopqrSt', 'abcdefBhijklmnopqrsT'], actual)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_wave_with_exception(self):
        """
        txt = builtins.bytes
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        strings.wave.wave(bytes(268435458))
    # endregion
    
    # endregion

