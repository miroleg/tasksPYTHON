
from math import *
from tkinter import *
import array


h_hil_y = 50
h_hil_yz = 70

#f = "200-x*x*.0001"
f = "100+sin(x/80)*h_hil_y"
#f= input('f(x):')
root = Tk()

canv = Canvas(root, width = 1300, height = 1000, bg = "lightblue")
j = 0

First_x = 0
First_z = 0

while j <= 12 :						# слои по оси Z
	#surface = array.array("i")
	for i in range(1000):

		try:
			x = First_x + i
			new_f = f.replace('x', str(x))
			z= First_z + j*30
			y = eval(new_f) + z*(1+cos(x/50)*.2)
			#surface.extend(y)
			canv.create_line(x, y+2, x, 600, width = 2, fill = 'lightgreen')

			canv.create_oval(x-2, 600-2, x+2, 600+2, fill = 'green')


			canv.create_oval(x-2, y-2, x + 2, y + 2, fill = 'green')

		except:
			pass
	canv.create_oval(x-2, y-2, x + 2, y + 2, fill = 'green')
	j +=1
#for k in range(100):
#	print (surface[1])

canv.pack()

root.mainloop()


