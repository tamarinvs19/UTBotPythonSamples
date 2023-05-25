import sys
sys.path.append(r'..\..\..')
import data_structures.stacks.stack_with_singly_linked_list
import types
import builtins
import data_structures
import unittest


class TestTopLevelFunctions(unittest.TestCase):
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

