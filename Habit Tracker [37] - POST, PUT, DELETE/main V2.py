import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
import requests
import os

# TOKEN = os.environ['pixela_token']
TOKEN = ""
HEADER = {
    'X-USER-TOKEN': TOKEN
}


def create_user_window():
    # global username, TOKEN
    # pixela_endpoint = "https://pixe.la/v1/users"
    #

    # TODO Enable submit button if the check buttons are checked
    def is_checked():
        if minor_btn_state.get() == "yes" and terms_btn_state.get() == "yes":
            create_btn['state'] = NORMAL

    def create_user():
        # TODO Get all the values
        token = token_entry.get()
        username = username_entry.get()
        terms = terms_btn_state.get()
        not_minor = minor_btn_state.get()

        # TODO Check whether all the entries are filled
        if token == "":
            token_entry.state(["invalid"])
            messagebox.showerror(message="Please enter the token id")
            token_entry.focus()
        elif username == "":
            username_entry.state(["invalid"])
            messagebox.showerror(message="Please enter the username")
            username_entry.focus()
        else:
            # TODO Save data in a dictionary
            username_params = {'token': token, 'username': username, 'agreeTermsOfService': terms,
                               'notMinor': not_minor}

            pixela_endpoint = "https://pixe.la/v1/users"

            # TODO Call the API
            try:
                response = requests.post(url=pixela_endpoint, json=username_params)
                response.raise_for_status()
                print(response.text)
            except:
                messagebox.showerror(message=response.text)
            else:
                # TODO If the API call was successful create graph
                bool_answer = messagebox.askyesno(message="User has been created successfully.\n"
                                                          "Do you wish to create a graph?")
                if bool_answer:
                    create_graph_window()

    # TODO Configure window
    user_window = Toplevel()
    user_window.minsize(width=400, height=200)
    user_window.title("Create a new user")
    user_window.iconphoto(False, app_icon)
    user_window.config(padx=20, pady=20)
    user_window.transient(window)

    # TODO Token
    token_frame = ttk.Frame(user_window)
    token_frame.pack()

    token_label = ttk.Label(token_frame, text="Token:")
    token_label.config(padding=10)
    token_label.pack(side="left")

    token_entry = ttk.Entry(token_frame)
    token_entry.focus()
    token_entry.pack(side="left")

    # TODO User name
    username_frame = ttk.Frame(user_window)
    username_frame.pack()

    username_label = ttk.Label(username_frame, text="Username:")
    username_label.config(padding=10)
    username_label.pack(side="left")

    username_entry = ttk.Entry(username_frame)
    username_entry.pack(side="left")

    # TODO not a minor
    minor_btn_state = StringVar()
    minor_button = ttk.Checkbutton(user_window, text="I'm not a minor", onvalue="yes", offvalue="no",
                                   variable=minor_btn_state, command=is_checked)
    minor_button.pack()

    # TODO Terms of service radio button
    terms_btn_state = StringVar()
    terms_button = ttk.Checkbutton(user_window, text="I've read and agreed to the terms of service", onvalue="yes",
                                   offvalue="no", variable=terms_btn_state, command=is_checked)
    terms_button.pack()

    create_btn = ttk.Button(user_window, text="Create Username", style="Accentbutton", state=DISABLED,
                            command=create_user)
    create_btn.pack()


