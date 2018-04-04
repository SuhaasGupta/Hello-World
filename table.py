t = input("Enter the digit to know its table")
print("Enter the ending point of the table")
a = int(raw_input(""))
k = a+1
for i in range(0,k):
    if(i<10):
        print t,"*",i," =",i*t
    else:
        print t,"*",i,"=",i*t
    

    
