from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
GUI = Tk() #นี่คือหน้าจอโปรแกม
GUI.title('โปรแกรมบันทึกข้อมูล') #ชื่อสำหรับหน้าจอ
GUI.geometry("500x400")# แล้วสามารถพิมพ์อธิบายได้

L1 = Label (GUI,text='โปรแกรมบันทึกประจำวัน',font=('Angsana New',30),fg='green')
L1.place (x=30,y=20)



def Button2 () :
    text = 'มีเงินในบัญชีอยู่ 300 บาท'
    #messagebox.showinfo('เงินในบัญชี',text)
    messagebox.showwarning('เงินในบัญชี',text)
     #messagebox.showerror('เงินในบัญชี',text)

FB1=Frame(GUI) #คล้ายกระดาษ
FB1.place(x=100,y=180)
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)
B2.pack(ipadx=50,ipady=50)

def Button3 () :
    text = 'วันนี้เรียนอะไรบ้าง ?'
    messagebox.showinfo('วันที่ 10-20  ก.พ.',text)
    #messagebox.showwarning('เงินในบัญชี',text)
    #messagebox.showerror('เงินในบัญชี',text)

FB2=Frame(GUI) #คล้ายกระดาษ
FB2.place(x=100,y=80)
B3 = ttk.Button(FB2,text='วันเวลาไหน',command=Button3)
B3.pack(ipadx=50,ipady=50)

GUI.mainloop()
