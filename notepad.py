from tkinter import *
from tkinter import ttk

roar=Tk()
roar.title("Notepad")
roar.geometry("500x500")
roar.state("zoomed")

def close():
    roar.destroy()

menubar=Menu(roar)
filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New             Ctrl+N")
filemenu.add_command(label="Open....        Ctrl+O")
filemenu.add_command(label="Save            Ctrl+S")
filemenu.add_command(label="Save As....")
filemenu.add_separator()
filemenu.add_command(label="Page Setup....")
filemenu.add_command(label="Print....       Ctrl+P")
filemenu.add_separator()
filemenu.add_command(label="Exit",command=close)

editmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Undo            Ctrl+Z")
editmenu.add_command(label="Cut             Ctrl+X")
editmenu.add_command(label="Copy            Ctrl+C")
editmenu.add_command(label="Paste           Ctrl+V")
editmenu.add_command(label="Delete          Del")
editmenu.add_separator()
editmenu.add_command(label="Find            Ctrl+F")
editmenu.add_command(label="Find Next       F3")
editmenu.add_command(label="Replace         Ctrl+H")
editmenu.add_command(label="Go To....       Ctrl+G")
editmenu.add_separator()
editmenu.add_command(label="Select All      Ctrl+A")
editmenu.add_command(label="Time/Date       F5")

formatmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Format",menu=formatmenu)
formatmenu.add_command(label="Word Wrap")
formatmenu.add_command(label="Font....")


viewmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="View",menu=viewmenu)
viewmenu.add_command(label="Zoom")
'''Zoommenu=Menu(viewmenu,tearoff=0)
Zoommenu.add_command(label="Zoom In                 Ctrl+Plus")
Zoommenu.add_command(label="Zoom Out                Ctrl+Minus")
Zoommenu.add_command(label="Restore Default Zoom    Ctrl+0")'''
viewmenu.add_command(label="Status bar")

helpimenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=helpimenu)
helpimenu.add_command(label="View Help")
helpimenu.add_separator()
helpimenu.add_command(label="About Notepad")

roar.config(menu=menubar)
roar.mainloop()

