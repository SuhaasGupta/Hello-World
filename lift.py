#Lift Stimulation
import time

g = True
p=0
def lift():
    global p
    
    s = raw_input("Enter u to go up d to go down")
    if(s=='u'):
        f = input("Enter the floor you want to reach")
        while(p!=f+1):
            print p,"..."
            
            time.sleep(2)
            p=p+1
            if(p==f+1):
                break
    elif(s=='d'):
        p=p-1
        f = input("Enter the floor you want to reach")
        while(p!=f-1):
            print p,"..." 
            time.sleep(2)
            p=p-1
            if(p==f-1):
                break

while(g):
    lift()
