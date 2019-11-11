from tkinter import*
w=Tk()
w.title("My calculator")
w.iconbitmap()
w.config(bg="#123456")
w.minsize(width=400,height=400)
fe=Frame(w,bg="#123456")
e=Entry(fe,font="arial 25 bold",justify=RIGHT)
e.pack(padx=10,pady=10,expand=YES,fill=BOTH)
fe.pack(padx=10,pady=10 ,expand=YES,fill=BOTH)
def display(x):
    global s1
    if x=="AC":
        s1=''
        s.set(s1)
    elif x=="DEL":
        s1=s1[:len(s.get())-1]
        s.set(s1)
    elif x!="=":
        s1=s1+x
        s.set(s1)
    else:
        try:
            s1=str(eval(s.get()))
            s.set(s1)
        except Exception as e:
            s.set(e)
            s1=''
s1=''
s=StringVar()
fe=Frame(w,bg="#123456")
for i in ["DEL","AC"]:
    b = Button(fe, text=i, bg="black", fg="white", font="arial 15 bold",relief=RAISED,COMMAND =lambda x=i:display(x))
    b.pack(side=LEFT, padx=5, pady=5, expand=YES, fill=BOTH)
fe.pack(padx=10,pady=10 ,expand=YES,fill=BOTH)
fe=Frame(w,bg="#123456")
for i in ["sin","cos","tan","log","ln"]:
    b = Button(fe, text=i, bg="grey", fg="white", font="arial 10 bold",relief=RAISED,COMMAND=lambda x=i:display(x))
    b.pack(side=LEFT, padx=4, pady=4, expand=YES, fill=BOTH)
fe.pack(padx=10,pady=10 ,expand=YES,fill=BOTH)
fe=Frame(w,bg="#123456")
for i in ["X2","X3","^","nCr"]:
    b = Button(fe, text=i, bg="grey", fg="white", font="arial 10 bold",relief=RAISED,COMMAND=lambda x=i:display(x))
    b.pack(side=LEFT, padx=4, pady=4, expand=YES, fill=BOTH)
fe.pack(padx=10,pady=10 ,expand=YES,fill=BOTH)
for i in ["789/","456*","123+",".0=-"]:
    f=Frame(w,bg="black")
    for j in i:
        b=Button(f,text=j,bg="black",fg="white",font="arial 15 bold",bd=5,relief=RAISED,COMMAND=lambda x=j:display(x))
        b.pack(side=LEFT,padx=10,pady=10,expand=YES,fill=BOTH)
    f.pack(padx=10,pady=10,expand=YES,fill=BOTH)
w.mainloop()
