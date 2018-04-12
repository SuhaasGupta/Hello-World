import Tkinter
import random

def rock():
    a=random.choice(['rock','paper','scissors'])
    if a=='rock':
        print('you choose rock')
        print('computer choose',a)
        print('So Draw')
    elif a=='paper':
        print('you choose rock')
        print('computer choose',a)
        print('YOU LOSE')
    else:
        print('you choose rock')
        print('computer choose',a)
        print('YOU WIN')

def paper():
    a=random.choice(['rock','paper','scissors'])
    if a=='rock':
        print('you choose paper')
        print('computer choose',a)
        print('YOU WIN')
    elif a=='paper':
        print('you choose paper')
        print('computer choose',a)
        print('Draw')
    else:
        print('you choose paper')
        print('computer choose',a)
        print('YOU LOSE')

def scissors():
    a=random.choice(['rock','paper','scissors'])
    if a=='rock':
        print('you choose scissors')
        print('computer choose',a)
        print('YOU LOSE')
    elif a=='paper':
        print('you choose scissors')
        print('computer choose',a)
        print('YOU WIN')
    else:
        print('you choose scissors')
        print('computer choose',a)
        print('Draw')


game = Tkinter.Tk()
game.title=("GAME")
r=Tkinter.Button(game,text='Rock',command=rock)
p=Tkinter.Button(game,text='Paper',command=paper)
s=Tkinter.Button(game,text='Scissor',command=scissors)
r.pack(padx=100,pady=50)
s.pack(padx=100,pady=50)
p.pack(padx=100,pady=50)
game.mainloop()
