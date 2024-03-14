import turtle

def pinta_triangulo(t, steps, ang):
    t.forward(steps)
    t.right(ang)
    t.forward(steps)

def pinta_estrella(t, steps, picos):
    alpha = 360/picos
    beta = 90 - alpha
    rotacion = 180 - beta
    rotacion = 360 / picos + 90
    for _ in range(picos):
        t.left(90)
        pinta_triangulo(t, steps, rotacion)

def main():
    t = turtle.Turtle()

    t.pensize(2)
    t.pencolor("blue")
    t.speed(100)
    t.pendown()
    
    pinta_estrella(t, 100, 8)
    input()

if __name__ == '__main__':
    main()