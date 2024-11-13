#calculator
from tkinter import*
root=Tk()
def btn_click(n):
    global data
    data=data+n
    #en.set(n)
    en.set(data)

def clr():
    global data
    data=""
    en.set(data)
def eql():
    global data
    val=eval(en.get())
    data=str(val)
    en.set(data)
def sqr():
    global data
    data=""
    eval(en.get())
    res=eval(en.get())
    data=str(res**2)
    en.set(data)
def cube():
    global data
    data=""
    eval(en.get())
    rs=eval(en.get())
    data=str(rs*3)
    en.set(data)
    
import math
def factorial():
    r=eval(en.get())
    r=math.factorial(r)
    data=str(r)
    en.set(data)

def backspace():
    global data
    data=""
    re=en.get()
    c=len(re)
    data=re[0:c-1]
    en.set(data)
    

data=""
en=StringVar()
Entry(root,textvariable=en).grid(row=0,columnspan=4)



Button(root,text='7',bg='pink',font='Now 25 bold',bd=10,command=lambda:btn_click('7')).grid(row=1,column=0)
Button(root,text='8',bg='pink',font='Now 25 bold',bd=10,command=lambda:btn_click('8')).grid(row=1,column=1)
Button(root,text='9',bg='pink',font='Now 25 bold',bd=10,command=lambda:btn_click('9')).grid(row=1,column=2)
Button(root,text='+',bg='pink',font='Now 25 bold',bd=10,command=lambda:btn_click('+')).grid(row=1,column=3)

Button(root,text='4',bg='pink',font='Now 25 bold',bd=10 ,command=lambda:btn_click('4')).grid(row=2,column=0)
Button(root,text='5',bg='pink',font='Now 25 bold' ,bd=10,command=lambda:btn_click('5')).grid(row=2,column=1)
Button(root,text='6',bg='pink',font='Now 25 bold',bd=10,command=lambda:btn_click('6')).grid(row=2,column=2)
Button(root,text='-',bg='pink',font='Now 25 bold',bd=10,command=lambda:btn_click('-')).grid(row=2,column=3)

Button(root,text='1',bg='pink',font='Now 25 bold',bd=10,command=lambda:btn_click('1')).grid(row=3,column=0)
Button(root,text='2',bg='pink',font='Now 25 bold' ,bd=10,command=lambda:btn_click('2')).grid(row=3,column=1)
Button(root,text='3',bg='pink',font='Now 25 bold',bd=10, command=lambda:btn_click('3')).grid(row=3,column=2)
Button(root,text='*',bg='pink',font='Now 25 bold',bd=10,command=lambda:btn_click('*')).grid(row=3,column=3)

Button(root,text='C',bg='pink',font='Now 25 bold',bd=10,command=clr).grid(row=4,column=0)
Button(root,text='0',bg='pink',font='Now 25 bold',bd=10).grid(row=4,column=1)
Button(root,text='=',bg='pink',font='Now 25 bold',bd=10,command=eql).grid(row=4,column=2)
Button(root,text='/',bg='pink',font='Now 25 bold',bd=10,command=lambda:btn_click('/')).grid(row=4,column=3)

Button(root,text='^2',bg='pink',font='Now 25 bold',bd=10,command=sqr).grid(row=5,column=0)
Button(root,text='^3',bg='pink',font='Now 25 bold',bd=10,command=cube).grid(row=5,column=1)
Button(root,text='n!',bg='pink',font='Now 25 bold',bd=10,command=factorial).grid(row=5,column=2)
Button(root,text='<--',bg='pink',font='Now 25 bold',bd=10,command=backspace).grid(row=5,column=3)



#square^2 cube^3 factorial n!  and for back space <--



