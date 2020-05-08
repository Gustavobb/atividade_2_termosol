import math

l = 0.3
h = 15
p = 0.03*4
a = 0.03**2
k = 200
m = math.sqrt((h*p)/(k*a))

temp_kelvin = []
x_list = [0]
divisions = 60
step = l/divisions

for i in range(divisions):
    x_list.append(x_list[i] + step)

for x in x_list:
    t = (math.cosh(m*(l - x)) + (h/(m*k)) * math.sinh(m*(l-x)))/(math.cosh(m*l) + (h/(m*k)) * math.sinh(m*l))
    temp_kelvin.append(t)

t_inf = 300
tb = 350

theta_b = tb - t_inf
T = temp_kelvin[30]*theta_b + t_inf
print(T)