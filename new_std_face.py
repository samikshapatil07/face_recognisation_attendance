from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from open_camera import OpenCamera


def New_Std_Face(master):
    
    def Save_Fun():
        messagebox.showinfo("","Image Saved Successfully...",parent=Take_Att)

    def StreamKey(strm):
        for key, value in stream_values.items():
            if value==strm:
                return key
    xml1 = 'xml1.xml' 
    imgpathS = 'Images\Student'
    trainimg = 'TrainImage.yml'
    def CameraCall():
        strm = ComboStream.get()
        strm_key = StreamKey(strm)
        RollKey = TxtRoll.get()
        OpenCamera(strm, RollKey, xml1 , imgpathS, Take_Att, trainimg)
        
    Take_Att = Toplevel(master)
    Take_Att.geometry("500x400+500+100")

    stream_values = {1:'CSE',2:'ENTC'}
    Take_Att.title("Face Register Form")

    Frm1 = LabelFrame(Take_Att, width=480, height=380,)
    Frm1.place(x=10,y=10)

    LblHead = Label(Frm1, text='Student Face Registration', font=('Arial',24), fg='blue')
    LblHead.place(x=80,y=10)
    
    LblStream = Label(Frm1, text='Stream', font=('Arial',16), fg='black')
    LblStream.place(x=10,y=70)
    ComboStream = Combobox(Frm1, width=18, font=('Arial',16), values=list(stream_values.values()))
    ComboStream.place(x=140,y=70)
    ComboStream.set(list(stream_values.values())[0])
    
    
    LblRoll = Label(Frm1, text='Roll No',font=('Arial',16))
    LblRoll.place(x=10,y=120)
    TxtRoll = Entry(Frm1, width=20,font=('Arial',16))
    TxtRoll.place(x=140, y=120)
    
    BtnCamera = Button(Frm1, text='Open Camera', bg='black', fg='white', width=12, font=('Arial',14), command=CameraCall)
    BtnCamera.place(x=100,y=280)
    BtnSave = Button(Frm1, text='Save', bg='black', fg='white', width=12, font=('Arial',14), command=Save_Fun)
    BtnSave.place(x=270,y=280)
    
    Take_Att.mainloop()