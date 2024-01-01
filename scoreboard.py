from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):   #imports from the turtle class

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)    #displays level at the top left at this position
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()    #clears the screen
        self.write(f"Level: {self.level}", align="left", font=FONT)     #displays level of difficulty to the left

    def increase_level(self):
        self.level += 1     #increases the level by 1
        self.update_scoreboard() #calls the function and updates it

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
