import turtle

window = turtle.Screen()
window.bgcolor("white")

pen = turtle.Turtle()
pen.color("red")
pen.speed(2)

side_length = 50
angle = 45

for _ in range(8):
    pen.forward(side_length)
    pen.right(angle)

turtle.done()
