import turtle
happy=turtle.Screen()
happy.bgpic("back.gif")
turtle=turtle.Turtle()
turtle.shape("turtle")
turtle.width(11)

  
def mov(x,y):
   turtle.up()
   turtle.setposition(0,0)
   turtle.setheading(90)
   turtle.lt(90)
   turtle.fd(x)
   turtle.rt(90)
   turtle.fd(y)
   turtle.pendown()

#letters
def A():
  turtle.rt(16)
  turtle.forward(60)
  turtle.rt(150)
  turtle.fd(60)
  turtle.backward(30)
  turtle.rt(105)
  turtle.fd(15)   
  
  
def B():
   turtle.forward(70)
   turtle.rt(90)
   for i in range(18):
      turtle.rt(9)
      turtle.fd(3)
   for i in range(18):
      turtle.rt(13)
      turtle.backward(4) 


def D():
   turtle.fd(60)
   turtle.rt(90)
   turtle.fd(9)
   for i in range(13):
      turtle.rt(14)
      turtle.fd(7.3)  

       
       
def Y():
   turtle.fd(40)
   turtle.left(47)
   turtle.fd(30)
   turtle.backward(30)
   turtle.rt(90)
   turtle.fd(30)
   


def H():
   turtle.fd(60)
   turtle.backward(30)
   turtle.rt(90)
   turtle.fd(30)
   turtle.lt(90)
   turtle.fd(30)
   turtle.backward(60)
   
   
def P():
   turtle.fd(60)
   turtle.rt(90)
   turtle.fd(7)
   for i in range(8):
       turtle.rt(20)
       turtle.fd(5)
       



# base of cake
turtle.speed(200)
turtle.width(6)
turtle.color("white")
mov(0,-55)
turtle.begin_fill()
turtle.lt(65)
turtle.fd(120)
turtle.rt(30)
turtle.fd(17)
turtle.rt(35)
turtle.fd(80)
for i in range(3):
    turtle.rt(30)
    turtle.fd(17)
turtle.fd(17)
turtle.rt(15)
turtle.fd(17)
turtle.rt(15)
turtle.fd(30)
turtle.rt(20)
turtle.fd(35)

turtle.lt(100)

turtle.fd(35)
turtle.rt(20)
turtle.fd(30)
turtle.rt(15)
turtle.fd(17)
turtle.rt(15)
turtle.fd(17)
for i in range(3):
    turtle.fd(17)
    turtle.rt(30)
turtle.fd(80)
turtle.rt(35)
turtle.fd(17)
turtle.rt(30)  
turtle.fd(122)
turtle.lt(65)
turtle.end_fill()


# cake topping
turtle.color("#1a0d00")
mov(0,-55)
turtle.lt(65)
turtle.fd(120)
turtle.rt(30)
turtle.fd(17)
turtle.rt(35)
turtle.fd(80)
for i in range(3):
    turtle.rt(30)
    turtle.fd(17)
turtle.fd(17)
turtle.rt(15)
turtle.fd(17)
turtle.rt(15)
turtle.fd(30)
turtle.rt(20)
turtle.fd(35)

turtle.lt(100)

turtle.fd(35)
turtle.rt(20)
turtle.fd(30)
turtle.rt(15)
turtle.fd(17)
turtle.rt(15)
turtle.fd(17)
for i in range(3):
    turtle.fd(17)
    turtle.rt(30)
turtle.fd(80)
turtle.rt(35)
turtle.fd(17)
turtle.rt(30)  
turtle.fd(122)
turtle.lt(65)



turtle.color("#331a00")
mov(-3,25)
turtle.begin_fill()
turtle.lt(65)
turtle.fd(124)
for i in range(5):
    turtle.rt(30)
    turtle.fd(17)
turtle.fd(17)
turtle.rt(15)
turtle.fd(17)
turtle.rt(15)
turtle.fd(30)
turtle.rt(20)
turtle.fd(35)

turtle.lt(90)

turtle.fd(35)
turtle.rt(20)
turtle.fd(30)
turtle.rt(15)
turtle.fd(17)
turtle.rt(15)
turtle.fd(17)
for i in range(5):
    turtle.fd(17)
    turtle.rt(30)
turtle.fd(124)
turtle.end_fill()



turtle.color("#1a0d00")
turtle.width(10)
mov(-3,25)
turtle.lt(65)
turtle.fd(124)
for i in range(5):
    turtle.rt(30)
    turtle.fd(17)
turtle.fd(17)
turtle.rt(15)
turtle.fd(17)
turtle.rt(15)
turtle.fd(30)
turtle.rt(20)
turtle.fd(35)

turtle.lt(90)

turtle.fd(35)
turtle.rt(20)
turtle.fd(30)
turtle.rt(15)
turtle.fd(17)
turtle.rt(15)
turtle.fd(17)
for i in range(5):
    turtle.fd(17)
    turtle.rt(30)
turtle.fd(124)


