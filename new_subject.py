import os
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox


def Subject(master):
    
    def Save_Fun():
        str_val = ComboStream.get()
        class_val = ComboClass.get()
        sub_name = TxtSub.get()
        try:
            os.makedirs(f'Subjects/{str_val}/{class_val}/{sub_name}')
            messagebox.showinfo("",f"{sub_name} For {class_val} {str_val} Added Successfully...",parent=subject_screen)
        except:
            messagebox.showerror("","Subject Already Exists...",parent=subject_screen)
    subject_screen = Toplevel(master)
    subject_screen.geometry("500x300+600+200")
    subject_screen.title("Add Subject")

    stream_values = {1:'CSE',2:'ENTC'}
    class_values = {1:'FY',2:'SY',3:'TY',4:'Btech'}

    Frm1 = LabelFrame(subject_screen, height=280, width=480)
    Frm1.place(x=10,y=10)

    LblHead = Label(Frm1, text='Add Subject', font=('Arial',24), fg='Blue')
    LblHead.place(x=130,y=10)

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
    
    LblSub = Label(Frm1, text='Add subject',font=('Arial',16))
    LblSub.place(x=10,y=170)
    TxtSub = Entry(Frm1, width=20, font=('Arial',16))
    TxtSub.place(x=140, y=170)

    BtnSave = Button(Frm1, text='Save', bg='black', fg='white', width=12, font=('Arial',14), command=Save_Fun)
    BtnSave.place(x=140, y=230)
    subject_screen.mainloop()

#Subject()