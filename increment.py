import Tkinter

a=1

def increment():
   global a
   a=a+1
   print(a)


root = Tkinter.Tk()
root.title("Plus 1")
k=Tkinter.Button(root,text='increse',command=increment)
k.pack(padx=100,pady=50)
root.mainloop()
           
