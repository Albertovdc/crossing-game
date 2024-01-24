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

# Controls
screen.listen()
screen.onkey(player.move_up, "Up")

game_on = True
while game_on:
  screen.update()
  time.sleep(0.1)
  # Reset position when the turtle arrive the goal
  if player.ycor() > 280:
    player.respawn()
    scoreboard.level_up()
