from turtle import *
speed(0)

def polygon(side, size):
    for i in range(side):
        fd(size)
        lt(360/side)

for i in range(6):
    
hideturtle()
mainloop()

