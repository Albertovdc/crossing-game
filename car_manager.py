import random
from turtle import Turtle

COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1


class CarManager:
  def __init__(self):
    self.cars = []
    # Using a variable with the starting speed
    self.car_speed = STARTING_MOVE_DISTANCE

  def create(self):
    self.num = random.randint(0,9)
    if self.num == 0:
      self.car = Turtle("square")
      self.car.shapesize(1, 2)
      self.car.setheading(180)
      self.car.color(random.choice(COLORS))
      self.car.penup()
      self.car.goto(290, random.randint(-250, 250))
      self.cars.append(self.car)

  def move(self):
    for car in self.cars:
      car.forward(self.car_speed)

  def increase_speed(self):
    # the variable modifies
    self.car_speed += MOVE_INCREMENT
