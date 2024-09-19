import turtle
import time 
import random

class games:
    def __init__(self):
          pass
    def part1(self):
        dly = 0.4
        scoren = 0
        high_score = 0
        #-----------------score -------------action --------------
        # writing --------------------------

        act = turtle.Turtle()
        act.speed(0)
        act.shape("square")
        act.color("white")
        act.penup()
        act.hideturtle()
        act.goto(100,-250)
        act.write("you can start...", align="center", font=("arail",16))
        #score----------------------------
        score = turtle.Turtle()
        score.speed(0)
        score.shape("square")
        score.color("white")
        score.penup()
        score.hideturtle()
        score.goto(0,250)
        score.write("score:0, high score:0", align="center", font=("arail",15))
        #--------------------------screen----------------------
        wn= turtle.Screen()
        wn.title("game of snake ")
        wn.bgcolor("blue")
        wn.setup(width = 600 , height = 600)
        wn.tracer(0)
        #----------------------snake head---------------------------
        hd = turtle.Turtle()
        hd.speed(0)
        hd.shape("square")
        hd.color("black")
        #hd.addshape ("C:/games/first/1.png", shape=(10,10))
        hd.shapesize(stretch_wid=1, stretch_len=1, outline=1)
        hd.penup()
        hd.goto(0,0)#the begin from the center
        hd.direction = "stop"

        #----------------------food of snake---------------------------
        fd = turtle.Turtle()
        fd.speed(0)
        fd.shape("circle")
        fd.color("red")
        fd.penup()
        fd.goto(0,100)#the begin from the center
        #-------------------function------------------------
        def go_up():
            hd.direction = "up"
        def go_down():
            hd.direction = "down"
        def go_right():
            hd.direction = "right"
        def go_left():
            hd.direction = "left"

        def move():
            if hd.direction == "up" :
                y = hd.ycor()
                hd.sety(y + 20)
            if hd.direction == "down" :
                y = hd.ycor()
                hd.sety(y - 20)
            if hd.direction == "right" :
                x = hd.xcor()
                hd.setx(x + 20)
            if hd.direction == "left" :
                x = hd.xcor()
                hd.setx(x - 20)

        #---------------------------keyboard-------------------------------
        wn.listen()
        wn.onkeypress(go_up, "Up")
        wn.onkeypress(go_down, "Down")
        wn.onkeypress(go_right, "Right")
        wn.onkeypress(go_left, "Left")
        #------------------------add a part of body-----------------------#
        #------------------------add a part of body-----------------------#
        s=[]
        def body():
            ws = turtle.Turtle()
            ws.speed(0)
            ws.shape("square")
            ws.color("grey")
            ws.penup()
            s.append(ws)
            return (s)

        #--------------------les noisie-------------------------#

        listn = []
        def getNoise():
            for i in range (90,300,20):
                    ns = turtle.Turtle()
                    ns.speed(0)
                    ns.shape("square")
                    ns.color("green")
                    ns.penup()
                    ns.goto(100,i)
                    listn.append(ns)
                        
            for i in range (200,300,20):
                    ns = turtle.Turtle()
                    ns.speed(0)
                    ns.shape("square")
                    ns.color("green")
                    ns.penup()
                    ns.goto(i,100)
                    listn.append(ns)
            for i in range (-90,-300,-20):
                    ns = turtle.Turtle()
                    ns.speed(0)
                    ns.shape("square")
                    ns.color("green")
                    ns.penup()
                    ns.goto(-50,i)
                    listn.append(ns)


            for i in range (-150,-300,-20):
                    ns = turtle.Turtle()
                    ns.speed(0)
                    ns.shape("square")
                    ns.color("green")
                    ns.penup()
                    ns.goto(i,-100)
                    listn.append(ns)
            if hd.distance(fd) < 20 :
                    scoren += 1
                    if scoren > high_score :
                        high_score = scoren
                    score.clear()
                    score.write("score: {}, high score: {}".format(scoren,high_score), align="center", font=("arail",16))
                    fd.goto(random.randint(-270,270), random.randint(-270,270))
                    if  dly >0.2:
                        dly=dly - 0.1
                        
            
        

        #________----______MAIN_________--------_____#



        while True :
            wn.update()

            if hd.distance(fd) < 20 :
                    scoren += 1
                    if scoren > high_score :
                        high_score = scoren
                    score.clear()
                    score.write("score: {}, high score: {}".format(scoren,high_score), align="center", font=("arail",16))
                    fd.goto(random.randint(-270,270), random.randint(-270,270))
                    if  dly >0.2:
                        dly=dly - 0.1
                #-------------------------add elament to body
                    s = body()

            for i in range(len(s)-1,0,-1):
                        x = s[i-1].xcor()
                        y = s[i-1].ycor()
                        s[i].goto(x,y)

            if len(s) > 0:
                        x = hd.xcor()
                        y = hd.ycor()
                        s[0].goto(x,y)

                #-------------------------after exist---------------#
                        
            if hd.xcor() > 270 or hd.xcor() < -270 or hd.ycor() > 270 or hd.xcor() > 270 or hd.ycor() < -270:
                    hd.goto(0,0)
                    hd.direction = "stop"
                    scoren=0
                    high_score = 0
                    score.clear()
                    score.write("score: {}, high score: {}".format(scoren,high_score), align="center", font=("arail",16))
                    act.clear()
                    act.color("red")
                    act.write("LOSER...", align="center", font=("arail",16))
                    dly = 0.5
                    
                    for w in s:
                            w.goto(1000,-1000)
                            s.remove(w)
                            while len(s)>0 :
                                    s[0].goto(1000,-1000)
                                    s.remove(s[0])
                                    
            
            
                                    
             #---------------if snake touch the noise---------------#
            for c in listn:
                if c.distance(hd) < 20 :
                    hd.goto(0,0)
                    hd.direction = "stop"
                    act.clear()
                    act.color("red")
                    act.write("LOSER.", align="center", font=("arail",20))
                    for w in s:
                        w.goto(1000,-1000)
                        s.remove(w)
                        while len(s)>0 :
                                s[0].goto(1000,-1000)
                                s.remove(s[0]) 
            
            if len(s) > 2 :
                dly = 0.5 
                scoren = 0
                high_score =0
                score.clear()
                score.write("score: {}, high score: {}".format(scoren,high_score), align="center", font=("arail",24))
                getNoise()
                
        
            
            if len(s) > 0 :
                act.clear()
                act.color("green")
                act.write("playing...", align="center", font=("arail",16))
                

            if len(s) > 22 :
                  break
            move()
            time.sleep(dly)


        wn.mainloop() 
    #def part2():
          
        
