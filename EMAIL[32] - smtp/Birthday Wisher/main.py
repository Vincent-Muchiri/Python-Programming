
import pandas
import datetime
import random
import smtplib

# --------------------------------------------- CONSTANTS AND VARIABLES ------------------------------------------------
MY_EMAIL = "tripiestands@gmail.com"
MY_PASSWORD = "F2i9lFnl8Wb0!C)"

recipient_letter = ""
recipient_email = ""

# TODO Read CSV data
birth_dates_df = pandas.read_csv("./birthdays.csv")

# for orientation in ("dict", "list", "series", "split", "records", "index"):
#     print(birth_dates_df.to_dict(orient=orientation))
#     print("")

birth_dates_dict = birth_dates_df.to_dict(orient="records")
# print(birth_dates_dict)

test_date = datetime.datetime(year=1997, month=9, day=11)

# TODO Loop through month and date in CSV and check whether the date matches
for birthday_data in birth_dates_dict:
    if birthday_data["month"] == test_date.month and birthday_data["day"] == test_date.day:
        # TODO Get the name of the recipient and email address
        recipient_name = birthday_data["name"]
        recipient_email = birthday_data["email"]

        # TODO Open the text a random text file
        template_letter = f"./letter_templates/letter_{random.randint(1, 3)}.txt"

        with open(template_letter, mode="r") as letter:
            # letter_contents = letter.readlines() Using readlines() outputs a list with each line as an elem.
            # This makes it harder to send the letter
            letter_contents = letter.read() # Outputs a string

        # TODO Replace the [NAME] with the recipient's name and save it to a separate file
        letter_contents = letter_contents.replace("[NAME]", recipient_name)

        # TODO Generate a recipient letter
        recipient_letter = f"{recipient_name}_birthday_letter.txt"

        # TODO Send the email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=recipient_email,
                msg=f"Subject:Happy Birthday {recipient_name}\n\n"
                    f"{letter_contents}"
            )
