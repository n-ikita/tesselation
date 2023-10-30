"""
Case-study №3
Students: Kuznetsov N. 70%
          Shishko S.   65%
"""


import turtle
import math
def draw_hexagon(x, y, side_len, color):
    joe = turtle.Turtle()
    joe.hideturtle()
    joe.up()
    joe.speed(5000)
    joe.color('black')
    joe.fillcolor(color)
    joe.goto(x, y)
    joe.down()
    joe.begin_fill()
    joe.left(30)
    joe.forward(side_len)

    for i in range(6):
        joe.left(60)
        joe.forward(side_len)
    joe.end_fill()
    joe.up()

def get_num_hexagons():
    print('Введите количество шестиугольников, располагаемых в ряд:')
    while 1:
        try:
            num = int(input())
            if 4<=num<=20:
                return num
                break
        except:
            None
        print('Оно должно быть от 4 до 20.\nПожалуйста, повторите попытку:')

def get_color_choice():
    colors = {'черный':'black',
              'белый':'white',
              'красный':'red',
              'синий':'blue',
              'желтый':'yellow',
              'зеленый':'green',
              'оранжевый':'orange'}
    print('Допустимые цвета заливки:')
    print(*colors.keys(), sep='\n')
    print('Пожалуйста, введите цвет:')
    while 1:
        color = input().lower()
        if color in colors.keys():
            return colors[color]
            break
        else:
            print("'" + color + "' не является верным значением.\nПопробуйте еще раз:")

turtle.screensize(500, 500)

color_1 = get_color_choice()
color_2 = get_color_choice()
colors = [color_1, color_2]
number = get_num_hexagons()

distance = 500/number
length = distance/(2*math.cos(math.pi/6))

x, y = -250+distance, 250-length*2

for k in range(number):
    for i in range(number):
        draw_hexagon(x, y, length, colors[(k//2)%2-i%2])
        x+=distance
    x-=distance*number
    x, y = x-(0.5-k%2)*distance, y-length*1.5
turtle.done()



