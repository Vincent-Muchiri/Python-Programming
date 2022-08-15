from shutil import move


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() == False:
    move()
    jump()

# while not at_goal(): #while not true
#     move()
#     jump()