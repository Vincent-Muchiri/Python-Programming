from twilio.rest import Client
import os

TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
TWILIO_ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_FROM_PHONE_NO = os.environ["TWILIO_FROM_PHONE_NO"]
TWILIO_TO_PHONE_NO = os.environ["TWILIO_TO_PHONE_NO"]


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""

    def send_message(self, message_list: list):

        for message_contents in message_list:
            # print(message_contents)
            client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

            # TODO Send message
            try:
                message = client.messages.create(
                    body=message_contents,
                    from_=TWILIO_FROM_PHONE_NO,
                    to=TWILIO_TO_PHONE_NO)
            except:
                print("Message failed to send")
            else:
                print("Message successfully sent!")
                # print(message.sid)
