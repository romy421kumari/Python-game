
# coding: utf-8

# In[1]:


import turtle
import winsound


# In[2]:


am=turtle.Screen()
am.title("Python game")
am.bgcolor("black")
am.setup(width=880, height=600)
am.tracer(0)

scorea=0
scoreb=0

# Paddle A
paddlea=turtle.Turtle()
paddlea.speed(0)
paddlea.shape("square")
paddlea.color("white")
paddlea.shapesize(stretch_wid=5,stretch_len=1)
paddlea.penup()
paddlea.goto(-350,0)

#Paddle B
paddleb=turtle.Turtle()
paddleb.speed(0)
paddleb.shape("square")
paddleb.color("white")
paddleb.shapesize(stretch_wid=5,stretch_len=1)
paddleb.penup()
paddleb.goto(350,0)

# Ball
ball=turtle.Turtle()
ball.speed(20)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=1
ball.dy=-1


pen=turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A : 0    Player B: 0", align="center", font=("Courier",24,"normal"))

#function

def paddleaup():
    y=paddlea.ycor()
    y+=20
    paddlea.sety(y)
    
def paddleadown():
    y=paddlea.ycor()
    y-=20
    paddlea.sety(y)
    
def paddlebup():
    y=paddleb.ycor()
    y+=20
    paddleb.sety(y)
    
def paddlebdown():
    y=paddleb.ycor()
    y-=20
    paddleb.sety(y)
    

    
    
#keyboard binding
am.listen()
am.onkeypress(paddleaup,"w")
am.onkeypress(paddleadown,"s")
am.onkeypress(paddlebup,"Up")
am.onkeypress(paddlebdown,"Down")


while True:
    am.update()
    
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
     
    #border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
        
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dy*=-1
        scorea+=1
        pen.clear()
        pen.write("Player A : {}    Player B: {}".format(scorea,scoreb), align="center", font=("Courier",24,"normal"))
        
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dy*=-1
        scoreb+=1
        pen.clear()
        pen.write("Player A : {}    Player B: {}".format(scorea,scoreb), align="center", font=("Courier",24,"normal"))
        
    # paddle ball collision
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddleb.ycor()+40 and ball.ycor()>paddleb.ycor()-40):
        ball.setx(340)
        ball.dx*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddlea.ycor()+40 and ball.ycor()>paddlea.ycor()-40):
        ball.setx(-340)
        ball.dx*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        
    
    

