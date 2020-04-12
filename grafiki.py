from math import *
from tkinter import *
from array import *


TOP_HIL_Y = 80			# высота холма для гармонической функции
BOTTOM_HIL_Y = 450		# нижняя точка  холма
N = 230					# количество шагов по оси x
M = 40					# количество шагов по оси z
First_x = 50
First_z = 0
STEP_X = 4				# шаг  по x  в точках
STEP_Z = 4				# шаг  по z  в точках
XZvew = 1
YZvew = 1

# f = input(' по умолчанию  (f = 100+sin(x/60)*TOP_HIL_Y)    введите f(x): ')
# if f == "":
f = "100 + sin(x/60)*TOP_HIL_Y"

root = Tk()
canv = Canvas(root, width=1300, height=650, bg="lightblue")
j = 0
z = 0
Suf_len = 2*N
surface = [0]*Suf_len				# массив графика для слоя по оси Z
line_on_surf = array('i')			# прямая линия на карте  z = x/5  КРАСНАЯ ПРЯМАЯ
red_line = 0.
line_on_surf2 = array('i')			# прямая линия на карте  z =1000-x/5  СИНЯЯ ПРЯМАЯ
blue_line = 0.
house = [0]*10					    # домик 1сечение
house2 = [0]*10					    # домик 2 сечение
house3 = [0]*10					    # домик 3 сечение

i_end_point = 0
while j <= M:						# слои по оси Z
    for i in range(N):
        x = First_x + i*STEP_X
        new_f = f.replace('x', str(x))
        z = First_z + j*STEP_Z
        y = eval(new_f) + z*(1 + cos(x/50)/YZvew)								# Добавим зависимость от Z
        surface[2*i] = int(First_x + i*STEP_X + j*STEP_Z/XZvew)
        surface[2*i+1] = int(y + j*STEP_Z/XZvew)
        if i/5 == j:
            line_on_surf.append(surface[2*i])   	# прямая линия на карте  z = x/5
            line_on_surf.append(surface[2*i+1])
        if (N-i)/5 == j:
            line_on_surf2.append(surface[2*i])   	# прямая линия на карте  z =1000 - x/5
            line_on_surf2.append(surface[2*i+1])

        if i == (N - 20) and 1 < j < 8:
            house[0] = surface[2*i]                 # house 1
            house[1] = surface[2*i+1]
            house[2] = surface[2*i]+60
            house[3] = surface[2*i+1]
            house[4] = surface[2*i]+60
            house[5] = surface[2*i+1]-60
            house[6] = surface[2*i]+30
            house[7] = surface[2*i+1]-80
            house[8] = surface[2*i]
            house[9] = surface[2*i+1]-60
        if i == 40 and 5 < j < 12:
            house2[0] = surface[2*i]                 # house 2
            house2[1] = surface[2*i+1]
            house2[2] = surface[2*i]+60
            house2[3] = surface[2*i+1]
            house2[4] = surface[2*i]+60
            house2[5] = surface[2*i+1]-60
            house2[6] = surface[2*i]+30
            house2[7] = surface[2*i+1]-100
            house2[8] = surface[2*i]
            house2[9] = surface[2*i+1]-60
        if i == 65 and 31 < j < 38:
            house3[0] = surface[2*i]                 # house 3
            house3[1] = surface[2*i+1]
            house3[2] = surface[2*i]+60
            house3[3] = surface[2*i+1]
            house3[4] = surface[2*i]+60
            house3[5] = surface[2*i+1]-60
            house3[6] = surface[2*i]+30
            house3[7] = surface[2*i+1]-70
            house3[8] = surface[2*i]
            house3[9] = surface[2*i+1]-60
    j += 1
    "Рисуем срез по оси z в виде многоугольника"
    y_bott = int(BOTTOM_HIL_Y + j*STEP_Z/YZvew)
    x_bott_beg = int(First_x + j*STEP_Z/XZvew)
    x_bott_end = int(First_x + j*STEP_Z/XZvew + N*STEP_X)
    canv.create_polygon(x_bott_beg, y_bott, surface, x_bott_end,  y_bott, fill='lightgreen', outline='black')
    "Ищем пересечение  с прямой z = x/3  Красный цвет"
    if len(line_on_surf) > 2:
        i_end_point = len(line_on_surf)
        l_x1 = line_on_surf[i_end_point - 4]
        l_y1 = line_on_surf[i_end_point - 3]
        l_x2 = line_on_surf[i_end_point - 2]
        l_y2 = line_on_surf[i_end_point - 1]
        canv.create_line(l_x1, l_y1,  l_x2, l_y2, fill='red', width=4)   						# рисуем отрезок красной линии
        red_line = red_line + sqrt(float(l_x2-l_x1)**2 + float(l_y2-l_y1)**2 + STEP_Z**2)  		# Расчет длины пути красной линии
    "Ищем пересечение  с прямой z = x/3    Синий цвет"
    if len(line_on_surf2) > 2:
        i_end_point = len(line_on_surf2)
        l_x1 = line_on_surf2[i_end_point - 4]
        l_y1 = line_on_surf2[i_end_point - 3]
        l_x2 = line_on_surf2[i_end_point - 2]
        l_y2 = line_on_surf2[i_end_point - 1]
        canv.create_line(l_x1, l_y1,  l_x2, l_y2, fill='blue', width=4)							# рисуем отрезок синей линии
        blue_line = blue_line + sqrt(float(l_x2-l_x1)**2 + float(l_y2-l_y1)**2 + STEP_Z**2) 	# Расчет длины пути синей линии
    "Рисуем домик"
    canv.create_polygon(house, fill='orange', outline='black')                                  # рисуем оранжевый домик
    canv.create_polygon(house2, fill='purple', outline='black')                                  # рисуем оранжевый домик
    canv.create_polygon(house3, fill='pink', outline='black')                                   # рисуем оранжевый домик

l_x1 = line_on_surf2[0]
l_y1 = line_on_surf2[1]
l_x2 = line_on_surf2[len(line_on_surf2) - 2]
l_y2 = line_on_surf2[len(line_on_surf2) - 1]
blue_line_xz = sqrt(float(l_x2-l_x1)**2 + float(l_y2-l_y1)**2 + float(z-First_z)**2)		# Расчет длины пути  проекций  на плоскости xz (как на карте)
print(" Синий путь = ", format(blue_line, "6.2f"), "проекция XZ = ", format(blue_line_xz, "6.2f"), "дельта = ", format(blue_line-blue_line_xz, "6.2f"))
l_x1 = line_on_surf[0]
l_y1 = line_on_surf[1]
l_x2 = line_on_surf[len(line_on_surf) - 2]
l_y2 = line_on_surf[len(line_on_surf) - 1]
red_line_xz = sqrt(float(l_x2-l_x1)**2 + float(l_y2-l_y1)**2 + float(z-First_z)**2)
print("красный путь = ", format(red_line, "6.2f"), "проекция XZ = ", format(red_line_xz, "6.2f"), "дельта = ", format(red_line-red_line_xz, "6.2f"))

canv.pack()
root.mainloop()
