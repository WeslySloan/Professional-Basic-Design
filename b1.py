import turtle

turtle.penup()
turtle.goto(-150, -75)  
turtle.pendown()
turtle.fillcolor("yellow")  
turtle.begin_fill()  
for _ in range(2):
    turtle.forward(300)  
    turtle.left(90)  
    turtle.forward(150)  
    turtle.left(90)  
turtle.end_fill()  

turtle.done()
