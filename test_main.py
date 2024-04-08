"""Test Guess the number functions"""
import unittest # Unit test framework (standard library) integrated in Python
from unittest.mock import patch
from main import player_entry, guess_validation # Import the function I need to test
class TestPlayerEntry(unittest.TestCase): # TestCase is a unittest collection
    """Class for testing player entry function"""
    @patch("builtins.input", return_value=10) # Patch simulates valid player's entry using mock_input
    def test_player_entry_valid(self, mock_input):
        """Test player entry with valid input"""
        player_name = "Wendy"
        result = player_entry(player_name) # calling function being evaluated from main.py
        self.assertEqual(result, 10) # Verifies if the result is the expected one

    @patch('builtins.input', side_effect=["not_a_number", 70])
    def test_player_entry_invalid_input_then_valid(self, mock_input):
        """Test one invalid player entries then one valid"""
        player_name = "Wendy"
        result = player_entry(player_name)
        self.assertEqual(result, 70) #Verifies if the result is the expected one

    @patch('builtins.input', side_effect=["not_a_number", "still_not_a_number", 70])
    def test_player_entry_invalid_input_twice_then_valid(self, mock_input):
        """Test two invalid player entries then one valid"""
        player_name = "Wendy"
        result = player_entry(player_name)
        self.assertEqual(result, 70) #Verifies if the result is the expected one

class TestGuessValidation(unittest.TestCase):
    """Class for testing guess validation function"""
    def test_guess_validation(self):
        """Test the guess validation function"""
        validation_true = guess_validation(5, 5)
        validation_false_high = guess_validation(5, 20)
        validation_false_low = guess_validation(20, 5)
        self.assertEqual(validation_true, True)
        self.assertEqual(validation_false_high, False)
        self.assertEqual(validation_false_low, False)

if __name__ == '__main__':
    unittest.main()
