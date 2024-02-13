import prob_calculator
from unittest import main

prob_calculator.random.seed(95)
hat = prob_calculator.Hat(blue=4, red=2, green=6)
probability = prob_calculator.experiment(hat=hat, expected_balls={"blue": 2,"red": 1},
                                         num_balls_drawn=4,
                                         num_experiments=3000
                                        )

print("Hat contents:", hat.contents)
print("Expected balls:", {"blue": 2, "red": 1})
print("Number of balls drawn:", 4)
print("Number of experiments:", 3000)
print("Probability:", probability)

# Run unit tests automatically
main(module='test_module', exit=False)