import turtle
def small_traingle(bo,n):
    """
    this is to draw smallest triangle.
    :param bo:
    :param n:
    :return none:
    """
    bo.right(60)
    bo.forward(int(n/4))
    bo.right(120)
    bo.forward(int(n/4))
    bo.right(120)
    bo.forward(int(n/4))

def triangle_draw(board,n):
    """
     this is to draw inside design
    :param board:
    :param n:
    :return none:
    """
    board.forward(n)  # draw base
    board.left(120)
    board.forward(n)
    board.left(120)
    board.forward(n)
    board.left(180)
    board.forward(int(n/2))
    board.right(60)
    board.forward(int(n/2))
    board.right(120)
    board.forward(int(n/2))
    board.right(120)
    board.forward(int(n/2))

    board.left(180)
    board.forward(int(n/4))
    small_traingle(board,n)
    board.left(120)
    board.forward(int(n/4))
    board.right(60)
    board.forward(int(n/4))
    small_traingle(board,n)
    board.right(120)
    board.forward(int(n/4))
    board.right(60)
    board.forward(int(n/2))
    small_traingle(board,n)

def draw_design(brd,n):
    """
    this is to draw a big triangle
    :param brd:
    :return:
    """
    #n=100
    triangle_draw(brd,n)
    brd.left(120)
    brd.forward(int((3*n)/4))
    triangle_draw(brd,n)
    brd.left(120)
    brd.forward(int((3*n)/4))
    triangle_draw(brd,n)

def main():
    n = int(input("enter the size").strip())
    brd = turtle.Turtle()
    brd.color('green','yellow')
    brd.begin_fill()
    draw_design(brd,n)
    brd.end_fill()
    turtle.done()

if __name__ == '__main__':
    main()



