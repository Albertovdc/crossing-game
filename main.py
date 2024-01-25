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


car = CarManager()
# Create turtle
player = Player()

# Controls
screen.listen()
screen.onkey(player.move_up, "Up")

game_on = True
while game_on:
  screen.update()
  time.sleep(0.1)

  car.create()
  car.move()

  for item in car.cars:
     if item.distance(player) < 20:
      game_on = False
      scoreboard.game_over()

  if player.ycor() > 270:
    player.respawn()
    scoreboard.level_up()
    car.increase_speed()

screen.exitonclick()
