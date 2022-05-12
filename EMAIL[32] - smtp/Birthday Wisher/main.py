
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
birthdates_df = pandas.read_csv("birthdays.csv")

# for orientation in ("dict", "list", "series", "split", "records", "index"):
#     print(birthdates_df.to_dict(orient=orientation))
#     print("")

birthdates_dict = birthdates_df.to_dict(orient="records")
# print(birthdates_dict)

test_date = datetime.datetime(year=1973, month=6, day=14)

# TODO Loop through month and date in CSV and check whether the date matches
for birthday_data in birthdates_dict:
    if birthday_data["month"] == test_date.month and birthday_data["day"] == test_date.day:
        # TODO Open the text a random text file
        template_letter = f"./letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(template_letter, mode="r") as letter:
            letter_contents = letter.readlines()
            # print(letter_contents)

        # TODO Generate a recipient letter
        recipient_letter = f"{birthday_data['name']}_birthday_letter.txt"
        # print(recipient_letter)

        # TODO Remove empty lines
        # for line in letter_contents:
        #     if line == '\n':
        #         letter_contents.remove(line)
        # print(letter_contents)
        # TODO Replace the [NAME] with the recipient's name and save it to a separate file
        letter_contents[0] = f"Hey {birthday_data['name']},\n"
        # print(letter_contents)

        # TODO Add the data in the list to a file
        with open(f"./sent_letters/{recipient_letter}", mode="w") as birthday_letter:
            for line in letter_contents:
                birthday_letter.write(line)

        # TODO Get the email address
        recipient_email = birthday_data["email"]

        # TODO Send the email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(to_addrs=recipient_email,
                                from_addr=MY_EMAIL,
                                msg=f"Subject:Happy Birthday {birthday_data['name']}\n\n"
                                    f"{letter_contents}")
