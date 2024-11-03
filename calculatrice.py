import tkinter
from tkinter import *

win = Tk()
win.geometry('445x570')
win.title("calculator")
win.config(background="#D1C48C")
win.resizable(False, False)

equation = ""

def afiche(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calcul():
    global equation
    result =""
    if equation !="":
        try:
            result= eval(equation)
        except:
            result ="error"
            equation = ""
    label_result.config(text=result)


label_result=Label(win,width=18,height=2,text="",font=("arial",30),bd="5")
label_result.place(x=10,y=20)

"// les buttone ///////////////////////////////////////////////////////////////////////////////////////// place les widget ////////"

Button(win,text="C",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#FAB927",command=lambda: clear()).place(x=5,y=138)
Button(win,text="%",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#68A2FA",command=lambda: afiche("%")).place(x=115,y=138)
Button(win,text="/",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#68A2FA",command=lambda: afiche("/")).place(x=226,y=138)
Button(win,text="*",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#68A2FA",command=lambda: afiche("*")).place(x=336,y=138)

Button(win,text="7",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#68A2FA",command=lambda: afiche("7")).place(x=5,y=225)
Button(win,text="8",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#68A2FA",command=lambda: afiche("8")).place(x=115,y=225)
Button(win,text="9",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#68A2FA",command=lambda: afiche("9")).place(x=226,y=225)
Button(win,text="-",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#68A2FA",command=lambda: afiche("-")).place(x=336,y=225)

Button(win,text="4",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#68A2FA",command=lambda: afiche("4")).place(x=5,y=312)
Button(win,text="5",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#68A2FA",command=lambda: afiche("5")).place(x=115,y=312)
Button(win,text="6",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#68A2FA",command=lambda: afiche("6")).place(x=226,y=312)
Button(win,text="+",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#68A2FA",command=lambda: afiche("+")).place(x=336,y=312)

Button(win,text="1",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#68A2FA",command=lambda: afiche("1")).place(x=5,y=398)
Button(win,text="2",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#68A2FA",command=lambda: afiche("2")).place(x=115,y=398)
Button(win,text="3",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#68A2FA",command=lambda: afiche("3")).place(x=226,y=398)

Button(win,text="0",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#68A2FA",command=lambda: afiche("0")).place(x=5,y=485)
Button(win,text="00",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#68A2FA",command=lambda: afiche("00")).place(x=115,y=485)
Button(win,text=".",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#68A2FA",command=lambda: afiche(".")).place(x=226,y=485)
Button(win,text="=",width=4,height=3,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#FAB927",command=lambda: calcul()).place(x=336,y=395)

win.mainloop()
