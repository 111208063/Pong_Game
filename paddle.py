from random import *
from turtle import *
import time

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        
        # 基本設置
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed(0)  # 最快的動畫速度
        
    def paddle1(self):
        """設置右側球拍（玩家1）"""
        self.goto(350, 0)
        self.color('cyan')  # 使用藍色標識玩家1
        
    def paddle2(self):
        """設置左側球拍（玩家2）"""
        self.goto(-350, 0)
        self.color('magenta')  # 使用洋紅色標識玩家2

    def up(self):
        """向上移動球拍"""
        # 添加邊界檢查
        if self.ycor() < 240:
            y = self.ycor() + 20
            self.goto(self.xcor(), y)
            
    def down(self):
        """向下移動球拍"""
        # 添加邊界檢查
        if self.ycor() > -240:
            x = self.ycor() - 20
            self.goto(self.xcor(), x)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        
        # 基本設置
        self.shape('circle')
        self.color('white')
        self.penup()
        self.speed(0)
        self.ball_size = 1.0  # 初始大小
        self.shapesize(self.ball_size, self.ball_size)
        
        # 球的軌跡效果
        self.trail_effect = False  # 是否顯示軌跡
        self.flash_count = 0  # 用於閃爍計數
        
        self.refresh()
        
    def refresh(self):
        """重置球的位置和速度"""
        self.goto(0, 0)
        self.xspeed = choice([10, -10])
        self.yspeed = choice([10, -10])
        
        # 當重新發球時，使用計時器而非sleep實現閃爍效果
        self.flash_count = 0
        self.start_flash()
        
    def start_flash(self):
        """開始閃爍效果，使用計時器代替sleep"""
        if self.flash_count < 6:  # 3次閃爍，共6次顏色變化
            if self.flash_count % 2 == 0:
                self.color('yellow')
            else:
                self.color('white')
            self.flash_count += 1
            # 使用計時器而非sleep
            self.getscreen().ontimer(self.start_flash, 100)

    def move(self):
        """移動球"""
        x = self.xcor() + self.xspeed
        y = self.ycor() + self.yspeed
        self.goto(x, y)
        
        # 隨著球的移動速度調整球的大小
        if abs(self.xspeed) > 15:
            self.shapesize(1.2, 1.2)
        else:
            self.shapesize(1.0, 1.0)

    def bounce(self):
        """從上下邊界反彈"""
        self.yspeed = -self.yspeed
        self.color('yellow')  # 反彈時變色
        # 恢復原色
        self.getscreen().ontimer(lambda: self.color('white'), 100)

    def hit(self):
        """從球拍反彈"""
        self.xspeed = -self.xspeed
        
        # 增加速度變化
        if abs(self.xspeed) < 20:
            if self.xspeed > 0:
                self.xspeed += 1
            else:
                self.xspeed -= 1
        
        self.color('orange')  # 擊中球拍時變色
        # 恢復原色
        self.getscreen().ontimer(lambda: self.color('white'), 100)




