import smtplib

# Due to removal of "Allow Less Secure Apps" by Google's gmail, this piece of code won't work try the solution in the
# link https://stackoverflow.com/questions/73026671/how-do-i-now-since-june-2022-send-an-email-via-gmail-using-a-python-script

# SMTP Information, port number TLS, SSL
# Gmail = smtp.gmail.com, 587, 465
# Yahoo = smtp.mail.yahoo.com, 465
# Outlook = smtp-mail.outlook.com, 587

my_email = "appdevemail.test@gmail.com"
password = "luopwtibvkbjwhvq"
#
# # TODO Create connection
with smtplib.SMTP("smtp.gmail.com", 465) as connection:
    print("Encrypting ...")
    # TODO Encrypt connection
    connection.starttls()
    print("Login you in...")
    connection.login(user=my_email, password=password)
    print("Sending the email...")
    connection.sendmail(from_addr=my_email,
                        to_addrs="appdevemail.test@yahoo.com",
                        msg="Subject: Python smtplib testing\n\n"
                            "#100DaysOfCode Day 32 Sending Email using Python smtplib.")
