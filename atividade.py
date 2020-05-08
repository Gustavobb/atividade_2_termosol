import math
import matplotlib.pyplot as pyplot

l = 0.3
h = 15
p = 0.03*4
a = 0.03**2
k = 200
t_inf = 300
tb = 350
m = math.sqrt((h*p)/(k*a))

temp_kelvin = []
x_list = [0]
divisions = 60
step = l/divisions

for i in range(divisions):
    x_list.append(x_list[i] + step)

for x in x_list:
    t = (math.cosh(m*(l - x)) + (h/(m*k)) * math.sinh(m*(l-x)))/(math.cosh(m*l) + (h/(m*k)) * math.sinh(m*l))
    temp_kelvin.append(t*(tb - t_inf) + t_inf)

pyplot.plot(x_list, temp_kelvin)
pyplot.show()