import turtle
import random
import math

def drawboard():
    turtle.setworldcoordinates(0,0,1000,1000)
    turtle.speed(0)
    turtle.goto(0,0) #draw first stick figure
    turtle.left(45)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.penup()
    turtle.goto(35,35)
    turtle.left(135)
    turtle.pendown()
    turtle.forward(75)
    turtle.penup()
    turtle.goto(0,85)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(75)
    turtle.penup()
    turtle.goto(35,110)
    turtle.pendown()
    turtle.circle(30)
    turtle.penup()
    turtle.goto(925,0) #draw second stick figure
    turtle.left(45)
    turtle.pendown()
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.penup()
    turtle.goto(960,35)
    turtle.left(135)
    turtle.pendown()
    turtle.forward(75)
    turtle.penup()
    turtle.goto(1000,85)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(75)
    turtle.penup()
    turtle.goto(960,110)
    turtle.right(180)
    turtle.pendown()
    turtle.circle(30)
    turtle.penup()

def setnums():
    global X1,Xi,Y1,Yi
    Xi=random.randint(1,61) #set random numbers for initial variables
    Yi=random.randint(0,51)
    X1=random.randint(62,121)
    Y1=random.randint(0,51)
    distance=X1-Xi #find distance between players
    turtle.goto(110,35)
    turtle.write("Xi: "+str(Xi)+" Yi: "+str(Yi)) #write initial variables and distance
    turtle.goto(450,500)
    turtle.write("Distance to receiver: "+str(distance))
    print("Distance to receiver: "+str(distance))
    turtle.hideturtle()

def getinput(): #get angle and velocity guess from user
    global A, V
    angle=int(input("Choose an angle(from 0-90 degrees): "))
    A=(math.pi * angle) / 180 #gotta fix the angle or else Vx and Vy are wrong
    V=int(input("Choose a velocity: "))

def calculate(A,V): #calculations for velocity vectors as well as detination coords using user guess
    global X2, Y2
    g=9.8
    Vx=V*math.cos(A)
    Vy=V*math.sin(A)
    for i in range(0,100):
        t=i/10 #calculate for every tenth of a second for up to ten seconds
        X2=Xi+Vx*t
        Y2=Yi+Vy*t-g*pow(t,2)/2
        if Y2<=0:
            break
        if X2>=X1:
            break
    

def checkpass(X1, X2, Y1, Y2): #check the pass
    if X1==X2 or X1==X2+1 or X1==X2-1:
        if Y1==Y2 or Y1==Y2+1 or Y1==Y2-1:
            return True
        elif Y1<Y2:
            print("Too short!")
            return False
        elif Y1>Y2:
            print("Too far!")
            return False
    elif X1<X2:
        print("Too far!")
        return False
    elif X1>X2:
        print("Too short!")
        return False

def game():
    drawboard()

    setnums()
    trycount=3 #you get three tries

    while True:
        getinput()
        calculate(A,V)
    
        if checkpass(X1,X2,Y1,Y2)==True:
            print("Pass complete!")
            return
        elif trycount>0:
            trycount=trycount-1
            print("Tries remaining: " + str(trycount))
            if trycount==0:
                gameplay=input("Game over! Press Enter.")
                return
def main():
    while True:
        game()
        
        gameplay=input("Play again? Y or N. ")
        if gameplay=='N' or gameplay=='n':
            return
        else:
            turtle.reset()
main()