import turtle

def main():     
    num = int(input("Numero de circulos: "))
    turtle.screensize(canvwidth=600, canvheight=600, bg="purple")   
    t = turtle.Turtle()
    t.pencolor("white")
    t.pensize(0.5)
    t.speed(11)            
    
    for _ in range(num): 
        t.circle(180)
        t.right(360/num)        
    t.hideturtle()
    input()

if __name__ == '__main__':
    main()