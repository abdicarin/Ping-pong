from turtle  import Turtle, Screen
#scren set up
screen= Screen()
screen.setup(800,600)
screen.bgcolor("black") 
screen.setup
screen.title("Ping pong")
screen.listen()

#pilar figur1
figur1=Turtle()
def upup():
    screen.onkey("Up")
    screen.onkey("Down")

figur1.penup()
figur1.setposition(600,0)
figur1.color("white")
figur1.shape("square")
figur1.color("white")
figur1.shapesize(4,0.5)
#pilar figur2
figur2=Turtle()
figur2.setposition(-600,0)
figur2.color("white")
figur2.shape("square")
figur2.color("white")
figur2.shapesize(4,0.5)

figur3=Turtle()
#bollen
figur3.color("white")
figur3.shape("circle")






screen.exitonclick()
