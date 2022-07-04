#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt




x = np.linspace(-4,4,60)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
randvar = np.loadtxt('uni.dat',dtype='double')
for i in range(0,60):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list


def F(x):
        if x<0:
                return 0
        elif x>1:
                return 1
        else :
                return x

y = [F(i) for i in x]

plt.plot(x,err,'o',label = "numerical")#plotting the CDF
plt.plot(x,y,label = "theory")
plt.grid() #creating the grid
plt.legend()
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

plt.savefig('../figs/uni_cdf.png')
plt.show() #opening the plot window
