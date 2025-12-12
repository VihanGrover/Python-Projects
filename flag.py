import turtle
pen=turtle.Turtle()
paper=turtle.Screen()
pen.speed(5)
pen.pensize(3)

# Stick of the Flag
pen.up()
pen.goto(-100,-150)
pen.left(90)
pen.down()
pen.goto(-100,100)

# Flag Shape
for i in range(1):
  pen.right(90)
  pen.forward(200)
  pen.right(90)
  pen.forward(100)
  pen.right(90)
  pen.forward(200)


# Orange Part
pen.up()
pen.goto(-100,65)
pen.down()
pen.fillcolor("orange")
pen.begin_fill()
pen.goto(100,65)
pen.goto(100,100)
pen.goto(-100,100)
pen.end_fill()

# Green Part
pen.up()
pen.goto(-100,30)
pen.fillcolor("green")
pen.begin_fill()
pen.down()
for i in range(1):
  pen.right(90)
  pen.right(90)
  pen.forward(200)
  pen.right(90)
  pen.forward(30)
  pen.right(90)
  pen.forward(200)
  pen.right(90)
  pen.forward(30)
pen.end_fill()

# Small Circle
pen.up()
pen.goto(1,48)
pen.fillcolor("blue")
pen.begin_fill()
pen.down()
pen.circle(4)
pen.end_fill()

# Big Circle
pen.up()
pen.goto(10,48)
pen.down()
pen.circle(13)
 

# Lines Going Between
pen.up()
pen.goto(-3,48)
pen.down()
pen.pensize(1)
for i in range(12):
  pen.forward(10)
  pen.right(90)
  pen.right(90)
  pen.forward(10)
  pen.right(30)

pen.hideturtle()
turtle.done()