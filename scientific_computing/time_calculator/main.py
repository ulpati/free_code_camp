from time_calculator import add_time
from unittest import main

start_time = "11:06 PM"
duration_time = "2:02"
print(f"start time:{start_time}\nduration time:{duration_time}\n")
print(add_time(start_time, duration_time))

# run unit tests automatically
main(module='test_module', exit=False)