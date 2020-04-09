#Convert the 2nd order differential equation into two 1st order equations.
#Boundary value problem: SHOOTING METHOD

def f(t,x,u):					#I have passed t,x,u to keep the form of acceleration general.
	return np.array([u,-g])
	
import numpy as np
import matplotlib.pyplot as plt

h=0.001
t_1=10
g=10
N=int(t_1/h)
x=np.zeros(N+1)
u=np.zeros(N+1)		# u is the first time derivative of x
t=np.linspace(0,t_1,N+1)
x[0]=0				# Given initial condition

u_low=0				#Set two extreme limits on the initial condition
u_high=g*t_1		#on u. "g*t_1" is some scale of u in the problem .

fig,ax=plt.subplots()
for j in range(5):	
	for i in range(N):			#Euler's method
		k=h*f(t[i],x[i],u[i])
		x[i+1]=x[i]+k[0]
		u[i+1]=u[i]+k[1]
	
	plt.plot(t,x,'b')
	if x[N]>0.01:				#If the final position is large positive
		u_high=u[0]				#then reduce initial velocity.
	elif x[N]<-0.01:			#If the final position is large negative
		u_low=u[0]				#then reduce initial velocity.
	else:
		break					#I have set the required tolerance as |x[N]|<=0.01
	u[0]=(u_high+u_low)/2		#Initial condition on u will taken as the midpoint of the extremes.
	

x_act=5*t*(t_1-t)		#Analytical solution
plt.plot(t,x_act,'r')

ax.set_xlabel(r'$t$',fontsize=16)
ax.set_ylabel(r'$x$',fontsize=16)
ax.grid(True)
ax.minorticks_on()
ax.grid(which='minor', linewidth='0.5', color='black',alpha=0.2)
ax.tick_params(axis='both', which='major', labelsize=14)
plt.show()