# cake layers... brown color
turtle.width(6)
mov(0,-30)
turtle.lt(65)
turtle.fd(120)
turtle.rt(30)
turtle.fd(17)
mov(-3,-30)
turtle.rt(65)
turtle.fd(120)
turtle.lt(30)
turtle.fd(17)
mov(0,-5)
turtle.lt(65)
turtle.fd(120)
turtle.rt(30)
turtle.fd(17)
mov(-3,-5)
turtle.rt(65)
turtle.fd(120)
turtle.lt(30)
turtle.fd(17)
turtle.width(3)
mov(30,30)
turtle.fd(2)
mov(60,10)
turtle.fd(2)
mov(110,35)
turtle.fd(2)
mov(30,-10)
turtle.fd(2)
mov(50,0)
turtle.fd(2)
mov(80,-15)
turtle.fd(2)
mov(-30,30)
turtle.fd(2)
mov(-60,10)
turtle.fd(2)
mov(-110,35)
turtle.fd(2)
mov(-30,-10)
turtle.fd(2)
mov(-50,0)
turtle.fd(2)
mov(-80,-15)
turtle.fd(2)

# candles
turtle.width(6)
turtle.speed(6)
turtle.color("yellow")
mov(100,105)
turtle.fd(60)
turtle.width(1)
turtle.color("black")
mov(100,165)
turtle.fd(5)
mov(100,170)
turtle.color("#ff9900")
x=12
while x>0:
    turtle.width(x)
    turtle.fd(2)
    x-=2
turtle.color("#ff0066")
turtle.width(6)
mov(-100,105)
turtle.fd(60)
turtle.width(1)
turtle.color("black")
mov(-100,165)
turtle.fd(5)
mov(-100,170)
turtle.color("#ff9900")
x=12
while x>0:
    turtle.width(x)
    turtle.fd(2)
    x-=2 

# love on cake
turtle.width(4)
turtle.color("#cc0000")
mov(35,55)
turtle.speed(3)
turtle.fd(20)
turtle.backward(20)
turtle.rt(90)
turtle.fd(10)

mov(-3,65)
turtle.speed(3)
for i in range(30):
  turtle.lt(12)
  turtle.fd(2)

mov(-15,55)
turtle.speed(3)
turtle.lt(20)
turtle.fd(21)
turtle.backward(21)
turtle.rt(40)
turtle.fd(21)

mov(-30,55)
turtle.speed(3)
turtle.fd(20)
turtle.backward(20)
turtle.rt(90)
turtle.fd(10)
turtle.rt(180)
turtle.fd(10)
turtle.rt(90)
turtle.fd(10)
turtle.rt(90)
turtle.fd(10)
turtle.rt(180)
turtle.fd(10)
turtle.rt(90)
turtle.fd(10)
turtle.rt(90)
turtle.fd(10)
turtle.backward(10)



# happy
turtle.speed(6)
turtle.width(9)
turtle.color("#ff0066")
mov(300,130)
turtle.width(9)
H()
turtle.speed(8)
turtle.width(5)
mov(260,130)
A()
mov(220,130)
P()
mov(190,130)
P()
mov(140,130)
Y()

# b'day'
turtle.speed(6)
turtle.width(9)
turtle.color("yellow")
mov(-150,130)
B()
mov(-190,180)
turtle.fd(10)
turtle.speed(8)
turtle.width(5)
mov(-210,130)
D()
mov(-250,130)
A()
mov(-310,130)
Y()

#emoji
turtle.width(11)
turtle.speed(100)
turtle.color("yellow")
mov(-230,-140)
turtle.begin_fill()
turtle.lt(90)
for x in range(30):
  turtle.fd(15)
  turtle.rt(12)
turtle.end_fill()
turtle.color("dark orange")
mov(-230,-140)
turtle.lt(90)
for x in range(30):
  turtle.fd(15)
  turtle.rt(12)
turtle.color("#4d2800")
turtle.width(16)
mov(-190,-65)
turtle.fd(1)
turtle.color("yellow")
turtle.width(6)
mov(-190,-62)
turtle.fd(1)
turtle.color("#4d2800")
turtle.width(6)
mov(-175,-50)
turtle.rt(30)
for x in range(8):
  turtle.rt(6)
  turtle.fd(3)
mov(-255,-50)
turtle.rt(90)
for x in range(6):
  turtle.rt(6)
  turtle.fd(4)
turtle.width(9)
mov(-255,-65)
turtle.rt(75)
for x in range(10):
  turtle.rt(4)
  turtle.fd(1)
mov(-220,-85)
turtle.width(4)
turtle.fd(2)
turtle.rt(80)
for x in range(30):
  turtle.fd(0.8)
  turtle.rt(6)
mov(-222,-98)
turtle.rt(90)
for x in range(30):
  turtle.rt(6)
  turtle.fd(0.8)
turtle.color("red")
mov(-269,-129)
turtle.begin_fill()
turtle.lt(30)
for x in range(8):
  turtle.fd(5)
  turtle.rt(5)
for x in range(30):
  turtle.rt(6)
  turtle.fd(1.8)
turtle.lt(125)
for x in range(30):
  turtle.fd(1.8)
  turtle.rt(6)
for x in range(8):
  turtle.rt(5)
  turtle.fd(5)
turtle.end_fill()

#star
mov(260,-100)
turtle.width(1)
turtle.color("#ff0066")
turtle.speed(20)
for i in range(60):
  turtle.fd(i*4)
  turtle.rt(144)
mov(235,-5000)
happy.exitonclick()