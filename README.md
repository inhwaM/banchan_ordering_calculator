![Screen Shot 2022-01-10 at 2 15 10 PM](https://user-images.githubusercontent.com/88123491/148827769-4bee6fdf-9ef2-42be-88e0-0f5f9524db44.png)

I used ‘tkinter’ module from Python’s standard libraries to create a GUI program. I used tkinter widgets such as labels to provide price information to the user, and buttons to make selection of items from the menu and calculate the total price. I also used the text widget to display order items with unit prices, and the entry widget to collect customer’s information such as name, email, and phone number. This was done following my belief that programs that are more visual with intuitive user interfaces are more approachable and easier to use. 

The user can update the menu items and their prices by simply writing the item names and their respective prices in a ‘banchan’ text file. In the Calculator class, the user can also add new items to the menu dictionary by calling the __setitem__() method defined in the Calculator class.

Once a customer’s order is received, the user tallies the order items by clicking item buttons. The program then outputs the itemized order details, total price, discount amount, and the net price.

I created two classes – Calculator and Customer. The Calculator class takes selected banchan as an argument (user clicks the banchan button to select, and the number of clicks corresponds to the order quantity), and then calculates the total order amount, eligible discount amount, and net order bill amount. The Customer class, which is for each unique person making an order, takes all of customer’s information and order information as arguments, and then writes this information to a csv file. This class returns a writer object which is responsible for converting the customer’s data into a delimited string.
