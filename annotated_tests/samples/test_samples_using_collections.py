import sys
import typing

sys.path.append(r'../../..')
import collections
import builtins
import samples
import unittest
import samples.using_collections


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable samples.using_collections.generate_collections
    
    # region FUZZER
    
    def test_generate_collections(self):
        """
        collection = collections.UserDict[typing.Any, typing.Any]
        """
        values_view = typing.ValuesView({})
        collection = collections.UserDict(values_view)
        collection1 = collection
        
        actual = samples.using_collections.generate_collections(collection1)
        
        user_dict = object.__new__(collections.UserDict)
        user_dict.data = {0: 100, }
        
        self.assertEqual([user_dict, {0: 100, }, [(0, 100)]], actual)
        
        self.assertEqual(user_dict, collection1)
    
    def test_generate_collections_with_exception(self):
        """
        collection = builtins.list[typing.Any]
        """
        # This test fails because function [samples.using_collections.generate_collections] produces [IndexError]
        samples.using_collections.generate_collections([])
    # endregion
    
    # endregion

