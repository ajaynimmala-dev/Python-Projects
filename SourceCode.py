
from random import randint
import turtle as t


class Point:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def is_point(self,rect_points):
        # print("lower point:",rect_points.low_left,"\n","upper point:","\n",rect_points.up_right)
        if rect_points.low_left[0]<self.x <rect_points.up_right[0] and rect_points.low_left[1]<self.y<rect_points.up_right[1]:
            return True
        else:
            return False

class Rectangle:

    def __init__(self,low_left,up_right):

        self.low_left=low_left

        self.up_right=up_right

    def Area(self):

        self.lenght=(self.up_right[0]-self.low_left[0])

        self.breadth=(self.up_right[1]-self.low_left[1])

        self.area=self.lenght*self.breadth

        return(self.area)

import turtle as t
class Trutle:

    def turctle_figure(self,rect_points):
        t.up()
        t.forward(rect_points.low_left[0])
        t.left(90)
        t.forward(rect_points.low_left[1])
        t.down()
        print(t.pos())
        t.color("blue")
        t.forward(abs(rect_points.low_left[0]-rect_points.up_right[0]))
        t.left(90)
        t.color("red")
        t.forward(abs(rect_points.low_left[1]-rect_points.up_right[1]))
        t.left(90)
        t.color("green")
        t.forward(rect_points.up_right[0] - rect_points.low_left[0])
        t.left(90)
        t.color("purple")
        t.forward(rect_points.up_right[1]-rect_points.low_left[1])
        t.up()
        t.done()



rect_points = Rectangle((randint(-150,150), randint(-150, 150)), (randint(150, 300), randint(150, 300)))

print("the rectangle points are:".title(), rect_points.low_left, rect_points.up_right)

point1 = Point((int(input("Guess X Point"))), int(input("Guess Y Point")))

Result = point1.is_point(rect_points)

print("your point was in side the rectangle".title(),Result)

Area_Rectangle=Rectangle.Area(rect_points)

print("the area of rectangle is:".title(),Area_Rectangle)

tur=Trutle()
tur.turctle_figure(rect_points)
