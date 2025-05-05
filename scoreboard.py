from turtle import *

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        
        # 創建玩家標籤
        self.player_labels()
        self.update()
        
    def player_labels(self):
        """顯示玩家1和玩家2的標籤"""
        self.goto(-100, 230)
        self.write("PLAYER 1", align='center', font=('Arial', 16, 'bold'))
        self.goto(100, 230)
        self.write("PLAYER 2", align='center', font=('Arial', 16, 'bold'))
        
    def update(self):
        """更新玩家分數顯示"""
        # 清除之前的分數但保留標籤
        self.clear()
        self.player_labels()
        
        # 玩家1分數
        self.goto(-100, 180)
        self.write(self.l_score, align='center', font=('Courier', 60, 'bold'))
        
        # 玩家2分數
        self.goto(100, 180)
        self.write(self.r_score, align='center', font=('Courier', 60, 'bold'))
        
        # 當有玩家達到一定分數時顯示獲勝信息
        if self.l_score >= 5 or self.r_score >= 5:
            self.show_winner()
            
    def show_winner(self):
        """顯示獲勝玩家"""
        self.goto(0, 0)
        if self.l_score >= 5:
            self.color('yellow')
            self.write("PLAYER 1 WINS!", align='center', font=('Arial', 30, 'bold'))
        elif self.r_score >= 5:
            self.color('yellow')
            self.write("PLAYER 2 WINS!", align='center', font=('Arial', 30, 'bold'))