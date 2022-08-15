import smtplib
import datetime as dt

# SMTP Information, port number TLS, SSL
# Gmail = smtp.gmail.com, 587, 465
# Yahoo = smtp.mail.yahoo.com, 465
# Outlook = smtp-mail.outlook.com, 587

my_email = "tripiestands@gmail.com"
password = "Enter Password"

# TODO Create connection
with smtplib.SMTP("smtp.gmail.com") as connection:
    # TODO Encrypt connection
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="vincentmuchiri1@gmail.com",
                        msg="Subject: Python smtplib testing\n\n"
                            "#100DaysOfCode Day 32 Sending Email using Python smtplib.")
