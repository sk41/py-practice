import turtle

def draw_circle(mTurtle,x, y, color,r):
    """
    Genetic draw circle given co-ordinates and color
    :param mTurtle: turle object
    :param x: co-ordinate
    :param y: co-ordinate
    :param color: color of circle
    :param r : radius of circle
    :return:
    """
    mTurtle.color(color)
    mTurtle.penup()
    mTurtle.goto(x, y)
    mTurtle.pendown()
    mTurtle.circle(r)



def draw_olympic(radius):
    """
    draw olympic circles with given radius
    TO-DO color the circles
    :param radius:
    :return: None
    """
    myturtle = turtle.Turtle()
    myturtle.width(5)
    draw_circle(myturtle,-110, -25, "blue",radius)
    draw_circle(myturtle,0, -25, "black",radius)
    draw_circle(myturtle,110, -25, "red",radius)
    draw_circle(myturtle,-55, -75, "yellow",radius)
    draw_circle(myturtle,55, -75, "green",radius)
    
    turtle.done()

def main():
    draw_olympic(45)

if __name__ == '__main__':
    main()
