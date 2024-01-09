from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.title("My Snake Game")
screen.bgpic("uk1.png")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()


screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

on = True
while on:
    screen.update()
    time.sleep(0.3)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.score += 1
        snake.extend()
        score.update()

    # Detect collision with wall
    if not -300 < snake.head.xcor() < 300 or not -300 < snake.head.ycor() < 300:
        on = False
        score.game_over()

    # Detect collison with tail
    for segment in snake.body_seg[1:]:
        if snake.head.distance(segment) < 15:
            on = False
            score.game_over()




screen.exitonclick()


