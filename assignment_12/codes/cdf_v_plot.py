#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import scipy




x = np.linspace(-4,4,30)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
randvar = np.loadtxt('v_samples.dat',dtype='double')

for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

def F(x):
        if x<0:
                return 0
        else :
                return 1 - np.exp(-x/2)

vec_F = scipy.vectorize(F,otypes=[float])

y = vec_F(x)


plt.plot(x,err,'o',label = "numerical")#plotting the CDF
plt.plot(x,y,label = "theory")
plt.grid() #creating the grid
plt.legend()
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

plt.savefig('../figs/v_cdf.png')

plt.show() #opening the plot window
