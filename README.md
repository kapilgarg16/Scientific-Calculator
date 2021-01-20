## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/kapilgarg16/Scientific-Calculator/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
from tkinter import*
from math import*
import time
import threading
w=Tk()
w.title("My calculator")
w.iconbitmap()
w.config(bg="black")
w.minsize(width=400,height=400)
def display(x):
    global s1
    if x=="AC":
        s1=''
        s.set(s1)
    elif x=="DEL":
        s1=s.get()
        s1=s1[:len(s.get())-1]
        s.set(s1)
    elif x!="=":
        s1=s1+x
        s.set(s1)
    else:
        try:
            if s1[0]=="√":
                s.set(str(sqrt(int(s.get()[1:]))))
            elif s1[0:3] == "sin":
                s.set(str(sin(int(s.get()[3:]))))
            elif s1[0:3] == "cos":
                s.set(str(cos(int(s.get()[3:]))))
            elif s1[0:3] == "tan":
                s.set(str(tan(int(s.get()[3:]))))
            elif s1[0:2] in "ln":
                s.set(str(log(float(s.get()[2:]))))
            elif s1[0:3] in "log":
                s.set(str(log10(float(s.get()[3:]))))
            elif s1[0]=="!":
                    s.set(str(factorial(int(s.get()[1:]))))
            elif s1[len(s1)-1] == "!":
                     s.set(str(factorial(int(s.get()[:len(s1)-1]))))
            elif s1[:4] == "cosh":
                s.set(str(cosh((int(s.get()[4:])))))
            elif s1[:4] == "sinh":
                s.set(str(sinh(int(s.get()[4:]))))
            elif s1[:4] == "tanh":
                s.set(str(tanh(int(s.get()[4:]))))
            elif s1[:2]=="e ":
                s.set(str(exp(int(s.get()[2:]))))
            elif s1[len(s1)-1:] == "²":
                s.set(str((int(s.get()[:len(s1)-1]))**2))
            elif s1[len(s1)-3:]==" x3":
                s.set(str((int(s.get()[:len(s1)-3]))**3))
            elif "^"in s1:
                l=s1.partition("^")
                s.set(str(int(l[0])**int(l[-1])))
            elif "c"in s1:
                l=s1.partition("c")
                per=factorial(int(l[0]))//(factorial(int(l[0])-int(l[-1]))*factorial(int(l[-1])))
                s.set(str(per))
            else:
                s.set(str(eval(s.get())))
        except Exception as e:
            s.set(e)
            s1=''
s1=''
s=StringVar()
fe=Frame(w,bg="#123456")
e=Entry(fe,textvariable=s,bg="powder blue",font="arial 25 bold",justify=RIGHT)
e.pack(padx=10,pady=10,expand=YES,fill=BOTH)
fe.pack(padx=10,pady=10 ,expand=YES,fill=BOTH)

fe=Frame(w,bg="#123456")
for i in ["sin","cos","tan","log","eⁿ"]:
    b = Button(fe, text=i, bg="grey", fg="black", font="arial 10 bold",relief=RAISED,command=lambda x=i if i!="eⁿ" else "e ":display(x))
    b.pack(side=LEFT, padx=4, pady=4, expand=YES, fill=BOTH)
fe.pack(padx=10,pady=10 ,expand=YES,fill=BOTH)
fe=Frame(w,bg="#123456")
for i in ["sinh","cosh","tanh","X!","ln"]:
    b = Button(fe, text=i, bg="grey", fg="black", font="arial 10 bold",relief=RAISED,command=lambda x=i if i!="X!"else "!":display(x))
    b.pack(side=LEFT, padx=4, pady=4, expand=YES, fill=BOTH)
fe.pack(padx=10,pady=10 ,expand=YES,fill=BOTH)
fe=Frame(w,bg="#123456")
for i in ["X²"," x3","√","^"]:
    b = Button(fe, text=i, bg="grey", fg="black", font="arial 10 bold",relief=RAISED,command=lambda x=i if i!="X²" else "²" :display(x))
    b.pack(side=LEFT, padx=4, pady=4, expand=YES, fill=BOTH)
fe.pack(padx=10,pady=10 ,expand=YES,fill=BOTH)
p=iter(["grey","powder blue","powder blue"])
fe=Frame(w,bg="#123456")
for i in ["nCr","DEL","AC"]:
    b = Button(fe, text=i, bg=next(p), fg="black", font="arial 10 bold",relief=RAISED,command=lambda x=i if i!="nCr" else "c" :display(x))
    b.pack(side=LEFT, padx=4, pady=4, expand=YES, fill=BOTH)
fe.pack(padx=10,pady=10 ,expand=YES,fill=BOTH)
for i in ["789/","456*","123+",".0=-"]:
    f=Frame(w,bg="black")
    for j in i:
        b=Button(f,text=j,bg="black",fg="white",font="arial 15 bold",relief=RAISED,command=lambda x=j:display(x))
        b.pack(side=LEFT,padx=10,pady=10,expand=YES,fill=BOTH)
    f.pack(padx=10,pady=10,expand=YES,fill=BOTH)

f1=Frame(w,bg="black")
def Time():
    while True:
        label["text"]=time.ctime()
        time.sleep(1)
label=Label(f1,font=("arial 20"),justify=RIGHT,bg="black",fg="white",relief=RAISED,bd=2)
label["text"]=time.ctime()
label.pack(expand=YES,fill=BOTH)
f1.pack(expand=YES,fill=BOTH)
t=threading.Thread(target=Time,daemon=True)
t.start()
w.mainloop()
```
