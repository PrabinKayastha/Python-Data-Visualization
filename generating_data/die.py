from random import randint

class Die:
    """Class for a single die."""
    def __init__(self, num_sides = 6):
        self.num_sides = num_sides


    def roll(self):
        """Return random number between 1 and number of sides."""
        return randint(1, self.num_sides)
