from msilib.schema import Font
from tkinter import *
from tkinter import ttk,messagebox
import csv
from datetime import datetime
 
def wcsv(data):
    with open('data.csv','a',newline='',encoding='utf-8') as file :
        fw = csv.writer(file)
        fw.writerow(data)

GUI = Tk()
GUI.geometry('500x300')
GUI.title('โปรแกรม')
FONT1 = ('Js sadayu',20)

L1 = ttk.Label(GUI,text='กรอกจำนวนกุ้ง (กิโลกรัม)',font=('Js sadayu',32))
L1.pack()

v_kilo = StringVar() # เอาไว้เก็บค่า

E1 = ttk.Entry(GUI,width=10,textvariable= v_kilo,font = ('Js sadayu',30),justify='right')
E1.pack(pady=20)

def calc(event=None):
    kilo = float(v_kilo.get())
    print(kilo*299)
    calr = kilo * 299
    dtf = datetime.now()
    year = dtf.year + 543
    dt = datetime.now().strftime('%d-%m-{} %H:%M:%S'.format(year))
    data = [dt,'กุ้ง','{:.2f}'.format(calr)]
    wcsv(data)
    messagebox.showinfo('รวมราคาทั้งหมด','ลูกค้าต้องจ่ายตัง : {:.2f} บาท'.format(calr))

GUI.bind('<Return>',calc)

B1 = ttk.Button(GUI,text='คำนวณราคา',command=calc)
B1.pack(ipadx=40,ipady=30)

GUI.mainloop()