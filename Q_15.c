//Question 15
//Comparision with analytical solution, Error bound on Euler's method.

#include<stdio.h>
#include<math.h>
int main()
{
	int i;
	float h=0.1;	//Step size
	int N=2/h;		//No. of steps
	float y[N+1];
	float t[N+1];
	float y_exact[N+1];
	float err[N+1];
	float bound[N+1];
	
	for(i=0;i<N+1;i++)
	{
		y[i]=0;		//Initialise solution to 0
		t[i]=i*h;	//Mesh points
	}
	
	y[0]=0.5;		//Initial condition
	for(i=0;i<N+1;i++)
	{
		y[i+1]=y[i]+h*(y[i]-pow(t[i],2)+1);			//Euler's method
		y_exact[i]=pow((t[i]+1),2)-0.5*exp(t[i]);	//Analytical exact solution
		err[i]=y_exact[i]-y[i];						//Absolute error
		bound[i]=(exp(2)-4)/20*(exp(t[i])-1);		//Error bound: using Lipschitz criterion
	}
	
	printf("    t      Euler      Exact    Error    Err bound\n");  //Required table
	for(i=0;i<N+1;i++)
	{
		printf("%f  %f  %f  %f  %f\n",t[i],y[i],y_exact[i],err[i], bound[i]);
	}
	
	return 0;
}

