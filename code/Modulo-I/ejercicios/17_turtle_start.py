import turtle

def pinta_triangulo(t, steps, ang):
    t.forward(steps)
    t.right(ang)
    t.forward(steps)

def main():
    t = turtle.Turtle()

    t.pensize(2)
    t.pencolor("blue")
    t.speed(100)
    t.pendown()
    ang = 0

    t.left(30)
    pinta_triangulo(t, 200, 150)
    t.left(90)
    pinta_triangulo(t, 200, 150)
    t.left(90)
    pinta_triangulo(t, 200, 150)
    t.left(90)
    pinta_triangulo(t, 200, 150)
    t.left(90)
    pinta_triangulo(t, 200, 150)
    t.left(90)
    pinta_triangulo(t, 200, 150)
    t.left(90)
    input()

if __name__ == '__main__':
    main()