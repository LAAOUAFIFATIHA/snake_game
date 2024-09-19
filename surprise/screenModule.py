import turtle
import time 
import random
#--------------------------------
class screen:
    def __init__(self):
        pass
    def screenWite(self):
        screen= turtle.Screen()
        screen.title("game of snake ")
        screen.bgcolor("white")
        
        screen.setup(width = 600 , height = 600)
        screen.tracer(0)
    def screenblack(self):
        screen= turtle.Screen()
        screen.title("game of snake ")
        screen.bgcolor("black")
        screen.setup(width = 600 , height = 600)
        screen.tracer(0)