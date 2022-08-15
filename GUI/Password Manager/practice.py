#------------------------------------------------IMPORT LIBRARIES------------------------------------------------------
import random
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox
from alphanumeric import letters_mix, symb, num
import random
import pandas
import json



#--------------------------------------------CONSTANTS & VARIABLES--------------------------------------------------------
LABEL_FONT = ("Ariel", 12, "normal")
BUTTON_FONT = ("Ariel", 12, "normal")

website = ""
email = ""
password = ""

website_list = []
email_list = []
password_list = []

json_data = {}


#--------------------------------------------------FUNCTIONS---------------------------------------------------------

def generate_password():
    # print("Passoword generated")
    random_password_list = []
    # TODO Generate a random list from the 3 lists
    for elem in range(4):
        random_password_list.append(random.choice(letters_mix))
        random_password_list.append(random.choice(num))
        random_password_list.append(random.choice(symb))
    # print(random_password_list)
    #TODO Scramble the elements
    random.shuffle(random_password_list)
    # print(random_password_list)
    # TODO Convert the list to a string
    random_password_string = ""
    random_password_string = random_password_string.join(random_password_list)
    # print(random_password_string)
    # TODO Delete any texts in the entry and set the password
    password_entry.delete(0, END)
    password_entry.insert(0, random_password_string)


def save():
    # print("Add button clicked")
    # TODO Make sure that all entries are field
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == "":
        website_entry.state(["invalid"])
        messagebox.showerror(title="Missing value", message="Please enter a website")
        website_entry.focus()
    elif email == "":
        website_entry.state(["invalid"])
        messagebox.showerror(title="Missing value", message="Please enter an email address")
        website_entry.focus()
    elif "@" not in email:
        website_entry.state(["invalid"])
        messagebox.showerror(title="Wrong email", message="Please enter a valid email address")
        website_entry.focus()
    elif password == "":
        website_entry.state(["invalid"])
        messagebox.showerror(title="Missing value", message="Please enter a password")
        website_entry.focus()
    else:
        # TODO Save data into a text file
        with open("practice.text", mode="a") as text_file:
            text_file.write(f"{website} | {email} | {password} \n")

        # TODO Saved data into a CSV file
        website_list.append(website)
        email_list.append(email)
        password_list.append(password)

        data_list_dict = {
            "Website": website_list,
            "Email": email_list,
            "Password": password_list
        }

        user_dataframe = pandas.DataFrame(data_list_dict)
        user_dataframe.to_csv("practice.csv")

        # TODO Save data into a json file
        # TODO Add data into a dictionary
        data_dict = {
            website: {
                "Email": email,
                "Password": password
            }
        }
        try:
            # TODO Trying extracting the data in the JSON file
            with open("practice.json", mode="r") as json_file:
                json_data = json.load(json_file)
                # print(type(json_data))

        except FileNotFoundError:
            # TODO Create a message box alerting the user that the file is missing
            response = messagebox.askquestion(title="Missing JSON file", message="The file you are trying to access doesn't exist. "
                                                                      "Would you like to create it?")
            # messagebox.askyesno(title="Missing JSON file", message="The file you are trying to access doesn't exist. "
            #                                                        "Would you like to create it?")
            # print(response)

            # TODO If the file is not present, create it
            if response == "yes":
                with open("practice.json", mode="w") as json_file:
                    json.dump(data_dict, json_file, indent=4)

                messagebox.showinfo(message="File created successfully")

        else:
            # TODO Update the old data with the new data and add rewrite the JSON file contents with the updated data
            with open("practice.json", mode="w") as json_file:
                json_data.update(data_dict)
                json.dump(json_data, json_file, indent=4)

        messagebox.showinfo(title="Data saved", message="Data was saved successfully")

        # TODO Reset the entries
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()


def search():
    # TODO Get the data in the website entry and store it in a variable
    website = website_entry.get().title()

    # TODO Check whether the website name has been entered
    if website == "":
        website_entry.state(["invalid"])
        messagebox.showwarning(title="Value missing", message="Please enter a website to search")
        website_entry.focus()
    else:
        try:
            # TODO Check whether the file exists
            with open("practice.json", mode="r") as search_file:
                search_data = json.load(search_file)
                # print(search_data)
        except FileNotFoundError:
            response = messagebox.askyesno(title="File missing", message="There are no passwords saved yet. "
                                                                         "Would you like to make the entry?")
            if response == True:
                generate_password()

        else:
            # TODO If the query entered exists in the database, extract the email and password and display it to the user
            if website in search_data:
                query_email = search_data[website]["Email"]
                query_password = search_data[website]["Password"]
                messagebox.showinfo(title=website, message=f"Email/Username: {query_email} \n"
                                                           f"Password: {query_password}")
                website_entry.delete(0, END)
                website_entry.focus()
            # TODO If the query doesn't exist, ask user whether they would want to create it
            else:
                response = messagebox.askyesno(message=f"{website} does not exist in the database.\n"
                                            f"Would you like to create it?")
                # print(type(response))
                if response == True:
                    generate_password()





#---------------------------------------------------GUI---------------------------------------------------------------
# TODO Create window
window = Tk()
window.title("Offline Password Manager")
window.minsize(500, 500)
window.config(padx=50, pady=50)

# TODO Create styling
style = ttk.Style(window)
window.tk.call('source', '../_packages/Azure-ttk-theme-main/azure/azure.tcl')
style.theme_use('azure')
style.configure("Accentbutton", foreground="white")

# TODO Create canvas for the logo
logo_img = PhotoImage(file="logo.png")
logo_canvas = Canvas(width=200, height=200)
logo_canvas.create_image(100, 100, image=logo_img)
logo_canvas.grid(row=0, column=1)

# TODO Create website label and entry
website_label = Label(text="Website:", font=LABEL_FONT)
website_label.config(pady=10, padx=10)
website_label.grid(row=1, column=0)

website_entry = ttk.Entry()
website = website_entry.get()
website_entry.focus()
website_entry.config(width=30)
website_entry.grid(row=1, column=1)

# TODO Create email/username label and entry
email_label = Label(text="Email/Username:", font=LABEL_FONT)
email_label.config(padx=10, pady=10)
email_label.grid(row=2, column=0)

email_entry = ttk.Entry()
email = email_entry.get()
email_entry.insert(0, "vincentmuchiri1@gmail.com")
email_entry.config(width=50)
email_entry.grid(row=2, column=1, columnspan=2)

# TODO Create password label and entry
password_label = Label(text="Password:", font=LABEL_FONT)
password_label.config(pady=10)
password_label.grid(row=3, column=0)

password_entry = ttk.Entry()
password = password_entry.get()
password_entry.config(width=30)
password_entry.grid(row=3, column=1)

# TODO Create buttons
search_btn = ttk.Button(text="Search", style="Accentbutton", command=search)
search_btn.config(width=16)
search_btn.grid(row=1, column=2)

generate_password_btn = ttk.Button(text="Generate Password", style="Accentbutton", command=generate_password)
generate_password_btn.grid(row=3, column=2)

add_btn = ttk.Button(text="Save", style="Accentbutton", command=save)
add_btn.config(width=48)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
