import turtle

db = turtle.Screen()
db.bgcolor("red")
db.title("poly")
x=turtle.Turtle()
y=turtle.Turtle()
n=5
angle=360.0/n*2
a=200

m=5
angle2=360/n*3
b=150

for i in range(m):
    y.right(angle2)
    y.forward(b)
for i in range(n):
    x.right(angle)
    x.forward(a)
turtle.done()

