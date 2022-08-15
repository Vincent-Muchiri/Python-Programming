from datetime import datetime

current_date = datetime.now().date().weekday()

recent_date = datetime(year=2022, month=2, day=4)
# print(recent_date)

dict = {
    "One": 1,
    "2": 2
}

print(list(dict.keys())[0])