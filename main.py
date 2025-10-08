import turtle
import pandas

#Screen setup
screen = turtle.Screen()
screen.title("U.S. States Quiz")
IMAGE = "./images/blank_states_img.gif"
screen.addshape(IMAGE) #Convert to a shape type
turtle.shape(IMAGE) #Use of the images as shape type

#Mausklick-Koordinaten erhalten
def get_mouse_click_coor(x,y):
    print(x,y)
turtle.onscreenclick(get_mouse_click_coor)

#Game setup
guessed_states = []

while len(guessed_states) < 50:
    #User Input
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State",
                                    prompt="What´s another state´s name?").title()
    print(answer_state)
    #Check user answer, get coordinates
    data = pandas.read_csv("./data/50_states.csv")
    state_list = data["state"].to_list()

    for state in state_list:
        if answer_state == state:

            #Create turtle to write name of the state
            t = turtle.Turtle()
            t.hideturtle()
            t.up()
            state_row = data[data.state == answer_state]
            t.goto(state_row.x.item(), state_row.y.item())
            t.write(f"{state}")
            if answer_state not in guessed_states:
                guessed_states.append(state)

turtle.mainloop() #alternative way to keep screen open
screen.exitonclick()