# !/usr/bin/python
# _*_ coding:utf-8 _*_

import turtle
from random import randint

print "The world is an incidental space constructed with random pieces"
print ",and that's the true beauty of universe."
turtle.speed(8)  # set turtle speed to slowest

# draw 16-by-16 lattice
turtle.color("gray")  # color for lattice
x = -300
for y in range(-300, 300+1, 10):
	turtle.penup()
	turtle.goto(x, y)  # Draw a horizontal line
	turtle.pendown()
	turtle.forward(600)

y = 300
turtle.right(90)
for x in range(-300, 300+1, 10):
	turtle.penup()
	turtle.goto(x, y)  # Draw a vertical line
	turtle.pendown()
	turtle.forward(600)

turtle.pensize(3)
turtle.color("red")

turtle.penup()
turtle.goto(0, 0)  # Go to the center
turtle.pendown()

x = y = 0  # Current pen location at the center of lattice
while abs(x) < 1000 and abs(y) < 1000:
	r = randint(0, 3)
	if r == 0:
		x += 10  # walk right
		turtle.setheading(0)
		turtle.forward(10)
	elif r == 1:
		y -= 10  # walk down
		turtle.setheading(270)
		turtle.forward(10)
	elif r == 2:
		x -= 10  # walk left
		turtle.setheading(180)
		turtle.forward(10)
	elif r == 3:
		y += 10  # walk up
		turtle.setheading(90)
		turtle.forward(10)

turtle.done()


