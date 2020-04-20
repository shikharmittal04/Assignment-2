#Question 8: 4 boundary value problems.
import scipy.integrate as scint
import numpy as np
import matplotlib.pyplot as plt

def fun1(x, y):
	return np.vstack((y[1], -np.exp(-2*y[0])))

def BC1(ya, yb):
	return np.array([ya[0], yb[0]-np.log(2)])

x1 = np.linspace(1, 2)
y_int = np.zeros((2, x1.size))
Sol1 = scint.solve_bvp(fun1, BC1, x1, y_int)
y1 = np.log(x1)
plt.plot(x1,Sol1.sol(x1)[0],'b',x1,y1,'r')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['solve_bvp','Analytical'])
plt.text(0.5, 1.5, r"$y''=-e^{-2y}$", fontsize=16)


def fun2(x, y):
	return np.vstack((y[1], y[1]*np.cos(x)-y[0]*np.log(y[0]) ))

def BC2(ya, yb):
	return np.array([ya[0]-1, yb[0]-np.exp(1)])

x2 = np.linspace(0, np.pi/2)
y_int = np.zeros((2, x2.size))
y_int[0]=1
Sol2 = scint.solve_bvp(fun2, BC2, x2, y_int)
y2 = np.exp(np.sin(x2))
plt.subplots()
plt.plot(x2,Sol2.sol(x2)[0],'b',x2,y2,'r')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['solve_bvp','Analytical'])
plt.text(0.5, 1.5, r"$y''=y'\cos x-y\ln y$", fontsize=16)


def fun3(x, y):
	return np.vstack((y[1], -(2*y[1]**3+y[0]**2*y[1])*np.cos(x)**(-1) ))

def BC3(ya, yb):
	return np.array([ya[0]-2**(-1/4), yb[0]-np.sqrt(np.sqrt(3)/2)])

x3 = np.linspace(np.pi/4, np.pi/3)
y_int = np.zeros((2, x3.size))
y_int[0]=2**(-1/4)
Sol3 = scint.solve_bvp(fun3, BC3, x3, y_int)
y3 = np.sqrt(np.sin(x3))
plt.subplots()
plt.plot(x3,Sol3.sol(x3)[0],'b',x3,y3,'r')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['solve_bvp','Analytical'])
plt.text(0.5, 1.5, r"$y''=-(2y'^3+y^2y')\sec(x)$", fontsize=16)


def fun4(x, y):
	return np.vstack((y[1], 0.5*(1-y[1]**2-y[0]*np.sin(x))  ))

def BC4(ya, yb):
	return np.array([ya[0]-2, yb[0]-2 ])

x4 = np.linspace(0, np.pi)
y_int = np.zeros((2, x4.size))
y_int[1]=1
Sol4 = scint.solve_bvp(fun4, BC4, x4, y_int)
y4 = 2+np.sin(x4)
plt.subplots()
plt.plot(x4,Sol4.sol(x4)[0],'b',x4,y4,'r')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['solve_bvp','Analytical'])
plt.text(0.5, 1.5, r"$y''=-e^{-2x}$", fontsize=16)
plt.show()
