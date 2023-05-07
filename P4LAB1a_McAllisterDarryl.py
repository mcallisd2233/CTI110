import turtle
  
t = turtle.Turtle()
 
s = int(input("Enter size of the shapes: "))
 
for _ in range(4):
  t.forward(s) 
  t.left(90)

for _ in range(3):
    t.forward(s)
    t.left(120)
 

