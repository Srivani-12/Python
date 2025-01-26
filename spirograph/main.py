import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,225)
    g = random.randint(0,225)
    b = random.randint(0,225)
    color = (r,g,b)
    return color

tim.speed("fastest")
def draw_circle(radius,tilt_angle):
    tim.setheading(tilt_angle)
    tim.circle(radius)
    tim.color(random_color())
    

def draw_spirograph(radius,num_of_circle):
    for i in range(num_of_circle):
        tilt_angle = i*(360/num_of_circle)
        draw_circle(radius,tilt_angle)
        tim.right(360/num_of_circle)
        

radius = 100
num_of_circle = 72

draw_spirograph(radius,num_of_circle)

tim.hideturtle()
screen = t.Screen()
screen.mainloop()
