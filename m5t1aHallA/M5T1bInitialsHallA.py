# CTI 110
# M5T1b Initials
# Hall, A
# 11 Oct 2017


import turtle 
win = turtle.Screen()
m = turtle.Turtle()

def main():
    #Display for square
    m.pensize(7)
    m.shape('turtle')
    m.pencolor('red')

    #Turtle Speed
    m.speed(2)

    # Commands For Initial A

    m.left(180)
    m.penup()
    m.forward(60)
    m.right(90)
    m.pendown()
    m.forward(90)
    m.right(90)
    m.forward(50)
    m.right(90)
    m.forward(90)
    m.back(40)
    m.right(90)
    m.forward(50)

    #Commands For Transition to Next Initial

    m.penup()
    m.left(90)
    m.forward(50)
    m.left(90)
    m.forward(120)
    m.left(90)
    m.pendown()

    #Commands For Initial H
    m.forward(90)
    m.penup()
    m.back(50)
    m.right(90)
    m.pendown()
    m.forward(50)
    m.right(90)
    m.forward(50)
    m.back(100)

main()
