#Convert the 2nd order differential equation into two 1st order equations
def f(x,y,u):
	return np.array([u,2*u-y+x*np.exp(x)-x])
	
import numpy as np
import matplotlib.pyplot as plt

h=0.01
N=int(1/h)
y=np.zeros(N+1)
u=np.zeros(N+1)		# u is the first derivative of y
y[0]=0				# Initial condition on y
u[0]=0				# Initial condition on y'
x=np.linspace(0,1,N+1)
for i in range(N):
	k1=h*f(x[i],y[i],u[i])
	k2=h*f(x[i]+h/2,y[i]+k1[0]/2,u[i]+k1[1]/2)
	k3=h*f(x[i]+h/2,y[i]+k2[0]/2,u[i]+k2[1]/2)
	k4=h*f(x[i]+h,y[i]+k3[0],u[i]+k3[1])
	y[i+1]=y[i]+(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6
	u[i+1]=u[i]+(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6



fig1,ax=plt.subplots()
plt.plot(x,y,'b')

#y_act=(x**3/6-x+2)*np.exp(x)-x-2						#Uncomment these 3 statements to see how perfectly 
#plt.plot(x,y_act,'r')									#the analytical solution matches with the 4th order RK.
#plt.legend(['Runge-Kutta','Analytical'],fontsize=14)

ax.set_xlabel(r'$x$',fontsize=16)
ax.set_ylabel(r'$y$',fontsize=16)
ax.text(0.3,0.1,r"$y''-2y'+y=xe^x-x$",fontsize=16)
ax.grid(True)
ax.minorticks_on()
ax.grid(which='minor', linewidth='0.5', color='black',alpha=0.2)
ax.tick_params(axis='both', which='major', labelsize=14)
plt.show()
