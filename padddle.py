import turtle as t
from time import sleep
from border import X, Y

PADDLE_COLOR = "white"
STARTER_BODY = 3
BODY_SIZE = 10
DISTANCE = BODY_SIZE * 5
DIRECTION = [90, 270]
SPEED = 0.05
SHAPE = "square"
SIZE = "auto"
PADDLE_DIRECTION = "up"
MV = "fastest"


class Paddle:


    def __init__(self, screen, side, auto=False):
        self.screen = screen
        self.paddle_body = []
        for i in range(STARTER_BODY):
            self.create_body()
        self.set_paddle(side)
        self.direction = PADDLE_DIRECTION
        self.paddle_body[0].seth(DIRECTION[1])
        self.paddle_body[2].seth(DIRECTION[0])
        self.auto = auto


    def set_paddle(self, side):
        """Creates paddle on the right or left of the screen"""

        i = 0
        sequence = [-1, 0, 1]
        for part in self.paddle_body:
            adjusted_distance = DISTANCE * sequence[i]
            if side == "right":
                x_paddle = X[1] - DISTANCE
            else:
                x_paddle = X[0] + DISTANCE
            y_paddle = 0 + adjusted_distance
            i += 1
            part.teleport(x_paddle, y_paddle)

    def create_body(self):
        bit = t.Turtle()
        bit.shape(SHAPE)
        bit.pencolor(PADDLE_COLOR)
        bit.penup()
        bit.pensize(BODY_SIZE)
        bit.resizemode(SIZE)
        bit.speed(MV)
        self.paddle_body.append(bit)

    def turn_up(self):
        self.direction = "up"

    def turn_down(self):
        self.direction = "down"

    def turn_direction(self):

        self.screen.onkey(key="k", fun=self.turn_up)
        self.screen.onkey(key="w", fun=self.turn_up)
        self.screen.onkey(key="s", fun=self.turn_down)
        self.screen.onkey(key="j", fun=self.turn_down)

        self.screen.listen()

    def move(self):

        if not self.auto:
            self.turn_direction()
        previous_position = None

        if self.in_border():
            if self.direction == "down" and self.auto:
                self.direction = "up"
            elif self.direction == "up" and self.auto:
                self.direction = "down"
            else:
                return None

        if self.direction == "down":
            beginning = 0
            final = len(self.paddle_body)
            for i in range(beginning, final):
                sleep(SPEED)
                current_part = self.paddle_body[i]
                if i == beginning:
                    previous_position = current_part.pos()
                    current_part.fd(DISTANCE)
                else:
                    current_position = current_part.pos()
                    current_part.goto(previous_position)
                    previous_position = current_position
        else:
            beginning = len(self.paddle_body) - 1
            final = -1
            for i in range(beginning, final, -1):
                sleep(SPEED)
                current_part = self.paddle_body[i]
                if i == beginning:
                    previous_position = current_part.pos()
                    current_part.fd(DISTANCE)
                else:
                    current_position = current_part.pos()
                    current_part.goto(previous_position)
                    previous_position = current_position

    def get_position(self):
        pos = []
        for i in self.paddle_body:
            pos.append(i.pos())
        return pos


    def in_border(self):
       positions = self.get_position()

       if self.direction == "up":
           limit = positions[2][1] + DISTANCE
           return limit == Y[1]
       elif self.direction == "down":
           limit = positions[0][1] - DISTANCE
           return limit == Y[0]
