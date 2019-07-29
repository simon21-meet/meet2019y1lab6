
import turtle

x = 0
while x<300:
   y = x**2/300 #x**2 is the same as x*x
   turtle.goto(x, y)
   x = x + 1
  
num_pts=5 #number sides to your drawing!
for i in range (num_pts):
   turtle.left(360/num_pts)
   turtle.forward(100)
 
turtle.tracer(1)
rounds = 10
size = 10
mike = turtle.clone()
steve = turtle.clone()
turtle.bgcolor("white")
turtle.hideturtle()
mike.color("gold")
steve.color("blue")
steve.goto(5,5)
while True:
    mike.forward(size)
    mike.left(90)
    steve.forward(-size)
    steve.left(-90)
    size += 10


turtle.mainloop()

result=[]
for count in range (1, 50):
   if count % 3 == 0:
      result.append("Fizz")
   else:
      result.append(count)

print(result)

