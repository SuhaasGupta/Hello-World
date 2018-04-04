fact = 1
k = input("enter a number")

def factorial():
    global k    
    for i in range (1,k):
        k = k*i
        
    print(k)

factorial()
