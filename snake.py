from turtle import Turtle  # Importing the Turtle class from the turtle module

# Constants defining starting positions, movement step, and directions
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        """Initialize the Snake object"""
        self.segment = []  # List to store the segments of the snake
        self.create_snake()  # Create the initial snake
        self.head = self.segment[0]  # Reference to the head segment of the snake

    def create_snake(self):
        """Create the initial segments of the snake"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Add a new segment to the snake"""
        turtle = Turtle(shape="square")  # Creating a new turtle segment
        turtle.color("red")  # Setting color of the segment
        turtle.penup()  # Lifting the pen to prevent drawing while moving
        turtle.goto(position)  # Positioning the segment
        self.segment.append(turtle)  # Adding the segment to the snake's segments list

    def extend(self):
        """Extend the length of the snake by adding a new segment"""
        self.add_segment(self.segment[-1].position())  # Adding a new segment at the last position of the snake

    def move_snake(self):
        """Move the snake forward by one step"""
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()  # Get the x-coordinate of the previous segment
            new_y = self.segment[seg_num - 1].ycor()  # Get the y-coordinate of the previous segment
            self.segment[seg_num].goto(new_x, new_y)  # Move the current segment to the previous segment's position
        self.head.forward(MOVE_STEP)  # Move the head segment forward by one step

    def up(self):
        """Change the direction of the snake to up"""
        if self.head.heading() != DOWN:  # If the snake is not moving downwards
            self.head.setheading(UP)  # Change the direction of the head segment to up

    def left(self):
        """Change the direction of the snake to left"""
        if self.head.heading() != RIGHT:  # If the snake is not moving rightwards
            self.head.setheading(LEFT)  # Change the direction of the head segment to left

    def down(self):
        """Change the direction of the snake to down"""
        if self.head.heading() != UP:  # If the snake is not moving upwards
            self.head.setheading(DOWN)  # Change the direction of the head segment to down

    def right(self):
        """Change the direction of the snake to right"""
        if self.head.heading() != LEFT:  # If the snake is not moving leftwards
            self.head.setheading(RIGHT)  # Change the direction of the head segment to right
