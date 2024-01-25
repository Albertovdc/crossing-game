import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen set up
screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.title("Cross Game")

# Create the scoreboard
scoreboard = Scoreboard()

# Create turtle
player = Player()

# Cars
car_objects = []

# Controls
screen.listen()
screen.onkey(player.move_up, "Up")

game_on = True
while game_on:
  screen.update()
  time.sleep(0.1)
  car = CarManager()
  num = random.randint(0, 9)
  if num == 1:
    car.create()
    car_objects.append(car)

  for car in car_objects:
    car.move()

  # Reset position when the turtle arrive the goal
  if player.ycor() > 280:
    player.respawn()
    scoreboard.level_up()

  # TODO Make a collision with the cars
  for car in car_objects:
    if car.distance(player) < 22:
      game_on = False
screen.exitonclick()