from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.7,stretch_len=0.7)
        self.penup()
        self.goto(0,-200)
        self.new_x = 10
        self.new_y = 10
        self.move_speed = 0.09

    def move(self):
        new_x = self.xcor() + self.new_x
        new_y = self.ycor() + self.new_y
        self.goto(new_x,new_y)
    def bounce_x(self):
        self.new_x *= -1
    def bounce_y(self):
        self.new_y *= -1
        self.move_speed *= 0.95
    def reset_postition(self):
        self.goto(0,-200)
        self.bounce_y()
        self.move_speed = 0.1
