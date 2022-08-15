import requests

# TODO Request a response from the endpoint URL
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status() # Raise exceptions for the response code

# TODO Get the actual data
data = response.json()
position = data["iss_position"]
long_lat_tuple = (float(position["longitude"]), float(position["latitude"]))
print(long_lat_tuple)
