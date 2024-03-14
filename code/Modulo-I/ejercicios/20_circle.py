import turtle


def main():
    turtle.screensize(canvwidth=600, canvheight=600, bg="purple")
    t = turtle.Turtle()        

    t.pensize(1)
    t.pencolor("white")
    t.speed(100)
    t.pendown()
    
    num = int(input("Número de circulos: "))
    for _ in range(num):
        t.circle(180)
        t.right(360/num)
    
    input()

if __name__ == '__main__':
    main()