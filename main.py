"""
Inhwa Min
Class: CS 521 - Fall 2
Date: 12/18/2021
Final Project
Purpose (1-2 sentence summary in your own words):
Write a program that creates GUI using tkinter frame widgets
and creates functions to send customer and order information by calling classes.
"""

# App GUI using tkinter module
import sys
from tkinter import *
from tkinter import messagebox

from calculator import *
from customer import *


def on_click(item):
    """Function - to print the order results
    when the banchan item buttons are clicked"""
    calculate = Calculator(item)
    calculate.banchan_add()

    text_1.delete('1.0', END)
    text_1.insert(INSERT, calculate.print_order())
    label_price.configure(text=f"Total Price: ${str(calculate.print_price())}\n"
                               f"Discount: ${str(calculate.discount())}\n"
                               f"Net Price: ${str(calculate.print_price() - calculate.discount())}")


def customer_info():
    """Function - to send the customer info with order price
     to the Customer class to save it into csv file"""
    name = entry1.get()
    if str(name) == '':
        messagebox.showerror('error', 'Please enter customer name!')
        entry1.focus()
        return
    email = entry2.get()
    phone = entry3.get()

    price_text = label_price.cget("text")
    price_text_li = price_text.split('\n')
    total = price_text_li[0][14:]
    discount = price_text_li[1][11:]
    net_price = price_text_li[2][12:]
    coupon = ''

    send_info = Customer(name, email, phone, total, discount, net_price)
    send_info.save_to_file(coupon)
    print(send_info)

    # after csv file is created/saved, send a message to refresh the program
    if os.path.getsize(f'{str(name)}.csv') > 0:
        success_msg = messagebox.askyesno("Yes|No", f"{str(name)}.csv "
                                                    f"is successfully saved.\ndo you want to re-start?")
        if success_msg:
            text_1.delete('1.0', END)
            label_price.configure(text=f"Total Price: $0\n"
                                       f"Discount: $0")
            entry1.delete(0, 'end')
            entry2.delete(0, 'end')
            entry3.delete(0, 'end')
            entry1.focus()

            Calculator.order_clear('')


def close():
    """close the program"""
    msg_box = messagebox.askquestion('confirming', 'Do you want to exit?')
    if msg_box == 'yes':
        exit()


def clear():
    """refresh the program"""
    clear_box = messagebox.askquestion('confirming', 'Do you want to re-start?')
    if clear_box == 'yes':
        text_1.delete('1.0', END)
        label_price.configure(text=f"Total Price: $0\n"
                                   f"Discount: $0")
        entry1.delete(0, 'end')
        entry2.delete(0, 'end')
        entry3.delete(0, 'end')
        entry1.focus()

        Calculator.order_clear('')


window = Tk()
window.title("Banchan ordering calculator")
window.geometry('800x700+400+200')
window.config(bg="white")
window.resizable(False, False)

"""Frame widgets"""
label_title = Label(text="Choose an option.",
                    bg="white", fg="black")
label_title.pack()

frame1 = Frame(width="750", height="20")
frame1.pack(fill="both")

frame2 = Frame(width="700")
frame2.pack(fill="both", expand=True)

frame3 = Frame(width="700", height="30")
frame3.pack()

frame4 = Frame(width="700", height="20")
frame4.pack()

# A button to save into csv file
btn_csv = Button(frame1, text="Download to\ncsv",
                 padx="10", pady="10", command=lambda: customer_info())
btn_csv.grid(row=0, column=0, padx=10, pady=10)

# A button to clear all data and re-start
btn_clear = Button(frame1, text="Restart",
                   padx="10", pady="10", command=lambda: clear())
btn_clear.grid(row=0, column=1, padx=10, pady=10)

# A button to exit the program
btn_exit = Button(frame1, text="Exit",
                  padx="10", pady="10", command=lambda: close())
btn_exit.grid(row=0, column=2, padx=10, pady=10)

# label to show price information
label_price = Label(frame1, text="Total: $0", width="40",
                    padx=10, pady="10", fg="blue", font='Arial 15')
label_price.grid(row=0, column=3, padx="10", pady="10")

# call file_open function to access the banchan with price dictionary
file_open()

# banchan item buttons
button = []
for k, v in price_banchan.items():
    button.append(Button(frame2, text=f"{k}\n${float(v)}",
                         padx="10", pady="10", width="10", command=lambda k=k: on_click(k)))
    if len(button) > 7:
        sys.exit('The max number of items is 6. please update banchan.txt.')
    for i in range(len(button)):
        button[i].grid(row=0, column=i + 1, padx=10, pady=10)

# text box for order calculation printing
text_1 = Text(frame3, padx="10", pady="20", bg="#efeff1")
text_1.pack(fill="both", expand=True)

# labels and entries for customer information
label_name = Label(frame4, text='Name', width=10, height=2)\
    .grid(row=0, column=0)
label_email = Label(frame4, text='Email', width=10, height=2)\
    .grid(row=1, column=0)
label_phone = Label(frame4, text='Phone', width=10, height=2)\
    .grid(row=2, column=0)
entry1 = Entry(frame4)
entry2 = Entry(frame4)
entry3 = Entry(frame4)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)

if __name__ == '__main__':
    window.mainloop()

