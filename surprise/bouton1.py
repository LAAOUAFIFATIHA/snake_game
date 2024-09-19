import turtle

# Fonction à exécuter lorsque le bouton est cliqué
def on_button_click(x, y):
    if x == -50 and y == 50 and width == 109 and height ==  50:
        pass

# Créer un objet Turtle pour dessiner le bouton
button_turtle = turtle.Turtle()

# Fonction pour dessiner un rectangle avec du texte à l'intérieur
def draw_button(x = -50, y = 50, width = 100, height =  50, text = "cliquer ici"):
    button_turtle.penup()
    button_turtle.goto(x, y)
    button_turtle.pendown()
    
    # Dessiner le rectangle du bouton
    button_turtle.fillcolor("lightgray")
    button_turtle.begin_fill()
    for _ in range(2):
        button_turtle.forward(width)
        button_turtle.right(90)
        button_turtle.forward(height)
        button_turtle.right(90)
    button_turtle.end_fill()
    
    # Écrire le texte sur le bouton
    button_turtle.penup()
    button_turtle.goto(x + width / 2, y + height / 2)
    button_turtle.pendown()
    button_turtle.write(text, align="center", font=("Arial", 12, "bold"))

