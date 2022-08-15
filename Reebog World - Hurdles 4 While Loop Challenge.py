def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    if is_facing_north() == True:
        print(right_is_clear())
        if right_is_clear() == True:
            
            turn_right()
            move()
            turn_right()
        else:
            move()

while not at_goal():
    if front_is_clear() == True:
        move()
    else:
        turn_left()
        jump()