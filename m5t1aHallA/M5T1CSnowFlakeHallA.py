# CTI 110
# M5T1C SnowFlake
# Hall, A
# 13 Oct 2017


import turtle
import random
win = turtle.Screen()
m = turtle.Turtle()
colours = ['red', 'pink','white','orange','purple','magenta','brown','green','yellow','indigo']



#Display for square
m.pensize(7)
m.shape('turtle')
m.pencolor('red')

#Turtle Speed
m.speed(8)

def main():
    win.bgcolor('black')
# First String
    for i in range (10):
        for i in range (2):
            m.forward(100)
            m.right(60)
            m.forward(100)
            m.right(120)
        m.right(36)
        m.color (random.choice (colours))

    m.penup()
    m.left(180)
    m.forward(200)
    m.right(90)
    m.forward(250)
    m.left(90)
    m.forward(20)


    m.pendown()
    m.pencolor('white')

# Second String

    for i in range (10):
        for i in range (2):
            m.forward(100)
            m.right(60)
            m.forward(100)
            m.right(120)
        m.right(36)
        m.color (random.choice (colours))
        

    m.pencolor('navy blue')
    m.penup()
    m.right(180)
    m.forward(200)
    m.pendown()

# Third String

    for i in range (10):
        for i in range(2):
            m.forward(100)
            m.right(60)
            m.forward(100)
            m.right(120)
        m.right(36)
        m.color (random.choice (colours))

    m.pencolor('red')
    m.penup()
    m.forward(200)
    m.pendown()

# Fourth String

    for i in range(10):
        for i in range (2):
            m.forward(100)
            m.right(60)
            m.forward(100)
            m.right(120)
        m.right(36)
        m.color (random.choice (colours))

    m.right(90)
    m.penup()
    m.forward(200)
    m.pencolor('white')
    m.pendown()

# Fifth String

    for i in range(10):
        for i in range(2):
            m.forward(100)
            m.right(60)
            m.forward(100)
            m.right(120)
        m.right(36)
        m.color (random.choice (colours))

    m.right(90)
    m.penup()
    m.forward(350)
    m.pencolor('navy blue')

    m.pendown()

# Sixth String

    for i in range(10):
        for i in range(2):
            m.forward(100)
            m.right(60)
            m.forward(100)
            m.right(120)
        m.right(36)
        m.color (random.choice (colours))

    m.left(90)
    m.penup()
    m.pencolor('red')
    m.forward(200)
    m.pendown()

# Seventh String

    for i in range(10):
        for i in range(2):
            m.forward(100)
            m.right(60)
            m.forward(100)
            m.right(120)
        m.right(36)
        m.color (random.choice (colours))

    m.left(90)
    m.penup()
    m.pencolor('white')
    m.forward(200)
    m.pendown()

# Eighth String

    for i in range(10):
        for i in range(2):
            m.forward(100)
            m.right(60)
            m.forward(100)
            m.right(120)
        m.right(36)
        m.color (random.choice (colours))

    m.penup()
    m.pencolor('navy blue')
    m.forward(100)
    m.pendown()

#Ninth String

    for i in range(10):
        for i in range(2):
            m.forward(100)
            m.right(60)
            m.forward(100)
            m.right(120)
        m.right(36)
        m.color (random.choice (colours))
        
    
    

main()








        

        





    
