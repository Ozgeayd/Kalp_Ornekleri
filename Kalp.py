import math
from turtle import *
def hearta_x(k):
    return 15 * math.sin(k) ** 3
def hearta_y(k):
    return 11.8 * math.cos(k)-5*math.cos(2*k)-2*math.cos(3*k)-math.cos(4*k)

speed(0)
bgcolor("black")
color("red")
pensize(2)

penup()
for i in range(0,628,2):
    k=i/100
    x=hearta_x(k)*20
    y=hearta_y(k)*20
    goto(x,y)
    pendown()
    
done()