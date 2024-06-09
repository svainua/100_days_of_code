import turtle
import pandas
FONT = ("Courier", 10, "italic")


screen = turtle.Screen()
screen.title("US States Game")
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
screen.bgpic(image)
# screen.addshape(image)
# turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = (screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another State's name?")).title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]

        df = pandas.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")   
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(f"{answer_state}", font=FONT, align="center")
        
     


# data = pandas.read_csv("50_states.csv")
# states = list(data.state)
# guesses = 0
# correct_answers = []

# should_continue = True
# while should_continue:
#     if answer_state in states:
#         turtle.hideturtle()
#         turtle.penup()
#         coordinates = data[data.state == answer_state]
#         x = int(coordinates.x)
#         y = int(coordinates.y)
#         turtle.goto(x=x, y=y)
#         turtle.write(f"{answer_state}", font=FONT, align="center")
#         guesses += 1
#         correct_answers.append(answer_state)
#         answer_state = (screen.textinput(title=f"{guesses}/50 States Correct", prompt="What's another State's name?")).title()






