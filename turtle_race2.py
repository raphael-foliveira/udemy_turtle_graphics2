from turtle import Turtle, Screen
from random import randint


HEIGHT = 400
WIDTH = 600


screen = Screen()
screen.setup(height=HEIGHT, width=WIDTH)
colors_list = ["Red", "Green", "Purple", "Blue", "Brown", "Black"]
racing_turtles = [Turtle(shape="turtle") for color in colors_list]
turtle_colors = zip(colors_list, racing_turtles)
turtle_grid_pos = -130

for i in range(len(racing_turtles)):
    racing_turtles[i].penup()
    racing_turtles[i].color(colors_list[i])
    racing_turtles[i].speed(0)
    racing_turtles[i].setpos(x=-250, y=turtle_grid_pos)
    turtle_grid_pos += 50


user_bet = screen.textinput(title="Place your bet!", prompt="Red, Green, Purple, Blue, Brown")
winner = None
keep_racing = True

while keep_racing:
    for turtle in racing_turtles:
        turtle.forward(randint(0, 50))
        if turtle.xcor() >= 250:
            keep_racing = False
            winner = turtle.pencolor()

if winner == user_bet:
    print("You win!")
else:
    print("You lose!")

screen.exitonclick()
