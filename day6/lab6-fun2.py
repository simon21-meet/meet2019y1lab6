#part 2
#2
import turtle
turtle.goto(0,0)

#def up():
 #   print("You pressed the up key")

#turtle.onkey(up, "Up")
#turtle.goto(0,0)
#turtle.listen()
turtle.direction=None
def up():
    turtle.direction="Up"
    print("you pressed the up key")
turtle.onkey(up, "Up")
turtle.listen()
def on_move():
    
