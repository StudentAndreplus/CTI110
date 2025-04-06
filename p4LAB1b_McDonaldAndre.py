import turtle

pen = turtle.Turtle()
pen.pensize(5)
pen.speed(2)
pen.color("salmon")


pen.penup()
pen.forward(20)
pen.left(75)
pen.pendown()
pen.forward(100)
pen.right(150)
pen.forward(100)
pen.backward(50)
pen.right(75)
pen.pendown()
pen.forward(25)
pen.penup()

pen.backward(25)
pen.right(90)
pen.forward(50)
pen.left(90)



pen.setheading(90)
pen.pendown()
pen.forward(100)
pen.right(135)
pen.forward(70)
pen.left(90)
pen.forward(70)
pen.right(135)
pen.forward(100)
pen.penup()



turtle.exitonclick()