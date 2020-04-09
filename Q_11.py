#Question 11: 4th order Runge-Kutta.
def f(t,u1,u2,u3):
	return np.array([u1+2*u2-2*u3+np.exp(-t),u2+u3-2*np.exp(-t),u1+2*u2+np.exp(-t)])
	
import numpy as np
import matplotlib.pyplot as plt

h=0.001
N=int(1/h)
u1=np.zeros(N+1)
u2=np.zeros(N+1)
u3=np.zeros(N+1)
u1[0]=3
u2[0]=-1
u3[0]=1
t=np.linspace(0,1,N+1)
for i in range(N):
	k1=h*f(t[i],u1[i],u2[i],u3[i])
	k2=h*f(t[i]+h/2,u1[i]+k1[0]/2,u2[i]+k1[1]/2,u3[i]+k1[2]/2)
	k3=h*f(t[i]+h/2,u1[i]+k2[0]/2,u2[i]+k2[1]/2,u3[i]+k2[2]/2)
	k4=h*f(t[i]+h,u1[i]+k3[0],u2[i]+k3[1],u3[i]+k3[2])
	u1[i+1]=u1[i]+(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6
	u2[i+1]=u2[i]+(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6
	u3[i+1]=u2[i]+(k1[2]+2*k2[2]+2*k3[2]+k4[2])/6


fig1,ax=plt.subplots()
plt.plot(t,u1,'b')
plt.plot(t,u2,'r')
plt.plot(t,u3,'g')

ax.set_xlabel(r'$t$',fontsize=16)
ax.grid(True)
ax.minorticks_on()
ax.grid(which='minor', linewidth='0.5', color='black',alpha=0.2)
ax.tick_params(axis='both', which='major', labelsize=14)
plt.legend([r'$u_1$','$u_2$','$u_3$'],fontsize=16)
plt.show()
