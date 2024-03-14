import turtle

QUADRANT = 380
axis = (-QUADRANT, QUADRANT)
lines = 3
def draw_axis(t):    
    draw_line(t, (axis[0], 0), (axis[1], 0))
    draw_line(t, (0, axis[1]), (0, axis[0]))
    
def draw_line(t, p1, p2):
    t.penup()
    t.goto(p1[0], p1[1])
    t.pendown()
    t.goto(p2[0], p2[1])

def draw_star(t):
    tam = round(QUADRANT /lines,1)
    x = tam
    y = QUADRANT
    for i in range(lines):
        perce = round((i + 1)/ lines * 100, 2)         
        draw_line(t, (x, 0), (0, y))
        draw_line(t, (0, y), (-x, 0))
        draw_line(t, (-x, 0), (0, -y))
        draw_line(t, (0, -y), (x, 0))
        x += tam 
        y -= tam 
        print(f'\rAvance: {perce}%    ', end='')
    print()

def init():
    width = 600
    height = 600
    turtle.screensize(canvwidth=width, canvheight=height, bg="purple")    

    t = turtle.Turtle()    
    t.pensize(0.3)
    t.pencolor("white")
    t.speed(11)
    return t

def main():
    global lines
    t = init()
    lines = int(input("Número de lneas: "))
    draw_axis(t)
    draw_star(t)
    t.hideturtle()
    
    
    input()

if __name__ == '__main__':
    main()