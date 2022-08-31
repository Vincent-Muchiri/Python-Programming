from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import pandas
from pprint import pprint
from flight_search import FlightSearch
from data_managerv3 import DataManagerV3
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from os import mkdir, path

SHEET_NAME = "flightDealFinderV3"

flight_search = FlightSearch()

# TODO First time run
data_manager = DataManagerV3(SHEET_NAME)


def update_search_command():
    """
    Update/change the search parameters recorded in the Google sheets e.g. the price entered
    :return:
    """
    pass


def delete_search_command():
    """Delete searches saved in the treeview, CSV file and Excel sheet"""
    pass


def results_command():
    """Shows a window with scrollable search results otherwise it shows an info messagebox"""

    def search_results_window():
        """Populates a window containing the search results if they are any"""


def refresh_command():
    """Refresh the selected treeview """
    pass


def search_flight_window():
    def search_flight_command():
        # TODO Get the search data and save it in a dict
        flight_search_params = {}

        try:
            # Create the dict later to conserve the order
            currency = currency_variable.get()
            ticket_budget = int(ticket_price_entry.get())
            departure_city_name = departure_entry.get()
            destination_city_name = destination_entry.get()
            date_from = search_date_from_entry.get()
            date_to = search_date_to_entry.get()
            max_stopovers = int(max_nights_spinbox.get())
            flight_type = flight_type_variable.get().lower()
            max_nights = int(max_nights_spinbox.get())
            min_nights = int(min_nights_spinbox.get())

            departure_city_name = departure_entry.get()
            destination_city_name = destination_entry.get()

        except ValueError:
            ticket_price_entry.state(["invalid"])
            messagebox.showerror(message="Please enter a value for the maximum budget")
            ticket_price_entry.focus()
        else:
            if departure_entry.get() == "":
                departure_entry.state(["invalid"])
                messagebox.showerror(message="Please enter a departure city code")
                departure_entry.focus()
            elif destination_entry.get() == "":
                destination_entry.state(["invalid"])
                messagebox.showerror(message="Please enter a destination city code")
                destination_entry.focus()
            else:

                false_codes = True
                # TODO Get the IATA codes using threads and verify the results
                while false_codes:
                    results = []
                    with ThreadPoolExecutor(max_workers=2) as executor:
                        city_list = [departure_city_name, destination_city_name]
                        for city_code in executor.map(flight_search.get_iata_code, city_list):
                            results.append(city_code)

                    if results[0] != results[1]:
                        flight_search_params["fly_from"] = results[0]
                        flight_search_params["fly_to"] = results[1]
                        flight_search_params["date_from"] = date_from
                        flight_search_params["date_to"] = date_to
                        flight_search_params["price_to"] = ticket_budget
                        flight_search_params["flight_type"] = flight_type
                        flight_search_params["curr"] = currency
                        flight_search_params["max_stopovers"] = max_stopovers
                        flight_search_params["nights_in_dst_from"] = min_nights
                        flight_search_params["nights_in_dst_to"] = max_nights

                        false_codes = False

                # TODO Search for the flight
                search_results = flight_search.search_flight(flight_search_params)

                if len(search_results) == 0:
                    response = messagebox.askyesno(message="There are no results for your search.\n"
                                                           "Would you like to save it for later?")
                    if response:
                        # TODO Add the data to the treeview
                        flight_search_params_tuple = (
                            departure_city_name.title(),
                            destination_city_name.title(),
                            f"{flight_search_params['curr']} {flight_search_params['price_to']}",
                            flight_search_params["flight_type"].title(),
                            flight_search_params["date_from"],
                            flight_search_params["date_to"],
                            0,
                            0
                        )
                        saved_searches_tree.insert("", tk.END, values=flight_search_params_tuple)

                        # TODO Create the data folder
                        if not path.exists("data"):
                            mkdir("data")
                        save_search_params = {}
                        # TODO Save the data in a CSV file and Google sheet
                        save_search_params["departureCity"] = flight_search_params["fly_from"]
                        save_search_params["destinationCity"] = flight_search_params["fly_to"]
                        save_search_params["budget"] = flight_search_params["price_to"]
                        save_search_params["currency"] = flight_search_params["curr"]
                        save_search_params["flightType"] = flight_search_params["flight_type"]
                        save_search_params["maxStopovers"] = flight_search_params["max_stopovers"]
                        save_search_params["minNightsInDestination"] = flight_search_params["nights_in_dst_from"]
                        save_search_params["maxNightsInDestination"] = flight_search_params["nights_in_dst_to"]
                        save_search_params["searchFrom"] = flight_search_params["date_from"]
                        save_search_params["searchTo"] = flight_search_params["date_to"]

                        data_manager.save_search(search_params=save_search_params)

                else:
                    # TODO Populate the results in a popup window


                    pass

    search_window = Toplevel()
    search_window.title("Search for a flight")
    search_window.geometry("500x600")
    search_window.grab_set()
    search_icon = PhotoImage(file="images/search_icon.png")
    search_window.iconphoto(False, search_icon)
    search_window.config(padx=20, pady=20)

    departure_label = ttk.Label(search_window, text="Departure City:")
    departure_label.grid(row=0, column=0)
    departure_entry = ttk.Entry(search_window)
    departure_entry.focus()
    departure_entry.grid(row=0, column=1, padx=20)

    destination_label = ttk.Label(search_window, text="Destination City:")
    destination_label.grid(row=1, column=0, pady=20)
    destination_entry = ttk.Entry(search_window)
    destination_entry.grid(row=1, column=1, padx=20, pady=20)

    ticket_price_label = ttk.Label(search_window, text="Max ticket budget:")
    ticket_price_label.grid(row=2, column=0)
    ticket_price_entry = ttk.Entry(search_window)
    ticket_price_entry.grid(row=2, column=1, padx=20)

    currency_label = ttk.Label(search_window, text="Choose currency: ")
    currency_label.grid(row=3, column=0, pady=20)
    currency_options = ["AED", "AUD", "BTC", "BTN", "BWP", "CAD", "CNY", "EUR", "USD", "GBP", "JPY", "KES", "NZD",
                        "SAR"]
    currency_variable = StringVar()
    currency_variable.set(currency_options[8])  # default value
    currency_menu = ttk.OptionMenu(search_window, currency_variable, *currency_options)
    currency_menu.grid(row=3, column=1, padx=20, pady=20)

    flight_type_label = ttk.Label(search_window, text="Choose the flight type: ")
    flight_type_label.grid(row=4, column=0)
    flight_type_options = ["Round", "Oneway"]
    flight_type_variable = StringVar()
    flight_type_variable.set(flight_type_options[0])  # default value
    flight_type_menu = ttk.OptionMenu(search_window, flight_type_variable, *flight_type_options)
    flight_type_menu.grid(row=4, column=1, padx=20)

    stopover_label = ttk.Label(search_window, text="Maximum stopovers")
    stopover_label.grid(row=5, column=0, pady=20)
    stopover_spinbox = ttk.Spinbox(search_window, from_=0, to=5, width=5)
    stopover_spinbox.set(0)
    stopover_spinbox.grid(row=5, column=1, padx=20, pady=20)

    min_nights_label = ttk.Label(search_window, text="Minimum nights in destination ")
    min_nights_label.grid(row=5 + 1, column=0)
    min_nights_spinbox = ttk.Spinbox(search_window, from_=1, to=365, width=5)
    min_nights_spinbox.set(1)
    min_nights_spinbox.grid(row=5 + 1, column=1, padx=20)

    max_nights_label = ttk.Label(search_window, text="Maximum nights in destination")
    max_nights_label.grid(row=6 + 1, column=0, pady=20)
    max_nights_spinbox = ttk.Spinbox(search_window, from_=1, to=365, width=5)
    max_nights_spinbox.set(1)
    max_nights_spinbox.grid(row=6 + 1, column=1, padx=20, pady=20)

    search_date_from_label = ttk.Label(search_window, text="Search flights from")
    search_date_from_label.grid(row=8, column=0)
    search_date_from_entry = ttk.Entry(search_window)
    search_date_from_entry.grid(row=8, column=1, padx=20)

    date_format_label = ttk.Label(search_window, text="dd/mm/yyyy")
    date_format_label.grid(row=8, column=2)

    search_date_to_label = ttk.Label(search_window, text="Search flights to")
    search_date_to_label.grid(row=9, column=0, pady=20)
    search_date_to_entry = ttk.Entry(search_window)
    search_date_to_entry.grid(row=9, column=1, padx=20, pady=20)

    search_flight_btn = ttk.Button(search_window, text="Search", style="Accentbutton", command=search_flight_command)
    search_flight_btn.config(width=20)
    search_flight_btn.grid(row=10, column=1)


# ------------------------------------------------------ GUI -----------------------------------------------------------
# TODO Create the main window
window = Tk()
window.title("Flight Search and Notification App")
window.geometry("670x470")
# window.resizable(False, False)
app_icon = PhotoImage(file="images/img_1.png")
window.iconphoto(False, app_icon)
window.config(padx=20, pady=20)

# TODO Set windows styling
style = ttk.Style(window)
window.tk.call('source',
               'C:/Users/Vin Muchiri/OneDrive/_packages/Azure-ttk-theme-main/azure/azure.tcl')
style.theme_use('azure')
style.configure("Accentbutton", foreground="white")

button_label_frame = ttk.LabelFrame(border=0)
button_label_frame.pack()

# -------------------------------------------- Search for Flights ------------------------------------------------------
# TODO Create search button that opens up window
search_btn = ttk.Button(button_label_frame, text="Search for flight", style="Accentbutton",
                        command=search_flight_window)
search_btn.grid(row=0, column=0)

# ------------------------------------------------- Delete Searches ----------------------------------------------------
delete_btn = ttk.Button(button_label_frame, text="Delete Search History", style="Accentbutton",
                        command=delete_search_command)
delete_btn.grid(row=0, column=1)

# -------------------------------------------------- Update Searches ---------------------------------------------------
update_btn = ttk.Button(button_label_frame, text="Update search parameters", style="Accentbutton",
                        command=update_search_command)
update_btn.grid(row=0, column=2, padx=20)

# --------------------------------------------------- View results -----------------------------------------------------
results_btn = ttk.Button(button_label_frame, text="View search results", style="Accentbutton", command=results_command)
results_btn.grid(row=1, column=0, padx=20, pady=20)

# -------------------------------------------------- Update results ----------------------------------------------------
refresh_btn = ttk.Button(button_label_frame, text="Refresh results", style="Accentbutton", command=refresh_command)
refresh_btn.grid(row=1, column=1, padx=20, pady=20)

# -------------------------------------------------- View Tree ---------------------------------------------------------
# TODO Create treeview that saves all the saved searches with their search parameter
treeview_columns = ("departureCity", "destinationCity", "budget", "flightType", "searchFrom", "searchTo",
                    "results", "available_ticket")

saved_searches_tree = ttk.Treeview(columns=treeview_columns, show='headings')

saved_searches_tree.column("departureCity", width=65, stretch=NO)
saved_searches_tree.heading('departureCity', text='Departure')
saved_searches_tree.column("destinationCity", width=70, stretch=NO)
saved_searches_tree.heading('destinationCity', text='Destination')
saved_searches_tree.column("budget", width=85, stretch=NO)
saved_searches_tree.heading('budget', text='Ticket budget')
saved_searches_tree.column("flightType", width=70, stretch=NO)
saved_searches_tree.heading('flightType', text='Flight type')
saved_searches_tree.column("searchFrom", width=80, stretch=NO)
saved_searches_tree.heading('searchFrom', text='Date from')
saved_searches_tree.column("searchTo", width=80, stretch=NO)
saved_searches_tree.heading("searchTo", text="Date to")
saved_searches_tree.column("results", width=70, stretch=NO)
saved_searches_tree.heading('results', text='Results')
saved_searches_tree.column("available_ticket", width=100, stretch=NO)
saved_searches_tree.heading("available_ticket", text="Available ticket")

# saved_searches_tree.grid(row=2, column=0, columnspan=4, sticky='nsew')
saved_searches_tree.pack(expand=YES, fill=BOTH, pady=20)

# TODO Make view tree scrollable both horizontally and vertically
# y_scrollbar = ttk.Scrollbar(orient=tk.VERTICAL, command=saved_searches_tree.yview)
# saved_searches_tree.configure(yscrollcommand=y_scrollbar.set)
# y_scrollbar.grid(row=3, column=4, sticky='ns')
# y_scrollbar.pack(side="left")

x_scrollbar = ttk.Scrollbar(orient="horizontal", command=saved_searches_tree.xview)
saved_searches_tree.configure(xscrollcommand=x_scrollbar.set)
# x_scrollbar.grid(row=3, column=0, sticky="ew")
x_scrollbar.pack()

# TODO Add data to treeview if it exists
if path.exists("data/saved searches.csv"):
    file_dataframe = pandas.read_csv("data/saved searches.csv")
    data_rows = file_dataframe.to_dict(orient="records")
    # pprint(data_rows)

    for row in data_rows:
        # TODO Create a tuple
        # saved_search_params_tuple = ()

        saved_search_params_tuple = (
            row["departureCity"].upper(),
            row["destinationCity"].upper(),
            f'{row["currency"]} {row["budget"]}',
            row["flightType"].title(),
            row["searchFrom"],
            row["searchTo"],
            0,
            0
        )
        saved_searches_tree.insert('', tk.END, values=saved_search_params_tuple)

window.mainloop()
