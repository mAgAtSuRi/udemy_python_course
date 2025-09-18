from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))


screen.listen()
screen.onkey(left_paddle.up, "z")
screen.onkey(left_paddle.down, "s")

screen.onkey(right_paddle.up, "i")
screen.onkey(right_paddle.down, "k")

game_is_on = True
while game_is_on:
	screen.update()
screen.exitonclick()