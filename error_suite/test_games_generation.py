import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import games
import unittest
import games.generation


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable games.generation.generate_one_ticket
    
    # region FUZZER
    
    def test_generate_one_ticket(self):
        actual = games.generation.generate_one_ticket()
        
        self.assertEqual('train_secret', actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable games.generation.generate_new_tickets
    
    # region FUZZER
    
    def test_generate_new_tickets(self):
        """
        count = zero (mutated from min)
        """
        actual = games.generation.generate_new_tickets(0)
        
        self.assertEqual([], actual)
    
    def test_generate_new_tickets1(self):
        """
        count = 512 (mutated from zero)
        """
        actual = games.generation.generate_new_tickets(512)
        
        self.assertEqual(['train_secret', 'plane_secret', 'car_double', 'car_secret', 'train_double', 'train_secret', 'car_secret', 'car_addition', 'car_secret', 'train_addition', 'train_double', 'car_addition', 'plane_secret', 'car_addition', 'car_secret', 'train_addition', 'car_double', 'car_double', 'car_addition', 'train_secret', 'car_secret', 'car_search', 'plane_double', 'car_secret', 'car_double', 'train_double', 'train_secret', 'plane_secret', 'train_secret', 'car_double', 'car_search', 'car_search', 'car_secret', 'plane_double', 'car_secret', 'car_search', 'train_search', 'car_secret', 'train_double', 'car_addition', 'car_search', 'plane_double', 'train_addition', 'train_addition', 'car_secret', 'car_double', 'car_secret', 'car_search', 'car_double', 'train_secret', 'car_addition', 'car_secret', 'train_double', 'car_secret', 'plane_double', 'train_double', 'car_secret', 'car_search', 'plane_double', 'car_search', 'car_double', 'train_secret', 'train_double', 'car_search', 'plane_secret', 'car_secret', 'plane_addition', 'train_double', 'car_secret', 'plane_double', 'car_addition', 'train_double', 'train_secret', 'train_double', 'car_secret', 'car_addition', 'train_secret', 'train_secret', 'car_double', 'car_search', 'car_search', 'car_double', 'car_secret', 'car_secret', 'car_secret', 'car_addition', 'plane_secret', 'train_double', 'train_addition', 'plane_search', 'car_secret', 'train_search', 'car_double', 'train_addition', 'train_double', 'train_secret', 'plane_secret', 'car_double', 'car_secret', 'car_secret', 'car_double', 'car_double', 'train_search', 'train_double', 'plane_double', 'train_double', 'car_double', 'car_secret', 'train_secret', 'train_secret', 'car_search', 'plane_double', 'train_secret', 'plane_secret', 'car_secret', 'train_addition', 'plane_double', 'train_addition', 'plane_secret', 'car_double', 'car_search', 'car_addition', 'train_secret', 'car_addition', 'car_secret', 'train_double', 'car_search', 'car_double', 'plane_addition', 'car_double', 'car_secret', 'car_secret', 'car_secret', 'plane_secret', 'car_double', 'train_secret', 'car_double', 'train_secret', 'car_addition', 'car_addition', 'car_secret', 'car_secret', 'train_secret', 'train_secret', 'car_addition', 'train_search', 'car_double', 'train_secret', 'train_double', 'train_secret', 'train_addition', 'car_addition', 'train_addition', 'car_double', 'car_double', 'train_secret', 'train_secret', 'car_double', 'car_search', 'car_double', 'train_addition', 'car_double', 'train_search', 'train_secret', 'train_secret', 'train_double', 'plane_addition', 'train_secret', 'car_addition', 'car_search', 'train_secret', 'car_search', 'train_double', 'plane_secret', 'car_secret', 'car_double', 'train_addition', 'car_double', 'car_secret', 'train_double', 'car_double', 'train_search', 'car_double', 'plane_secret', 'car_secret', 'train_addition', 'train_secret', 'plane_secret', 'plane_search', 'train_addition', 'plane_double', 'car_secret', 'train_secret', 'train_addition', 'train_double', 'car_search', 'car_addition', 'train_search', 'car_secret', 'train_search', 'car_secret', 'car_secret', 'train_secret', 'train_search', 'plane_search', 'car_double', 'plane_secret', 'car_secret', 'plane_double', 'plane_double', 'train_addition', 'train_addition', 'car_double', 'car_addition', 'car_secret', 'car_secret', 'train_search', 'plane_secret', 'train_secret', 'plane_search', 'car_double', 'train_secret', 'train_addition', 'plane_double', 'car_addition', 'train_addition', 'train_double', 'car_secret', 'train_secret', 'train_secret', 'plane_addition', 'car_secret', 'train_search', 'plane_double', 'car_secret', 'plane_double', 'plane_double', 'train_secret', 'plane_double', 'plane_double', 'car_search', 'car_double', 'plane_secret', 'car_secret', 'plane_double', 'car_secret', 'car_double', 'car_double', 'plane_addition', 'train_double', 'car_search', 'plane_double', 'car_addition', 'plane_double', 'train_secret', 'plane_secret', 'train_addition', 'car_double', 'car_secret', 'plane_search', 'train_secret', 'car_addition', 'car_search', 'train_secret', 'car_secret', 'train_addition', 'plane_addition', 'car_secret', 'train_double', 'train_secret', 'train_secret', 'train_search', 'plane_double', 'car_secret', 'car_search', 'plane_secret', 'car_double', 'plane_double', 'car_secret', 'car_addition', 'plane_double', 'car_double', 'train_search', 'car_secret', 'train_double', 'car_secret', 'plane_addition', 'plane_secret', 'car_secret', 'car_secret', 'car_secret', 'plane_secret', 'car_double', 'train_secret', 'car_search', 'car_double', 'train_addition', 'train_secret', 'train_addition', 'plane_double', 'car_secret', 'car_double', 'car_search', 'car_double', 'car_search', 'car_search', 'car_double', 'car_addition', 'car_search', 'train_search', 'car_secret', 'car_double', 'car_double', 'car_double', 'car_secret', 'train_secret', 'car_secret', 'plane_secret', 'plane_secret', 'train_addition', 'car_secret', 'train_addition', 'train_double', 'car_search', 'car_secret', 'plane_double', 'car_secret', 'car_search', 'train_secret', 'car_addition', 'car_double', 'train_double', 'train_secret', 'train_secret', 'train_double', 'car_double', 'train_secret', 'car_secret', 'train_secret', 'train_secret', 'plane_double', 'car_addition', 'car_search', 'car_secret', 'car_double', 'train_addition', 'car_secret', 'car_secret', 'train_double', 'train_double', 'car_secret', 'train_search', 'plane_secret', 'car_secret', 'car_secret', 'train_addition', 'plane_search', 'train_search', 'car_double', 'train_secret', 'plane_secret', 'train_search', 'car_secret', 'train_double', 'train_secret', 'train_double', 'car_double', 'train_secret', 'plane_secret', 'car_addition', 'car_secret', 'train_search', 'train_double', 'car_secret', 'car_double', 'train_addition', 'car_secret', 'train_double', 'car_secret', 'train_secret', 'car_double', 'car_secret', 'car_secret', 'plane_double', 'train_secret', 'car_double', 'train_addition', 'train_double', 'car_secret', 'plane_double', 'train_double', 'plane_secret', 'plane_secret', 'plane_secret', 'car_double', 'train_search', 'train_secret', 'train_double', 'train_secret', 'train_double', 'train_secret', 'car_secret', 'car_secret', 'train_double', 'train_search', 'car_double', 'train_secret', 'car_secret', 'car_addition', 'car_addition', 'plane_double', 'train_secret', 'plane_secret', 'car_addition', 'car_double', 'car_secret', 'plane_secret', 'car_double', 'train_search', 'train_search', 'train_secret', 'car_double', 'train_secret', 'train_secret', 'train_double', 'plane_secret', 'train_addition', 'car_addition', 'train_secret', 'train_double', 'train_search', 'train_secret', 'plane_secret', 'car_addition', 'car_double', 'car_double', 'plane_double', 'car_search', 'train_double', 'train_double', 'car_double', 'train_secret', 'train_secret', 'train_addition', 'train_double', 'car_double', 'plane_double', 'car_search', 'car_secret', 'plane_double', 'train_search', 'car_addition', 'car_search', 'car_addition', 'plane_double', 'train_secret', 'car_double', 'train_search', 'car_search', 'plane_double', 'car_addition', 'car_secret', 'car_search', 'train_secret', 'plane_secret', 'car_addition', 'car_double', 'train_addition', 'car_secret', 'car_double', 'car_secret', 'train_addition', 'train_secret', 'car_secret', 'car_search', 'car_secret', 'plane_addition', 'plane_double', 'car_double', 'car_search', 'car_double', 'car_secret', 'car_double', 'train_secret', 'car_search', 'train_double', 'train_secret', 'train_double', 'car_secret', 'car_addition', 'train_secret', 'car_secret', 'car_search', 'train_addition', 'car_search', 'car_double', 'train_addition', 'car_search', 'plane_secret', 'train_double', 'plane_secret', 'plane_addition', 'train_double', 'plane_double', 'train_double', 'train_secret', 'car_double', 'car_double', 'plane_double', 'train_secret', 'train_secret', 'train_search'], actual)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_generate_new_tickets_with_exception(self):
        """
        count = 170141183460469231731687303715884105695 (mutated from max)
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        games.generation.generate_new_tickets(170141183460469231731687303715884105695)
    # endregion
    
    # endregion
    
    # region Test suites for executable games.generation.generate_cities_for_detectives
    
    # region FUZZER
    
    def test_generate_cities_for_detectives(self):
        actual = games.generation.generate_cities_for_detectives()
        
        self.assertEqual([76, 78, 127, 108, 41], actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable games.generation.generate_city_for_misterx
    
    # region FUZZER
    
    def test_generate_city_for_misterx_with_exception(self):
        """
        color = 32 (mutated from zero)
        """
        # This test fails because function [games.generation.generate_city_for_misterx] produces [KeyError]
        games.generation.generate_city_for_misterx(32)
    # endregion
    
    # endregion

