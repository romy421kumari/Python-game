
# coding: utf-8

# In[1]:


import turtle
import time
from random import randint



am= turtle.Screen()
am.title("Race ")
am.bgcolor("pink")
am.setup(width=700, height=600)
a=turtle.Turtle()
a.color("black")
a.speed(0)
a.penup()
a.setpos(-100,240)
a.penup()
a.write("Turtle race",font=("Arial",30,"bold"))
a.penup()
a.hideturtle()


# Finish line
a=turtle.Turtle()
a.penup()
a.color("green")
a.shape("square")
a.shapesize(stretch_wid=60, stretch_len=1)
a.goto(320,280)
a.speed(0)


#turtle 1

a1=turtle.Turtle()
a1.speed(0)
a1.color("blue")
a1.shape("turtle")
a1.penup()
a1.goto(-250,150)
a1.pendown()


# turle 2
a2=turtle.Turtle()
a2.speed(0)
a2.color("orange")
a2.shape("turtle")
a2.penup()
a2.goto(-250,100)
a2.pendown()


# turle 3
a3=turtle.Turtle()
a3.speed(0)
a3.color("red")
a3.shape("turtle")
a3.penup()
a3.goto(-250,50)
a3.pendown()


# turle 4
a5=turtle.Turtle()
a5.speed(0)
a5.color("brown")
a5.shape("turtle")
a5.penup()
a5.goto(-250,0)
a5.pendown()


# turle 5
a6=turtle.Turtle()
a6.speed(0)
a6.color("yellow")
a6.shape("turtle")
a6.penup()
a6.goto(-250,-50)
a6.pendown()

# turle 6
a4=turtle.Turtle()
a4.speed(0)
a4.color("black")
a4.shape("turtle")
a4.penup()
a4.goto(-250,-100)
a4.pendown()

# turle 7
a7=turtle.Turtle()
a7.speed(0)
a7.color("green")
a7.shape("turtle")
a7.penup()
a7.goto(-250,-150)
a7.pendown()

time.sleep(1)

for i in range(178):
    a1.forward(randint(1,5))
    a1.penup()
    a2.forward(randint(1,5))
    a2.penup()
    a3.forward(randint(1,5))
    a3.penup()
    a4.forward(randint(1,5))
    a4.penup()
    a5.forward(randint(1,5))
    a5.penup()
    a6.forward(randint(1,5))
    a6.penup()
    a7.forward(randint(1,5))
    a7.penup()
    
    
turtle.exitonclick()
    

