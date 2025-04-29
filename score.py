from turtle import Turtle

X = 0
Y = 500
ALIGN = "center"
FONT = ("arial", 16)
S_COLOR = "white"
SPEED = "fastest"
TEXT = "GAME OVER"

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.text = None
        self.count = 0
        self.penup()
        self.color(S_COLOR)
        self.hideturtle()
        self.goto(X, Y)
        self.speed(SPEED)
        self.refresh()

    def refresh(self):
        self.text = f"Score: {self.count}"
        self.write(self.text, False, ALIGN, FONT)

    def update(self):
        self.count += 1
        self.clear()
        self.refresh()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(TEXT, align=ALIGN, font=FONT)

