import turtle

def pintaCuadro(t, lado, ang):
    for _ in range(4):
        t.forward(lado)
        t.right(90 + ang)    

def main():
    t = turtle.Turtle()

    t.pensize(2)
    t.pencolor("blue")
    t.speed(100)
    t.pendown()
    ang = 0
    for _ in range(10):
        pintaCuadro(t, 150, ang)
        ang += 1
        
    # for steps in range(20, 100):
    #     for c in ('blue', 'red', 'green'):
    #         t.color(c)
    #         t.forward(steps)
    #         t.right(20)


    input()

if __name__ == '__main__':
    main()