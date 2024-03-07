import turtle

ts= turtle.Screen()
ts.bgcolor("green")
ts.title("shirinkings")

ti = turtle.Turtle()
ti.color("blue")

def ss(size):
    for i in range(4):
        ti.forward(size)
        ti.left(90)
        size=size/2
ss(150)
ss(100)
turtle.done()