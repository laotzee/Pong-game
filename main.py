from time import sleep

import border as b
import turtle as t
import padddle as p
import ball as bl

screen = t.Screen()
screen.bgcolor("black")
user_paddle = p.Paddle(screen, "left")
machine_paddle = p.Paddle(screen, "right", auto=True)
border = b.Border()
ball = bl.Ball()
game_on = True
screen.tracer(0)

while game_on:
    screen.update()

    user_paddle.move()
    machine_paddle.move()
    if not ball.wall_collision():
        ball.move()

    ball.on_collision(user_paddle.get_position())

    if ball.out_of_bounds():
        game_on = False



# Improve collision with the other paddle

print("game over")
screen.exitonclick()