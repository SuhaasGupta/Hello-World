import Tkinter
#from Tkinter import *
#import openpyxl
import tkFileDialog
import os


copy = 'a'

def path():
    global copy
    copy=tkFileDialog.askopenfilename()
    #print(copy)
  
    print "successfully printed path of file\n",copy 


def filetype():
    global copy
    copy=tkFileDialog.askopenfilename()
    for each in copy:
        #if(each=='.'):
            #x=copy.index('.')
            d = [i for i, v in enumerate(copy) if v == '.']
    print "successfully printed type of file\n", copy[d[-1]:]
   

def filename():
          global copy
          copy=tkFileDialog.askopenfilename()
          for each in copy:
              d = [i for i, v in enumerate(copy) if v == '.']
              if(each=='.'):
                    x=copy.index('.')
              d = [i for i, v in enumerate(copy) if v == '/']
          print "successfully printed type of file\n", copy[d[-1]:x]


ui=Tkinter.Tk()
ui.title('path')
m=Tkinter.Button(ui,text='Path',command=path)
m1=Tkinter.Button(ui,text='Type',command=filetype)
m2=Tkinter.Button(ui,text='Name',command=filename)
m.pack(padx=100,pady=50)
m1.pack(padx=100,pady=50)
m2.pack(padx=100,pady=50)
ui.mainloop()
