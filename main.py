from turtle import *
import time
from paddle import *
from scoreboard import *

# 設置遊戲屏幕
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong!!!')
screen.tracer(0)
screen.listen()

# 遊戲狀態
game_paused = False
game_on = True
ball_speed = 0.08  # 初始球速

# 創建中線
def draw_center_line():
    line = Turtle()
    line.color('white')
    line.penup()
    line.goto(0, 300)
    line.pendown()
    line.setheading(270)
    line.hideturtle()
    for _ in range(30):
        line.forward(10)
        line.penup()
        line.forward(10)
        line.pendown()

# 創建邊界
def draw_border():
    border = Turtle()
    border.hideturtle()
    border.penup()
    border.color('white')
    border.goto(-390, -290)
    border.pendown()
    for _ in range(2):
        border.forward(780)
        border.left(90)
        border.forward(580)
        border.left(90)

# 顯示遊戲標題
def draw_title():
    title = Turtle()
    title.color('yellow')
    title.penup()
    title.hideturtle()
    title.goto(0, 260)
    title.write("PONG GAME", align="center", font=("Arial", 24, "bold"))

# 顯示控制說明
def draw_controls():
    controls = Turtle()
    controls.color('white')
    controls.penup()
    controls.hideturtle()
    controls.goto(0, -260)
    controls.write("Player 1: ↑↓  Player 2: W/S  Pause: Space  Reset: R", align="center", font=("Arial", 14, "normal"))

# 創建暫停提示對象
pause_text = Turtle()
pause_text.color('red')
pause_text.penup()
pause_text.hideturtle()
pause_text.goto(0, 0)

# 暫停/恢復遊戲
def toggle_pause():
    global game_paused
    game_paused = not game_paused
    if game_paused:
        pause_text.clear()
        pause_text.write("GAME PAUSED", align="center", font=("Arial", 30, "bold"))
    else:
        pause_text.clear()

# 重置遊戲
def reset_game():
    global ball_speed
    scoreboard.l_score = 0
    scoreboard.r_score = 0
    scoreboard.update()
    ball.refresh()
    ball_speed = 0.08
    # 確保遊戲不處於暫停狀態
    global game_paused
    game_paused = False
    pause_text.clear()

# 初始化遊戲元素
draw_center_line()
draw_border()
draw_title()
draw_controls()
scoreboard = Scoreboard()
paddle1 = Paddle()
paddle1.paddle1()
paddle2 = Paddle()
paddle2.paddle2()
ball = Ball()

# 設置按鍵控制
screen.onkey(paddle1.up, 'Up')
screen.onkey(paddle2.up, 'w')
screen.onkey(paddle1.down, 'Down')
screen.onkey(paddle2.down, 's')
screen.onkey(toggle_pause, 'space')
screen.onkey(reset_game, 'r')

# 遊戲主循環
while game_on:
    if not game_paused:
        ball.move()
        
        # 球與上下邊界碰撞
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce()
        
        # 球與球拍碰撞
        if ball.distance(paddle1) < 50 and ball.xcor() > 335:
            ball.hit()
            # 每次擊中增加球速
            if ball_speed > 0.03:
                ball_speed *= 0.95
        
        if ball.distance(paddle2) < 50 and ball.xcor() < -335:
            ball.hit()
            # 每次擊中增加球速
            if ball_speed > 0.03:
                ball_speed *= 0.95
        
        # 計分
        if ball.xcor() > 380:
            ball.refresh()
            scoreboard.l_score += 1
            scoreboard.update()
            ball_speed = 0.08  # 重置球速
        
        if ball.xcor() < -380:
            ball.refresh()
            scoreboard.r_score += 1
            scoreboard.update()
            ball_speed = 0.08  # 重置球速
    
    screen.update()
    time.sleep(ball_speed)

screen.exitonclick()