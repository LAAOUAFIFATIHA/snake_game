

# Initialisation de Turtle
turtle.speed(0)  # Vitesse maximale
turtle.hideturtle()  # Cacher la tortue

# Coordonnées et dimensions du bouton
button_x = -50
button_y = 0
button_width = 100
button_height = 50

# Dessiner le rectangle du bouton
turtle.penup()
turtle.goto(button_x, button_y)
turtle.pendown()
turtle.fillcolor("lightgrey")
turtle.begin_fill()
for _ in range(2):
    turtle.forward(button_width)
    turtle.right(90)
    turtle.forward(button_height)
    turtle.right(90)
turtle.end_fill()

# Positionner le texte au centre du bouton
turtle.penup()
turtle.goto(button_x + button_width / 2, button_y + button_height / 2)
turtle.pendown()
turtle.write("Cliquez ici", align="center", font=("Arial", 12, "normal"))

# Fonction pour détecter les clics de souris
def button_click(x, y):
    if button_x <= x <= button_x + button_width and button_y <= y <= button_y + button_height:
        print("Bouton cliqué !")

# Lier la fonction button_click au clic de souris
turtle.onscreenclick(button_click)
turtle.done()