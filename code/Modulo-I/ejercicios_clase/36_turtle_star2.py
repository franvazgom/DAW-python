import turtle

QUADRANT = 500
LINES = 3
# p1 es una tupla con las coordenadas de x y y  p1 = (x,y) 
def draw_line(t, p1, p2):
    t.penup()
    t.goto(p1[0], p1[1])
    t.pendown()
    t.goto(p2[0], p2[1])
    
def draw_axis(t):
    draw_line(t, (-QUADRANT, 0), (QUADRANT, 0))
    draw_line(t, (0, QUADRANT), (0, -QUADRANT))

def draw_star(t):
    tam = round(QUADRANT / LINES, 1)
    x = tam
    y = QUADRANT
    for _ in range(LINES):
        draw_line(t, (x,0), (0,y))        
        draw_line(t, (0,y), (-x,0))
        draw_line(t, (-x,0), (0,-y))
        draw_line(t, (0,-y), (x,0))
        x += tam
        y -= tam


def main():   
    global LINES
    LINES = int(input("Numero de lineas: ")) 
    turtle.screensize(canvwidth=600, canvheight=600, bg="purple")   
    t = turtle.Turtle()
    t.pencolor("white")
    t.pensize(0.5)
    t.speed(11)            
    #Se dibuja los ejes X y Y
    draw_axis(t)
    draw_star(t)
    input()

if __name__ == '__main__':
    main()