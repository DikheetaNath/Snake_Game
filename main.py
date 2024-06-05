from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

# Screen Setup:
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(8)


# Objects:
snake = Snake()
food = Food()
score = Scoreboard()


# Controls:
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
i = 0

score.update_score(i)

# Game Starts:
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food:
    if snake.head.distance(food) < 15:
        food.change_pos()
        i += 1
        snake.extend()
        score.update_score(i)

    # Detect collision with wall:
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # Detect collision with its own body:
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()
