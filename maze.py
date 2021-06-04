

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
        if right_is_clear():
            turn_right()
    elif right_is_clear():
        turn_right()
        if wall_on_right():
            turn_right()
    else:
        turn_left()