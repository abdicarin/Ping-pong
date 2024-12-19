from turtle  import Turtle, Screen
#scren set up
screen= Screen()
screen.setup(800,600)
screen.bgcolor("black") 
screen.setup
screen.title("Ping pong")

#pilar figur1
figur1=Turtle()
def upup():
    screen.onkey("Up")
    screen.onkey("Down")

figur1.penup()
figur1.setposition(-350,0)
figur1.color("white")
figur1.shape("square")
figur1.color("white")
figur1.shapesize(4,0.5)
#pilar figur2
figur2=Turtle()
figur2.setposition(350,0)
figur2.color("white")
figur2.shape("square")
figur2.color("white")
figur2.shapesize(4,0.5)

boll=Turtle()
#bollen
boll.color("white")
boll.shape("circle")
boll.penup()
boll.goto(0,0)



def figur1_up():
    if figur1.ycor() < 250:
        figur1.sety(figur1.ycor() + 20)

def figur1_down():
    if figur1.ycor() > -250:
        figur1.sety(figur1.ycor() - 20)

def figur2_up():
    if figur2.ycor() < 250:
        figur2.sety(figur2.ycor() + 20)

def figur2_down():
    if figur2.ycor() > -250:
        figur2.sety(figur2.ycor() - 20)

screen.listen()
screen.onkeypress(figur1_up, "w")       
screen.onkeypress(figur1_down, "s")    
screen.onkeypress(figur2_up, "Up")      
screen.onkeypress(figur2_down, "Down")


def flyta_upp1():
    ny_plats=figur1.ycor()+20
    figur1.goto(figur1.xcor(), ny_plats)

def flyta_ner1():
    ny_plats=figur1.ycor()-20
    figur1.goto(figur1.xcor(), ny_plats)

# screen.onkey(flyta_upp1, "Up")
# screen.onkey(flyta_ner1, "Down")
screen.listen()

# game = True
# while game == True:
#     flyta_boll()

  






screen.exitonclick()
