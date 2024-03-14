import turtle
import random

def draw(t, num_circles):
    turtle.colormode(255)
    colors = ['white']
    for color in colors:
        turtle.bgcolor(color)        
        for _ in range(num_circles):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            t.pencolor(r, g, b)
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