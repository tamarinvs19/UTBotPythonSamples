import sys
sys.path.append(r'../../..')
import builtins
import samples
import unittest
import samples.graph


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable samples.graph.bfs
    
    # region FUZZER
    
    def test_bfs(self):
        """
        nodes = builtins.list[typing.Any]
        """
        actual = samples.graph.bfs([])
        
        self.assertEqual([], actual)
    # endregion
    
    # endregion

