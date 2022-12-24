from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from pprint import pprint

# TODO Create a window
window = Tk()
window.title("Automated LinkedIn Job Application")
window.geometry("400x400+200+200")
# window.minsize(width=400, height=400)
window.config(padx=10, pady=10)

# TODO Link the styling file
style = ttk.Style(window)
window.tk.call('source',
               'C:/Users/Vin Muchiri/OneDrive/_packages/Azure-ttk-theme-main/azure/azure.tcl')
style.theme_use('azure')
style.configure("Accentbutton", foreground="white")

# TODO Create a 'login details' label frame
login_frame = ttk.Labelframe(text="Login Details")
login_frame.pack(fill="both")
login_frame.config(padding=10)

# TODO Add the email and password labels and entry boxes
email_label = ttk.Label(login_frame, text="Email address:")
email_label.grid(column=0, row=0)

email_entry = ttk.Entry(login_frame)
email_entry.config(width=30)
email_entry.grid(column=1, row=0)

password_label = ttk.Label(login_frame, text="Password:")
password_label.grid(column=0, row=1)

password_entry = ttk.Entry(login_frame)
password_entry.config(width=30)
password_entry.grid(column=1, row=1, padx=20, pady=10)

# TODO Create a 'Search query' label frame
search_frame = ttk.Labelframe(text="Search query")
search_frame.pack(fill="both", pady=20)
search_frame.config(padding=10)

# TODO Create a multi line text box
search_text = Text(search_frame, height=3)
# Puts cursor in textbox.
search_text.focus()
# Adds some text to begin with.
search_text.insert(END, "Enter search parameters seperated by a ,")
# print(search_text.get("1.0", END))
search_text.pack()

# TODO Create an apply button
apply_btn = ttk.Button(text="Apply", style="Accentbutton")
apply_btn.pack()


window.mainloop()
