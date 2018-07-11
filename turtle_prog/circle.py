import turtle

def draw_circle(rad):
    """
    draw circle with given radius
    :param rad:
    :return:
    """
    myTurtle = turtle.Turtle()
    myTurtle.circle(rad)
    turtle.getscreen()._root.mainloop()


def main():
    draw_circle(30)

if __name__ == '__main__':
    main()