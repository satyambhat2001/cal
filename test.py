import unittest
from datetime import datetime
from tkinter import Tk, Label, Entry, Button

class TestAgeCalculator(unittest.TestCase):
    def test_calculate_age(self):
        birth_date = datetime.strptime("2000-01-01", "%Y-%m-%d")
        current_date = datetime(2023, 6, 22)
        age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
        self.assertEqual(age, 23)

if __name__ == '__main__':
    unittest.main()
