from turtle import Turtle

FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.level = 0
    self.hideturtle()
    self.penup()
    self.goto(0, 270)
    self.color("black")
    self.update()

  def update(self):
    self.write(f"Level {self.level}", align="center", font=FONT)

  def level_up(self):
    self.clear()
    self.level += 1
    self.update()


