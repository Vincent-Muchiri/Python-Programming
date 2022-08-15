from tkinter import *
import tkinter.ttk as ttk
import pandas
from tkinter import messagebox
import random
import pyperclip
import json


def search():
    query = website_entry.get()
    if query == "":
        messagebox.showerror(title="Empty search", message="Please enter a search term")
    else:
        try:
            with open("data.json", "r") as search_file:
                data = json.load(search_file)
                # print("JSON file opened")
                web_json_list = [website for website in data]
                # print(web_json_list)
        except FileNotFoundError:
            create_file = messagebox.askyesno(title="File missing",
                                              message="The JSON file you are trying to search doesn't "
                                                                          "exist. Would you like to create the file?")
            if create_file:
                with open("data.json", "w") as search_file:
                    # json.dump("", search_file) # Generates an attribute error while trying to save data.
                    json.dump({}, search_file)
        else:
            if query in web_json_list:
                messagebox.showinfo(title=f"Search results for {query}",
                                    message=f"Email address/username: {data[query]['email']} \n"
                                            f"Password: {data[query]['password']}")
            else:
                yes_selected = messagebox.askyesno(title=f"Search results for {query}",
                                                   message=f'"{query}" does not exist. Would you like to save it?')
                if yes_selected:
                    generate_password()
                else:
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)
                    website_entry.focus()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))

    password_letters = [random.choice(letters) for items in range(nr_letters)]

    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    password_symbols = [random.choice(symbols) for item in range(nr_symbols)]
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)
    password_numbers = [random.choice(numbers) for item in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char
    password = "".join(password_list)

    # print(f"Your password is: {password}")

    # TODO Insert the password into the entry and delete any previous suggestion
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    # TODO Add password to the paperclip using pyperclip
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


website_list = []
email_username_list = []
password_list = []


def save():
    # TODO get the values of the entries
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    # TODO Create a dict to dump data into a json file
    data_dict = {
        website: {
            "email": email_username,
            "password": password
        }
    }

    # print(data_dict)

    # TODO Check whether some fields have been left empty
    if len(website) == 0:
        website_entry.state(["invalid"])
        messagebox.showwarning(message="Please enter the name of the website")
        website_entry.focus()
    elif len(email_username) == 0:
        email_username_entry.state(["invalid"])
        messagebox.showwarning(message="Please enter your email address or username")
        email_username_entry.focus()
    elif "@" not in email_username:
        email_username_entry.state(["invalid"])
        messagebox.showwarning(message="Invalid email address.")
        email_username_entry.focus()
    elif len(password) == 0:
        password_entry.state(["invalid"])
        messagebox.showwarning(message="Please enter your password")
        password_entry.focus()
    else:
        email_username_entry.state()
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details you've entered: \n"
                                                              f"Email: {email_username}"
                                                           f" \nPassword: {password}.\nIs it ok to save?")

        if is_ok:
            # print("Data saved!")
            # print(website, email_username, password)

            # TODO Save data in a json file

            # with open("data.json", mode="r") as json_file:
            #     current_data = json.load(json_file)
            #     current_data.update(data_dict)
            #     print(current_data)
            #
            # with open("data.json", mode="w") as json_file:
            #     json.dump(data_dict, json_file, indent=4)
            try:
                with open("data.json", mode="r") as json_file:
                    data = json.load(json_file)
                    print(data)
                    # some_dict = {"Test": "Passed"}
                    # data.update(some_dict)

                    # print(data)
            except FileNotFoundError:
                # website_entry.insert(website)
                # password_entry.insert(password)
                # print("File missing")
                create_file = messagebox.askyesno(title="Error opening file", message="The JSON file you're trying to "
                                                     "access doesn't exist. Would you like to create it?")
                if create_file:
                    with open("data.json", mode="w") as json_file:
                        json.dump(data_dict, json_file, indent=4)
                        messagebox.showinfo(message="Data was added successfully")
            else:
                data.update(data_dict)
                print(data)
                # print(type(data))
                with open("data.json", mode="w") as json_file:
                    json.dump(data, json_file, indent=4)
                    messagebox.showinfo(message="Data saved!")



            # TODO Create a text file and save the data in it
            with open("data.txt", mode="a") as log_file:
                # log_file.write(website)
                # log_file.write(" | ")
                # log_file.write(email_username)
                # log_file.write(" | ")
                # log_file.write(password)
                # log_file.write("\n")
                log_file.write(f"{website} | {email_username} | {password}\n")

            # TODO Create a CSV file and save the data in it
            website_list.append(website)
            email_username_list.append(email_username)
            password_list.append(password)

            user_data_dict = {
                "Website": website_list,
                "Email/Username": email_username_list,
                "Password": password_list
            }
            # print(user_data_dict)
            user_data_df = pandas.DataFrame(user_data_dict)
            user_data_df.to_csv("data.csv")

        # TODO Delete the text from the display entry
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# TODO Create window
window = Tk()
window.title("Offline Password Manager")
window.config(padx=50, pady=50)

# TODO Set window styling
style = ttk.Style(window)
window.tk.call('source', 'C:/Users/Vin Muchiri/OneDrive/Python Programming/_packages/Azure-ttk-theme-main/azure/azure.tcl')
style.theme_use('azure')
style.configure("Accentbutton", foreground="white")

LABEL_FONT = ("Arial", 12, "normal")
BUTTON_FONT = ("Arial", 18, "normal")

# TODO Create canvas
logo_image = PhotoImage(file="logo.png")
logo = Canvas(width=200, height=200)
logo.create_image(100, 100, image=logo_image)
logo.config()
logo.grid(row=0, column=1)

# TODO Create the "Website" label
website_label = Label(text="Website:", font=LABEL_FONT)
website_label.config(pady=10)
website_label.grid(row=1, column=0)

# TODO Create the "Email/Username" label
email_username_label = Label(text="Email/Username:", font=LABEL_FONT)
email_username_label.config(padx=10, pady=10)
email_username_label.grid(row=2, column=0)

# TODO Create the "Password" label
password_label = Label(text="Password:", font=LABEL_FONT)
password_label.config(pady=10)
password_label.grid(row=3, column=0)

# TODO Create the website entry
website_entry = ttk.Entry()
website_entry.config(width=30)
website_entry.focus()
website_entry.grid(row=1, column=1)

# TODO Create a search button
search_btn = ttk.Button(window, style="Accentbutton", text="Search", command=search)
search_btn.config(width=16)
search_btn.grid(row=1, column=2)


# TODO Create the email/username entry
email_username_entry = ttk.Entry()
email_username_entry.config(width=50)
email_username_entry.insert(0, "vincentmuchiri1@gmail.com")
email_username_entry.grid(row=2, column=1, columnspan=2)

# TODO Create the password entry
# password_entry = Entry()
password_entry = ttk.Entry(window)
password_entry.config(width=30)
password_entry.grid(row=3, column=1)

# TODO Create the "Generate password" button
# generate_password_btn = Button(text="Generate Password", font=LABEL_FONT)
generate_password_btn = ttk.Button(window, text="Generate Password", style="Accentbutton", command=generate_password)
generate_password_btn.grid(row=3, column=2)

# TODO Create the "Add" button
# add_btn = Button(text="Add", font=LABEL_FONT)
add_btn = ttk.Button(window, text="Add", style="Accentbutton", command=save)
add_btn.config(width=48)
add_btn.grid(row=4, column=1, columnspan=2)

# TODO Print details stored in the CSV file
# data = pandas.read_csv("User Data.csv")
# print(data)

window.mainloop()
