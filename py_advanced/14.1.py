# from turtle import *
#
#
# def signature():
#     import os
#     text = "Rif.  " + os.path.basename(__file__)
#     penup()
#     setpos(Screen().screensize()[0] - 30, -Screen().screensize()[1] - 20)
#     write(text, move=False, align="right", font=("Arial", 8, "normal"))
#
#
# def turtlette():
#     bgcolor("black")
#     pencolor('white')
#     pensize(1)
#     hideturtle()
#     speed(0)
#
#     for i in range(40, 160):
#         left(8 - 160 // i)
#         circle(i)
#
#     signature()
#     done()
#
#
# if __name__ == '__main__':
#     turtlette()

# ----------------- 1 --------------------

# import turtle
#
#
# def rectangle(width, height):
#     for _ in range(2):
#         turtle.forward(width)
#         turtle.left(90)
#         turtle.forward(height)
#         turtle.left(90)
#
#
# w = int(input('Введите ширину = '))
# h = int(input('Введите высоту = '))
#
# rectangle(w, h)

# ----------------- 2 --------------------

class Triangle:
    def __init__(self, side):
        self.side = side

    def triangle(self, side):
        import turtle
        for _ in range(2):
            turtle.forward(side)
            turtle.left(120)
        turtle.done()


First = Triangle(int(input()))
First.triangle(int(input()))
