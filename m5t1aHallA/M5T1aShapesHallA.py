# CTI 110
# M5T1a Shapes
# Hall, A
# 11 Oct 2017

import turtle #Allows Use of turtle


def main():
    win = turtle.Screen()
    m = turtle.Turtle()

#Display for square
    m.pensize(3)
    m.shape('turtle')
    m.pencolor('red')

#Turtle Speed
    m.speed(4)

#Turtle Commands for Square
    m.forward(50)
    m.left(90)
    m.forward(50)
    m.left(90)
    m.forward(50)
    m.left(90)
    m.forward(50)
    m.left(90)
    m.penup()
    m.forward(100)

#Turtle Display
    m.pencolor('blue')
    m.pendown()

#Turtle Commands for Triangle
    m.forward(100)
    m.left(120)
    m.forward(100)
    m.left (120)
    m.forward(100)

    
main()


    

    


