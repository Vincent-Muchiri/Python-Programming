import pandas, os

example_dict = {'curr': 'USD', 'price_to': 1200, 'date_from': '29/08/2022', 'date_to': '30/08/2022', 'max_stopovers': 1, 'flight_type': 'round', 'nights_in_dst_from': 1, 'nights_in_dst_to': 1, 'fly_from': 'NBO', 'fly_to': 'LON'}
data_dict_2 = {
    'student': ["Vincent", "Diana"],
    'score': [90, 92],
    'curr': 'USD', 'price_to': 1200
}

selected_header = True
search_params_dataframe = pandas.DataFrame(example_dict, index=[0])
if os.path.exists("data/test.csv"):
    selected_header = False

search_params_dataframe.to_csv("data/test.csv", mode="a", header=selected_header)
