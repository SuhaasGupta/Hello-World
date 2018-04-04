k=0
d=1
p=input("enter the number")

def febennoci():
    for i in range(0,p):
        print(k)
        f = k+d
        k=d
        d=f
        global k
        global d
febennoci()
