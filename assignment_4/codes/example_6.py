import numpy as np


if __name__ == "__main__":

    freq = np.random.uniform(low=0.0, high=20000.0, size=1000)
    
    class1 = 0
    class2 = 0
    class3 = 0
    class4 = 0

    i=0
    while i < 1000:
        if freq[i] < 4000:
            class1 += 1
        elif freq[i] >= 4000 and freq[i] <= 9000:
            class2 += 1
        elif freq[i] > 9000 and freq[i] <=14000:
            class3 += 1
        else:
            class4 += 1
        i += 1
        
    print("Distance        Frequency\n< 4000          %.0f\n4000 - 9000     %.0f\n9001 - 14000    %.0f\n> 14000         %.0f\n" % (class1,class2,class3,class4))
    
    
