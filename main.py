import turtle

#Screen setup
screen = turtle.Screen()
screen.title("U.S. States Quiz")
IMAGE = "./images/blank_states_img.gif"
screen.addshape(IMAGE) #Convert to a shape type
turtle.shape(IMAGE) #Use of the images as shape type

screen.exitonclick()