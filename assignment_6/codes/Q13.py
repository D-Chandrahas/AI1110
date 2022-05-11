from random import randint

if __name__ == "__main__":
    RB = 0
    BR = 0
    BB = 0
    RR = 0

    for i in range(1000):
        x = randint(1,18)
        y = randint(1,18)
        
        if x<9:
            if y<9:
                RR+=1
            else:
                RB+=1
        else:
            if y<9:
                BR+=1
            else:
                BB+=1
                
    print("First Draw    Second Draw    Probability\n\
Red           Black          %.3f\n\
Black         Black          %.3f\n\
Red           Red            %.3f\n\
Black         Red            %.3f\n" % (RB/1000,BB/1000,RR/1000,BR/1000))
