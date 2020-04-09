#Question 6
#Boundary value problem: RELAXATION METHOD
import numpy as np
import matplotlib.pyplot as plt

def F(t,x,v):							#Just as before, t,x,v are passed only to keep the form general.
	return -g*np.ones(np.size(t)-2)		#In this problem, RHS is a constant.

h=0.1
t_1=10
g=10
N=int(t_1/h)
t=np.linspace(0,t_1,N+1)
x=np.zeros(N+1)
v=np.zeros(N+1)

A=np.zeros((N-1,N-1))				#Prepare the coefficient matrix of d^2x/dt^2. It is a tridiagonal matrix
for i in range(N-1):
	for j in range(N-1):
		if i==j:
			A[i][j]=-2/h**2
		elif j==i+1:
			A[i][j]=1/h**2
		elif j==i-1:
			A[i][j]=1/h**2

x_act=5*t*(t_1-t)					#Analytical solution.

for i in range(5):
	sol=np.linalg.solve(A,F(t,x,v))	#Finally we get a system of linear equations.
	x[1:N]=sol						#Boundary points are fixed in this problem.
	for k in range(N+1):			#In this for loop I set up the velocity array, but in this
		if k==0:					#problem it is not required, since RHS is v independent.
			v[0]=(x[1]-x[0])/h
		elif k==N:
			v[N]=(x[N]-x[N-1])/h
		else:
			v[k]=(x[k+1]-x[k-1])/(2*h)
	if np.allclose(x,x_act)==True:
		break						#The iteration will terminate in the very first step, since RHS is constant.

fig,ax=plt.subplots()
plt.plot(t,x,'b')

plt.plot(t,x_act,'r')

ax.set_xlabel(r'$t$',fontsize=16)
ax.set_ylabel(r'$x$',fontsize=16)
ax.grid(True)
ax.minorticks_on()
ax.grid(which='minor', linewidth='0.5', color='black',alpha=0.2)
ax.tick_params(axis='both', which='major', labelsize=14)
plt.show()
