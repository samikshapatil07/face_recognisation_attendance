import csv
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

from new_std_face import New_Std_Face


def NewDetailsRegister(master):
    Take_Att = Toplevel(master)
    Take_Att.geometry("500x400+500+100")
    
    def show_selected_record(event):
        pass
    
    
    def Reset_Form():
        Take_Att.geometry("500x400+500+100")
        BtnList['text'] = 'List'
        BtnList['command'] = Expand_Form

    def Expand_Form():
        Take_Att.geometry("900x400+300+100")
        BtnList['text'] = 'Reset'
        BtnList['command'] = Reset_Form
        
    
    def Save_Data():
        val_str = ComboStream.get()
        val_class = ComboClass.get()
        val_roll = TxtRoll.get()
        val_name = TxtName.get()
        
        row = [val_str, val_roll, val_name, val_class]
        
        with open(
            "StudentDetails\studentdetails.csv",
            "a+",
        ) as csvFile:
            writer = csv.writer(csvFile, delimiter=",")
            writer.writerow(row)
            csvFile.close()
        
        messagebox.showinfo("","Student Added Successfully...",parent=Take_Att)
        Take_Att.destroy()
        New_Std_Face(master)
    
    stream_values = {1:'CSE',2:'ENTC',3:'AIDS'}
    class_values = {1:'FY',2:'SY',3:'TY',4:'Btech'}

    Take_Att.title("Student Register Form")

    Frm1 = LabelFrame(Take_Att, width=480, height=380,)
    Frm1.place(x=10,y=10)
    
    Frm2 = LabelFrame(Take_Att, width=390, height=380,)
    Frm2.place(x=500,y=10)
    
    LblHead = Label(Frm1, text='Student Registration Form', font=('Arial',24), fg='blue')
    LblHead.place(x=80,y=10)
    
    LblStream = Label(Frm1, text='Stream', font=('Arial',16), fg='black')
    LblStream.place(x=10,y=70)
    ComboStream = Combobox(Frm1, width=18, font=('Arial',16), values=list(stream_values.values()))
    ComboStream.place(x=140,y=70)
    ComboStream.set(list(stream_values.values())[0])
    
    LblClass = Label(Frm1, text='Class', font=('Arial',16), fg='black')
    LblClass.place(x=10,y=120)
    ComboClass = Combobox(Frm1, width=18, font=('Arial',16), values=list(class_values.values()))
    ComboClass.place(x=140,y=120)
    ComboClass.set(list(class_values.values())[0])
    
    LblRoll = Label(Frm1, text='Roll No',font=('Arial',16))
    LblRoll.place(x=10,y=170)
    TxtRoll = Entry(Frm1, width=20,font=('Arial',16))
    TxtRoll.place(x=140, y=170)
    
    LblName = Label(Frm1, text='Enter Name',font=('Arial',16))
    LblName.place(x=10,y=220)
    TxtName = Entry(Frm1, width=20,font=('Arial',16))
    TxtName.place(x=140, y=220)
    
    BtnSave = Button(Frm1, text='Save & Next', bg='green', fg='white', width=12, font=('Arial',14), command=Save_Data)
    BtnSave.place(x=100,y=280)

    BtnList = Button(Frm1, text='List', bg='brown', fg='white', width=12, font=('Arial',14), command=Expand_Form)
    BtnList.place(x=260,y=280)
    
    style = ttk.Style()
    style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Arial', 12)) # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", highlightthickness=0, bd=0, font=('Arial', 11)) # Modify the font of the body

    columns = ("#1", "#2", "#3", "#4")
    TreeViewOptions = ttk.Treeview(Frm2, show="headings", height="10", columns=columns, style="mystyle.Treeview")

    TreeViewOptions.heading('#1', text='Roll No', anchor='center')
    TreeViewOptions.column('#1', width=60, anchor='center', stretch=False)
    TreeViewOptions.heading('#2', text='Name', anchor='center')
    TreeViewOptions.column('#2', width=10, anchor='center', stretch=True) 
    TreeViewOptions.heading('#3', text='Stream', anchor='center')
    TreeViewOptions.column('#3', width=10, anchor='center', stretch=True) 
    TreeViewOptions.heading('#4', text='Class', anchor='center')
    TreeViewOptions.column('#4', width=10, anchor='center', stretch=True) 

    vsb= ttk.Scrollbar(Frm2, orient=tk.VERTICAL,command=TreeViewOptions.yview)  
    vsb.place(x=365, y=5, height=370)
    TreeViewOptions.configure(yscroll=vsb.set)
    TreeViewOptions.place(x=5,y=5,height=370,width=360)
    TreeViewOptions.bind("<Double-1>", show_selected_record)

    
    
    
    Take_Att.mainloop()
    
#NewDetailsRegister()