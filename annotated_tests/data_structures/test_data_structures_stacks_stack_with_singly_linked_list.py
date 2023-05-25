import sys
sys.path.append(r'../..')
import data_structures.stacks.stack_with_singly_linked_list
import builtins
import types
import data_structures
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable data_structures.stacks.stack_with_singly_linked_list.__str__
    
    # region FUZZER
    
    def test___str__(self):
        """
        self = data_structures.stacks.stack_with_singly_linked_list.Node[builtins.object]
        """
        node = data_structures.stacks.stack_with_singly_linked_list.Node(object())
        
        actual = node.__str__()
        
        self.assertEqual('<object object at 0x000002DB67C88C30>', actual)
        
        self.assertEqual(node, node)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.stacks.stack_with_singly_linked_list.__str__
    
    # region FUZZER
    
    def test___str__1(self):
        """
        self = data_structures.stacks.stack_with_singly_linked_list.LinkedStack[builtins.object]
        """
        linked_stack = data_structures.stacks.stack_with_singly_linked_list.LinkedStack()
        
        actual = linked_stack.__str__()
        
        self.assertEqual('', actual)
        
        self.assertEqual(linked_stack, linked_stack)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.stacks.stack_with_singly_linked_list.__len__
    
    # region FUZZER
    
    def test___len__(self):
        """
        self = data_structures.stacks.stack_with_singly_linked_list.LinkedStack[builtins.object]
        """
        linked_stack = data_structures.stacks.stack_with_singly_linked_list.LinkedStack()
        
        actual = linked_stack.__len__()
        
        self.assertEqual(0, actual)
        
        self.assertEqual(linked_stack, linked_stack)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.stacks.stack_with_singly_linked_list.is_empty
    
    # region FUZZER
    
    def test_is_empty(self):
        """
        self = data_structures.stacks.stack_with_singly_linked_list.LinkedStack[builtins.object]
        """
        linked_stack = data_structures.stacks.stack_with_singly_linked_list.LinkedStack()
        
        actual = linked_stack.is_empty()
        
        self.assertEqual(True, actual)
        
        self.assertEqual(linked_stack, linked_stack)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.stacks.stack_with_singly_linked_list.push
    
    # region FUZZER
    
    def test_push(self):
        """
        self = data_structures.stacks.stack_with_singly_linked_list.LinkedStack[builtins.object]
        item = builtins.object
        """
        linked_stack = data_structures.stacks.stack_with_singly_linked_list.LinkedStack()
        item = builtins.object()
        item1 = item
        
        actual = linked_stack.push(item1)
        
        self.assertEqual(None, actual)
        
        self.assertEqual(item, item1)
        
        self.assertEqual(linked_stack, linked_stack)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.stacks.stack_with_singly_linked_list.pop
    
    # region FUZZER
    
    def test_pop_with_exception(self):
        """
        self = data_structures.stacks.stack_with_singly_linked_list.LinkedStack[builtins.object]
        """
        linked_stack = data_structures.stacks.stack_with_singly_linked_list.LinkedStack()
        # This test fails because function [data_structures.stacks.stack_with_singly_linked_list.pop] produces [IndexError]
        linked_stack.pop()
        
        self.assertEqual(linked_stack, linked_stack)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.stacks.stack_with_singly_linked_list.peek
    
    # region FUZZER
    
    def test_peek_with_exception(self):
        """
        self = data_structures.stacks.stack_with_singly_linked_list.LinkedStack[builtins.object]
        """
        linked_stack = data_structures.stacks.stack_with_singly_linked_list.LinkedStack()
        # This test fails because function [data_structures.stacks.stack_with_singly_linked_list.peek] produces [IndexError]
        linked_stack.peek()
        
        self.assertEqual(linked_stack, linked_stack)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.stacks.stack_with_singly_linked_list.clear
    
    # region FUZZER
    
    def test_clear(self):
        """
        self = data_structures.stacks.stack_with_singly_linked_list.LinkedStack[builtins.object]
        """
        linked_stack = data_structures.stacks.stack_with_singly_linked_list.LinkedStack()
        
        actual = linked_stack.clear()
        
        self.assertEqual(None, actual)
        
        self.assertEqual(linked_stack, linked_stack)
    # endregion
    
    # endregion

