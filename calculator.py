"""
Inhwa Min
Class: CS 521 - Fall 2
Date: 12/18/2021
Final Project
Purpose (1-2 sentence summary in your own words):
Write a program to open the txt file and add the data to dict, and create Calculator class.
The class will calculate order price and discount,
and show the calculation in the program back to the user.
"""
import sys

# menu data from the text file where Banchan menu (with prices) are written.
INPUT_FILE = 'banchan.txt'

price_banchan = {}  # menu dictionary


def file_open():
    """Function - to Open the txt file and add menu data into a dict.
    return: dictionary of banchan items as key and respective unit price as value"""
    try:
        banchan_file = open(INPUT_FILE, 'r')

    except IOError:
        print(f'ERROR: Could not find the {INPUT_FILE}')
        sys.exit()
    else:
        print(f'{INPUT_FILE} File exists!')

    for line in banchan_file:
        (key, val) = line.strip().split(', ')
        price_banchan[str(key)] = float(val)

    banchan_file.close()
    print(f'menu : {price_banchan}')


order_banchan = {}
total_price = 0

# total discount amount per order is always under $10.0
discount_list = [0.0, 0.5, 2.0, 5.0]
assert float(sum(discount_list)) <= float(10.0), \
    "total discount amount per order should always be under $10.0"


class Calculator:
    """This class constructs the Calculator object
    and it's calculation of net order bill"""

    def __init__(self, item):
        """A constructor"""
        self.item = item
        assert isinstance(item, str), 'item is not string!'

    def __getitem__(self, key):
        """Optional processing - access the value of menu dict"""
        return price_banchan[key]

    def __setitem__(self, new_key, new_value):
        """Optional processing - directly add a new item to
        the menu dict (price_banchan), and for unit testing"""
        if new_key is not None and new_value is not None:
            price_banchan[new_key] = new_value
            return price_banchan
        else:
            return price_banchan

    def banchan_add(self):
        """calculate total order price,
        and add order item with order quantity into order_banchan dict"""
        global price_banchan, order_banchan, total_price
        if self.item not in price_banchan:
            print("There is no such menu.")
        this_price = price_banchan.get(self.item)
        total_price += this_price

        if self.item in order_banchan:
            order_banchan[self.item] = order_banchan.get(self.item) + 1
        else:
            order_banchan[self.item] = 1

        self.print_order()
        self.print_price()
        self.discount()

    def print_order(self):
        """convert order item and quantity dictionary into string with order price
        for printing to show it back to the user"""
        global order_banchan
        order_print = ""
        price_tmp = 0
        for i in order_banchan:
            price_tmp = round((price_banchan[i] * order_banchan.get(i)), 2)
            order_print = order_print + i + " X " + str(order_banchan.get(i)) + " = " + str(price_tmp) + "\n"
        return order_print

    def print_price(self):
        """round the total order price to 1st decimal place
        for printing to show it back to the user"""
        global total_price
        total_price = round(total_price, 1)
        return total_price

    def discount(self):
        """calculate the discount amount based on the order quantity by each item.
        return: sum of all discounts by each item"""
        global order_banchan, discount_list

        # using set() to make total discount amount per order under $10.0
        order_discount = set()
        for k, v in order_banchan.items():
            if v >= 6:
                order_discount.add(discount_list[3])
            elif v >= 4:
                order_discount.add(discount_list[2])
            elif v >= 2:
                order_discount.add(discount_list[1])
            else:
                order_discount.add(discount_list[0])
        return sum(order_discount)


    def order_clear(self):
        """clear all prints"""
        global order_banchan, total_price
        order_banchan = {}
        total_price = 0
        return order_banchan

