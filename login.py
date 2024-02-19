from tkinter import *
from tkinter import ttk
win=Tk()
win.title("www.personaldetails.com")
win.geometry("500x500+500+500")
win.state("zoomed")

def login():
    a=tbEntrya
    b=tbEntryb
    if(a=="rooban" & b=="1234"):
        print("You are enterd....")
    else:
        print("You are not allowed....")


label1msg=Label(win,text="User Name",font=("Batang",14),fg="black")
label1msg.grid(row=1,column=20,pady=10)
tbEntrya=Entry(win, width=60)
tbEntrya.grid(row=1,column=25)

label1msg=Label(win,text="Password",font=("Batang",14),fg="black")
label1msg.grid(row=2,column=20,pady=10)
tbEntryb=Entry(win, width=60)
tbEntryb.grid(row=2,column=25)

btnlo=Button(win,text="Login",font=("Batang",14),fg="White",bg="Green",command=login)
btnlo.grid(row=7,column=1)