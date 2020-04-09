#Question 1
#Backward integration: Euler's Method
import numpy as np
import matplotlib.pyplot as plt

###############################################
#Part 1
h=0.01					#Step size
N=int(1/h)  			#No.of grid points
x=np.linspace(0,1,N+1)
y1=np.zeros(N+1)
y1[0]=np.exp(1)			#Initial condition
for i in range(N):
	y1[i+1]=y1[i]/(1+h*9)

fig1,ax1=plt.subplots()
plt.plot(x,y1,'b')
ax1.set_xlabel(r'$x$',fontsize=16)
ax1.set_ylabel(r'$y$',fontsize=16)

ax1.grid(True)
ax1.minorticks_on()
ax1.grid(which='minor', linewidth='0.5', color='black',alpha=0.2)
ax1.tick_params(axis='both', which='major', labelsize=14)
ax1.text(0.5, 1.5, r"$\frac{dy}{dx}=-9y$", fontsize=12)
###############################################
#Part 2
h=0.01
y2=np.zeros(N+1)
y2[0]=1/3
for i in range(N):
	y2[i+1]=x[i+1]-1/(40*h)+np.sqrt(x[i+1]/10+(y2[i]-x[i+1])/(20*h)+1/(1600*h**2)) #Implicit eqn is a quadratic which
																				   #gives 2 solutions. Choose the one which
																				   #gives meaningful result for h=0.
fig2,ax2=plt.subplots()															   
plt.plot(x,y2,'b')
ax2.set_xlabel(r'$x$',fontsize=16)
ax2.set_ylabel(r'$y$',fontsize=16)
ax2.text(0.5, 1, r"$\frac{dy}{dx}=-20(y-x)^2+2x$", fontsize=12)

ax2.grid(True)
ax2.minorticks_on()
ax2.grid(which='minor', linewidth='0.5', color='black',alpha=0.2)
ax2.tick_params(axis='both', which='major', labelsize=14)

plt.show()
