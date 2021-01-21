import unittest

from src.high_scores import *

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0

class HighScoresTest(unittest.TestCase):
    
    # Tests
    def setUp(self):
        self.high_score_list = [9, 9, 7, 10, 6, 5]
        self.two_score_list = [2, 3]
        self.single_score_list = [1]

    # Test latest score (the last thing in the list)
    def test_latest_score(self):
        self.assertEqual(5, latest(self.high_score_list))

    # Test personal best (the highest score in the list)
    def test_personal_best(self):
        self.assertEqual(10, personal_best(self.high_score_list))

    # Test top three from list of scores
    def test_personal_top_three(self):
        self.assertEqual([10, 9, 9], personal_top_three(self.high_score_list))

    # Test ordered from highest tp lowest
    def test_highest_to_lowest(self):
        self.assertEqual([10, 9, 9, 7, 6, 5], highest_to_lowest(self.high_score_list))
    
    # Test top three when there is a tie
    def test_top_three_tie(self):
        self.assertEqual([10, 9, 9], personal_top_three(self.high_score_list))

    # Test top three when there are less than three
    def test_top_three_two_score_list(self):
        self.assertEqual([3, 2], personal_top_three(self.two_score_list))

    # Test top three when there is only one
    def test_top_three_single_score_list(self):
        self.assertEqual([1], personal_top_three(self.single_score_list))
