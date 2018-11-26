"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Lucas D'Alesio.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
red_turtle = rg.SimpleTurtle('turtle')
rg.Pen('red', 30)
red_turtle.speed = 5
size = 100
for k in range(10):
    red_turtle.draw_square(size)
    red_turtle.pen_up()
    red_turtle.right(100)
    red_turtle.backward(100)
    red_turtle.pen_down()
    size = size - 10

green_turtle = rg.SimpleTurtle('arrow')
rg.Pen('green', 20)
green_turtle.speed = 8
size = 200
for k in range(20):
    green_turtle.draw_circle(size)
    green_turtle.pen_up()
    green_turtle.forward(100)
    green_turtle.right(50)
    green_turtle.backward(100)
    green_turtle.pen_down()
    size = size - 20
