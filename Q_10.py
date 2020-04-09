# Question 10
# Make a variable change: u=t/(1+t), so that u=[0,1).
# We are asked the value of x at t=3.5e6 or in terms of u it corresponds to u=0.9999997142857959,
# which is nearly 1. The plot suggests that x=x(t) flattens after nearly t=100. Thus, if we use a 
# step size of 0.001, we should get an accurate value of x(t=3.5e6) by simpy quoting the last value
# in the array x (of size 1000). But if very high accuracy is required, then we should use a step 
# size of h=1-0.9999997142857959=2.857142040735283e-07, and then quote the second last value of array x.
def f(u,x):
	return 1/(u**2+x**2*(1-u)**2)
	
import numpy as np
import matplotlib.pyplot as plt

h=0.001
N=int(1/h)		#Domain size in variable u is 1.
x=np.zeros(N+1)
x[0]=1			#Because for t=0, u=0 and thus x(u=0)=1
u=np.linspace(0,1,N+1)
for i in range(N):
	k1=h*f(u[i],x[i])
	k2=h*f(u[i]+h/2,x[i]+k1/2)
	k3=h*f(u[i]+h/2,x[i]+k2/2)
	k4=h*f(u[i]+h,x[i]+k3)
	x[i+1]=x[i]+(k1+2*k2+2*k3+k4)/6

t=u/(1-u) 		#back to original independent variable
print('x(t=3.5e6)=',x[N])
fig1,ax=plt.subplots()
plt.plot(t,x,'b')
plt.xlim([0,100])
ax.set_xlabel(r'$t$',fontsize=16)
ax.set_ylabel(r'$x$',fontsize=16)
ax.text(10,1.5,r"$\frac{dx}{dt}=\frac{1}{x^2+t^2}$",fontsize=20)
ax.text(10,1.3,r"$x(t=3.5\times 10^6)=2.144818$",fontsize=14)
ax.grid(True)
ax.minorticks_on()
ax.grid(which='minor', linewidth='0.5', color='black',alpha=0.2)
ax.tick_params(axis='both', which='major', labelsize=14)
plt.show()
