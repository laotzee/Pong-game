from turtle import Turtle

WIDTH = 1600
HEIGHT = 1000
BORDER_SIZE = 10
SIZE_MODE = "auto"
MV = "fastest"
LINE_H = 40
BORDER_COLOR = "white"
X = (-WIDTH/2, WIDTH/2)
Y = (-HEIGHT/2, HEIGHT/2)

START_X = X[0]
START_Y = Y[0]


class Border(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pensize(BORDER_SIZE)
        self.resizemode(SIZE_MODE)
        self.speed(MV)
        self.color(BORDER_COLOR)
        self.penup()
        self.goto(START_X, START_Y)
        self.draw_border()
        self.draw_division()

    def draw_border(self):
        self.pendown()
        for i in range(2):
           self.fd(WIDTH)
           self.left(90)
           self.fd(HEIGHT)
           self.left(90)

    def draw_division(self):
        self.fd(X[1])
        self.left(90)
        for i in range(0, HEIGHT, LINE_H):
            if self.isdown():
                self.penup()
            else:
                self.pendown()
            self.fd(LINE_H)

