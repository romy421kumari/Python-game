
# coding: utf-8

# In[1]:


import turtle
import math
import random


# In[1]:


s= turtle.Screen()
s.bgcolor("black")
s.title("Game")
s.setup(height=600, width=700)

#Border
border=turtle.Turtle()
border.penup()
border.color("white")
border.setpos(-300,-250)
border.pendown()
border.pensize(3)
border.forward(600)
border.left(90)
border.forward(510)
border.left(90)
border.forward(600)
border.left(90)
border.forward(510)
border.left(90)
border.hideturtle()

# goal
goal=turtle.Turtle()
goal.color("yellow")
goal.penup()
goal.shape("circle")
goal.goto(100,100)

#score
scorea=0
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: {}".format(scorea), align="center", font=("Courier",24,"normal"))




player=turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
#speed variable
speed=2

def turnleft():
    player.left(20)
    
def turnright():
    player.right(20)
    
def inspeed():
    global speed
    speed+=1


turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(inspeed,"Up")

while True:
    player.forward(speed)
    
    if player.xcor()>295 or player.xcor()<-295:
        player.right(180)
        
    if player.ycor()<-250 or player.ycor()>260:
        player.left(180)
    
    d=math.sqrt(math.pow(player.xcor()-goal.xcor(),2)+math.pow(player.ycor()-goal.ycor(),2))
    if d<20:
        goal.penup()
        goal.setposition(random.randint(-295,295), random.randint(-250,260))
        scorea+=1
        pen.clear()
        pen.write("Score: {}".format(scorea), align="center", font=("Courier",24,"normal"))
        

        

