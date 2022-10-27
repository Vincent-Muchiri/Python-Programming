import smtplib
my_email = "tripiestands@gmail.com"
password = "vtfiffsqycfppuop"

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
# with smtplib.SMTP("smtp.gmail.com", port=465) as connection:
with smtplib.SMTP("smtp.gmail.com") as connection:
    # TODO Encrypt connection
    connection.starttls()
    connection.login(user="Python Code", password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="vincentmuchiri1@gmail.com",
                        msg=f"Subject: This is a test\n\n"
                            f"Python says hello world.")
    print("Email sent successfully!")
