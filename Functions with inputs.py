def greet(name, weather):
    print("Hi " +name+ "!. How are you?")
    print("Today is quite "+weather.lower() +", isn't it?")
    print

greet(weather = "sunny",name = "Vincent") #Keyword argument
greet("Vincent", "Sunny") #Positional argument