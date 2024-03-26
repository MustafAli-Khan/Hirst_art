import random
import turtle as t

def new_dots():
 Annu.setheading(90)
 Annu.forward(50)
 Annu.setheading(180)
 Annu.forward(500)
 Annu.setheading(0)

t.colormode(255)
Annu = t.Turtle()
Annu.penup()
Annu.hideturtle()
Annu.speed("fastest")


color_list = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188),
 (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149),
 (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16),
 (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)]

Annu.setheading(225)
Annu.forward(300)
Annu.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
 Annu.dot(20, random.choice(color_list))
 Annu.forward(50)
 if dot_count % 10 == 0:
  new_dots()



# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg',30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_rgb =(r, g, b)
#     rgb_colors.append(new_rgb)
# print(rgb_colors)


screen = t.Screen()
screen.exitonclick()


