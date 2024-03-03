from turtle import Turtle  # Importing the Turtle class from the turtle module
import random  # Importing the random module


class Food(Turtle):
    def __init__(self):
        super().__init__()  # Initializing the Turtle superclass
        self.shape("circle")  # Setting the shape of the food to a circle
        self.penup()  # Lifting the pen to prevent drawing
        self.shapesize(0.5, 0.5)  # Setting the size of the food
        self.color("blue")  # Setting the color of the food
        self.speed("fastest")  # Setting the animation speed of the food
        self.refresh()  # Generating initial random position for the food

    def refresh(self):
        """Refreshes the position of the food to a random location within the screen boundaries"""
        random_x = random.randint(-280, 280)  # Generating a random x-coordinate within the screen boundaries
        random_y = random.randint(-280, 280)  # Generating a random y-coordinate within the screen boundaries
        self.goto(random_x, random_y)  # Moving the food to the randomly generated position
