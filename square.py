#!/usr/bin/env python

import turtle

def square(t ,x:int ,y:int):
    '''
    ---- Draw a square ----
    t: your turtle
    x: start x position
    y: start y position

    '''
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range (4):
        t.left(90)
        t.forward(100)

def quit():
    turtle.bye()

my_turtle = turtle.Turtle() #create

turtle.Screen().listen() #tell the screen to listen for key events

turtle.onkeypress(quit,key="Escape") #press Esc to quit

square(my_turtle,-100,-100)

turtle.mainloop() #enter main loop so window stays in view




