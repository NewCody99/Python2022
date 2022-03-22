from tkinter import *
from tkinter import ttk,messagebox
 
 
GUI = Tk()
GUI.geometry('500x300')
GUI.title('Python GUI EP1 ^^')

def showpop():
    messagebox.showinfo('Show Box','hello world')


B1 = ttk.Button(GUI,text='Click here!!',command= showpop)
B1.pack(ipadx=20,ipady=20)



GUI.mainloop()