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

### Order Information Database

Stores all the data about the orders in a backend excel file using the pandas library in python. It also reads the last order id entered in the excel file to generate a sequencial order id that makes it easy for employees to access and use.
