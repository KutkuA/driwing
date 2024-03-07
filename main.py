import turtle
drawingBoard = turtle.Screen()
drawingBoard.bgcolor("red4")
drawingBoard.title("Pyhton Turtle")
turtle_instance1 = turtle.Turtle()
turtle_instance2 = turtle.Turtle()
for i in range(4):
    turtle_instance1.forward(100)
    turtle_instance1.left(90)


turtle.done()