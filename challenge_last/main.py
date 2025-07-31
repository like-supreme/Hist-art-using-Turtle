from turtle import Turtle, Screen
import random
import turtle as t
"""
import colorgram
import os

rgb_colors = []

# 🔧 Bu dosyanın bulunduğu dizine göre tam yol oluştur
current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "image.jpg")

colors = colorgram.extract(image_path, 30)

for color in colors:
    rgb = color.rgb
    rgb_colors.append((rgb.r, rgb.g, rgb.b))

print(rgb_colors)
# the above code is used to extract colors from an image
"""
color_list= [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
tim = Turtle()
tim.shape("arrow")
tim.speed("fast")
t.colormode(255)
tim.penup()
tim.goto(0,0)
tim.pendown()
coor_x = 0
coor_y = 0

while coor_y < 500:
    for i in range(10):
    
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()
    coor_y += 50
    coor_x = tim.position()[0]
    tim.penup()
    tim.goto(0 , coor_y)
    tim.pendown()
    if coor_y > 500 or coor_x > 500:
        break


screen = Screen()
screen.exitonclick()