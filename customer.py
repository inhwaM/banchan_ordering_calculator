"""
Inhwa Min
Class: CS 521 - Fall 2
Date: 12/18/2021
Final Project
Purpose (1-2 sentence summary in your own words):
Write a program to create Customer class.
The class will save all customer information and order price information into csv file.
"""
import csv
import os
import datetime


class Customer:
    """This class constructs the Customer object
    and save customer info with order price into a csv file"""

    def __init__(self, name, email, phone, total, discount, net_price):
        """A constructor"""
        self.__name = name  # private attribute
        self.email = email
        self.phone = phone
        self.total = total
        self.discount = discount
        self.net_price = net_price
        self.__date = datetime.datetime.now().strftime('%m-%d-%Y, %H:%M:%S')  # private attribute

    def save_to_file(self, coupon):
        """save customer information with order price into csv file"""
        info_tuple = (self.__name, self.email, self.phone, self.total,
                      self.discount, self.net_price, self.__date, self.__new_customer_promotion())

        # for a new order for an existing csv file/customer,
        # the new data will be adding to the existing file.
        file = open(f"{self.__name}.csv", mode="a", newline='')
        writer = csv.writer(file)
        writer.writerow(["Name", "Email", "Phone", "Total Price", "Discount", "Net price", "Date", "Coupon"])
        writer.writerow(info_tuple)
        file.close()

    def __repr__(self):
        """return a string message in console after csv file is successfully written"""
        return f"Completed : {self.__name}.csv"

    # private method which is only being called inside of the Customer class
    def __new_customer_promotion(self):
        """check to see if there's an existing file for the name.
        if the file does not exist (new customer),
        provide additional discount coupon for future order"""
        path = f'{self.__name}.csv'
        if os.path.isfile(path) and os.access(path, os.R_OK):
            print('=-' * 10 + "The customer is NOT NEW!")
            return None
        else:
            print('=-' * 10 + "The customer is NEW! "
                              "and eligible for additional discount for future orders.")
            return str(1.0)
