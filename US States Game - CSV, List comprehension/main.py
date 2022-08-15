from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=725, height=491)
screen.title("US States Guessing Game")
screen.bgpic("blank_states_img.gif")
screen.tracer(0)




# TODO Create a dictionary for the state and their locations
import pandas
data_states = pandas.read_csv("50_states.csv")
states_list = data_states.state.to_list()

# print(data_states)

# TODO Initialization
tries = 50
points = 0
correct_guesses = []
remaining_states_dict = {}
remaining_states_list = states_list

guess = screen.textinput(title="Make a guess", prompt="Enter a state in US").title()
is_game_on = True
while is_game_on:
    screen.update()
    tries -= 1

    if guess == "Exit":
        break

    # for state in data_states.state:
    # if guess == state:
    # for state in states_list:


    if guess in states_list:
        correct_guesses.append(guess)

        # TODO Make a csv of missed states
        remaining_states_list.remove(guess)
        # print(len(remaining_states_list))
        remaining_states_dict["Missed States"] = remaining_states_list
        data = pandas.DataFrame(remaining_states_dict)
        data.to_csv("Missed States.csv")

        points += 1
        state_data = data_states[data_states.state == guess]
        # print(monday)
        x = int(state_data.x)
        y = int(state_data.y)
        # print(x, y)

        state = Turtle()
        state.penup()
        state.hideturtle()
        state.goto(x, y)
        state.write(f"{guess}", False, "Center", font=("Calibre", 8, "normal"))
        screen.update()

    if tries == 0:
        is_game_on = False
        game_over = Turtle()
        game_over.penup()
        game_over.hideturtle()
        game_over.goto(0, 0)
        game_over.write(f"Game Over! Score = {points}", False, "Center", font=("Courier", 20, "bold"))
        screen.update()

    guess = screen.textinput(title=f"{points}/50 States Correct", prompt=f"Enter a state in US.  Tries left: {tries}").title()
