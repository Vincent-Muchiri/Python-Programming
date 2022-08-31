from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import pandas
from pprint import pprint
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from os import mkdir, path
from data_manager import DataManager

users_data_manager = DataManager(sheet_name="users")


def login_popup_window():

    def login_command():
        firstname = firstname_entry.get().title()
        lastname = lastname_entry.get().title()
        email_address = email_entry.get().lower()
        confirm_email = confirm_email_entry.get().lower()

        if firstname == "":
            email_entry.state(["invalid"])
            messagebox.showerror(message="Please fill in your first name")
            email_entry.focus()
        elif lastname == "":
            email_entry.state(["invalid"])
            messagebox.showerror(message="Please fill in your last name")
            email_entry.focus()
        elif email_address == "":
            email_entry.state(["invalid"])
            messagebox.showerror(message="Please fill in your email address")
            email_entry.focus()
        elif confirm_email == "":
            confirm_email_entry.state(["invalid"])
            messagebox.showerror(message="Please confirm your email address")
            confirm_email_entry.focus()
        elif email_address != confirm_email:
            confirm_email_entry.state(["invalid"])
            messagebox.showerror(message="Your confirmation email doesn't match")
            confirm_email_entry.delete(0, END)
            confirm_email_entry.focus()
        elif "@" not in email_address:
            email_entry.state(["invalid"])
            messagebox.showerror(message="Please enter a valid email address")
            email_entry.delete(0, END)
            confirm_email_entry.delete(0, END)
            email_entry.focus()
        else:
            # TODO Create a dict of user info
            login_info_dict = {
                "firstName": firstname,
                "lastName": lastname,
                "email": email_address
            }
            # TODO If user doesn't exist, add them and if they do prompt user whether to edit email
            true_response = users_data_manager.login_process(login_info_dict)

            # TODO If user wants to edit email
            if true_response:
                email_entry.delete(0, END)
                confirm_email_entry.delete(0, END)
                email_entry.focus()

            # TODO If user doesn't want to edit email end
            else:
                login_toplevel.destroy()

    login_toplevel = Toplevel()
    login_toplevel.title("Sign up or login")
    login_toplevel.grab_set()
    login_toplevel.config(padx=20, pady=20)
    login_toplevel.geometry("470x300+265+300")
    # app_icon = PhotoImage(file="images/img_1.png")
    # login_toplevel.iconphoto(False, app_icon)

    firstname_label = ttk.Label(login_toplevel, text="Enter your first name:")
    firstname_label.grid(row=0, column=0)

    firstname_entry = ttk.Entry(login_toplevel)
    firstname_entry.grid(row=0, column=1, padx=20)

    lastname_label = ttk.Label(login_toplevel, text="Enter your last name:")
    lastname_label.grid(row=1, column=0)

    lastname_entry = ttk.Entry(login_toplevel)
    lastname_entry.grid(row=1, column=1, padx=20, pady=20)

    prompt_label = ttk.Label(login_toplevel, text="Enter your email address:")
    prompt_label.grid(row=2, column=0)

    email_entry = ttk.Entry(login_toplevel)
    email_entry.config(width=30)
    email_entry.grid(row=2, column=1, padx=20)

    confirm_label = ttk.Label(login_toplevel, text="Confirm your email address:")
    confirm_label.grid(row=3, column=0)

    confirm_email_entry = ttk.Entry(login_toplevel)
    confirm_email_entry.config(width=30)
    confirm_email_entry.grid(row=3, column=1, padx=20, pady=20)

    login_btn = ttk.Button(login_toplevel, text="Login", style="Accentbutton", command=login_command)
    login_btn.config(width=20)
    login_btn.grid(row=4, column=0, columnspan=2)


# ------------------------------------------------------ GUI -----------------------------------------------------------
# TODO Create the main window
window = Tk()
window.title("Flight Search and Notification App")
window.geometry("600x470+200+200")
# window.resizable(False, False)
# app_icon = PhotoImage(file="images/img_1.png")
# window.iconphoto(False, app_icon)
window.config(padx=20, pady=20)
window.lower()

# TODO Set windows styling
style = ttk.Style(window)
window.tk.call('source',
               'C:/Users/Vin Muchiri/OneDrive/_packages/Azure-ttk-theme-main/azure/azure.tcl')
style.theme_use('azure')
style.configure("Accentbutton", foreground="white")





login_popup_window()
window.mainloop()
