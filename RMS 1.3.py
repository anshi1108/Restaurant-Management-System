#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


# Define global variables
menu_windows = []  # Define menu_windows globally
entry_quantities = []  # Define entry_quantities globally
w=500
h=500


# Define functions
def tooltip(loc):
    tooltip_label = tk.Label(loc, text='', relief='solid', wraplength=200)
    tooltip_label.config(font=('Helvetica', 10), background='lightgrey')
    def create_tooltip(widget, text):
        def show_tooltip(event, txt):
            x, y, width = event.widget.winfo_x(), event.widget.winfo_y(), event.widget.winfo_width()
            tooltip_label.place(x=x + width + 5, y=y - 10)
            tooltip_label.config(text=txt)
        def hide_tooltip(event=None):
            tooltip_label.place_forget()
        widget.bind('<Enter>', lambda event, txt=text: show_tooltip(event, txt))
        widget.bind('<Leave>', lambda event: hide_tooltip())
    return create_tooltip


def close_program():
    root.destroy()
    
    
def display_menu():
    global root, menu_windows, entry_quantities
    # Hide or withdraw the root (main) window
    root.withdraw()  # This will hide the root window
    # Close previous menu windows
    while menu_windows:
        menu_windows.pop().destroy()
    menu_windows = []  # Reset the menu_windows list
    menu_window = tk.Toplevel()
    menu_window.geometry("%dx%d" % (w, h))
    menu_window.title("Menu")
    tk.Label(menu_window, text=name.title(), font=('Helvetica', 16)).place(x=w/2, y=35, anchor="center")
    tk.Label(menu_window, text="Menu:", font=('Helvetica', 20)).place(x=w/2, y=80, anchor="center")
    entry_quantities = []
    y_position = 120
    for index, (item, details) in enumerate(menu_list.items(), start=0):
        item_label = tk.Label(menu_window, text=f"{details['name'].title()}: Rs.{details['price']}", font=('Helvetica', 13))
        item_label.place(x=35, y=y_position)
        num_ordered = tk.Entry(menu_window, font=('Helvetica', 13))
        num_ordered.place(x=250, y=y_position)
        entry_quantities.append(num_ordered)
        y_position += 40  # Increase y-coordinate for the next item
    btn_place_order = tk.Button(menu_window, text='Place Order', command=confirm_order, width=23, height=3)
    btn_place_order.place(x=w/2, y=400, anchor="center")
    create_tooltip = tooltip(menu_window)
    create_tooltip(btn_place_order, 'Place your order here!')
    menu_windows.append(menu_window)
    

def generate_receipt(order_details, total_amount, restaurant_name, restaurant_address):
    # Current Date and Time (You can use datetime module)
    import datetime
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pdf_filename = "receipt.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    c.setFont("Helvetica", 12)
    # Restaurant Details
    c.drawString(100, 750, f"Restaurant: {restaurant_name}\n")
    c.drawString(100, 730, f"Date: {date_time.split()[0]}")
    c.drawString(350, 730, f"Time: {date_time.split()[1]}")
    address_lines = restaurant_address.split(",")
    y_position=710
    c.drawString(100, y_position, 'Address: ')
    y_position -= 30
    for _, line in enumerate(address_lines):  # Use _ to represent the index, as it's not needed here
        c.drawString(100, y_position, line)
        y_position -= 15 
    # Table Headers
    y_position -= 25
    c.drawString(100, y_position, "Item")
    c.drawString(250, y_position, "Price")
    c.drawString(350, y_position, "Quantity")
    c.drawString(450, y_position, "Total")
    y_position -= 20
    total_price = 0
    # Item Details Table
    for idx, item in enumerate(order_details, start=1):
        c.drawString(100, y_position, item['name'].title())
        c.drawString(250, y_position, str(item['price']))
        c.drawString(350, y_position, str(item['quantity']))
        item_total = item['price'] * item['quantity']
        total_price += item_total
        c.drawString(450, y_position, str(item_total))
        y_position -= 20
    # Additional Charges
    additional_charges = {
        "Handling Charges": 51,  # Change the value accordingly
        "Others": 75  # Change the value accordingly
    }
    additional_charges_total = sum(additional_charges.values())
    # Display Additional Charges
    y_position -= 20
    for charge, amount in additional_charges.items():
        c.drawString(100, y_position, f"{charge}: {amount}")
        y_position -= 20
    # Calculate GST
    gst = total_price * 0.18  # Assuming 18% GST
    # Display GST and Final Total
    c.drawString(100, y_position - 20, f"GST (18%): {gst}")
    final_total = total_price + gst + additional_charges_total
    c.drawString(100, y_position - 40, f"Total Amount (Including Taxes): {final_total}")
    c.save()
    show_order_confirmation_frame(pdf_filename)

    
