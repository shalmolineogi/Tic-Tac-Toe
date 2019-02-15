#import random
from tkinter import *
import sys
import os
import tkinter.messagebox
#from tkinter import ttk
#import tkMessagebBox
root = Tk()

g = 0
f1 = 2
f2 = 2
f3 = 2
f4 = 2
f5 = 2
f6 = 2
f7 = 2
f8 = 2
f9 = 2
c = 0


'''canvas = Canvas(root,width='200',height='100')
canvas.pack()
b = canvas.create_line(0,0,30,15)'''
'''class button1:
    def __init__(self,master):
        f1 = Frame(master).pack()
        #f2 = Frame(master).pack()
        #f3 = Frame(master).pack()
        self.b1 = Button(f1,width='10',height='5',command=self.click()).pack(side=LEFT)
        self.b2 = Button(f1,width='10',height='5',command=self.click()).pack(side=LEFT)
        self.b3 = Button(f1,width='10',height='5',command=self.click()).pack(side=LEFT)
        #self.b4 = Button(f2,width='10',height='5',command=self.click()).pack(side=LEFT)
        #self.b5 = Button(f2,width='10',height='5',command=self.click()).pack(side=LEFT)
        #self.b6 = Button(f2,width='10',height='5',command=self.click()).pack(side=LEFT)
        #self.b7 = Button(f3,width='10',height='5',command=self.click()).pack(side=LEFT)
        #self.b8 = Button(f3,width='10',height='5',command=self.click()).pack(side=LEFT)
        #self.b9 = Button(f3,width='10',height='5',command=self.click()).pack(side=LEFT)
    def click(self):
        s = random.randint(0,1)
        if s==0:
            print('0')
        else:
            print('*')'''
def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

def won(n,i,j,k):
    if [i,j,k]==[1,2,3]:
        label_1.config(bg="green")
        label_2.config(bg="green")
        label_3.config(bg="green")
    elif [i,j,k]==[1,4,7]:
        label_1.config(bg="green")
        label_4.config(bg="green")
        label_7.config(bg="green")
    elif [i,j,k]==[1,5,9]:
        label_1.config(bg="green")
        label_5.config(bg="green")
        label_9.config(bg="green")
    elif [i,j,k]==[3,5,7]:
        label_3.config(bg="green")
        label_5.config(bg="green")
        label_7.config(bg="green")
    elif [i,j,k]==[3,6,9]:
        label_3.config(bg="green")
        label_6.config(bg="green")
        label_9.config(bg="green")
    elif [i,j,k]==[4,5,6]:
        label_4.config(bg="green")
        label_5.config(bg="green")
        label_6.config(bg="green")
    elif [i,j,k]==[7,8,9]:
        label_7.config(bg="green")
        label_8.config(bg="green")
        label_9.config(bg="green")
    elif [i,j,k]==[2,5,8]:
        label_2.config(bg="green")
        label_5.config(bg="green")
        label_8.config(bg="green")
    if n==1:
        tkinter.messagebox.showinfo('Winner','Player 1:X WON!!!!:)')
    else:
        tkinter.messagebox.showinfo('Winner','Player 2:O WON!!!!:)')
    if tkinter.messagebox.askokcancel("Exit","Play Again?"):
        restart_program()
    else:
        root.destroy()


    
