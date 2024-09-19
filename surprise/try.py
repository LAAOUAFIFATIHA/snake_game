import turtle
import time 
import random
from module1 import games
from screenModule import screen

#-----------------------function----------------------#

 
screeny = screen()
screeny.screenWite()



player_action = turtle.textinput("Joueur", "do you want to play (yes / no ): ")
if player_action == "yes":
    game = games ()
    game.part1()




# Associer la fonction get_click au clic de souris sur l'écran