def place_order():
    global entry_quantities
    order_details = []
    total_amount = 0
    for i, (item, details) in enumerate(menu_list.items(), start=1):
        quantity = entry_quantities[i - 1].get()
        if quantity and quantity.isdigit() and int(quantity) > 0:
            item_name = details['name']
            item_price = details['price']
            item_quantity = int(quantity)
            order_details.append({'name': item_name, 'price': item_price, 'quantity': item_quantity})
            total_amount += item_price * item_quantity
    if order_details:
        generate_receipt(order_details, total_amount,name,address)
    else:
        messagebox.showinfo("Information", "No items selected for order.")
        display_menu()

        
def calculate_total_amount(entry_quantities):
    total_amount = 0
    for i, quantity_entry in enumerate(entry_quantities):
        quantity = quantity_entry.get()
        if quantity:
            price = int(menu_list[f'Item {i + 1}']['price'])  # Convert the price to an integer
            total_amount += int(quantity) * price
    return total_amount


def show_main_view():
    for widget in home.winfo_children():
        widget.pack()
    for widget in home.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()


def confirm_order():
    global menu_windows
    confirm = messagebox.askquestion("Confirmation", "Are you sure you want to confirm the order?")
    if confirm == 'yes':
        place_order()
        # Close the menu window upon order confirmation
        for window in menu_windows:
            window.destroy()
        menu_windows = [] 
        
        
def show_order_confirmation_frame(pdf_filename):
    confirmation_frame = tk.Toplevel(root)
    confirmation_frame.title("Order Confirmed!")
    confirmation_frame.geometry("%dx%d" % (w, h))
    lbl_confirmation = tk.Label(confirmation_frame, text="Order Confirmed!", font=('Helvetica', 18))
    lbl_confirmation.place(x=w/2, y=110, anchor="center")
    tk.Label(confirmation_frame, text=f"We hope to see you again at {name}!", font=('Helvetica', 14)).place(x=w/2, y=170, anchor="center")
    tk.Button(confirmation_frame, text='Order again', command=display_menu, width=23, height=3).place(x=150, y=400, anchor="center")
    tk.Button(confirmation_frame, text='Exit', command=close_program, width=23, height=3).place(x=350, y=400, anchor="center")
    # Button to open the receipt PDF
    def open_receipt_pdf():
        import os
        os.startfile(pdf_filename)  # Opens the PDF file using the default application
    tk.Button(confirmation_frame, text='View reciept', command=open_receipt_pdf, width=18, height=2).place(x=250, y=300, anchor="center")
    
    
# Read user data from file
with open(r"user requirment.txt") as file:
    user_data = file.read().split('\n')
# Extract data from user requirement file
name = user_data[0]
menu_items = user_data[1].split(',')
menu_prices = user_data[2].split(',')
address = user_data[3]  # Assuming the address is on the fourth line
# Create menu list
menu_list = {
    f'Item {index}': {'name': item, 'price': int(price)} for index, (item, price) in enumerate(zip(menu_items, menu_prices), start=1)
}


# Create root window
root = tk.Tk()
root.title(name)
root.resizable(False, False)
root.geometry("%dx%d" % (w, h))
#labels
tk.Label(root, text=name.title(), font=('Helvetica', 23)).place(x=w/2, y=100, anchor="center")
tk.Label(root, text=f'Welcome to {name.title()}!', font=('Helvetica', 18)).place(x=w/2, y=180, anchor="center")
#button
create_home_tooltip = tooltip(root)
btn = tk.Button(root, text='Menu', command=display_menu, width=23, height=3, anchor="center")
btn.place(x=w/2-80, y=330)
create_home_tooltip(btn, 'View the menu!')

    
root.mainloop()


# In[ ]:




