import requests
import os
from datetime import datetime
from tkinter import messagebox, simpledialog
from tkinter import *
import tkinter.ttk as ttk

# --------------------------------------------- VARIABLES AND CONSTANTS ------------------------------------------------
# username = os.environ['pixela_username']
graph_id = ""
# graph_id = "graph"

TOKEN = os.environ['pixela_token']
HEADER = {
    'X-USER-TOKEN': TOKEN
}


# ------------------------------------------------- FUNCTIONS ----------------------------------------------------------
def date_format():
    # TODO Get the current date
    # choice_date = datetime.now().date()

    # TODO Get the date from the calendar widget

    # TODO Convert the datetime module to a string
    choice_date_str = choice_date.strftime("%Y%m%d")
    return choice_date_str


# TODO Create new username
def create_username():
    global username, TOKEN
    pixela_endpoint = "https://pixe.la/v1/users"

    username_params = {}
    username_params = {
        'token': TOKEN,
        'username': username,
        'agreeTermsOfService': "yes",
        'notMinor': "yes"
    }

    response = requests.post(url=pixela_endpoint, json=username_params)
    # response.raise_for_status()
    print(response.text)

def create_user_window():

# def create_graph():
#     global graph_id, username
#     # TODO Prompt user to create a new graph
#     graph_id = simpledialog.askstring("", "Enter the Graph ID")
#     unit =
#
#     graph_params = {
#         'id': graph_id,
#         'name': "Cycling Graph",
#         'unit': "Km",
#         'type': "float",
#         'color': "shibafu",
#     }
#
#     pixela_graph_endpoint = f"https://pixe.la/v1/users/{username}/graphs"
#     response = requests.post(url=pixela_graph_endpoint, json=graph_params, headers=HEADER)
#     response.raise_for_status()
#     print(response.text)

def create_graph_window():
    # TODO Function called by create button
    def create_graph():
        # TODO Get the values of entry
        graph_id = graph_id_entry.get()
        graph_name = name_entry.get()
        units = unit_entry.get()

        # TODO Get the values from the radio buttons
        type_str = type_radiostate.get()
        colour_str = switch_variable.get()

        # TODO Make sure the graph parameters aren't empty
        # variable_dict = [{'value': "graph_id",'widget': "graph_id_entry"},
        #                  {'value': "graph_name", 'widget': "name_entry"},
        #                  {'value': "units", 'widget': "unit_entry"},
        #                  {'value': "type_str", 'widget': type_radiostate.get()},
        #                  {'value': "color", 'widget': "graph_id_entry"},
        #                  {'value': "graph_id", 'widget': "graph_id_entry"},
        #                  name_entry, unit_entry, type_radiostate, switch_variable]
        #
        # for variable in variable_list:
        #     value = variable.get()
        #     if value == "":
        #         messagebox.showerror(message=f"Please enter ")

        # TODO Store values in a dict
        graph_params = {}
        graph_params['id'] = graph_id
        graph_params['name'] = graph_name
        graph_params['unit'] = units
        graph_params['type'] = type_str
        graph_params['color'] = colour_str

        print(graph_params)

        # TODO Call API to create graph
        pixela_graph_endpoint = f"https://pixe.la/v1/users/{username}/graphs"
        response = requests.post(url=pixela_graph_endpoint, json=graph_params, headers=HEADER)
        response.raise_for_status()
        print(response.text)

    # TODO Configure window
    graph_window = Toplevel()
    graph_window.geometry('415x350')
    graph_window.title("Create a graph")
    graph_window.iconphoto(False, app_icon)
    graph_window.config(padx=20, pady=20)
    graph_window.transient(window)  # Popup reduction impossible
    # graph_window.grab_set()

    # TODO Create graph id frame
    graph_frame = ttk.Frame(graph_window)
    graph_frame.pack()

    graph_id_label = ttk.Label(graph_frame, text="Graph ID:")
    graph_id_label.config(padding=10)
    graph_id_label.pack(side="left")

    graph_id_entry = ttk.Entry(graph_frame)
    graph_id_entry.focus()
    graph_id_entry.pack(side="left")

    # TODO Create graph name frame
    name_frame = ttk.Frame(graph_window)
    name_frame.pack()

    name_label = ttk.Label(name_frame, text="Graph Label:")
    name_label.config(padding=10)
    name_label.pack(side="left")

    name_entry = ttk.Entry(name_frame)
    name_entry.pack(side="left")

    # TODO Create unit frame
    unit_frame = ttk.Frame(graph_window)
    unit_frame.pack()

    unit_label = ttk.Label(unit_frame, text="Units:")
    unit_label.config(padding=10)
    unit_label.pack(side="left")

    unit_entry = ttk.Entry(unit_frame)
    # unit_entry.insert(0, "commit, kilogram, calory, km etc")
    unit_entry.config(width=30)
    unit_entry.pack(side="left")

    # TODO Create a labelframe widget with radio buttons for type
    type_labelframe = LabelFrame(graph_window, text="Select the value type")
    type_labelframe.config(padx=50)
    type_labelframe.pack()

    # Variable to hold on to which radio button value is checked.
    type_radiostate = StringVar(value="float")
    float_radio_btn = ttk.Radiobutton(type_labelframe, text="Float", value="float", variable=type_radiostate)
    float_radio_btn.config(padding=10)
    int_radio_btn = ttk.Radiobutton(type_labelframe, text="Int", value="int", variable=type_radiostate)
    float_radio_btn.grid(row=0, column=1)
    int_radio_btn.grid(row=0, column=0)

    # TODO Create a labelframe for the graph colour
    pixel_colour_labelframe = LabelFrame(graph_window, text="Select the pixel colour")
    pixel_colour_labelframe.config(padx=50, pady=10)
    pixel_colour_labelframe.pack()

    switch_variable = StringVar()
    red_button = Radiobutton(pixel_colour_labelframe, variable=switch_variable,
                             indicatoron=False, value="momiji", width=3, bg="red", offrelief="flat")
    purple_button = Radiobutton(pixel_colour_labelframe, variable=switch_variable,
                                indicatoron=False, value="ajisai", width=3, bg="purple", offrelief="flat")
    green_button = Radiobutton(pixel_colour_labelframe, variable=switch_variable,
                               indicatoron=False, value="shibafu", width=3, bg="green", offrelief="flat")
    blue_button = Radiobutton(pixel_colour_labelframe, variable=switch_variable,
                              indicatoron=False, value="sora", width=3, bg="blue", offrelief="flat")
    black_button = Radiobutton(pixel_colour_labelframe, variable=switch_variable,
                               indicatoron=False, value="kuro", width=3, bg="black", offrelief="flat")
    yellow_button = Radiobutton(pixel_colour_labelframe, variable=switch_variable,
                                indicatoron=False, value="ichou", width=3, bg="yellow", offrelief="flat")

    red_button.pack(side="left")
    purple_button.pack(side="left")
    green_button.pack(side="left")
    blue_button.pack(side="left")
    black_button.pack(side="left")
    yellow_button.pack(side="left")

    # TODO Create "create" button
    create_frame = ttk.Frame(graph_window)
    create_frame.config(padding=10)
    create_frame.pack()

    create_btn = ttk.Button(create_frame, text="Create", style="Accentbutton", command=create_graph)
    create_btn.pack()


