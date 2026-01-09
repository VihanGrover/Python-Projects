import turtle
pen=turtle.Turtle()
paper=turtle.Screen()
pen.speed(0)
pen.pensize(3)
paper.setup(width=730, height=800)
# Width halfway = 365
# Height halfway = 400

# Sky
color_sky = input("What color do you want the sky to be?")
paper.bgcolor(color_sky)

# Sun
color_of_sun = input("What color do you want the sun to be?")
pen.color(color_of_sun)
pen.up()
pen.goto(0,200)
pen.begin_fill()
pen.down()
pen.circle(50)
pen.end_fill()
pen.up()
pen.goto(0,250)
pen.down()
for i in range(19):
    pen.right(90)
    pen.forward(75)
    pen.back(75)
    pen.right(5)

# Sand Dunes
pen.up()
pen.goto(-365,-200)
pen.down()
pen.fillcolor("tan")
pen.pencolor("tan")
pen.begin_fill()
pen.goto(-365,-400)
pen.goto(365,-400)
pen.goto(365,-200)
pen.goto(-365,-200)
pen.up()
pen.goto(-200,-200)
pen.down()
pen.goto(-365,-50)
pen.goto(-365,-200)
pen.goto(-200,-200)
pen.up()
pen.goto(200,-200)
pen.down()
pen.goto(365,50)
pen.goto(365,-200)
pen.goto(200,-200)
pen.end_fill()

# Cactus (Actual Shape)
pen.up()
pen.goto(-100,0)
pen.down()
pen.pencolor("green")
pen.fillcolor("green")
pen.begin_fill()
pen.left(90)
for i in range(18):
    pen.forward(14)
    pen.right(10)
pen.forward(200)
pen.right(87.5)
pen.forward(125)
pen.right(83)
pen.forward(200)
pen.up()
pen.goto(-90,-100)
pen.left(90)
pen.down()
square = 1
while square < 3:
    pen.forward(100)
    pen.right(90)
    square = square + 1
pen.forward(25)
pen.right(90)
pen.forward(75)
pen.left(90)
pen.forward(73)
pen.end_fill()
# Cactus (Spiky Part)
def cactus_spikes(x,y):
    """This function makes spikes on a cactus"""
    pen.up()
    pen.goto(x,y)
    pen.down()
    pen.pencolor("lightgreen")
    pen.fillcolor("lightgreen")
    pen.begin_fill()
    pen.circle(3)

# Calling the Spikes
cactus_spikes(0,0)
cactus_spikes(-50,-50)
cactus_spikes(-25,-100)
cactus_spikes(-50,-130)
cactus_spikes(35,-180)
cactus_spikes(-50,-185)
cactus_spikes(50,-35)
cactus_spikes(10,45)
cactus_spikes(-50,-50)
cactus_spikes(10,-150)
cactus_spikes(40,-75)
cactus_spikes(40,-120)
cactus_spikes(-35,50)
cactus_spikes(-50,20)
cactus_spikes(0,-50)
cactus_spikes(-10,-75)
cactus_spikes(-75,-190)
cactus_spikes(-75,-100)
cactus_spikes(-75,-35)

cactus_spikes(-125,-90)
cactus_spikes(-150,-95)
cactus_spikes(-175,-75)
cactus_spikes(-180,-50)
cactus_spikes(-175,-25)

# Oasis
pen.up()
pen.goto(0,-225)
pen.color("light blue")
pen.begin_fill()
oasis = 1
while oasis < 37:
    pen.forward(14)
    pen.right(10)
    oasis = oasis + 1
pen.end_fill()

# Birds
def making_birds(x,y):
    """This function makes birds"""
    pen.up()
    pen.goto(x,y)
    pen.down()
    pen.color("black")
    pen.pensize(5)
    for i in range(5):
        pen.forward(14)
        pen.right(10)
    pen.right(200)
    for i in range(5):
        pen.forward(14)
        pen.right(10)

# Calling the Birds
making_birds(-300,300)
making_birds(-275,0)
making_birds(330,300)
making_birds(185,85)



turtle.done()
pen.hideturtle()