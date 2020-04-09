#Question 2
import numpy as np
import matplotlib.pyplot as plt

def dydx(t,y):
	return y/t-(y/t)**2
###############################################
h=0.1
N=int(1/h)
t=np.linspace(1,2,N+1)
y1=np.zeros(N+1)
y1[0]=1
for i in range(N):
	y1[i+1]=y1[i]+h*dydx(t[i],y1[i])

fig1,ax=plt.subplots()
plt.plot(t,y1,'b')

y_act=t/(1+np.log(t))	#Analytical values of y for the same mesh points
plt.plot(t,y_act,'r')

Err=y_act-y1			#Local absolute error
Tot_err=sum(Err)		#Total absolute error
print('Total absolute error = ',Tot_err)

Rel_err=(y_act-y1)/y_act			#Local relative error
Tot_rel_err=sum(Rel_err)			#Total relative error
print('Total relative error = ',Tot_rel_err)

ax.set_xlabel(r'$t$',fontsize=16)
ax.set_ylabel(r'$y$',fontsize=16)

ax.grid(True)
ax.minorticks_on()
ax.grid(which='minor', linewidth='0.5', color='black',alpha=0.2)
ax.tick_params(axis='both', which='major', labelsize=14)
plt.legend(['Euler','Analytical'],fontsize=16)
plt.show()
