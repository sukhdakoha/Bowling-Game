class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        """Record a roll"""
        self.rolls.append(pins)

    def score(self):
        """Calculate the total score for the game"""
        total_score = 0
        roll_index = 0
        for frame in range(10):  # 10 frames in total
            if self.is_strike(roll_index):  # Strike case
                total_score += 10 + self.strike_bonus(roll_index)
                roll_index += 1
            elif self.is_spare(roll_index):  # Spare case
                total_score += 10 + self.spare_bonus(roll_index)
                roll_index += 2
            else:  # Normal open frame
                total_score += self.frame_score(roll_index)
                roll_index += 2
        return total_score

    def is_strike(self, roll_index):
        """Check if the roll is a strike (10 pins on first try)"""
        return self.rolls[roll_index] == 10

    def strike_bonus(self, roll_index):
        """Bonus for a strike is the next two rolls"""
        return self.rolls[roll_index + 1] + self.rolls[roll_index + 2]

    def is_spare(self, roll_index):
        """Check if the roll is a spare (10 pins in two tries)"""
        return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10

    def spare_bonus(self, roll_index):
        """Bonus for a spare is the next roll"""
        return self.rolls[roll_index + 2]

    def frame_score(self, roll_index):
        """Total score for a frame (two rolls)"""
        return self.rolls[roll_index] + self.rolls[roll_index + 1]
