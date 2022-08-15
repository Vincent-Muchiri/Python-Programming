# import turtle

from turtle import Turtle, Screen #From the module import attribute(class)


#Draw turtle graphics
timmy = Turtle() #Object = attribute
timmy.shape("turtle")
timmy.color("DarkRed")
#Move turtle
timmy.forward(100)


#Create a screen
my_screen = Screen()
# print(my_screen.canvheight)
my_screen.title("#100 Days of Code: Day16 Turtle Graphics")
my_screen.exitonclick()

print(timmy)