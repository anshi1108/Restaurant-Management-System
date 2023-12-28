# Restaurant Management System (RMS)

This Python project is a simple restaurant management system (RMS) designed using simple python libraries to take orders, display a menu, process payments, manage and generate receipts and connectivity to an exel file.  The graphical user interface (GUI) is built using the Tkinter library.

## Google Drive link to download:

https://drive.google.com/file/d/1kDuhx1zi84t79SkpKs8r2mLkcYc3VJyQ/view?usp=sharing

## User Requirements

### User Requirement Document

The user requirement document for this project is utilized to gather essential information such as the restaurant name and menu details.
Ensure this file is in the same folder as the project.

### Format and Entry Order

When updating or entering data into the UserRequirementDocument.txt file, please follow this format and order:

1. **Restaurant Name:** Enter the name of the restaurant at the beginning of the document.
2. **Menu Items and Prices:** List the menu items and their corresponding prices in two separate sections. The menu items and prices should align in their respective sections. Each item or price should be on a separate line.
3. **Address:** Write down the address seperated by "," to be printed in the reciept

Example Entry:

Moonlight Cafe

Burger,Pizza,Pasta

20,10,15

402,Hamilton Street,New York


### Receipt Generation

Generates a pdf using canvas library in python that displays the total amount of the purchase along with date, time, restaurant name, restaurant address, order id, all the order information like the items and prices and displays total amount along with application of taxes in a well formated page.

Each receipt has a unique name with the following format:
receipt_order-id_date_time

Due to the variables, the reciept generated is always unique and thus prevents overwriting and loss of necessary data.


### Order Information Database

Stores all the data about the orders in a backend excel file using the pandas library in python. 
It stores the order id, the quantity of each menu item ordered (0 by default), the total cost and the final price with all the additional charges and tax added, rounded off to the next integer.
It also reads the last order id entered in the excel file to generate the new id, which has a value incremented by 1. Thus, the IDs generated are sequencial in nature that makes it easy for employees to access and use.
