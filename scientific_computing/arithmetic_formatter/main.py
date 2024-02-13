from pytest import main
from arithmetic_arranger import arithmetic_arranger

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))

# run unit tests automatically
main(['test_module.py','-vv'])