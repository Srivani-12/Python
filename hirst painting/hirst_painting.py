import turtle as t
import random


t.colormode(255)
tim = t.Turtle()

color_list = [(234, 236, 241), (241, 236, 228), (243, 235, 240), (235, 243, 240), (198, 162, 111), (151, 59, 80), (54, 103, 126), (149, 174, 190), (150, 87, 64), (133, 32, 53), (218, 203, 124), (187, 154, 163), (26, 49, 64), (71, 29, 41), (179, 162, 50), (184, 87, 104), (55, 33, 29), (174, 186, 183), (73, 101, 100), (187, 92, 84), (183, 197, 191), (215, 179, 188), (116, 39, 35), (30, 76, 90), (56, 59, 83), (180, 190, 206), (219, 179, 173), (22, 46, 45), (170, 198, 207), (41, 79, 78)]
tim.speed('fastest')
tim.penup()

# setting tim from middle of the screen to bottom of the screen
tim.setheading(220)
tim.forward(250)
tim.setheading(0)

no_of_dots = 100
for dot in range(1,no_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if dot % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen=t.Screen()
screen.exitonclick()