# Import Required Library
from tkinter import *
from tkcalendar import Calendar

# Create Object
root = Tk()

# Set geometry
root.geometry("400x400")

# Add Calendar
cal = Calendar( selectmode = 'day',
			year = 2020, month = 5,
			day = 22)

# cal.pack(pady = 20)
cal.grid(row=0, column=0)

def grad_date():
	date.config(text = "Selected Date is: " + cal.get_date())

print(cal.get_date())
print(type(cal.get_date()))

# Add Button and Label
Button( text = "Get Date",
	command = grad_date).grid(row=1, column=0)

date = Label( text = "")
# date.pack(pady = 20)
date.grid(row=2, column=0)

# Execute Tkinter
root.mainloop()
