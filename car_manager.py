from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)    #random cars will be continuously genenrated making it impossible for turtle to move.hence to slow down the number of cars generated
        if random_chance == 1:  #limits the probability of generating cars to be 1/6
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2) #stretches the shape and size
            new_car.penup()     #doesn't draw while moving
            new_car.color(random.choice(COLORS))       #generates cars with random colors
            random_y = random.randint(-250, 250)    #generates y position for the car to travel constantly for diff x values, horizontally
            new_car.goto(300, random_y)             #goes to right extreme of screen
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:   #cars are initially to the right extreme
            car.backward(self.car_speed) #the cars have to move left, that is backwards

    def level_up(self):
        self.car_speed += MOVE_INCREMENT    #as level increases increase the car speed
