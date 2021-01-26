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

scale = 128
ps = [Vec2D(-.5, -.5) * scale, Vec2D(-.5, .5) * scale, Vec2D(.5, .5) * scale, Vec2D(.5, -.5) * scale]
#ps = [Vec2D(-1, 0) * scale, Vec2D(0, 1) * scale, Vec2D(1, 0) * scale, Vec2D(0, -1) * scale]
points = []
max_iter = 3

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

outer_max = 256

k = 0
dk = 1
max_k = 10
while(True):
    for j in range(outer_max):
        t.clear()
        t.pu()
        t.setpos(points[0])
        t.pd()
        fj = j / outer_max
        for i in range(len(points)):        
            fi = i / len(points)
            
            f = fi + fj# + k / max_k
            f2 = fi - fj
            f3 = fi - .5 * fj
            if f > 1:
                f = f - 1
            #if f > 1:
            #    f = f - 1

            col = .5 * (math.sin(f * 2 * math.pi) + 1)
            col2 = .5 * (math.sin(f2 * 2 * math.pi) + 1)
            col3 = .5 * (math.cos(f3 * 2 * math.pi) + 1)

            t.pencolor(col, col2, col3)
            t.setpos(points[i])
        turtle.update()
    #k += dk
    #if k == max_k or k == 0:
    #    dk = -dk

t.pu()
t.forward(10000)

input()