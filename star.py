import turtle

db = turtle.Screen()
db.bgcolor("red")
db.title("star")
x=turtle.Turtle()
x.left(60)
x.forward(200)
x.right(120)
x.forward(200)
x.right(150)
import math

y=math.sqrt(3)
x.forward(400/y)
x.right(150)
x.forward(200)
x.right(150)
x.forward(400/y)

turtle.done()