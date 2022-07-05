#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import math



x = np.linspace(-4,4,30)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

def Q(x):
        return math.erfc(x/(2**(1/2)))/2

def F(x):
        return 1-Q(x)

vec_F = np.vectorize(F,otypes=[float])

y = vec_F(x)
	
plt.plot(x,err,'o',label = "numerical")#plotting the CDF
plt.plot(x,y,label="theory")
plt.grid()#creating the grid
plt.legend()
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')


plt.savefig('../figs/gau_cdf.png')
plt.show() #opening the plot window
