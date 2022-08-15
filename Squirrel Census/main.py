# TODO Create a CSV file type of fur colours and the number
import pandas

# Angela's solution
data = pandas.read_csv("Squirrel Census Data.csv")
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
# print(grey_squirrel_count)
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
fur_colour_dict = {
    "Fur colour": ["Grey", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}
df = pandas.DataFrame(fur_colour_dict)
df.to_csv("Angela_squirrel_colour_data.csv")

########################################################################################################################
# TODO Open the CSV file
squirrel_pop_data = pandas.read_csv("Squirrel Census Data.csv")
# print(squirrel_pop_data)
# TODO Add the Primary Fur Color data into a list
raw_fur_colour_list = squirrel_pop_data["Primary Fur Color"].to_list()
# print(raw_fur_colour_list)

# TODO Remove repetition in the list
clean_fur_colour_list = []
for colour in raw_fur_colour_list:
    if clean_fur_colour_list.count(colour) == 0:
        clean_fur_colour_list.append(colour)

clean_fur_colour_list = clean_fur_colour_list[1:]
# print(clean_fur_colour_list)

# TODO Count the number of times the number of squirrel have the colours and add them into a list
fur_colour_num_list = []
for colours in clean_fur_colour_list:
    num_colour = raw_fur_colour_list.count(colours)
    # print(f"{colours} = {num_colour}")
    fur_colour_num_list.append(num_colour)
# print(fur_colour_num_list)

# TODO Add the colours and their corresponding number in a dictionary
colour_pop_dict = {}
colour_pop_dict["Colours"] = clean_fur_colour_list
colour_pop_dict["Total number"] = fur_colour_num_list
# print(colour_pop_dict)

# TODO Convert the dictionary into a Dataframe
colour_pop_dataframe = pandas.DataFrame(colour_pop_dict)
# print(colour_pop_dataframe)

# TODO Store the dictionary data into a new CSV file
colour_pop_dataframe.to_csv("squirrel_colour_data.csv")
