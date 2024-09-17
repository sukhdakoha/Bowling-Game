**Bowling Game Backend**


This project implements the backend logic for a 10-pin bowling game. The goal is to simulate and calculate the total score based on standard bowling rules, including strikes, spares, and open frames.

**Class: BowlingGame**

Methods:

__init__(self)

Initializes the bowling game by setting up an empty list to store the number of pins knocked down in each roll.

Args: None

Returns: None

roll(self, pins)
Records the number of pins knocked down in each roll.

Args:

pins (int): The number of pins knocked down during the roll.

Returns: None

score(self)

Calculates the total score for the game based on the pins knocked down in each frame. A bowling game consists of 10 frames, with special rules for strikes, spares, and the 10th frame.


Args: None

Returns:

total_score (int): The total score for the game.
is_strike(self, roll_index)

Checks if the roll is a strike (i.e., all 10 pins are knocked down on the first ball of the frame).


Args:


roll_index (int): The index of the current roll in the rolls list.

Returns:


bool: Returns True if the roll is a strike, otherwise False.
strike_bonus(self, roll_index)

Calculates the bonus for a strike, which is the sum of the next two rolls after the strike.


Args:


roll_index (int): The index of the current roll in the rolls list.

Returns:


bonus (int): The sum of the next two rolls after a strike.
is_spare(self, roll_index)

Checks if the frame is a spare (i.e., all 10 pins are knocked down in two attempts).


Args:


roll_index (int): The index of the current roll in the rolls list.

Returns:


bool: Returns True if the frame is a spare, otherwise False.
spare_bonus(self, roll_index)

Calculates the bonus for a spare, which is the sum of the next roll after the spare.


Args:


roll_index (int): The index of the current roll in the rolls list.

Returns:


bonus (int): The next roll after a spare.
frame_score(self, roll_index)

Calculates the total score for a frame (the sum of the two rolls in that frame).


Args:


roll_index (int): The index of the current roll in the rolls list.

Returns:


score (int): The total score for the frame.

**Test Cases**

The project includes unit tests for various scenarios including strikes, spares, open frames, perfect games, and edge cases.


How to Run the Project

Install Python (if not installed).

Clone the repository or download the project files.

To run the tests, use the following command:


python -m unittest test_bowling_game.py

The game logic can be manually tested by running the main.py file.
