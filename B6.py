import turtle

def draw_house(side_length):
    turtle.forward(side_length)
    turtle.left(120)
    turtle.forward(side_length)
    turtle.left(120)
    turtle.forward(side_length)
    turtle.left(30)
    turtle.forward(side_length)
    turtle.left(90)
    turtle.forward(side_length)
    turtle.left(90)
    turtle.forward(side_length)
    turtle.left(30)
    turtle.forward(side_length)
    turtle.left(120)
    turtle.forward(side_length)
    turtle.left(120)
    turtle.forward(side_length)
    turtle.left(30)

def draw_houses(side_length, num_houses):
    for _ in range(num_houses):
        draw_house(side_length)
        turtle.penup()
        turtle.forward(2 * side_length)
        turtle.pendown()

side_length = float(input("Enter the side length of the house: "))
num_houses = int(input("Enter the number of houses: "))

turtle.speed(3)
draw_houses(side_length, num_houses)

turtle.done()
