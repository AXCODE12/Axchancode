import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    water = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    water.shape('circle')
    # Set your turtle's speed using .speed(2)
    water.speed(5)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    water.color('red')
    water.pencolor('blue')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?
    water.forward(250)
    # Move your turtle left or right using .left(90) or .right(90)
    water.left(40)
    water.right(99)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?
    for i in range(4):
        water.forward(50)
        water.left(90)
    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    water.goto(30,230)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    water.begin_fill()
    water.circle(30,steps=60)
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below
    water.end_fill()
    # Draw 3 more shapes with different fill colors!
    water.begin_fill()
    for i in range(4):
        water.forward(60)
        water.left(90)
    water.end_fill()
    water.goto(0,0)
    water.color('green')
    water.begin_fill()
    for i in range(3):
        water.forward(60)
        water.left(120)
    water.end_fill()

    water.goto(-30,-50)
    water.begin_fill()
    water.forward(100)
    water.right(130)
    water.forward(150)
    water.right(130)
    water.forward(100)
    water.right(50)
    water.forward(20)
    water.end_fill()
    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
