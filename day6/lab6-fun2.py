#part 2
#2
import turtle
turtle.goto(0,0)

#def up():
 #   print("You pressed the up key")

#turtle.onkey(up, "Up")
#turtle.goto(0,0)
#turtle.listen()
def on_move():
    x, y = turtle.pos()
    if turtle.direction=="Up":
        turtle.goto(x,y+100)
    elif turtle.direction=="Down":
        turtle.goto(x,y-100)
    elif turtle.direction=="Left":
        turtle.goto(x-100,y)
    else:
        turtle.goto(x+100,y)
turtle.direction=None
def up():
    turtle.direction="Up"
    on_move()
turtle.onkey(up, "Up")
turtle.listen()
 
def down():
    turtle.direction="Down"
    on_move()
turtle.onkey(down, "Down")
turtle.listen()

def left():
    turtle.direction= "Left"
    on_move()
turtle.onkey(left, "Left")
turtle.listen()

def right():
    turtle.direction="Right"
    on_move()
turtle.onkey(right, "Right")
turtle.listen()

turtle.mainloop()
        
    
    
        
        
    
    
