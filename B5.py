import turtle

def draw_colored_squares(colors):
    window = turtle.Screen()
    window.bgcolor("white")

    pen = turtle.Turtle()
    pen.speed(2)

    for color in colors:
        pen.color(color)
        pen.forward(100)
        pen.right(90)

    turtle.done()

colors = ["red", "green", "blue", "yellow"]

draw_colored_squares(colors)
