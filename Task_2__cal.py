import tkinter
from tkinter import *

class Cal:

    def __init__(calsi, subroot):

        subroot.title("CALCULATOR")
        subroot.geometry("355x422+0+0")
        subroot.config(bg='grey')
        subroot.resizable(False, False)

        calsi.equation = StringVar()
        calsi.entry_value = ''

        Entry(width=17, bg='#fff', font=('Arial Bold', 28), textvariable=calsi.equation).place(x=0, y=0)

        Button(width=11,height=4,text='(',bg='white',command=lambda:calsi.show('(')).place(x=0,y=50)
        Button(width=11,height=4,text=')',bg='white',command=lambda:calsi.show(')')).place(x=90,y=50)
        Button(width=11,height=4,text='%',bg='white',command=lambda:calsi.show('%')).place(x=180,y=50)
        Button(width=11,height=4,text='1',bg='white',command=lambda:calsi.show('1')).place(x=0,y=125)
        Button(width=11,height=4,text='2',bg='white',command=lambda:calsi.show('2')).place(x=90,y=125)
        Button(width=11,height=4,text='3',bg='white',command=lambda:calsi.show('3')).place(x=180,y=125)
        Button(width=11,height=4,text='4',bg='white',command=lambda:calsi.show('4')).place(x=0,y=200)
        Button(width=11,height=4,text='5',bg='white',command=lambda:calsi.show('5')).place(x=90,y=200)
        Button(width=11,height=4,text='6',bg='white',command=lambda:calsi.show('6')).place(x=180,y=200)
        Button(width=11,height=4,text='7',bg='white',command=lambda:calsi.show('7')).place(x=0,y=275)
        Button(width=11,height=4,text='8',bg='white',command=lambda:calsi.show('8')).place(x=180,y=275)
        Button(width=11,height=4,text='9',bg='white',command=lambda:calsi.show('9')).place(x=90,y=275)
        Button(width=11,height=4,text='0',bg='white',command=lambda:calsi.show('0')).place(x=90,y=350)
        Button(width=11,height=4,text='.',bg='white',command=lambda:calsi.show('.')).place(x=180,y=350)
        Button(width=11,height=4,text='+',bg='white',command=lambda:calsi.show('+')).place(x=270,y=275)
        Button(width=11,height=4,text='-',bg='white',command=lambda:calsi.show('-')).place(x=270,y=200)
        Button(width=11,height=4,text='/',bg='white',command=lambda:calsi.show('/')).place(x=270,y=50)
        Button(width=11,height=4,text='x',bg='white',command=lambda:calsi.show('*')).place(x=270,y=125)

        Button(width=11, height=4, text='=', bg='lightblue', command=calsi.solve).place(x=270, y=350)
        Button(width=11, height=4, text='C', bg='red', command=calsi.clear).place(x=0, y=350)

    def show(calsi, value):
        calsi.entry_value += str(value)
        calsi.equation.set(calsi.entry_value)

    def clear(calsi):
        calsi.entry_value = ''
        calsi.equation.set(calsi.entry_value)

    def solve(calsi):
        try:
            result = eval(calsi.entry_value)
            calsi.equation.set(result)
        except ZeroDivisionError:
            calsi.equation.set("Error")

root = Tk()
cals = Cal(root)
root.mainloop()
