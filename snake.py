import turtle
import time
import random
delay = 0.2
score =0
high_score=0

wn= turtle.Screen()
wn.title('Snake game')
wn.bgcolor("silver")
wn.setup(width=600, height=600)
wn.tracer(0)


head = turtle.Turtle()
head.speed(0)
head.color("black")
head.shape("square")
head.penup()
head.goto(0,0)
head.direction='stop'



segement=[]


pen= turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()
pen.goto(0,280)
pen.shape("square")
pen.color("yellow")
pen.write("SCORE : 0  HIGHSCORE: 0", align="center" ,font=("Arial",10,"normal"))


food = turtle.Turtle()
food.speed(0)
food.color("red")
food.shape("circle")
food.penup()
food.goto(0,200)
food.direction='stop'
food.shapesize(0.9)


def go_up():
    if head.direction!= "down":
        head.direction= "up"
def go_down():
    if head.direction!= "up":
        head.direction= "down"
def go_right():
    if head.direction!= "left":
        head.direction= "right"
def go_left():
    if head.direction!= "right":
        head.direction= "left"


def move():
    if head.direction=="up":
        y= head.ycor()
        head.sety(y + 20)
    if head.direction=="down":
        y= head.ycor()
        head.sety(y - 20)
    if head.direction=="left":
     x= head.xcor()
     head.setx(x - 20)
    if head.direction=="right":
        x= head.xcor()
        head.setx(x + 20)


wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_right,"d")
wn.onkeypress(go_left,"a")


while True:
    wn.update()

    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
         time.sleep(0.1)
         head.goto(0,0)
         head.shape("square")
         head.direction="stop"

         for seg in segement:
             seg.goto(10000,10000)

         segement.clear()
         score=0
         pen.clear()
         pen.write(" SCORE : {}  HIGHSCORE: {}".format(score,high_score), align="center" ,font=("Arial",10,"normal"))

    for seg in segement:
        if seg.distance(head)<20:
            time.sleep(0.1)
            head.goto(0,0)
            head.shape("square")
            head.direction="stop"

            for seg in segement:
                seg.goto(10000,10000)

            segement.clear()


            score=0
            pen.clear()
            pen.write(" SCORE : {}  HIGHSCORE: {}".format(score,high_score), align="center" ,font=("Arial",10,"normal"))

    if head.distance(food)<20:

        x= random.randint(-270,270)
        y= random.randint(-270.,270)
        food.goto(x,y)


        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.color("green")
        new_segment.penup()
        new_segment.shape("circle")
        segement.append(new_segment)


        delay =delay-0.001


        score += 10
        if score> high_score:
            high_score= score
        pen.clear()
        pen.write(" SCORE : {}  HIGHSCORE: {}".format(score,high_score), align="center" ,font=("Arial",10,"normal"))


    for index in range(len(segement)-1,0,-1):
        x=segement[index-1].xcor()
        y =segement[index-1].ycor()
        segement[index].goto(x,y)


    if len(segement)>0:
        x= head.xcor()
        y=head.ycor()
        segement[0].goto(x,y)
        head.shape("circle")




    move()
    time.sleep(delay)

wn.mainloop()
