from sympy import *
from math import *
import matplotlib.pyplot as plt
from trajectory1 import X,l,phi
from mpl_toolkits import mplot3d
fig = plt.figure()
ax = plt.axes(projection ='3d')
T=(11/7)/1000
E=1
I2=1
Iy=1
d=1
m=1
F=1

F_strt=1

tht_strt = 0
K=10
x, z, tht, T, t= symbols('x z tht T t')

x = (l/24)*(12*t-t**3)
z = (l/120)*(120-20*t**2+t**4)
tht = t
x_dot = diff(x,t)
x_Ddot = diff(x_dot,t)
z_dot = diff(z,t)
z_Ddot = diff(z_dot,t)
tht_dot = diff(tht,t)
tht_Ddot = diff(tht_dot,t)
T = 0.5*m*l*l*((tht**6)/900 - (19/2880)*(tht**4) - (tht**2)/72 + 0.25)*(tht_dot**2) + 0.5*Iy*(tht_dot**2)
T_dell_thtdot = m*l*l*((tht**6)/900 - (19/2880)*(tht**4) - (tht**2)/72 + 0.25)*(tht_dot) + Iy*tht_dot
T_dt_dell_thtdot = m*l*l*(((tht**6)/900 - (19/2880)*(tht**4) - (tht**2)/72 + 0.25)*(tht_Ddot)+((tht**5)/150 - (19/720)*(tht**3) - tht/36)*(tht_dot**2)) + Iy*tht_Ddot
T_dell_tht = m*l*l*((tht**5)/300 - (19/1440)*(tht**3) - tht/72)*(tht_dot**3)
U_dell_tht = E*I2*tht/l
Q=F*d
Q = T_dt_dell_thtdot - T_dell_tht + U_dell_tht

tht_Ddot = (F*d - E*I2*tht/l - m*l*l*((tht**5)/300 - (19/1440)*(tht**3) - tht/72)*(2*tht_dot*tht_dot - tht_dot**3))/(Iy + m*l*l*((tht**6)/900 - (19/2880)*(tht**4) - (tht**2)/72 + 0.25))

F_arr = []
tht_des=[]
for i in range(0,1000):
    tht_des.append(X[i][6])
tht_calc = [0]
tht_dot_calc = [0]
x_calc=[]
y_calc=[]
z_calc=[]
F_arr.append(F_strt)
T1=[]
T2=[]
T3=[]
T4=[]
for i in range(0,10):
    F_req = F_arr[i]
    while True:
        tht_Ddot_1_int = tht_Ddot.subs(F,F_req)
        tht_Ddot_1 = tht_Ddot_1_int.subs(t,i)
        tht_dot_calc_i = (tht_dot_calc[i] + tht_Ddot_1*(1/1000))
        tht_calc_i = (tht_calc[i] + tht_dot_calc[i]*(1/1000))
        e = tht_calc[i] - tht_des[i]
        if i!=0 : 
            e_dot = ((tht_calc[i] - tht_des[i]) - (tht_calc[i-1] - tht_des[i-1]))
        else : 
            e_dot = e*1000
        F_req = K*e + K*e_dot 
        if (e<0.1): break
    tht_dot_calc.append(tht_dot_calc_i)
    tht_calc.append(tht_calc_i)
    F_arr.append(F_req)
    T1.append(F_req*cos(phi))
    T2.append(F_req*sin(phi))
    x1=x.subs(tht,tht_calc[i]*cos(phi))
    z1=z.subs(tht,tht_calc[i])
    x_calc.append(x1*cos(phi))
    y_calc.append(x1*sin(phi))
    z_calc.append(z1)
ax.plot3D(x_calc,y_calc, z_calc, 'green')
plt.show()