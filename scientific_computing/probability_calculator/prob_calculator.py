import copy
import random

class Hat:
    # initializes the Hat object with specified colors and quantities
    def __init__(self, **kwargs):
        self.contents = []
        for color, quantity in kwargs.items():
            self.contents.extend([color] * quantity)

    # draws a specified number of balls randomly from the hat
    def draw(self, num_balls):
        drawn_balls = []
        if num_balls >= len(self.contents):
            return self.contents

        for _ in range(num_balls):
            ball_index = random.randrange(len(self.contents))
            drawn_balls.append(self.contents.pop(ball_index))
        return drawn_balls

# conducts experiments to estimate the probability of drawing specific balls from the hat
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        # check if all expected balls are drawn
        success = all(
            drawn_balls.count(color) >= quantity
            for color, quantity in expected_balls.items())
        if success:
            successful_experiments += 1

    return successful_experiments / num_experiments