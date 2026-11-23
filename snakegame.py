import turtle
import random
import time

s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("light blue")
s.setup(width=600, height=600)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.shapesize(2, 2)
head.penup()
head.goto(0, 0)
head.showturtle()

turtle.done()