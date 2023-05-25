import sys
sys.path.append(r'../..')
import builtins
import data_structures.stacks.stack_with_doubly_linked_list
import types
import data_structures
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable data_structures.stacks.stack_with_doubly_linked_list.push
    
    # region FUZZER
    
    def test_push(self):
        """
        self = data_structures.stacks.stack_with_doubly_linked_list.Stack[builtins.object]
        data = builtins.object
        """
        stack = data_structures.stacks.stack_with_doubly_linked_list.Stack()
        data = builtins.object()
        data1 = data
        
        actual = stack.push(data1)
        
        self.assertEqual(None, actual)
        
        self.assertEqual(data, data1)
        
        self.assertEqual(stack, stack)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.stacks.stack_with_doubly_linked_list.pop
    
    # region FUZZER
    
    def test_pop(self):
        """
        self = data_structures.stacks.stack_with_doubly_linked_list.Stack[builtins.object]
        """
        stack = data_structures.stacks.stack_with_doubly_linked_list.Stack()
        
        actual = stack.pop()
        
        self.assertEqual(None, actual)
        
        self.assertEqual(stack, stack)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.stacks.stack_with_doubly_linked_list.top
    
    # region FUZZER
    
    def test_top(self):
        """
        self = data_structures.stacks.stack_with_doubly_linked_list.Stack[builtins.object]
        """
        stack = data_structures.stacks.stack_with_doubly_linked_list.Stack()
        
        actual = stack.top()
        
        self.assertEqual(None, actual)
        
        self.assertEqual(stack, stack)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.stacks.stack_with_doubly_linked_list.__len__
    
    # region FUZZER
    
    def test___len__(self):
        """
        self = data_structures.stacks.stack_with_doubly_linked_list.Stack[builtins.object]
        """
        stack = data_structures.stacks.stack_with_doubly_linked_list.Stack()
        
        actual = stack.__len__()
        
        self.assertEqual(0, actual)
        
        self.assertEqual(stack, stack)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.stacks.stack_with_doubly_linked_list.is_empty
    
    # region FUZZER
    
    def test_is_empty(self):
        """
        self = data_structures.stacks.stack_with_doubly_linked_list.Stack[builtins.object]
        """
        stack = data_structures.stacks.stack_with_doubly_linked_list.Stack()
        
        actual = stack.is_empty()
        
        self.assertEqual(True, actual)
        
        self.assertEqual(stack, stack)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.stacks.stack_with_doubly_linked_list.print_stack
    
    # region FUZZER
    
    def test_print_stack(self):
        """
        self = data_structures.stacks.stack_with_doubly_linked_list.Stack[builtins.object]
        """
        stack = data_structures.stacks.stack_with_doubly_linked_list.Stack()
        
        actual = stack.print_stack()
        
        self.assertEqual(None, actual)
        
        self.assertEqual(stack, stack)
    # endregion
    
    # endregion

