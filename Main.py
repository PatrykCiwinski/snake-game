import turtle
from turtle import *
import time
from snake import *
from food import *
from scoreboard import Scoreboard

my_screen=turtle.Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.tracer(0)
snake=Snake()
food=Food()
scoreboard=Scoreboard()
my_screen.listen()
my_screen.onkey(snake.up,'Up')
my_screen.onkey(snake.down, 'Down')
my_screen.onkey(snake.left, 'Left')
my_screen.onkey(snake.right, 'Right')
score=0
game_on=True

while game_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    #collision with food
    if snake.segments[0].distance(food)<15:
        food.refresh()
        scoreboard.increase_score()
        snake.extension()


    #collision with wall
    if snake.segments[0].xcor()>300 or snake.segments[0].xcor()<-300 or snake.segments[0].ycor()>300 or snake.segments[0].ycor()<-300:
        game_on=False
        scoreboard.game_over()
    #collision with tail

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment)<10:
            game_on=False
            scoreboard.game_over()



my_screen.exitonclick()

