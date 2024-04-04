"""Test Guess the number functions"""
import unittest # Unit test framework (standard library) integrated in Python
from main import guess_validation # Import the function I need to test

class TestGuessValidation(unittest.TestCase):
    """Class for guess validation function"""
    def test_guess_validation(self):
        """Mock function"""
        validation_true = guess_validation(5, 5)
        validation_false_high = guess_validation(5, 20)
        validation_false_low = guess_validation(20, 5)
        self.assertEqual(validation_true, True)
        self.assertEqual(validation_false_high, "The number is greater than your guess\n")
        self.assertEqual(validation_false_low, False)
        
if __name__ == '__main__':
    unittest.main()
