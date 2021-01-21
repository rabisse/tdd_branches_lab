import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):
    def setUp(self):
        self.home_win = {
            "home_score": 1,
            "away_score": 0
            }
        self.away_win = {
            "home_score": 0,
            "away_score": 1
            }
        self.draw = {
            "home_score": 0,
            "away_score": 0
            }
        self.list_of_scores = [
            {"home_score": 1, "away_score": 0},
            {"home_score": 0, "away_score": 1},
            {"home_score": 0,"away_score": 0}
        ]

    # Test we get the right result string for a final score dictionary representing -
    def test_home_win(self):
        self.assertEqual("Home win", get_result(self.home_win))

    def test_away_win(self):
        self.assertEqual("Away win", get_result(self.away_win))

    def test_draw(self):
        self.assertEqual("Draw", get_result(self.draw))

    def test_get_results(self):
        self.assertEqual(["Home win", "Away win", "Draw"], get_results(self.list_of_scores))
    # Test we get right list of result strings for a list of final score dictionaries.
