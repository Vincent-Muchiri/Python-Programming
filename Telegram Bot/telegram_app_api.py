from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
import configparser
from os import path

# TODO Create a config.ini file with the following:
# app_title, short_name, app_api_hash, app_api_id, phone_number, username
config = configparser.ConfigParser()
config.read('config.ini')
app_api_id = int(config.get('app_details', 'app_api_id'))
app_api_hash = config.get('app_details', 'app_api_hash')
username = config.get('user_details', 'username')
phone_no = config.get('user_details', 'phone_number')

# TODO Create a client
client = TelegramClient('session_name', api_id=app_api_id, api_hash=app_api_hash)
client.start()
print("Client Created")


# # Ensure you're authorized
# if not client.is_user_authorized():
#     client.send_code_request(phone_no)
#     try:
#         client.sign_in(phone_no, input('Enter the code: '))
#     except SessionPasswordNeededError:
#         client.sign_in(password=input('Password: '))

async def main():
    # Getting information about yourself
    me = await client.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    print(me.stringify())

    # When you print something, you see a representation of it.
    # You can access all attributes of Telegram objects with
    # the dot operator. For example, to get the username:
    my_username = me.username
    print(my_username)
    print(me.phone)

    # You can print the message history of any chat:
    async for message in client.iter_messages('me'):
        print(message.id, message.text)

with client:
    client.loop.run_until_complete(main())
