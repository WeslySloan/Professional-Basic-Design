import turtle

def draw_square(side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)

def draw_figure(side_length):
    draw_square(side_length)
    turtle.penup()
    turtle.forward(side_length * 2)
    turtle.pendown()
    draw_square(side_length * 2)
    turtle.penup()
    turtle.right(90)
    turtle.forward(side_length * 2)
    turtle.left(90)
    turtle.pendown()
    draw_square(side_length * 4)

side_length = float(input(""))

turtle.speed(3)
draw_figure(side_length)

turtle.done()
