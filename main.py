import time
from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from block_manager import BlockManger
screen = Screen()
screen.title("Breakou Game")
screen.bgcolor("skyblue")
screen.setup(width=500,height=600)
screen.tracer(0)

paddle = Paddle()
block_manager = BlockManger()
ball = Ball()
scoreboard = ScoreBoard()

ball.speed(10)

screen.listen()
screen.onkey(paddle.go_right,"Right")
screen.onkey(paddle.go_left,"Left")

game_continue = True
while game_continue:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with side walls
    if ball.xcor() > 220 or ball.xcor() < -230:
        ball.bounce_x()
    # Detect collision with up wall
    if ball.ycor() > 280:
        ball.bounce_y()
    # Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -227:
        ball.bounce_y()
    # Detect paddle misses
    if ball.ycor() < -300:
        ball.reset_postition()
        scoreboard.lose_life()
    # Detect collision with blocks
    for block in block_manager.all_blocks:
        if ball.distance(block) < 33:
            ball.bounce_y()
            block_manager.remove_blocks(block)
            scoreboard.give_score()
    #playyer won by destroying all blocks
    if scoreboard.score == 27:
        scoreboard.win()
        game_continue = False
    # playyer lose by losing all life
    if scoreboard.lives < 1:
        scoreboard.lose()
        game_continue = False
screen.exitonclick()