def update_user_window():
    # ----------------------------------------------------- Functions --------------------------------------------------
    def update_user():
        # TODO Check whether entries are not empty
        if username_entry.get() == "":
            username_entry.state(["invalid"])
            username_entry.focus()
            messagebox.showerror(message="Please enter the username")
        elif auth_token_entry.get() == "":
            auth_token_entry.state(["invalid"])
            auth_token_entry.focus()
            messagebox.showerror(message="Please enter the username")
        else:
            # TODO Get the data from the entries
            username = username_entry.get()
            auth_token = auth_token_entry.get()

            # TODO Create endpoint URL and params
            url = f"https://pixe.la//v1/users/<{username}>"
            params = {
                'newToken': auth_token
            }

            # TODO Call the API
            try:
                response = requests.put(url=url, json=params, headers=HEADER)
                response.raise_for_status()
                # print(response.text)
            except:
                messagebox.showerror(message=response.text)
            else:
                messagebox.showinfo(message="User Details updated successfully!")

    # -------------------------------------------------------- UI ------------------------------------------------------
    # TODO Configure window
    update_user_pop_window = Toplevel()
    # update_user_window.minsize(width=400, height=200)
    update_user_pop_window.geometry("300x180")
    update_user_pop_window.title("Update details of an existing user")
    update_user_pop_window.iconphoto(False, app_icon)
    update_user_pop_window.config(padx=20, pady=20)
    update_user_pop_window.transient(window)

    # TODO Username window
    username_frame = ttk.Frame(update_user_pop_window)
    username_frame.pack()

    username_label = ttk.Label(username_frame, text="Username: ")
    # username_label.grid(row=0, column=0, padx=10)
    username_label.pack(side="left")

    username_entry = ttk.Entry(username_frame)
    username_entry.focus()
    username_entry.pack(side="right")

    # TODO Auth token frame
    auth_token_frame = ttk.Frame(update_user_pop_window)
    auth_token_frame.config(padding=20)
    auth_token_frame.pack()

    auth_token_label = ttk.Label(auth_token_frame, text="Auth Token: ")
    # username_label.grid(row=0, column=0, padx=10)
    auth_token_label.pack(side="left")

    auth_token_entry = ttk.Entry(auth_token_frame)
    auth_token_entry.pack(side="right")

    # TODO Create update button
    update_user_btn = ttk.Button(update_user_pop_window, style="Accentbutton", text="Update User", command=update_user)
    # update_user_btn.grid(row=1, column=0)
    update_user_btn.config(width=30)
    update_user_btn.pack()


def delete_user_window():
    # ------------------------------------------------- Functions -----------------------------------------------------
    def delete_user():
        pass

    # ----------------------------------------------------- GUI --------------------------------------------------------
    # TODO Setup window
    delete_user_pop_window = Toplevel()
    delete_user_pop_window.geometry("400x200")
    delete_user_pop_window.iconphoto(False, app_icon)
    delete_user_pop_window.title("Delete a user")
    delete_user_pop_window.transient(window)

    # TODO Username window
    username_frame = ttk.Frame(delete_user_pop_window)
    username_frame.pack()

    username_label = ttk.Label(username_frame, text="Username: ")
    # username_label.grid(row=0, column=0, padx=10)
    username_label.pack(side="left")

    username_entry = ttk.Entry(username_frame)
    username_entry.focus()
    username_entry.pack(side="right")

    # TODO Create update button
    delete_user_btn = ttk.Button(delete_user_pop_window, style="Accentbutton", text="Update User", command=delete_user)
    # update_user_btn.grid(row=1, column=0)
    delete_user_btn.config(width=30)
    delete_user_btn.pack(pady=20)


