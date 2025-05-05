from turtle import *
import time
from paddle import *
from scoreboard import *

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong!!!')
game_on = True
screen.listen()
screen.tracer(0)
scoreboard = Scoreboard()
paddle1 = Paddle()
paddle1.paddle1()
paddle2 = Paddle()
paddle2.paddle2()
ball = Ball()
screen.onkey(paddle1.up, 'Up')
screen.onkey(paddle2.up, 'w')
screen.onkey(paddle1.down, 'Down')
screen.onkey(paddle2.down, 's')


while game_on:
    ball.move()
    screen.update()
    time.sleep(0.1)
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()
    if ball.distance(paddle1) < 50 and ball.xcor()>335:
        ball.hit()
    if ball.distance(paddle2) < 50 and ball.xcor()<-335:
        ball.hit()
    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.l_score += 1
        scoreboard.update()
    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.r_score += 1
        scoreboard.update()







screen.update()








screen.exitonclick()