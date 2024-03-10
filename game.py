import turtle as t
import random

def turn_up():
    t.left(2)

def turn_down():
    t.right(2)

def fire():
    ang=t.heading()
    while t.ycor()>0:
        t.forward(15)
        t.right(5)
    d=t.distance(target,0)
    t.sety(random.randint(10,100))
    if d<25:
        t.color("blue")
    else:
        t.color("pink")
        t.goto(-200,10)
        t.setheading(ang)

    t.mainloop()