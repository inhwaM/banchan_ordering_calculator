"""
Inhwa Min
Class: CS 521 - Fall 2
Date: 12/18/2021
Final Project
Purpose (1-2 sentence summary in your own words):
Write a program to conduct unit tests of the calculator.
It will test public methods in Calculator class - banchan_add(), print_order(), and print_price()
to check to see if all methods work as intended.
"""
from calculator import *

# For the 2 unit tests, banchan_add() method should be called first

# Unit test 1 : test a public method (print_price()) in the class Calculator,
# that returns a price for the item given as an argument for the class.

# Unit test 2 : test a public method (print_order()) in the class Calculator,
# that returns a string of a calculation (item x quantity = price).


if __name__ == '__main__':
    file_open()  # open menu dictionary (price_banchan)
    print('-' * 30)
    try:
        item_1 = 'kimchi'
        assert isinstance(item_1, str)
    except AssertionError:
        print('item is not string!')
        sys.exit()
    except NameError:
        print('the item is not valid')
        sys.exit()

    calculate_1 = Calculator(item_1)  # instantiate Calculator object
    calculate_1.banchan_add()
    assert item_1 in price_banchan, "There is no such menu."
    # test print_price method
    print(f'price for {item_1} is ${str(calculate_1.print_price())}')
    # test print_order method
    print(str(calculate_1.print_order()))

    # add a new item to the menu dict (price_banchan)
    print(calculate_1.__setitem__('new_item', 1.22))
    calculate_1.order_clear()

    # and do unit tests for the 2 public methods again for the new item.
    try:
        item_2 = 'new_item'
        assert isinstance(item_2, str)
    except AssertionError:
        print('the new item is not string!')
        sys.exit()
    except NameError:
        print('the new item is not valid')
        sys.exit()

    calculate_2 = Calculator(item_2)  # instantiate Calculator object
    calculate_2.banchan_add()
    assert item_2 in price_banchan, "There is no such menu."
    # test print_price method
    print(f'price for {item_2} is ${str(calculate_2.print_price())}')
    # test print_order method
    print(str(calculate_2.print_order()))

    print('Unit test passed!!')
