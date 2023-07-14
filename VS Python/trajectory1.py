from sympy import *
from math import *
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
 
fig = plt.figure()

# syntax for 3-D projection
ax = plt.axes(projection ='3d')
l=20

T=(11/7)/1000
phi = (22/7)/4
x, y, z, t = symbols('x y z t')

x = (l/24)*(12*t-t**3)*cos(phi)

z = (l/120)*(120-20*t**2+t**4)*sin(phi)
tht = t

x_dot = diff(x,t)
x_Ddot = diff(x_dot,t)
z_dot = diff(z,t)
z_Ddot = diff(z_dot,t)
tht_dot = diff(tht,t)
tht_Ddot = diff(tht_dot,t)


X=[]
x_1= []

z_1=[]
for a in range(0,1000):
    a=a*T
    x1=x.subs(t,a)
    x1_dot=x_dot.subs(t,a)
    x1_Ddot=x_Ddot.subs(t,a)
    z1=z.subs(t,a)
    z1_dot=z_dot.subs(t,a)
    z1_Ddot=z_Ddot.subs(t,a)
    tht1=tht.subs(t,a)
    tht1_dot=tht_dot.subs(t,a)
    tht1_Ddot=tht_Ddot.subs(t,a)
    x_1.append(x1*cos(phi))
    z_1.append(z1)
    X.append([x1,x1_dot,x1_Ddot,z1,z1_dot,z1_Ddot,tht1,tht1_dot,tht1_Ddot])
# plt.scatter(x_1,z_1)
# plt.show()
y_1=[]
for i in range(0,1000):
    y_1.append(x_1[i]*tan(phi))


ax.plot3D(x_1,y_1, z_1, 'green')

plt.show()