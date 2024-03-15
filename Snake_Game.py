import turtle
import random
import time
delay=0.1
sc=0
hs=0
#sb=0

#creating a body of Snake
bodies=[]

#creating a screen
s=turtle.Screen()
s.title("Snake Game")
s.bgcolor("white")
s.setup(width=650,height=650) #size of screen

#creating a head
head=turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("blue")
head.fillcolor("red")
head.penup()
head.goto(0,0)
head.direction="stop"

#creating a food
food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("black")
food.fillcolor("green")
food.penup()
food.goto(0,0)
food.direction="stop"

#score board
sb=turtle.Turtle()
sb.ht()
sb.penup()
sb.goto(-250,250)#250
sb.write("Score:0 | Highest Score:0")

#to print message on screen

def Moveup():
    if head.direction!="down":
        head.direction="up"
def Movedown():
    if head.direction!="up":
        head.direction="down"
def Moveleft():
    if head.direction!="right":
        head.direction="left"
def Moveright():
    if head.direction!="left":
        head.direction="right"
def Movestop():
    head.direction="stop"
def Move():
    if head.direction!="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction!="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction!="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction!="right":
        x=head.xcor()
        head.setx(x+20)

#event handling -key mapping
s.listen()
s.onkey(Moveup,"Down")
s.onkey(Movedown,"Up")
s.onkey(Moveleft,"Right")
s.onkey(Moveright,"Left")
s.onkey(Movestop,"space")

#mainloop

while True:
    s.update() #to update screen
    if head.xcor()>325:
        head.setx(-325)
        
    if head.xcor()<-325:
        head.setx(325)#290
        
    if head.ycor()>325:
        head.sety(-325)
        
    if head.xcor()<-325:
        head.setx(325)

    #cheak collision with food
    if head.distance(food)<20:
        x=random.randint(-325,325)
        y=random.randint(-325,325)
        food.goto(x,y)
        
        #increase the length of snake
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("green")
        bodies.append(body)
        
        #increase the score
        sc=sc+10
        if sc>hs:
            hs=sc
        sb.clear()
        sb.write("Score:{} | Highest Score:{}".format(sc,hs))
        
        #increse speed
        delay=delay-0.001

    #move the snake bodies
    for index in range(len(bodies)-1,0,-1):
        x=bodies[index-1].xcor()
        y=bodies[index-1].ycor()
        bodies[index].goto(x,y)
    if len (bodies)>0:
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
    Move()

    #check collision with snake body
    for body in bodies:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            for body in bodies:
                body.ht()
            bodies.clear()
            sc=0
            delay=0.1
            sb.clear()
            sb.write("Score:{} | Highest Score:{}".format(sc,hs))
    time.sleep(delay)
s.mainloop()









        

    

