# ----------------------------------------------LIBRARIES AND CLASSES---------------------------------------------------
import json
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import alphanumeric
import random
import pandas

# -----------------------------------------------CONSTANTS AND VARIABLES------------------------------------------------
LABEL_FONT = ("Ariel", 12, "normal")

record = []

id = ""
part_name = ""
customer_name = ""
retailer_name = ""
price = 0


# ---------------------------------------------------FUNCTIONS----------------------------------------------------------
def get_entry_values():
    """Gets values in the entries and assigns them in variables named:\n
    part_name\n
    customer_name\n
    retailer_name\n
    price(float)"""
    global part_name, customer_name, retailer_name, price
    part_name = part_entry.get()
    customer_name = customer_entry.get()
    retailer_name = retailer_entry.get()
    price = float(price_entry.get())


def part_id_generator():
    """Generates a random 12-digit id.\n
    Once a part has been saved, its ID cannot be changed."""
    num_id_list = []
    num = alphanumeric.num

    for length in range(12):
        num_id_list.append(random.choice(num))

    # TODO Convert the list to a string
    num_id = "".join(num_id_list)

    # TODO Return the random ID
    return num_id


# TODO Add records to the Treeview
def first_time_run():
    """Retrieves record data stored in the JSON file and adds the data into the Treeview when the program runs for the
    first time.\n
    If the file doesn't exist, the program skips."""
    try:
        # TODO Retrieve data from the JSON file
        with open("parts.json", mode="r") as json_file:
            parts_data_json = json.load(json_file)

        # TODO Retrieve data from the CSV file
        parts_data_df = pandas.read_csv("parts.csv")
        parts_data_dict = parts_data_df.to_dict(orient="list")

    except FileNotFoundError:
        # TODO If the file doesn't exist, don't do anything
        pass

    else:
        # TODO Add the data as tuples to the treeview
        # TODO JSON
        for part in parts_data_json:
            id = part
            part_name = parts_data_json[part]["Name"]
            customer = parts_data_json[part]["Customer"]
            retailer = parts_data_json[part]["Retailer"]
            price = float(parts_data_json[part]["Price"])

            # TODO Add the data to a tuple
            part_tuple = (id, part_name, customer, retailer, price)

            # TODO Add the data to the treeview
            # tree.insert('', tkinter.END, values=part_tuple)

        # TODO CSV
        for index in range(len(parts_data_dict['Part'])):
            id = parts_data_dict['ID'][index]
            part_name = parts_data_dict['Part'][index]
            customer = parts_data_dict['Customer'][index]
            retailer = parts_data_dict['Retailer'][index]
            price = parts_data_dict['Price'][index]

            # TODO Add the data to a tuple
            part_tuple = (id, part_name, customer, retailer, price)

            # TODO Add the data to the treeview
            tree.insert('', tkinter.END, values=part_tuple)


# TODO Display the records in the entry
def item_selected(event):
    """Extracts the values from the record selected and adds them to their respective entries."""
    global record
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        # TODO Clear all entries
        for entry in (part_entry, customer_entry, retailer_entry, price_entry):
            entry.delete(0, END)

        # TODO Display the data of the record selected in the respective entry
        part_entry.insert(0, record[1])
        customer_entry.insert(0, record[2])
        retailer_entry.insert(0, record[3])
        price_entry.insert(0, record[4])


