from turtle import *

pencolor("yellow")
bgcolor("black")
speed("fastest")
n=0
while n <=200:
    fd(50+n)
    rt(360/6)
    write(n, font=("calibri", 8))
    n+=5

hideturtle()
mainloop()
