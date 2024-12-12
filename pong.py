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
def flyta_boll():
    boll_x=boll.xcor()+10
    boll_y=boll.ycor()+10
    boll.goto(boll_x,boll_y)




def flyta_upp1():
    ny_plats=figur1.ycor()+20
    figur1.goto(figur1.xcor(), ny_plats)

screen.onkey(flyta_upp1, "Up")
screen.listen()

game = True
while game == True:
    flyta_boll()

def flyta_upp1():
    ny_plats=figur1.ycor()+20
    figur1.goto(figur1.xcor(), ny_plats)

def flyta_ner1():
    ny_plats=figur1.ycor()-20
    figur1.goto(figur1.xcor(), ny_plats)

screen.onkey(flyta_upp1, "Up")
screen.onkey(flyta_ner1, "Down")
screen.listen()

game = True
while game == True:
    flyta_boll()

  






screen.exitonclick()
