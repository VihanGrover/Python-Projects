# functions - 

# built- in functions - .up(), .down(), .color() , .pensize(), input()
# user defined functions 

import turtle

pen = turtle.Turtle()
screen = turtle.Screen()

pen.speed(8)

# functions in python- REUSABILITY and to keep code organized 
pen_size = input("What size of the pen do you want?")

# create
def square(x,y,color_for_square): # parameters  
  """ this functions makes a square """
  pen.up()
  pen.goto(x,y)
  pen.down()
  # pen.color(color_for_square)
  pen.fillcolor(color_for_square)
  pen.pensize(pen_size) 
  pen.begin_fill()
  for i in range(4):
    pen.forward(100)
    pen.right(90)
  pen.end_fill()
    
# calling the functions 
square(-50,50,"blue",)# arguments for the parameters

square(20,20,"green")

square(-100,100,"red")

turtle.done()