def create_graph_window():
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

        # print(graph_params)

        # TODO Call API to create graph
        # pixela_graph_endpoint = f"https://pixe.la/v1/users/{username}/graphs"
        # response = requests.post(url=pixela_graph_endpoint, json=graph_params, headers=HEADER)
        response_code = 200
        # response_code = response.status_code
        # print(response.text)

        # TODO Ask whether to create a graph if successful

    # TODO Configure window
    graph_window = Toplevel()
    graph_window.geometry('415x350')
    graph_window.title("Create a graph")
    # graph_window.iconphoto(False, app_icon)
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

    switch_variable = tk.StringVar()
    red_button = tk.Radiobutton(pixel_colour_labelframe, variable=switch_variable,
                                indicatoron=False, value="momiji", width=3, bg="red", offrelief="flat")
    purple_button = tk.Radiobutton(pixel_colour_labelframe, variable=switch_variable,
                                   indicatoron=False, value="ajisai", width=3, bg="purple", offrelief="flat")
    green_button = tk.Radiobutton(pixel_colour_labelframe, variable=switch_variable,
                                  indicatoron=False, value="shibafu", width=3, bg="green", offrelief="flat")
    blue_button = tk.Radiobutton(pixel_colour_labelframe, variable=switch_variable,
                                 indicatoron=False, value="sora", width=3, bg="blue", offrelief="flat")
    black_button = tk.Radiobutton(pixel_colour_labelframe, variable=switch_variable,
                                  indicatoron=False, value="kuro", width=3, bg="black", offrelief="flat")
    yellow_button = tk.Radiobutton(pixel_colour_labelframe, variable=switch_variable,
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


def update_graph_window():
    pass


def delete_graph_window():
    pass


def post_pixel_window():
    # --------------------------------------------------- Functions ----------------------------------------------------

    # ------------------------------------------------------ UI --------------------------------------------------------
    add_pixel = Toplevel()
    add_pixel.transient(window)
    add_pixel.title("Add a pixel")
    add_pixel.minsize(width=400, height=200)
    add_pixel.geometry("400x200")
    add_pixel.config(padx=20, pady=20)

    # TODO Date
    id_frame = ttk.Frame(add_pixel)
    id_frame.pack()

    pixel_id_label = ttk.Label(id_frame, text="ID:")
    pixel_id_label.config(padding=20)
    pixel_id_label.pack(side="left")

    pixel_id_entry = ttk.Entry(id_frame)
    pixel_id_entry.pack(side="left")

    # TODO Quantity
    pixel_name_frame = ttk.Frame(add_pixel)
    pixel_name_frame.pack()

    pixel_name_label = ttk.Label(pixel_name_frame, text="Pixel Name:")
    pixel_name_label.config(padding=20)
    pixel_name_label.pack(side="left")

    pixel_name_entry = ttk.Entry(pixel_name_frame)
    pixel_name_entry.pack(side="left")


def get_pixel_window():
    pass


def update_pixel_window():
    pass


def delete_pixel_window():
    pass


window = Tk()
# window.minsize(width=400, height=400)
window.title("Pixela API GUI")
window.geometry("400x360")
window.config(padx=20, pady=20)

# TODO Window icon
app_icon = PhotoImage(file="images/calendar_dark_512.png")
window.iconphoto(False, app_icon)

# TODO Set window styling
style = ttk.Style(window)
window.tk.call('source',
               'C:/Users/Vin Muchiri/OneDrive/Python Programming/_packages/Azure-ttk-theme-main/azure/azure.tcl')
style.theme_use('azure')
style.configure("Accentbutton", foreground="white")

# TODO User labelframe
user_labelframe = ttk.Labelframe(text="User")
user_labelframe.config(padding=10)
user_labelframe.pack(fill="both")

create_user_btn = ttk.Button(user_labelframe, text="Create user", style="Accentbutton", command=create_user_window)
create_user_btn.grid(row=0, column=0)

update_user_btn = ttk.Button(user_labelframe, text="Update user", style="Accentbutton", command=update_user_window)
update_user_btn.grid(row=0, column=1, padx=20)

delete_user_btn = ttk.Button(user_labelframe, text="Delete user", style="Accentbutton", command=delete_user_window)
delete_user_btn.grid(row=0, column=2)

# TODO User profile labelframe
user_profile_lf = ttk.Labelframe(text="User Profile")
user_profile_lf.config(padding=5)
user_profile_lf.pack(fill="both")

view_user_btn = ttk.Button(user_profile_lf, style="Accentbutton", text="View User Profile")
view_user_btn.config(width=20)
view_user_btn.pack(side="left", padx=5, pady=5)

update_user_btn = ttk.Button(user_profile_lf, style="Accentbutton", text="Update User Profile")
update_user_btn.config(width=20)
update_user_btn.pack(side="right", padx=5, pady=5)

# TODO Graph labelframe
graph_labelframe = ttk.Labelframe(text="Graph")
graph_labelframe.config(padding=10)
graph_labelframe.pack(fill="both")

create_graph_btn = ttk.Button(graph_labelframe, text="Create Graph", style="Accentbutton", command=create_graph_window)
create_graph_btn.grid(row=0, column=0)

update_graph_btn = ttk.Button(graph_labelframe, text="Update Graph", style="Accentbutton", command=update_graph_window)
update_graph_btn.grid(row=0, column=1, padx=10)

delete_graph_btn = ttk.Button(graph_labelframe, text="Delete Graph", style="Accentbutton", command=delete_graph_window)
delete_graph_btn.grid(row=0, column=2)

# TODO Pixel labelframe
pixel_labelframe = ttk.Labelframe(text="Pixel")
pixel_labelframe.pack(fill="both")

post_pixel_btn = ttk.Button(pixel_labelframe, style="Accentbutton", text="Post A Workout", command=post_pixel_window)
post_pixel_btn.grid(row=0, column=0)

get_pixel_btn = ttk.Button(pixel_labelframe, style="Accentbutton", text="Get Workout Data", command=get_pixel_window)
get_pixel_btn.grid(row=0, column=1)

update_pixel_btn = ttk.Button(pixel_labelframe, style="Accentbutton", text="Update Workout Data",
                              command=update_pixel_window)
update_pixel_btn.grid(row=1, column=0, padx=10, pady=10)

delete_pixel_btn = ttk.Button(pixel_labelframe, style="Accentbutton", text="Delete Workout Data",
                              command=delete_pixel_window)
delete_pixel_btn.grid(row=1, column=1, padx=10, pady=10)

window.mainloop()
