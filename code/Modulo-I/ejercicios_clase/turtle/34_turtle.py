import turtle

def main():
    t = turtle.Turtle()
    t.pensize(2)
    t.pencolor("blue")
    t.speed(5)
    t.forward(400)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(400)
    t.right(90)
    t.pencolor("purple")
    t.forward(200)
    t.left(90)
    t.penup()
    t.forward(200)
    t.pendown()
    t.pensize(5)
    t.forward(200)
    input()
if __name__ == '__main__':
    main()
