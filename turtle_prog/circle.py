import turtle

def draw_circle(rad):
    """
    draw circle with given radius
    :param rad:
    :return:
    """
    myTurtle = turtle.Turtle()
    myTurtle.circle(rad)
    #turtle.getscreen()._root.mainloop()

def draw_olympic(radius):
    """
    draw olympic circles with given radius
    TO-DO color the circles
    :param radius:
    :return: None
    """
    myTurtle = turtle.Turtle(shape="circle")
    myTurtle.circle(radius)
    myTurtle.penup()
    myTurtle.setposition(-120, 0)
    myTurtle.pendown()
    myTurtle.circle(radius)

    myTurtle.penup()
    myTurtle.setposition(60, 60)
    myTurtle.pendown()
    myTurtle.circle(radius)

    myTurtle.penup()
    myTurtle.setposition(-60, 60)
    myTurtle.pendown()
    myTurtle.circle(radius)

    myTurtle.penup()
    myTurtle.setposition(-180, 60)
    myTurtle.pendown()
    myTurtle.circle(radius)

    turtle.getscreen()._root.mainloop()

def main():
    draw_circle(30)
    draw_olympic(30)

if __name__ == '__main__':
    main()