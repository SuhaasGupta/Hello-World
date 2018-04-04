import time
import random

def repeat():
    d = raw_input("Enter y to continue n to exit")
    while(d!='y' or d!='n' or d!='Y' or d!='N'):
        d = raw_input("Enter y to continue n to exit")
        if(d=='y' or d=='Y'):
            a=True
            break
        elif(d=='n' or d=='N'):
            a=False
            print("Thank for playing")
            break

a= True
b = [1,2,3,4,5,6]
while(a):
    x = raw_input("Enter any alphabet....\n")
    time.sleep(1)
    print "loading.",
    for i in range(1,5):
       time.sleep(1)
       print ".",
    if(i==4):
        print("stopped")
        c = random.choice(b)
        print(c)
        d = raw_input("Enter y to continue n to exit")
        if(d=='y' or d=='Y'):
            a=True
        elif(d=='n' or d=='N'):
            a=False
            print("Thank for playing")
        else:
            repeat()



