import turtle

def steps(t, width, height, num_steps):
    for _ in range(num_steps):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.left(90)

window = turtle.Screen()
window.bgcolor("white")

pen = turtle.Turtle()
pen.color("black")
pen.speed(2)

step_width = 50
step_height = 30
num_of_steps = 5

steps(pen, step_width, step_height, num_of_steps)

turtle.done()
