import turtle

ts1 = turtle.Screen()
ts1.bgcolor("green")
ts1.title("spiral")
ti1 = turtle.Turtle()
ti1.color("blue")

tiColors = ["red" , "black" , "blue", "yellow"]


for i in range(10):
    ti1.color(tiColors[i%4])


    ti1.circle(10*i)
    ti1.circle(-10*i)

turtle.done()
