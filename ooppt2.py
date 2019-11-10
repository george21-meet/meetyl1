import turtle
from turtle import Turtle
a=0
class Ball(Turtle):
	def __init__(self,r,colour,dx,dy):
		Turtle.__init__(self)
		self.penup()
		self.r=r
		self.colour=colour
		self.dx=dx
		self.dy=dy
		self.shape("circle")
		self.color(colour)
		self.turtlesize(r/10)
	def move(self,screen_width,screen_length):
		current_x=self.xcor()
		new_x=current_x+self.dx
		current_y=self.ycor()
		new_y=current_y+self.dy
		right_side_ball=new_x+self.r
		left_side_ball=new_x-self.r
		top_side_ball=new_y+self.r
		down_side_ball=new_y-self.r
		self.goto(new_x,new_y)
		if right_side_ball>=screen_width and left_side_ball<=screen_width:
			self.dx=self.dx*-1/10
			for i in range(10):
				self.goto(self.dx/10,self.dy*-1)
		"""
		if left_side_ball<=screen_width:
			print("test")
			self.dx=self.dx*-1
			for i in range(10):
				self.goto(self.dx/10,self.dy*-1)
		"""

		if top_side_ball>=screen_length and down_side_ball<=screen_length:
			self.dy=self.dy*-1
			for i in range(10):
				self.goto(self.dx*-1,self.dy/10)
		"""
		if down_side_ball<=screen_length:
			self.dy=self.dy*-1
			for i in range(10):
				self.goto(self.dx*-1,self.dy/10)
		"""
		screen_width=turtle.getcanvas().winfo_width()/2
		screen_length=turtle.getcanvas().winfo_height()/2
for i in range(3):
	balla=Ball(10,"black",500,500)
	balla.move(500,1000)