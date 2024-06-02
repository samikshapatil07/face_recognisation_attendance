from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import os
import time
import cv2
import pandas as pd
import datetime

def TakeStdAttendence(master):
    
    def Take_Attendance():
        strm = ComboStream.get()
        sub = ComboSub.get()
        now = time.time()
        future = now + 10
        
        if sub == "":
            messagebox.showerror("","Please Select Subject",parent=TakeAtt_screen)
        else:
            try:
                recognizer = cv2.face.LBPHFaceRecognizer_create()
                try:
                    recognizer.read('TrainImage.yml')
                    
                except:
                    messagebox.showerror("","Model not found,please train model",parent=TakeAtt_screen)
                
                facecasCade = cv2.CascadeClassifier('xml1.xml')
                df = pd.read_csv('StudentDetails/studentdetails.csv')
                print(df)
                cam = cv2.VideoCapture(0)
                font = cv2.FONT_HERSHEY_SIMPLEX
                col_names = ["Roll", "Name"]
                attendance = pd.DataFrame(columns=col_names)
                
                while True:
                    ___, im = cam.read()
                    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                    faces = facecasCade.detectMultiScale(gray, 1.2, 5)
                    for (x, y, w, h) in faces:
                        global Id
                        Id, conf = recognizer.predict(gray[y : y + h, x : x + w])
                        #print(str(Id)+"----"+str(conf))
                        if conf < 70:
                            global Subject
                            global aa
                            global date
                            global timeStamp
                            Subject = ComboSub.get()
                            ts = time.time()
                            date = datetime.datetime.fromtimestamp(ts).strftime(
                                "%Y-%m-%d"
                            )
                            timeStamp = datetime.datetime.fromtimestamp(ts).strftime(
                                "%H:%M:%S"
                            )

                            aa = df.loc[df["Roll"] == Id]["Name"].values
                            global tt
                            tt = str(Id) + "-" + aa
                            # En='1604501160'+str(Id)
                            attendance.loc[len(attendance)] = [
                                Id,
                                aa,
                            ]
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 4)
                            cv2.putText(
                                im, str(tt), (x + h, y), font, 1, (255, 255, 0,), 4
                            )
                            
                        else:
                            Id = "Unknown"
                            tt = str(Id)
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
                            cv2.putText(
                                im, str(tt), (x + h, y), font, 1, (0, 25, 255), 4
                            )
                    if time.time() > future:
                        break
                    
                    attendance = attendance.drop_duplicates(
                        ["Roll"], keep="first"
                    )
                    cv2.imshow("Filling Attendance...", im)
                    key = cv2.waitKey(30) & 0xFF
                    if key == 27:
                        break

                ts = time.time()
                # attendance["date"] = date
                # attendance["Attendance"] = "P"
                attendance[date] = 1
                date = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S")
                Hour, Minute, Second = timeStamp.split(":")
                # fileName = "Attendance/" + Subject + ".csv"
                attendance_path = f'Subjects/{ComboStream.get()}/{ComboClass.get()}'
                path = os.path.join(attendance_path, Subject)
                
                fileName = (
                    f"{path}/"
                    + Subject
                    + "_"
                    + date
                    + "_"
                    + Hour
                    + "-"
                    + Minute
                    + "-"
                    + Second
                    + ".csv"
                )
                attendance = attendance.drop_duplicates(["Roll"], keep="first")
                attendance.to_csv(fileName, index=False)

                messagebox.showinfo("",f"Attendance Filled Successfully of {Subject}",parent=TakeAtt_screen)
                cam.release()
                cv2.destroyAllWindows()

            except:
                messagebox.showerror("","No Face found for attendance",parent=TakeAtt_screen)
                cv2.destroyAllWindows()

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
    TakeAtt_screen = Toplevel(master)
    TakeAtt_screen.geometry("500x300+600+200")
    TakeAtt_screen.title("Take Attendance")
    
    Frm1 = LabelFrame(TakeAtt_screen, height=280, width=480)
    Frm1.place(x=10,y=10)
    
    LblHead = Label(Frm1, text='Take Attendance', font=('Arial',24), fg='blue')
    LblHead.place(x=120,y=10)
    
    stream_values = {1:'CSE',2:'ENTC'}
    class_values = {1:'FY',2:'SY',3:'TY',4:'Btech'}

    Frm1 = LabelFrame(TakeAtt_screen, height=280, width=480)
    Frm1.place(x=10,y=10)

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

    ComboClass.bind("<<ComboboxSelected>>", List_Sub_Event)
    ComboStream.bind("<<ComboboxSelected>>", List_Sub_Event)

    BtnTakeAtt = Button(Frm1, text='Camera', bg='black', fg='white', width=12, font=('Arial',14), command=Take_Attendance)
    BtnTakeAtt.place(x=140, y=230)
    TakeAtt_screen.mainloop()

#TakeStdAttendence()