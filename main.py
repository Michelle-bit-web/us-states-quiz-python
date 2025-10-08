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

game_over = False

while not game_over:
    #User Input
    answer_state = screen.textinput(title="Guess the State",  prompt="What´s another state´s name?")

    #Check user answer, get coordinates
    data = pandas.read_csv("./data/50_states.csv")
    state_list = data["state"].to_list()
    for state in state_list:

        if answer_state == state:
            found_row = data[data.state == answer_state]
            print(f"State found: {answer_state}.")
            #create turtle to write name of the state
        else:
            print("This is no U.S. state.")

    turtle.mainloop() #alternative way to keep screen open