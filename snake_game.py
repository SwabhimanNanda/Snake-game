# Importing necessary modules
from snake import Snake  # Importing Snake class
from turtle import Screen  # Importing Screen class from turtle module
from food import Food  # Importing Food class
from scoreboard import Scoreboard  # Importing Scoreboard class
import time  # Importing time module

# Setting up the screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turns off animation

# Creating instances of Snake, Food, and Scoreboard
snake = Snake()
food = Food()
score = Scoreboard()

# Listening for key events
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Delay for smoother movement
    screen.update()  # Update the screen
    snake.move_snake()  # Move the snake

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()  # Refresh the food position
        snake.extend()  # Extend the snake
        score.increase_score()  # Increase the score

    # Detect collision with wall
    if snake.head.xcor() > 283 or snake.head.xcor() < -283 or snake.head.ycor() > 283 or snake.head.ycor() < -283:
        game_is_on = False  # End the game
        score.game_over()  # Display game over message

# Detect collision with tail
for segment in snake.segment[1:]:
    if snake.head.distance(segment) < 10:
        game_is_on = False  # End the game
        score.game_over()  # Display game over message

# Exit the game on click
screen.exitonclick()
