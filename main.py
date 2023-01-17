from turtle import *
from tkinter import *

state = {'turn': 0}

def flip():
    state['turn'] += 10

def spinner():
    clear()
    angle = state['turn'] / 10
    right(angle)
    forward(100)
    dot(100, 'red')
    back(100)
    right(120)
    forward(100)
    dot(100, 'blue')
    back(100)
    right(120)
    forward(100)
    dot(100, 'green')
    back(100)
    right(120)
    update()

def animate():
    if state['turn'] > 0:
        state['turn'] -= 1
    spinner()
    ontimer(animate, 20)

setup(420, 420, 370, 0)
tracer(0)
hideturtle()
width(20)
onkey(flip, 'space')
listen()
animate()
done()