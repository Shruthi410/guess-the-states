import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
score = 0

while len(guessed_states) < 50:

    guess = screen.textinput(title=f"{score}/50 States correct", prompt="Enter state: ").title()

    if guess == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break

    if guess in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == guess]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        guessed_states.append(guess)
        score += 1

