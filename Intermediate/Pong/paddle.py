from turtle import Turtle


class Paddle(Turtle):
	def __init__(self, coord):
		super().__init__()
		self.paddle = Turtle()
		self.paddle.color("white")
		self.paddle.shape("square")
		self.paddle.penup()
		self.paddle.shapesize(5, 1)
		self.paddle.goto(coord)
	
	def up(self):
		new_coord = (self.paddle.xcor(), self.paddle.ycor() + 20)
		self.paddle.goto(new_coord)

	def down(self):
		new_coord = (self.paddle.xcor(), self.paddle.ycor() - 20)
		self.paddle.goto(new_coord)