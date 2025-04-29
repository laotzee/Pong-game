from turtle import Turtle
from padddle import BODY_SIZE, SPEED, DISTANCE
from border import X, Y, BORDER_SIZE
from random import choice, randint

BODY_SIZE = BODY_SIZE

ANGLES = []
ANGLES.extend(list(range(120, 241)))
ANGLES.extend(list(range(60, 0, -1)))
ANGLES.extend(list(range(300, 360)))
offby = [2, -2]
#ANGLES = [180]
SHAPE = "circle"
COLOR = "red"
SIZE = "auto"
MV = "fastest"


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.pencolor(COLOR)
        self.penup()
        self.pensize(BODY_SIZE)
        self.resizemode(SIZE)
        self.speed(SPEED)
        self.seth(choice(ANGLES))

    def move(self):
        self.fd(DISTANCE)

    def wall_collision(self):

        if self.ycor() - DISTANCE <= Y[0] or self.ycor() + DISTANCE >= Y[1]: # Floor
            new_heading = 360 - self.heading()
            self.seth(new_heading)
            print(self.heading())
            self.move()
            return True
        else:
            return False
    def out_of_bounds(self):
        if self.xcor() >= X[1] or self.xcor() <= X[0]:
            return True



    def on_collision(self, paddle_pos):
        off = choice(offby)

        for pos in paddle_pos:
            if self.distance(pos) < 30:
                print("COLLISIONNN")
                self.seth(180 - off - self.heading())
                self.move()








