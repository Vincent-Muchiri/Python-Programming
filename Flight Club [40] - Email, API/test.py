import requests


some_word = "users"
some_word = some_word.removesuffix("s")


response = requests.get(url="https://api.sheety.co/8d71f9dad050e97aca87b3b97e94d5d9/flightClubLesson40/users")
response.raise_for_status
print(response)