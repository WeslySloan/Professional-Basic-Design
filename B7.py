import turtle

def draw_square(side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)

def draw_double_square(side_length):
    draw_square(side_length)
    turtle.penup()
    turtle.forward(side_length)
    turtle.pendown()
    draw_square(side_length)

side_length = float(input(""))

turtle.speed(3)
draw_double_square(side_length)

turtle.done()