def post_pixel():
    # TODO Post a pixel
    pixela_pixel_endpoint = f"https://pixe.la/v1/users/{username}/graphs/{graph_id}"

    pixel_params = {
        'date': date_format(),
        'quantity': "8.3"  # Type string
    }

    response = requests.post(url=pixela_pixel_endpoint, json=pixel_params, headers=HEADER)
    response.raise_for_status()
    print(response.text)
    # https://pixe.la/v1/users/vincent2/graphs/graph.html


def update_entry():
    # TODO Updating an already existing pixel using PUT request
    date_str = date_format()
    pixela_put_endpoint = f"https://pixe.la/v1/users/{username}/graphs/{graph_id}/{date_str}"
    put_params = {
        'quantity': "9.0",
    }
    response = requests.put(url=pixela_put_endpoint, json=put_params, headers=HEADER)
    response.raise_for_status()
    print(response.text)


def delete_entry():
    # TODO Delete an entry
    pixela_delete_endpoint = f"https://pixe.la/v1/users/{username}/graphs/{graph_id}/{date_format()}"
    response = requests.delete(url=pixela_delete_endpoint, headers=HEADER)
    response.raise_for_status()
    print(response.text)


# -------------------------------------------------- UI ----------------------------------------------

# TODO Create window and set attributes
window = Tk()
window.title("Habit Tracker UI")

# TODO Create an icon
app_icon = PhotoImage(file="images/calendar_dark_512.png")
window.iconphoto(False, app_icon)
window.minsize(width=400, height=400)
# window.geometry("1080x460")
window.config(padx=20, pady=20)

# TODO Set window styling
style = ttk.Style(window)
window.tk.call('source',
               'C:/Users/Vin Muchiri/OneDrive/Python Programming/_packages/Azure-ttk-theme-main/azure/azure.tcl')
style.theme_use('azure')
style.configure("Accentbutton", foreground="white")

# TODO Add an entry
amount_entry = ttk.Entry()
amount_entry.grid(row=0, column=0)

# TODO Enter a calendar widget

# TODO Create buttons
add_btn = ttk.Button(text="Save Workout", style="Accentbutton")
add_btn.grid(row=2, column=0)

delete_button = ttk.Button(text="Delete Entry", style="Accentbutton")
delete_button.grid(row=2, column=1)

history_button = ttk.Button(text="History", style="Accentbutton")
history_button.grid(row=2, column=2)

window.mainloop()
