import sys
sys.path.append(r'../..')
import samples.graph
import builtins
import types
import samples
import unittest


class TestNode(unittest.TestCase):
    # region Test suites for executable samples.graph.add_child
    
    # region FUZZER
    
    def test_add_child(self):
        """
        self = samples.graph.Node
        child = samples.graph.Node
        """
        node = builtins.object.__new__(samples.graph.Node)
        node.name = 'foo'
        node.children = []
        node1 = builtins.object.__new__(samples.graph.Node)
        node1.name = 'abcdefghijklmnopqrst'
        node1.children = []
        child = node1
        
        actual = node.add_child(child)
        
        self.assertEqual(None, actual)
        
        node2 = builtins.object.__new__(samples.graph.Node)
        node3 = builtins.object.__new__(samples.graph.Node)
        node3.name = 'foo'
        node3.children = [node2]
        node2.name = 'abcdefghijklmnopqrst'
        node2.children = [node3]
        
        self.assertEqual(node2, child)
        
        self.assertEqual(node3, node)
    # endregion
    
    # endregion

