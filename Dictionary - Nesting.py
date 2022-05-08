#Nesting a list in a dictoinary
travel_log = {
    "Kenya" : ["Nairobi", "Mombasa", "Kisumu"],
    "South Africa": ["Durban", "Joburg", "Cape Town"]
}

#Nesting a dictionary inside another dictionary
cities_visited = {
    "Kenya": "Naivasha",
    "South Africa": "Pritoria"
}
travel_log = {
    "Kenya" : ["Nairobi", "Mombasa", "Kisumu"],
    "South Africa": ["Durban", "Joburg", "Cape Town"],
    "cities_visited" : cities_visited
}

# print(travel_log)

#Nesting a dictionary inside a list
travel_log = [
    {
        "country" : "Kenya",
        "cities_visited" : ["Nairobi", "Mombasa", "Kisumu"],
        "no_of_visits" : 12
    },
    {
        "country": "South Africa",
        "cities_visited": ["Durban", "Joburg", "Cape Town"],
        "no_of_visits" : 12
    }
]

#Adding new entries
def add_new_country (country, times_visited, cities_visited): 
    new_country = {}
    new_country["country"] = country
    new_country["cities_visited"] = cities_visited
    new_country["no_of_visits"] = times_visited
    
    # travel_log.append(new_country)
    travel_log[-1] = new_country


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
# print(travel_log[0]["country"])