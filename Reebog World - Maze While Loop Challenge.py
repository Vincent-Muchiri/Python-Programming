def turn_right():
    turn_left()
    turn_left()
    turn_left

while not at_goal():
    if front_is_clea():
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()
    elif wall_in_front():
        turn_right()