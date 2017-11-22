# CTI 110
# M5Lab: Nested Loops
# Hall, A
# 16 Oct 2017

# Commands To Use Turtle
import turtle
import random
win = turtle.Screen()
m = turtle.Turtle()

# Random Pen Colors and Speed

colours = ['yellow','teal','black']
m.speed (7)



#Display for turtle
m.pensize(7)
m.shape('turtle')
m.pencolor('black')

# Command for Multi-Sided Snowflake

def main():
    for i in range (10):
        for i in range (2):
             m.forward(100)
             m.right(60)
             m.forward(100)
             m.right(120)
        m.right (36)
        m.color (random.choice (colours))

        
        win.bgcolor('green')
main()
