import turtle
import pandas
FONT = ("Arial", 16, "normal")
ALIGNMENT = 'center'

# Create screen with image fon
screen = turtle.Screen()
screen.setup(width=750, height=500)
screen.title("USA states game")
image = "fon.gif"
screen.addshape(image)
turtle_image = turtle.Turtle()
turtle_image.shape(image)


# def get_mouse_coor(x, y):
#     print(x, y)
#
# turtle.onclick(get_mouse_coor)

# Read and Convert data to dict of states
data = pandas.read_csv("50_states.csv")
data_dict = data.to_dict(orient='records')
all_states = []

for data in data_dict:
    # print(data)
    state = data["state"]
    x = data['x']
    y = data['y']
    all_states.append({state: (x, y)})

# print(all_states)

# Game loop
while len(all_states) > 0:
    # Ask user about states
    user_input = screen.textinput(title="Your Guess", prompt="What's state?").title()

    # Exit procedure with printing all missing states
    if user_input == "Exit":
        missing_states = []
        for state in all_states:
            key_string = list(state.keys())[0]
            missing_states.append(key_string)
        print(missing_states)
        break

    # Draw state if it's right
    for state in all_states:
        if user_input in state:
            # Draw state on the map
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(state[user_input])
            t.write(user_input)
            # Remove guessed state from a list
            all_states.remove(state)

screen.mainloop()
