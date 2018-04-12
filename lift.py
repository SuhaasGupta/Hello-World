#Lift Stimulation
import time

g = True
p=0
def lift():
    global p
    
    s = raw_input("Enter u to go up d to go down\t")
    if(s=='u'):
        f = input("Enter the floor you want to reach\t")
        if(f>p):
            while(p!=f+1):
                print p,"..."
                time.sleep(2)
                p=p+1
        else:
            print('Wrong input')
          
    elif(s=='d'):
        p=p-1
        f = input("Enter the floor you want to reach\t")
        if(f<p):
            while(p!=f-1):
                print p,"..." 
                time.sleep(2)
                p=p-1
        else:
            print('wrong input')
while(g):
    lift()
