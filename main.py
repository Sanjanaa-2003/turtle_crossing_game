import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)    #update method has to be present if this is there

player = Player()           #call these classes
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1) ##Delay execution for a given number of seconds. The argument may be a floating point number for subsecond precision.
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.all_cars:    #width=40 pixels; length=20 pixels
        if car.distance(player) < 20:   #if distance between middle of car and player is less than 20 then it is most likely the player collides
            game_is_on = False      #the game is over
            scoreboard.game_over()

    #Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()    #goes to start
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()
