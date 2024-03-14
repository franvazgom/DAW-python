import turtle

def draw(t, num_circles):
    colors = ['white', 'green', 'blue', 'yellow']
    for color in colors:
        t.pencolor(color)
        for _ in range(num_circles):
            t.circle(180)
            t.right(360/num_circles)

def main():
    turtle.screensize(canvwidth=600, canvheight=600, bg="purple")
    t = turtle.Turtle()        

    t.pensize(1)    
    t.speed(100)
    t.pendown()
    
    num = int(input("Número de circulos: "))
    draw(t, num)
    t.hideturtle()
    input()

if __name__ == '__main__':
    main()