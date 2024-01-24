import random
from turtle import Turtle

COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
  def __init__(self):
    super().__init__()
    self.setheading(180)
    self.penup()
    self.shape("square")
    self.shapesize(stretch_wid=1, stretch_len=2)
    self.color(random.choice(COLORS))
    self.goto(280, random.randint(-270, 270))

  def move(self):
    self.forward(STARTING_MOVE_DISTANCE)
