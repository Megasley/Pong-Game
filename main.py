from paddle import Paddle
from turtle import Screen, Turtle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

center_line = Turtle()
center_line.hideturtle()
center_line.penup()
center_line.sety(-300)
center_line.left(90)
center_line.color("white")


while center_line.ycor() < 300:
    center_line.pendown()
    center_line.forward(20)
    center_line.penup()
    center_line.forward(20)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_speed = 0.1

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # Detecting collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detecting collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detecting r_paddle miss
    if ball.xcor() > 400:
        ball.missed()
        scoreboard.l_point()

    # Detecting l_paddle miss
    if ball.xcor() < -400:
        ball.missed()
        scoreboard.r_point()

screen.exitonclick()
