import numpy as np


if __name__ == "__main__":

    freq = np.random.uniform(low=0.0, high=20000.0, size=1000)
    
    class1 = [f for f in freq if f < 4000]
    class2 = [f for f in freq if f >= 4000 and f <= 9000]
    class3 = [f for f in freq if f > 9000 and f <= 14000]
    class4 = [f for f in freq if f > 14000]
        
    print("Distance        Frequency\n< 4000          %.0f\n4000 - 9000     %.0f\n9001 - 14000    %.0f\n> 14000         %.0f\n\n" % (len(class1),len(class2),len(class3),len(class4)))
    
    
