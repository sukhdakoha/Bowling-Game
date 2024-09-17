import unittest
from bowling_game import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        """Initialize a new game before each test"""
        self.game = BowlingGame()

    def roll_many(self, rolls, pins):
        """Helper function to roll multiple times"""
        for _ in range(rolls):
            self.game.roll(pins)

    def roll_strike(self):
        """Helper function to roll a strike"""
        self.game.roll(10)

    def roll_spare(self):
        """Helper function to roll a spare (5 + 5)"""
        self.game.roll(5)
        self.game.roll(5)

    def test_gutter_game(self):
        """Test a game of all 0's"""
        self.roll_many(20, 0)  # 20 rolls, all gutter balls
        self.assertEqual(self.game.score(), 0)

    def test_all_ones(self):
        """Test a game of all 1's"""
        self.roll_many(20, 1)
        self.assertEqual(self.game.score(), 20)

    def test_spare(self):
        """Test a game with a spare"""
        self.roll_spare()
        self.game.roll(3)
        self.roll_many(17, 0)
        self.assertEqual(self.game.score(), 16)

    def test_strike(self):
        """Test a game with a strike"""
        self.roll_strike()
        self.game.roll(3)
        self.game.roll(4)
        self.roll_many(16, 0)
        self.assertEqual(self.game.score(), 24)

    def test_perfect_game(self):
        """Test a perfect game (12 strikes in a row)"""
        self.roll_many(12, 10)
        self.assertEqual(self.game.score(), 300)

    def test_open_frame(self):
        """Test a game with an open frame"""
        self.game.roll(7)
        self.game.roll(2)
        self.roll_many(18, 0)
        self.assertEqual(self.game.score(), 9)

    def test_tenth_frame_strike(self):
        """Test the tenth frame with a strike and bonus rolls"""
        self.roll_many(18, 0)
        self.roll_strike()  # Tenth frame strike
        self.game.roll(10)  # First bonus roll
        self.game.roll(10)  # Second bonus roll
        self.assertEqual(self.game.score(), 30)

if __name__ == '__main__':
    unittest.main()
