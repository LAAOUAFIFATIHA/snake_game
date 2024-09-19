import pygame
import sys 
from pygame import Vector2
import random 
import model2  
import turtle
import time 
import random
from surprise import module1 
from surprise  import screenModule




screeny =screenModule.screen()
screeny.screenWite()



player_action = turtle.textinput("Joueur", "do you want to play (yes / no ): ")
if player_action == "yes":
    screeny.screenblack()
    player_action = turtle.textinput("Joueur", "do you want to play first game (f) OR  seconde game (s) : ")
    if player_action == "f":
        screeny.screenWite()
        game = module1.games()
        game.part1()
    elif player_action == "s":
        game = model2.new_game()
