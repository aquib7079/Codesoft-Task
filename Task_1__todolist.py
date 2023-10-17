import tkinter
from tkinter import *
root = Tk()
root.title("To-Do-List")
root.resizable(False,False)
root.geometry("400x630+100+100")

task_list = []

def addTask():
    task = task_input.get()
    task_input.delete(0,END)

    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)


def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")

        listbox.delete(ANCHOR)


def openTaskFile():
    
    try:
        global task_list
        with open("tasklist.txt",'r') as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END,task)

    
    except:
        file = open('tasklist.txt','w')
        file.close()






#main

#heading

heading=Label(root,text="TO DO LIST",font="boulder 24 bold",fg="black",bg="green").pack()

#add task

frame = Frame(root,width = 600,height = 50, bg = "grey")
frame.place(x=0,y=100)

task = StringVar()
task_input = Entry(frame,width = 28,font = "arial 18",bd = 0)
task_input.place(x=0,y=10)
task_input.focus()

button = Button(frame,text="Add",font="amertypemdbt 20 bold",width=6,bg="grey",fg="white",bd=0,command=addTask)
button.place(x=300,y=0)

#all task
frame1 = Frame(root,bd=3,width = 700,height=280,bg="#32405b")
frame1.pack(pady=(160,0))

listbox = Listbox(frame1,font = ('arial',12),width=40,height=16,bg="#32405b")
listbox.pack(side = LEFT, fill=BOTH,padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()


#removetask
frame2 = Frame(root,width = 600,height = 50, bg = "white")
frame2.place(x=0,y=550)
button = Button(frame2,text="Delete",font="arial 20 bold",width=6,bg="lightblue",fg="red",bd=0,command=deleteTask)
button.place(x=150,y=0)


root.mainloop()