# TODO Save the data in a local file
def save_data():
    """Saves the record data locally in a file and displays it on the Treeview"""

    id_list = []
    part_name_list = []
    customer_list = []
    retailer_list = []
    price_list = []

    # print("Add button clicked")
    # TODO get the data from the entries
    if part_entry.get() == "":
        part_entry.state(["invalid"])
        messagebox.showerror(title="Part Name Missing", message="Please input the part name!")
        part_entry.focus()
    elif customer_entry.get() == "":
        customer_entry.state(["invalid"])
        messagebox.showerror(title="Customer Name Missing", message="Please input the customer!")
        customer_entry.focus()
    elif retailer_entry.get() == "":
        retailer_entry.state(["invalid"])
        messagebox.showerror(title="Retailer Name Missing", message="Please input the retailer!")
        retailer_entry.focus()
    elif price_entry.get() == "":
        price_entry.state(["invalid"])
        messagebox.showerror(title="Price Missing", message="Please input the price!")
        price_entry.focus()
    else:
        try:
            get_entry_values()
        except ValueError:
            price_entry.state(["invalid"])
            messagebox.showerror(title="Value Error", message="Enter only numbers as the price!")
            price_entry.delete(0, END)
            price_entry.focus()
        else:
            # TODO Generate part ID
            id = part_id_generator()

            #  TODO Add the data to the tree
            part_tuple = (id, part_name, customer_name, retailer_name, price)
            tree.insert('', tkinter.END, values=part_tuple)

            # TODO JSON File
            # TODO ADD the data to a dictionary
            part_dict = {
                id: {
                    "Name": part_name,
                    "Customer": customer_name,
                    "Retailer": retailer_name,
                    "Price": price
                }
            }

            # TODO Save data in a JSON file
            try:
                # TODO Check whether the file exists
                with open("parts.json", mode="r") as parts_file:
                    parts_data = json.load(parts_file)
            except FileNotFoundError:
                with open("parts.json", mode="w") as parts_file:
                    json.dump(part_dict, parts_file, indent=4)
            else:
                # TODO Update the data to the existing JSON data
                parts_data.update(part_dict)

                # TODO Add the updated data to the JSON file
                with open("parts.json", mode="w") as parts_file:
                    json.dump(parts_data, parts_file, indent=4)

            # TODO CSV file
            try:
                # TODO Open the CSV file to check whether it exists or not
                csv_data = pandas.read_csv("parts.csv")
            except FileNotFoundError:
                # TODO If file doesn't exist, create it and add the data
                # TODO Add the data to lists
                id_list.append(id)
                part_name_list.append(part_name)
                customer_list.append(customer_name)
                retailer_list.append(retailer_name)
                price_list.append(price)

                csv_dict = {}

                csv_dict["ID"] = id_list
                csv_dict["Part"] = part_name_list
                csv_dict["Customer"] = customer_list
                csv_dict["Retailer"] = retailer_list
                csv_dict["Price"] = price_list

                csv_df = pandas.DataFrame(csv_dict)
                csv_df.to_csv("parts.csv", index=False)
            else:
                new_row_dict = {
                    "ID": [id],
                    "Part": [part_name],
                    "Customer": [customer_name],
                    "Retailer": [retailer_name],
                    "Price": [price]
                }

                new_row_df = pandas.DataFrame(new_row_dict)
                # TODO Append the new row of data to the CSV file
                new_row_df.to_csv("parts.csv", mode="a", index=False, header=False)

            # TODO Clear the entries
            for entry in (part_entry, customer_entry, retailer_entry, price_entry):
                entry.delete(0, END)
            part_entry.focus()


def remove():
    """Deletes the record from the Treeview and the local file."""
    parts_dict = {}
    try:
        get_entry_values()
    except ValueError:
        messagebox.showerror(title="Deletion failed", message="Click on a record to delete")
    else:
        record = [part_name, customer_name, retailer_name, price]

        with open("parts.json", mode="r") as json_file:
            parts_data = json.load(json_file)

        # TODO Convert the dictionary to a list
        parts_list = []
        for part in parts_data:
            id = part
            parts_list.append([parts_data[part]["Name"], parts_data[part]["Customer"], parts_data[part]["Retailer"], parts_data[part]["Price"]])
        # TODO Remove part
        for part in parts_list:
            if part == record:
                # TODO Display warning message
                response = messagebox.askyesno(title="Delete record", message="Are you sure you want to delete the record?")

                if response == True:
                    parts_list.remove(part)

                    # TODO Change the list to a dict
                    for part in parts_list:
                        parts_dict = {
                            id: {
                                "Name": part[0],
                                "Customer": part[1],
                                "Retailer": part[2],
                                "Price": part[3]
                            }
                        }

                    # TODO Clear the entries
                    for entry in (part_entry, customer_entry, retailer_entry, price_entry):
                        entry.delete(0, END)

                    # TODO Delete the record from the treeview
                    deleted_record = tree.selection()[0]
                    tree.delete(deleted_record)

                    # TODO Delete the record in the JSON file
                    # TODO Override the JSON data
                    with open("parts.json", mode="r") as parts_file:
                        data = json.load(parts_file)

                    data = parts_dict

                    with open("parts.json", mode="w") as parts_file:
                        json.dump(data, parts_file, indent=4)

                    messagebox.showinfo(message=f"{part_name} has been deleted successfully")


