#Reeborg's World
# https://reeborg.ca/

#code for hurdle section
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    move()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()

# Maze Code
def in_open_space():
    if right_is_clear() and front_is_clear():
        turn_left()
        turn_left()
        if right_is_clear() and front_is_clear():
            turn_left()
            turn_left()
            return True
        else:
            turn_left()
            turn_left()
    return False

while not at_goal():
    if in_open_space():
        move()
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()