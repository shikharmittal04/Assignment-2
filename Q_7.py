#Question 7: 4 initial value problems. 
import scipy.integrate as scint
import numpy as np
import matplotlib.pyplot as plt

Sol1=scint.solve_ivp(lambda t, y: t*np.exp(3*t)-2*y, [0, 1], [0],t_eval=np.linspace(0,1))
t1=np.linspace(0,1)
y1=(5*t1-1)*np.exp(3*t1)/25-np.exp(-2*t1)/25
plt.plot(Sol1.t,Sol1.y[0],'b',t1,y1,'r')
plt.xlabel('t')
plt.ylabel('y')
plt.legend(['solve_ivp','Analytical'])
plt.text(0.5, 1.5, r"$\dot{y}=te^{3t}-2y$", fontsize=16)

Sol2=scint.solve_ivp(lambda t, y: 1-(t-y)**2, [2, 3], [2],t_eval=np.linspace(2,3))
t2=np.linspace(2,3)
y2=t2
plt.subplots()
plt.plot(Sol2.t,Sol2.y[0],'b',t2,y2,'r')
plt.xlabel('t')
plt.ylabel('y')
plt.legend(['solve_ivp','Analytical'])
plt.text(2.2, 1.5, r"$\dot{y}=1-(t-y)^2$", fontsize=16)

Sol3=scint.solve_ivp(lambda t, y: 1+y/t, [1, 2], [2],t_eval=np.linspace(1,2))
t3=np.linspace(1,2)
y3=t3*(2+np.log(t3))
plt.subplots()
plt.plot(Sol3.t,Sol3.y[0],'b',t3,y3,'r')
plt.xlabel('t')
plt.ylabel('y')
plt.legend(['solve_ivp','Analytical'])
plt.text(1.5, 2.5, r"$\dot{y}=1+y/t$", fontsize=16)

Sol4=scint.solve_ivp(lambda t, y: np.cos(2*t)+np.sin(3*t), [0, 1], [1],t_eval=np.linspace(0,1))
t4=np.linspace(0,1)
y4=np.sin(2*t4)/2-np.cos(3*t4)/3+4/3
plt.subplots()
plt.plot(Sol4.t,Sol4.y[0],'b',t4,y4,'r')
plt.xlabel('t')
plt.ylabel('y')
plt.legend(['solve_ivp','Analytical'])
plt.text(0.5, 1.5, r"$\dot{y}=\cos2t+\sin3t$", fontsize=16)
plt.show()

