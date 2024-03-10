import turtle as t
t.shape("circle")
t.pensize(5)
t.speed(0)



#시계 원형틀 잡기
t.left(180)
t.penup()
t.forward(250)
t.left(90)

t.pendown()
t.color("pink")
t.begin_fill()
t.circle(250)
t.end_fill()

#시계 눈금 그리기
t.color("hotpink")

#90도씩 기준 눈금 그리기
def draw_gradation_90(angle):
    t.penup()
    t.home()
    t.left(angle)
    t.forward(210)
    t.pendown()
    t.forward(50)
    t.penup()
    t.backward(470)
    t.pendown()
    t.backward(50)

draw_gradation_90(90)
draw_gradation_90(180)

#30도씩 세부 눈금그리기
def draw_gradation_30(angle):
    t.penup()
    t.home()
    t.left(angle)
    t.forward(220)
    t.pendown()
    t.forward(30)
    t.penup()
    t.backward(470)
    t.pendown()
    t.backward(30)

draw_gradation_30(30)
draw_gradation_30(60)
draw_gradation_30(120)
draw_gradation_30(150)

#6도씩 더 세부적인 눈금 그리기
def draw_gradation_6(angle):
    t.penup()
    t.home()
    t.left(angle)
    t.forward(240)
    t.pendown()
    t.forward(10)
    t.penup()
    t.backward(490)
    t.pendown()
    t.backward(10)

for i in range(6, 180, 6):
    draw_gradation_6(i)



# #시계 원점 그리기 
# t.penup()
# t.home()
# t.forward(10)
# t.left(90)

# t.color("purple")
# t.begin_fill()
# t.circle(10)
# t.end_fill()

#분침 만들기
import time 
line=t.Turtle()
line.color("purple")
line.speed(0)
line.pensize(3)

def hourhand(angle):
    line.forward(200)
    time.sleep(1/2)
    line.clear()
    line.penup()
    line.home()
    line.pendown()
    line.left(angle)

for i in range(1, 360, 20):
    hourhand(i)

#시침 만들기
# hand=t.Turtle()
# hand.color("purple")
# hand.speed(0)
# hand.pensize(5)

# def hourhand(angle):
#     hand.forward(100)
#     time.sleep(1/2)
#     hand.clear()
#     hand.penup()
#     hand.home()
#     hand.pendown()
#     hand.left(angle)

# for h in range(1/240, 360, 1/240):
#     hourhand(h)

# def hourhand():
#     ang=t.heading
#     t.forward(15)
#     t.right(5)

t.mainloop()

# def hourhand(angle):
#     t.left(angle)
#     t.forward(150)
# hourhand(30)
# t.ontimer(hourhand,1000)

#본격적으로!! 타임모듈 써보기
