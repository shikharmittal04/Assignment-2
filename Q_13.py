#Question 11: Euler's method
#Convert 2nd order ODE into 2 1st order ODEs
def f(t,y,u):
	return np.array([u,t*np.log(t)-2*y/t**2+2*u/t])
	
import numpy as np
import matplotlib.pyplot as plt

h=0.001
N=int(1/h)
u=np.zeros(N+1)
y=np.zeros(N+1)
u[0]=0
y[0]=1
t=np.linspace(1,2,N+1)
for i in range(N):
	D=f(t[i],y[i],u[i])
	y[i+1]=y[i]+h*D[0]
	u[i+1]=u[i]+h*D[1]
	
y_act=7*t/4+t**3/2*np.log(t)-0.75*t**3	#Analytical solution

fig1,ax=plt.subplots()
plt.plot(t,y,'b')
plt.plot(t,y_act,'r')

ax.set_xlabel(r'$t$',fontsize=16)
ax.grid(True)
ax.minorticks_on()
ax.grid(which='minor', linewidth='0.5', color='black',alpha=0.2)
ax.tick_params(axis='both', which='major', labelsize=14)
plt.legend(['Euler','Exact'],fontsize=16)
plt.show()
