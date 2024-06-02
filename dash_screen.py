from tkinter import *
from new_student_register import NewDetailsRegister
from new_std_face import New_Std_Face
from new_subject import Subject
from take_std_attendance import TakeStdAttendence
from show_std_attendance import ShowStdAttendance
from PIL import ImageTk, Image



def Dash_Screen():
    dash_screen = Tk()
    dash_screen.state("zoomed")
    menubar = Menu(dash_screen)
    filemenu = Menu(menubar, tearoff=0)

    filemenu1 = Menu(menubar, tearoff=0)
    filemenu1.add_command(label="Student Details", command = lambda:NewDetailsRegister(dash_screen))
    filemenu1.add_command(label="Facial Details", command = lambda:New_Std_Face(dash_screen))

    filemenu2 = Menu(menubar, tearoff=0)
    filemenu2.add_command(label="Teacher Details")
    filemenu2.add_command(label="Facial Details")

    filemenu.add_cascade(label="Student Register",menu=filemenu1)
    filemenu.add_cascade(label="Teacher Register",menu=filemenu2)
    filemenu.add_command(label="Subject",command = lambda:Subject(dash_screen))

    menubar.add_cascade(label="Register", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)

    filemenu3 = Menu(menubar, tearoff=0)
    filemenu3.add_command(label="Student",command=lambda:TakeStdAttendence(dash_screen))
    filemenu3.add_command(label="Teacher")
    editmenu.add_cascade(label="Take Attendence",menu=filemenu3)

    filemenu4 = Menu(menubar, tearoff=0)
    filemenu4.add_command(label="Student",command=lambda:ShowStdAttendance(dash_screen))
    filemenu4.add_command(label="Teacher")
    editmenu.add_cascade(label="Show Attendence",menu=filemenu4)

    menubar.add_cascade(label="Attendance", menu=editmenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index")

    #menubar.add_cascade(label="Help", menu=helpmenu)

    dash_screen.config(menu=menubar)
    
    
    screen_width = dash_screen.winfo_screenwidth()
    screen_height = dash_screen.winfo_screenheight()
    
    image1 = Image.open("./Images/background.jpg")
    resized_image= image1.resize((screen_width,screen_height), Image.ANTIALIAS)

    img = ImageTk.PhotoImage(resized_image)
    label = Label(dash_screen, image = img)
    label.pack()
    
    dash_screen.mainloop()
    
