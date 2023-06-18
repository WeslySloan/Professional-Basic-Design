import turtle

def draw_right_triangle(a, b):
    c = (a ** 2 + b ** 2) ** 0.5 
    window = turtle.Screen()
    window.bgcolor("white")

    pen = turtle.Turtle()
    pen.color("black")
    pen.speed(2)

    pen.forward(a)
    pen.left(90)
    pen.forward(b)
    pen.goto(0, 0)  
    turtle.done()

a = float(input(""))
b = float(input(""))

draw_right_triangle(a, b)
