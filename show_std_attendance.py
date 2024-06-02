import csv
import os
import tkinter as tk
import tkinter.ttk as ttk
from glob import glob
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

import pandas as pd


def ShowStdAttendance(master):
    
    def List_Sub():
        str1 = ComboStream.get()
        str2 = ComboClass.get()
        lst1 = os.listdir(f'Subjects/{str1}/{str2}')
        return lst1

    def List_Sub_Event(event):
        str1 = ComboStream.get()
        str2 = ComboClass.get()
        lst1 = os.listdir(f'Subjects/{str1}/{str2}')
        ComboSub['values'] = lst1
    
    def Show_Data():
        str_val = ComboStream.get()
        class_val = ComboClass.get()
        sub_name = ComboSub.get()
        
        if sub_name =="":
            messagebox.showerror("",'Please enter the subject name.',parent=Show_Att_screen)
        #os.chdir(f'Subjects/{str_val}/{class_val}/{sub_name}')
        filenames = glob(
            f"Subjects\{str_val}\{class_val}\{sub_name}\{sub_name}*.csv"
        )
        df = [pd.read_csv(f) for f in filenames]
        newdf = df[0]   
        for i in range(1, len(df)):
            newdf = newdf.merge(df[i], how="outer")
        newdf.fillna(0, inplace=True)
        newdf["Attendance"] = 0
        for i in range(len(newdf)):
            newdf["Attendance"].iloc[i] = str(int(round(newdf.iloc[i, 2:-1].mean() * 100)))+'%'
            #newdf.sort_values(by=['Enrollment'],inplace=True)
        newdf.to_csv(f"Subjects/{str_val}/{class_val}/{sub_name}/attendance.csv", index=False)

        root = Toplevel(master)
        root.title("Attendance of "+sub_name)
        root.configure(background="black")
        cs = f"Subjects/{str_val}/{class_val}/{sub_name}/attendance.csv"
        with open(cs) as file:
            reader = csv.reader(file)
            r = 0
            for col in reader:
                c = 0
                for row in col:

                    label = Label(
                        root,
                        width=10,
                        height=1,
                        fg="yellow",
                        font=("times", 15, " bold "),
                        bg="black",
                        text=row,
                        relief=RIDGE,
                    )
                    label.grid(row=r, column=c)
                    c += 1
                r += 1
        root.mainloop()
        print(newdf)

    Show_Att_screen = Toplevel()
    Show_Att_screen.geometry("500x400+500+100")

    stream_values = {1:'CSE',2:'ENTC'}
    class_values = {1:'FY',2:'SY',3:'TY',4:'Btech'}

    Show_Att_screen.title("Student Attendance")
    Frm1 = LabelFrame(Show_Att_screen, width=480, height=380,)
    Frm1.place(x=10,y=10)

    Frm2 = LabelFrame(Show_Att_screen, width=390, height=380,)
    Frm2.place(x=500,y=10)

    LblHead = Label(Frm1, text='Student Attendance Form', font=('Arial',24), fg='blue')
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
    
    LblSub = Label(Frm1, text='Subject',font=('Arial',16))
    LblSub.place(x=10,y=170)
    ComboSub = Combobox(Frm1, font=('Arial',16), values=List_Sub())
    ComboSub.place(x=140, y=170)
    
    ComboStream.bind("<<ComboboxSelected>>",List_Sub_Event)
    ComboClass.bind("<<ComboboxSelected>>",List_Sub_Event)
    
    BtnShow = Button(Frm1, text='Show', bg='green', fg='white', width=12, font=('Arial',14), command=Show_Data)
    BtnShow.place(x=100,y=280)
    
    Show_Att_screen.mainloop()
    
#ShowStdAttendance()