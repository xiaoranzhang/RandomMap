# !/usr/bin/python
# _*_ coding:utf-8 _*_

import turtle
from random import randint

turtle.speed(10)

turtle.color('gray')
x = -180 # 80
for y in range(-180, 180 +1, 10): # 80
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()
	turtle.forward(360) # 160

y = 180
turtle.right(90)
for x in range(-180, 180 + 1, 10):
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()
	turtle.forward(360)

turtle.pensize(3)
turtle.color('red')

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

x = y = 0
while abs(x) < 180 and abs(y) < 180:
	r = randint(0, 5)
	if r == 0:
		x += 10
		turtle.setheading(0)
		turtle.forward(10)
	elif r == 1:
		y -= 10
		turtle.setheading(270)
		turtle.forward(10)
	elif r == 2:
		x -= 10
		turtle.setheading(180)
		turtle.forward(10)
	elif r == 3:
		y += 10
		turtle.setheading(90)
		turtle.forward(10)

turtle.done()

