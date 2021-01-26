import turtle
import math
from turtle import Screen, Vec2D

def Hilbert(ps, n, points):
    if n == 0:
        points.extend(ps)        
    else:
        c = (ps[2] + ps[0]) * .5

        p0 = (ps[0] - c) * .5
        p1 = (ps[1] - c) * .5
        p2 = (ps[2] - c) * .5
        p3 = (ps[3] - c) * .5

        Hilbert([ps[0] + p0, ps[0] + p3, ps[0] + p2, ps[0] + p1], n - 1, points)
        Hilbert([ps[1] + p0, ps[1] + p1, ps[1] + p2, ps[1] + p3], n - 1, points)
        Hilbert([ps[2] + p0, ps[2] + p1, ps[2] + p2, ps[2] + p3], n - 1, points)
        Hilbert([ps[3] + p2, ps[3] + p1, ps[3] + p0, ps[3] + p3], n - 1, points)

scale = 1
ps = [Vec2D(-.5, -.5) * scale, Vec2D(-.5, .5) * scale, Vec2D(.5, .5) * scale, Vec2D(.5, -.5) * scale]
#ps = [Vec2D(-1, 0) * scale, Vec2D(0, 1) * scale, Vec2D(1, 0) * scale, Vec2D(0, -1) * scale]
points = []
max_iter = 6

Hilbert(ps, max_iter, points)
print (len(points))
#print (points[1000])

### VISUALIZE

s = turtle.getscreen()
s.delay(0)
t = turtle.Turtle()

t.hideturtle()
turtle.bgcolor(0.0, 0.0, 0.0)
t.color(1.0, 0.0, 0.0)
t.speed(0)

turtle.hideturtle()
turtle.tracer(0, 0)

from matplotlib import pyplot as plt

img = plt.imread("artist.jpg")

rows = len(img)
cols = len(img[0])

img_scale = 256

t.pu()
t.setpos(points[0] * img_scale)
t.pd()

for point in points:
    x = int((point[0] + 1) * len(img) * .5)
    y = int((-point[1] + 1) * len(img[0]) * .5)
    
    c = img[y][x]/256
    
    r = float(c[0])
    g = float(c[1])
    b = float(c[2])

    t.pencolor(r, g, b)
    t.setpos(point * img_scale)

turtle.update()
t.pu()
t.forward(10000)

input()