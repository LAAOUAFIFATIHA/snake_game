import turtle
import time 
import random
from module1 import games


#-----------------------------part of game -----------------------------------#
games()
    #-------------------------screen-------------------------#
    
screen= turtle.Screen()
screen.title("game of snake ")
screen.bgcolor("green")
screen.setup(width = 600 , height = 600)
screen.tracer(0)


# Créer une fenêtre turtle
window = turtle.Screen()

# Charger l'image
window.register_shape( "C:\\games\\surprise\\start.GIF")
turtle.shape( "C:\\games\\surprise\\start.GIF")

# Attendre un moment avant d'effacer l'image
turtle.delay(2000)

# Effacer l'image
turtle.clear()

# Fermer la fenêtre
window.bye()

        # writing --------------------------

act = turtle.Turtle()
act.speed(0)
act.shape("square")
act.color("white")
act.penup()
act.hideturtle()
act.goto(30,-30)
act.write(" 'z' to start...", align="center", font=("arail",40))
def startscreen():
        screen= turtle.Screen()
        screen.title("game of snake ")
        screen.bgcolor("green")
        screen.setup(width = 600 , height = 600)
        screen.tracer(0)

        # writing --------------------------

        act = turtle.Turtle()
        act.speed(0)
        act.shape("square")
        act.color("white")
        act.penup()
        act.hideturtle()
        act.goto(30,-30)
        act.write(" 'z' to start...", align="center", font=("arail",40))




while True :
    screen.update()
    screen.listen()
    screen.onkeypress(games, "z")
    time.sleep(5)





    time.sleep(1)

screen.mainloop()