'''def click(n):
    global g,f1,f2,f3,f4,f5,f6,f7,f8,f9
    g+=1
    if n==1able_1:
        if g%2==0:
            label_1.config(text="O",state='disable')
            f1=0
        else:
            label_1.config(text="X",state='disable')
            f1=1
        if f1==f2 and f2==f3:
            won(f1)
        elif f1==f5 and f5==f9:
            won(f1)
        elif f1==f4 and f4==f7:
            won(f1)
    elif n==1able_2:
        if g%2==0:
            label_2.config(text="O",state='disable')
            f2=0
        else:
            label_2.config(text="X",state='disable')
            f2=1
        if f2==f1 and f2==f3:
            won(f2)
        elif f2==f5 and f5==f8:
            won(f2)
    elif n==1able_3:
        if g%2==0:
            label_3.config(text="O",state='disable')
            f3=0
        else:
            label_3.config(text="X",state='disable')
            f3=1
        if f3==f5 and f5==f7:
            won(f3)
        elif f3==f1 and f1==f2:
            won(f3)
    elif n==1able_4:
        if g%2==0:
            label_4.config(text="O",state='disable')
            f4=0
        else:
            label_4.config(text="X",state='disable')
            f4=1
        if f4==f5 and f5==f6:
            won(f4)
        elif f1==f4 and f4==f7:
            won(f4)
    elif n==1able_5:
        if g%2==0:
            label_5.config(text="O",state='disable')
            f5=0
        else:
            label_5.config(text="X",state='disable')
            f5=1
        if f4==f5 and f5==f6:
            won(f5)
        elif f2==f5 and f5==f8:
            won(f5)
        elif f1==f5 and f5==f9:
            won(f5)
        elif f3==f5 and f5==f7:
            won(f5)
    elif n==6:
        if g%2==0:
            label_6.config(text="O",state='disable')
            f6=0
        else:
            label_6.config(text="X",state='disable')
            f6=1
        if f6==f5 and f5==f4:
            won(f6)
        elif f3==f6 and f6==f9:
            won(f6)
    elif n==7:
        if g%2==0:
            label_7.config(text="O",state='disable')
            f7=0
        else:
            label_7.config(text="X",state='disable')
            f7=1
        if f3==f5 and f5==f7:
            won(f7)
        elif f7==f8 and f8==f9:
            won(f7)
    elif n==8:
        if g%2==0:
            label_8.config(text="O",state='disable')
            f8=0
        else:
            label_8.config(text="X",state='disable')
            f8=1
        if f7==f8 and f8==f9:
            won(f8)
        elif f2==f5 and f5==f8:
            won(f8)
    elif n==9:
        if g%2==0:
            label_9.config(text="O",state='disable')
            f9=0
        else:
            label_9.config(text="X",state='disble')
            f9=1
        if f1==f5 and f5==f9:
            won(f9)
        elif f7==f8 and f8==f9:
            won(f9)
        elif f3==f6 and f6==f9:
            won(f9)
    return
    if f1==f2 and f2==f3:
        won(f1)
    elif f1==f5 and f5==f9:
        won(f1)
    elif f1==f4 and f4==f7:
        won(f1)
    elif f2==f5 and f5==f8:
        won(f2)
    elif f3==f5 and f5==f7:
        won(f3)
    elif f3==f6 and f6==f9:
        won(f3)
    elif f4==f5 and f5==f6:
        won(f6)
    elif f7==f8 and f8==f9:
        won(f7)'''
    
        
def click1():
    global g,f1,f2,f3,f4,f5,f6,f7,f8,f9,c
    g+=1
    c+=1
    if g%2==0:
        label_1.config(text="O",state='disabled')
        f1=0
    else:
        label_1.config(text="X",state='disabled')
        f1=1
    if f1==f5 and f5==f9:
        won(f5,1,5,9)
    elif f1==f2 and f2==f3:
        won(f2,1,2,3)
    elif f1==f4 and f4==f7:
        won(f1,1,4,7)
    if c==9:
        tkinter.messagebox.showinfo('Draw','Match Draw:(')
        if tkinter.messagebox.askokcancel("Exit","Play Again?"):
            restart_program()
        else:
            root.destroy()
    

def click2():
    global g,f1,f2,f3,f4,f5,f6,f7,f8,f9,c
    c+=1
    g+=1
    if g%2==0:
        label_2.config(text="O",state='disabled')
        f2=0
    else:
        label_2.config(text="X",state='disabled')
        f2=1
    if f2==f5 and f2==f8:
        won(f2,2,5,8)
    elif f1==f2 and f2==f3:
        won(f2,1,2,3)
    if c==9:
        tkinter.messagebox.showinfo('Draw','Match Draw:(')
        if tkinter.messagebox.askokcancel("Exit","Play Again?"):
            restart_program()
        else:
            root.destroy()

def click3():
    global g,f1,f2,f3,f4,f5,f6,f7,f8,f9,c
    c+=1
    g+=1
    if g%2==0:
        label_3.config(text="O",state='disabled')
        f3=0
    else:
        label_3.config(text="X",state='disabled')
        f3=1
    if f1==f2 and f2==f3:
        won(f3,1,2,3)
    elif f3==f5 and f5==f7:
        won(f3,3,5,7)
    elif f3==f6 and f6==f9:
        won(f3,3,6,9)
    if c==9:
        tkinter.messagebox.showinfo('Draw','Match Draw:(')
        if tkinter.messagebox.askokcancel("Exit","Play Again?"):
            restart_program()
        else:
            root.destroy()

def click4():
    global g,f1,f2,f3,f4,f5,f6,f7,f8,f9,c
    c+=1
    g+=1
    if g%2==0:
        label_4.config(text="O",state='disabled')
        f4=0
    else:
        label_4.config(text="X",state='disabled')
        f4=1
    if f4==f5 and f5==f6:
        won(f4,4,5,6)
    elif f1==f4 and f4==f7:
        won(f4,1,4,7)
    if c==9:
        tkinter.messagebox.showinfo('Draw','Match Draw:(')
        if tkinter.messagebox.askokcancel("Exit","Play Again?"):
            restart_program()
        else:
            root.destroy()


