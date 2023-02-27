from turtle import Turtle,Screen

# turt = Turtle()
# def square():
#     turt.color("red")
#     turt.forward(50)
#     turt.right(90)

# for i in range(0,4):
#     square()

# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(50)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

turt = Turtle()
# def dotted_line():
#     turt.forward(5)
#     turt.color("white")
#     turt.forward(5)
#     turt.color("black")

# for i in range(0,10):
#     dotted_line()

def triangle():
    for i in range(0,2):
        turt.forward(50)
        turt.right(120)
    turt.forward(50)

def square():
    turt.right(120)
    for i in range(0,3):
        turt.forward(50)
        turt.right(90)
    turt.forward(50)

def pentagon():
    turt.right(90)
    for i in range(0,4):
        turt.forward(50)
        turt.right(72)
    turt.forward(50)

def hexagon():
    turt.right(72)
    for i in range(0,6):
        turt.forward(50)
        turt.right(60)

def octagon():
    for i in range(0,8):
        turt.forward(50)
        turt.right(45)

def nanogon():
    for i in range(0,9):
        turt.forward(50)
        turt.right(40)

def decagon():
    for i in range(0,10):
        turt.forward(50)
        turt.right(36)

triangle()
square()
pentagon()
hexagon()
octagon()
nanogon()
decagon()



screen = Screen()
screen.exitonclick()