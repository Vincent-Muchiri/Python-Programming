import pandas

data_frame = pandas.read_csv("parts.csv")
print(data_frame)

parts_dict = data_frame.to_dict(orient="list")

print(parts_dict)

id = 217637431667813
part = input("Part: ")
customer = input("Customer: ")
retailer = input("Retailer: ")
price = float(input("Price: "))

new_row_dict = {
    "ID": [id],
    "Part": [part],
    "Customer": [customer],
    "Retailer": [retailer],
    "Price": [price]
}

print(new_row_dict)

new_row_df = pandas.DataFrame(new_row_dict)
new_row_df.to_csv("parts.csv", mode="a", index=True, header=False)