def click5():
    global g,f1,f2,f3,f4,f5,f6,f7,f8,f9,c
    c+=1
    g+=1
    if g%2==0:
        label_5.config(text="O",state='disabled')
        f5=0
    else:
        label_5.config(text="X",state='disabled')
        f5=1
    if f1==f5 and f5==f9:
        won(f5,1,5,9)
    elif f3==f5 and f5==f7:
        won(f5,3,5,7)
    elif f4==f5 and f5==f6:
        won(f5,4,5,6)
    elif f2==f5 and f5==f8:
        won(f5,2,5,8)
    if c==9:
        tkinter.messagebox.showinfo('Draw','Match Draw:(')
        if tkinter.messagebox.askokcancel("Exit","Play Again?"):
            restart_program()
        else:
            root.destroy()

def click6():
    global g,f1,f2,f3,f4,f5,f6,f7,f8,f9,c
    c+=1
    g+=1
    if g%2==0:
        label_6.config(text="O",state='disabled')
        f6=0
    else:
        label_6.config(text="X",state='disabled')
        f6=1
    if f3==f6 and f6==f9:
        won(f6,3,6,9)
    elif f4==f5 and f5==f6:
        won(f6,4,5,6)
    if c==9:
        tkinter.messagebox.showinfo('Draw','Match Draw:(')
        if tkinter.messagebox.askokcancel("Exit","Play Again?"):
            restart_program()
        else:
            root.destroy()

def click7():
    global g,f1,f2,f3,f4,f5,f6,f7,f8,f9,c
    c+=1
    g+=1
    if g%2==0:
        label_7.config(text="O",state='disabled')
        f7=0
    else:
        label_7.config(text="X",state='disabled')
        f7=1
    if f1==f4 and f4==f7:
        won(f7,1,4,7)
    elif f7==f8 and f8==f9:
        won(f7,7,8,9)
    elif f3==f5 and f5==f7:
        won(f7,3,5,7)
    if c==9:
        tkinter.messagebox.showinfo('Draw','Match Draw:(')
        if tkinter.messagebox.askokcancel("Exit","Play Again?"):
            restart_program()
        else:
            root.destroy()

def click8():
    global g,f1,f2,f3,f4,f5,f6,f7,f8,f9,c
    c+=1
    g+=1
    if g%2==0:
        label_8.config(text="O",state='disabled')
        f8=0
    else:
        label_8.config(text="X",state='disabled')
        f8=1
    if f2==f5 and f5==f8:
        won(f8,2,5,8)
    elif f7==f8 and f8==f9:
        won(f8,7,8,9)
    if c==9:
        tkinter.messagebox.showinfo('Draw','Match Draw:(')
        if tkinter.messagebox.askokcancel("Exit","Play Again?"):
            restart_program()
        else:
            root.destroy()
        

def click9():
    global g,f1,f2,f3,f4,f5,f6,f7,f8,f9,c
    c+=1
    g+=1
    if g%2==0:
        label_9.config(text="O",state='disabled')
        f9=0
    else:
        label_9.config(text="X",state='disabled')
        f9=1
    if f7==f8 and f8==f9:
        won(f9,7,8,9)
    elif f3==f6 and f6==f9:
        won(f9,3,6,9)
    elif f1==f5 and f5==f9:
        won(f9,1,5,9)
    if c==9:
        tkinter.messagebox.showinfo('Draw','Match Draw:(')
        if tkinter.messagebox.askokcancel("Exit","Play Again?"):
            restart_program()
        else:
            root.destroy()
    


label_1= Button(root,width='10',height='5',command=click1)
label_2= Button(root,width='10',height='5',command=click2)
label_3= Button(root,width='10',height='5',command=click3)
label_4= Button(root,width='10',height='5',command=click4)
label_5= Button(root,width='10',height='5',command=click5)
label_6= Button(root,width='10',height='5',command=click6)
label_7= Button(root,width='10',height='5',command=click7)
label_8= Button(root,width='10',height='5',command=click8)
label_9= Button(root,width='10',height='5',command=click9)

label_1.grid(row=0,column=0)
label_2.grid(row=0,column=1)
label_3.grid(row=0,column=2)
label_4.grid(row=1,column=0)
label_5.grid(row=1,column=1)
label_6.grid(row=1,column=2)
label_7.grid(row=2,column=0)
label_8.grid(row=2,column=1)
label_9.grid(row=2,column=2)


#b = button1(root)
root.mainloop()
