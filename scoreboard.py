from turtle import Turtle  # Importing the Turtle class from the turtle module

# Constants for text alignment and font style
ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        """Initialize the Scoreboard object"""
        super().__init__()  # Initializing the Turtle superclass
        self.score = 0  # Initial score
        self.color("white")  # Setting the color of the text
        self.penup()  # Lifting the pen to prevent drawing
        self.hideturtle()  # Hiding the turtle icon
        self.goto(0, 270)  # Positioning the scoreboard
        self.update_scoreboard()  # Updating the scoreboard text

    def game_over(self):
        """Display 'GAME OVER' message"""
        self.goto(0, 0)  # Positioning the cursor to the center of the screen
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)  # Writing 'GAME OVER' message

    def update_scoreboard(self):
        """Update the scoreboard with current score"""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)  # Writing the current score

    def increase_score(self):
        """Increase the score by 1 and update the scoreboard"""
        self.score += 1  # Incrementing the score
        self.clear()  # Clearing the previous score
        self.update_scoreboard()  # Updating the scoreboard with the new score
