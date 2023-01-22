import turtle

s = turtle.Screen()
s.bgcolor('orange')
# s.bgpic('mario.png')

p = turtle.Pen()
p.shape('turtle')
p.shapesize(3)
p.pensize(4)
p.pencolor('red')

p.fillcolor('green')
p.begin_fill()
p.forward(100)
p.left(120)
p.forward(100)
p.left(120)
p.forward(100)
p.end_fill()

p.hideturtle()
s.exitonclick()

# exercise 1
'''
کشیدن مربع توخالی
کشیدن مربع توپر با رنگ آبی
کشیدن پنج ضلعی توپر بارنگ قرمز

'''
