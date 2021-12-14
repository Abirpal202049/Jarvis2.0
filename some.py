from platform import java_ver
from JARVIS import *
from tkinter import *


def rtx():
    d=boom(speak, wishMe, takeCommando, command)
    return d

root= Tk()
root.title('J.A.R.V.I.S')
root.geometry('400x800')
# root.iconbitmap('boss.ico')
root.iconbitmap('hero.ico')
root.maxsize(400,800)
root.minsize(400,800)

p=Label(text='My Personal Assistance',bg='#00ff00',font=('Product Sans Light',20,'bold'),padx='10',pady='10',border=30,relief=RIDGE,borderwidth=5,activebackground='red',activeforeground='red')
p.pack(fill=X,padx='1',pady='1')

l=Button(root,text='J.A.R.V.I.S',bg='red',fg='#000000',font=('Product Sans Light', 35, 'bold'),borderwidth=5,relief=RAISED,padx='7',pady='7',height=30,activebackground='red',activeforeground='#000000',command=rtx)

l.pack(side=BOTTOM,pady='300')
root.mainloop()
# .pyw extension helps to remove the python console 