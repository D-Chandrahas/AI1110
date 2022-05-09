from random import randint

if __name__ == "__main__":
    w=0
    b=0
    d = [0,0,0,0,0,0]

    for i in range(1000):
        if randint(1,2)==1:
            if randint(1,7) < 4:
                b+=1
            else:
                w+=1
        else:
            d[randint(0,5)] += 1

    print("Outcome   Probability\n(H,W)     %.3f\n(H,B)     %.3f" % (w/1000,b/1000))
    for i in range(6):
        print("(T,D%d)    %.3f"%(i,d[i]/1000))
        
