from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.

### Write your code below:
#turn 5 times
t.begin_fill()
t.fillcolor("blue")

answer = input("give me a number of sides, please...")
sides = int(answer)
print("you gave me" + str(sides))

for x in range(0, 3):
    t.forward(250)
    t.left(90)
    
t.end_fill()

# Close window on click.
exitonclick()
