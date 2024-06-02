import os
from tkinter import messagebox

import cv2
import numpy as np
from PIL import Image


def getImagesAndLables(path):
    newdir = [os.path.join(path, d) for d in os.listdir(path)]
    imagePath = [
        os.path.join(newdir[i], f)
        for i in range(len(newdir))
        for f in os.listdir(newdir[i])
    ]
    faces = []
    Ids = []
    for imagePath in imagePath:
        pilImage = Image.open(imagePath).convert("L")
        imageNp = np.array(pilImage, "uint8")
        Id = int(os.path.split(imagePath)[-1].split("_")[1])
        faces.append(imageNp)
        Ids.append(Id)
    return faces, Ids

def OpenCamera(l1, l2, haarcasecade_path, trainimage_path, master, trainimagelabel_path):
    if l1=='':
        messagebox.showerror('Please Select Stream.',parent=master)
    elif l2 == "":
        messagebox.showerror('Please Enter the your Roll No.',parent=master)
    else:
        try:
            cam = cv2.VideoCapture(0)
            detector = cv2.CascadeClassifier(haarcasecade_path)
            Stream = l1
            Enrollment = l2
            sampleNum = 0
            directory = Enrollment + "_" + Stream
            path = os.path.join(trainimage_path, directory)
            os.mkdir(path)
            while True:
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    sampleNum = sampleNum + 1
                    cv2.imwrite(
                        f"{path}\ "
                        + Stream
                        + "_"
                        + Enrollment
                        + "_"
                        + str(sampleNum)
                        + ".jpg",
                        gray[y : y + h, x : x + w],
                    )
                    cv2.imshow("Frame", img)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
                elif sampleNum > 50:
                    break
            cam.release()
            cv2.destroyAllWindows()

            recognizer = cv2.face.LBPHFaceRecognizer_create()
            faces, Id = getImagesAndLables(trainimage_path)
            recognizer.train(faces, np.array(Id))
            recognizer.save(trainimagelabel_path)

            res = "Images Taken for Roll No:" + Enrollment + " Stream:" + Stream
            messagebox.showinfo("",res,parent=master)

        except FileExistsError as F:
            F = "Student Data already exists"
            messagebox.showinfo("",F, parent=master)