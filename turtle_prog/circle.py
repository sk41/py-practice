import turtle

def draw_circle(x, y, color, mTurtle):
    """
    Genetic draw circle given co-ordinates and color
    :param x: co-ordinate
    :param y: co-ordinate
    :param color: color of circle
    :param mTurtle: turle object
    :return:
    """
    mTurtle.color(color)
    mTurtle.penup()
    mTurtle.goto(x, y)
    mTurtle.pendown()
    mTurtle.circle(45)



def draw_olympic(radius):
    """
    draw olympic circles with given radius
    TO-DO color the circles
    :param radius:
    :return: None
    """
    myturtle = turtle.Turtle()
    myturtle.width(5)
    draw_circle(-110, -25, "blue",myturtle)
    draw_circle(0, -25, "black",myturtle)
    draw_circle(110, -25, "red",myturtle)
    draw_circle(-55, -75, "yellow",myturtle)
    draw_circle(55, -75, "green",myturtle)
    
    turtle.done()

def main():
    draw_olympic(30)

if __name__ == '__main__':
    main()
