import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    x = np.arange(-10,10,0.01,dtype=float)
    
    plt.figure(figsize=(8, 4.5),dpi=80)
    
    plt.subplot(1,2,1)
    plt.title(r"$f\,(x)= \dfrac{1}{2\,\cosh \left(\dfrac{\pi}{2}\,x\right)}$")
    plt.plot(x,1/(2*np.cosh((np.pi/2)*x)))
    plt.ylabel("probability desity function")
    plt.xlabel(r"value of $x$")

    plt.subplot(1,2,2)
    plt.title(r"$F\,(x)=\dfrac{2}{\pi}\,\arctan\exp\left(\dfrac{\pi}{2}\,x\right)$")
    plt.plot(x,(2/np.pi)*np.arctan(np.exp((np.pi/2)*x)))
    plt.ylabel("cumulative distribution function")
    plt.xlabel(r"value of $x$")
    
    plt.show()
