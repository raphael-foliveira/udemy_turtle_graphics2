from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed(0)


def move_forward():
    tim.forward(20)


def turn_left():
    tim.left(18)


def turn_right():
    tim.right(18)


def move_backward():
    tim.back(20)


def reset_canvas():
    tim.clear()
    tim.penup()
    tim.goto(0, 0)
    tim.pendown()


screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_right, "Right")
screen.onkey(turn_left, "Left")
screen.onkey(fun=reset_canvas, key="c")

screen.exitonclick()