def update():
    """Updates the values of the selected record both on the Treeview and the local file.\n
    The part ID remains unchanged."""
    # TODO Make sure the record has been selected
    try:
        get_entry_values()
    except ValueError:
        messagebox.showerror(title="Value Error", message="Make sure a record has been selected")
    else:
        # TODO Get the id number of the record
        record_number = tree.focus()
        id = tree.item(record_number, 'values')[0]

        # TODO Replace the values in the entries in the treeview
        tree.item(record_number, text="", values=(id, part_name, customer_name, retailer_name, price))

        # TODO Replace the record in the JSON file
        # TODO Get data from the JSON file
        with open("parts.json", mode="r") as parts_file:
            parts_dict = json.load(parts_file)

        # TODO Replace the data in the dictionary
        for part in parts_dict:
            if part == id:
                parts_dict[part]["Name"] = part_name
                parts_dict[part]["Customer"] = customer_name
                parts_dict[part]["Retailer"] = retailer_name
                parts_dict[part]["Price"] = price

        # TODO Save the new dictionary to the JSON file
        with open("parts.json", mode="w") as parts_file:
            json.dump(parts_dict, parts_file, indent=4)

        messagebox.showinfo(title="Update successful", message= part_name + " has been updated successfully.")


def clear():
    """Clears the entries."""
    # TODO Clear all the entries
    part_entry.delete(0, END)
    customer_entry.delete(0, END)
    retailer_entry.delete(0, END)
    price_entry.delete(0, END)

    # TODO Set cursor to the part name entry
    part_entry.focus()


# ------------------------------------------------------GUI-------------------------------------------------------------
# TODO Setup the window
window = Tk()
window.title("Part Manager")
window.minsize(width=1080, height=460)
# window.geometry("1080x460")
window.config(pady=20)

# TODO Set Window icon
database_512 = PhotoImage(file="../_images/database.png")
database_24 = PhotoImage(file="../_images/database 24.png")
window.iconphoto(False, database_24)

# TODO Set transparent background
window.attributes('-alpha', 0.9)

# TODO Set window styling
style = ttk.Style(window)
window.tk.call('source', 'C:/Users/Vin Muchiri/OneDrive/Python Programming/_packages/Azure-ttk-theme-main/azure/azure.tcl')
style.theme_use('azure')
style.configure("Accentbutton", foreground="white")

# TODO Create a LabelFrame
# data_entry_frame = LabelFrame(text="Data Entry")
# data_entry_frame.pack(expand="yes", fill="both")

# TODO Create 'part name" label and entry
part_label = Label(text="Part Name: ", font=LABEL_FONT)
part_label.config(padx=20)
part_label.grid(row=0, column=0)

part_entry = ttk.Entry()
part_entry.focus()
part_entry.grid(row=0, column=1)

# TODO Create 'Customer' label and entry
customer_label = Label(text="Customer: ", font=LABEL_FONT)
customer_label.config(padx=20)
customer_label.grid(row=0, column=2)

customer_entry = ttk.Entry()
customer_entry.grid(row=0, column=3)

# TODO Create 'Retailer' label and entry
retailer_label = Label(text="Retailer: ", font=LABEL_FONT)
retailer_label.config(pady=20)
retailer_label.grid(row=1, column=0)

retailer_entry = ttk.Entry()
retailer_entry.grid(row=1, column=1)

# TODO Create 'Price' label and entry
price_label = Label(text="Price", font=LABEL_FONT)
price_label.grid(row=1, column=2)

price_entry = ttk.Entry()
price_entry.grid(row=1, column=3)

# TODO Create the CRUD(Create, Read, Update and Delete) button
add_btn = ttk.Button(text="Add Part", style="Accentbutton", command=save_data)
add_btn.config(width=15)
add_btn.grid(row=2, column=0)

remove_btn = ttk.Button(text="Remove Part", style="Accentbutton", command=remove)
remove_btn.config(width=15)
remove_btn.grid(row=2, column=1)

update_btn = ttk.Button(text="Update Part", style="Accentbutton", command=update)
update_btn.config(width=15)
update_btn.grid(row=2, column=2)

clear_btn = ttk.Button(text="Clear Input", style="Accentbutton", command=clear)
clear_btn.config(width=15)
clear_btn.grid(row=2, column=3)

# TODO Create treeview
# TODO Define the columns
columns = ("Part ID", "Part Name", "Customer", "Retailer", "Price")

tree = ttk.Treeview(columns=columns, show='headings')

# TODO Define headings
tree.heading("Part ID", text="Part ID")
tree.heading("Part Name", text="Part Name")
tree.heading("Customer", text="Customer")
tree.heading("Retailer", text="Retailer")
tree.heading("Price", text="Price")

tree.grid(row=4, column=0, columnspan=4, sticky='nsew', pady=20, padx=20)

tree.bind('<<TreeviewSelect>>', item_selected)

# TODO Create a scrollbar for the treeview
scrollbar = ttk.Scrollbar(orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=3, column=4, sticky='ns')

# TODO Add the data stored in the JSON file in  the treeview
first_time_run()

window.mainloop()
