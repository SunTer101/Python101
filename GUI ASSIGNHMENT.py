from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
import tkinter as tk
GUI = Tk() #นี่คือหน้าจอโปรแกม
GUI.title('โปรแกรมบันทึกข้อมูลออกกำลังกาย') #ชื่อสำหรับหน้าจอ
GUI.geometry("350x700")# แล้วสามารถพิมพ์อธิบายได้

L1 = Label (GUI,text='EXERCISE',font=('Angsana New',25),fg='blue')
L1.place (x=30,y=20)

L2 = Label (GUI,text='Prat of play',font=('Angsana New',20),fg='orange')
L2.place (x=30,y=70)


L3 = Label (GUI,text='Times',font=('Angsana New',20),fg='red')
L3.place (x=220,y=70)


##########################

def Button1():
    text = 'Successfully'
    messagebox.showinfo('14 FEB 2023',text)
    
B1 = ttk.Button(GUI,text='Record',command=Button1)
B1.place (x=50,y=500)
##########################

def Button2():
    text = 'Failed'
    messagebox.showwarning('New record',text)
    
B2 = ttk.Button(GUI,text='Cancel',command=Button2)
B2.place (x=200,y=500)

##########

GUI.mainloop()
