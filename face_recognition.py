import tkinter as tk
from tkinter import Message, Text
import shutil
import csv
import cv2
import os
import numpy as np
import PIL
from PIL import Image, ImageTk
import pandas as pd
from pandas.core.dtypes.inference import is_number
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font

window = tk.Tk()
window.title("STUDENT ATTENDANCE USING FACE RECOGNITION SYSTEM")
window.geometry('800x520')

dialog_title = 'QUIT'
dialog_text = "are you sure?"
window.configure(background='green')
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)


def clear():
    std_name.delete(0, 'end')
    res = ""
    label4.configure(text=res)


def clear2():
    std_number.delete(0, 'end')
    res = ""
    label4.configure(text=res)


def takeImage():
    name = (std_name.get())
    Id = (std_number.get())
    if name.isalpha():
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        
        os.mkdir("TrainingImages")

        while True:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.1, 3)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                sampleNum = sampleNum + 1
                cv2.imwrite(os.path.join("TrainingImages", name + "." + Id + '.' + str(sampleNum) + ".jpg"),
                            gray[y:y + h, x:x + h])
                cv2.imshow('frame', img)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            if sampleNum > 60:
                break

        cam.release()
        cv2.destroyAllWindows()
        res = 'Student details saved with: \n Matric number : ' + Id + ' and  Full Name:' + name
        row = [Id, name, str(datetime.date.today()), str(datetime.datetime.now().time())]

        col_names = ['Id', 'Name', 'Date', 'Time']

        with open('studentDetails.csv', 'a+') as csvFile:
               
            writer = csv.writer(csvFile)
            writer.writerow(col_names)
            writer.writerow(row)
        csvFile.close()
        label4.configure(text=res)
    else:

        if name.isalpha():
            res = "Enter correct Matric Number"
            label4.configure(text=res)


def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    Ids = []
    for imagePath in imagePaths:
        pilImage = Image.open(imagePath).convert('L')
        imageNp = np.array(pilImage, 'uint8')
        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(imageNp)
        Ids.append(Id)
    return faces, Ids


def trainImage():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, Id = getImagesAndLabels("TrainingImages")
    recognizer.train(faces, np.array(Id))
    recognizer.save("Trainner.yml")
    res = "Image Trained"
    label4.configure(text=res)


def trackImage():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    df = pd.read_csv("studentDetails.csv")
    font = cv2.FONT_HERSHEY_SIMPLEX
    cam=cv2.VideoCapture(0)
    col_names = {'Id', 'Name', 'Date', 'Time'}
    attendance = pd.DataFrame(columns=col_names)
    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.1, 3)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if conf < 70:
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M')
                aa=df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id) + "-" + aa
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]
            else:
                Id = 'Unknown'
                tt = str(Id)
                if os.path.exists("ImagesUnknown") == False:
                    os.mkdir("ImagesUnknown")
                if conf > 85:
                    noOfFile = len(os.listdir("ImagesUnknown")) + 1
                    cv2.imwrite(os.path.join("ImagesUnknown", "Image" + str(noOfFile) + ".jpg"), img[y:y + h, x:x + w])
            attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
            cv2.putText(img, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
        cv2.imshow('Face Recognizer', img)
        if cv2.waitKey(1) == ord('q'):
           break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M')
    fileName = 'Attendance\Attendance_' + date + '-' + timeStamp + '.csv'
    attendance.to_csv(fileName, index=False)
    cam.release()
    cv2.destroyAllWindows()
    print(attendance)
    res = attendance
    label4.configure(text=res)





label1 = tk.Label(window, background="green", fg="black", text="Full Name :", width=10, height=1,
                  font=('Helvetica', 16))
label1.place(x=50, y=40)
std_name = tk.Entry(window, background="yellow", fg="black", width=25, font=('Helvetica', 14))
std_name.place(x=250, y=41)
label2 = tk.Label(window, background="green", fg="black", text="Matric Number :", width=14, height=1,
                  font=('Helvetica', 16))
label2.place(x=50, y=90)
std_number = tk.Entry(window, background="yellow", fg="black", width=25, font=('Helvetica', 14))
std_number.place(x=250, y=91)

clearBtn1 = tk.Button(window, background="red", command=clear, fg="white", text="CLEAR", width=8, height=1,
                      activebackground="red", font=('Helvetica', 10))
clearBtn1.place(x=550, y=42)
clearBtn2 = tk.Button(window, background="red", command=clear2, fg="white", text="CLEAR", width=8,
                      activebackground="red", height=1, font=('Helvetica', 10))
clearBtn2.place(x=550, y=92)

label3 = tk.Label(window, background="green", fg="red", text="Notification", width=10, height=1,
                  font=('Helvetica', 20, 'underline'))
label3.place(x=300, y=155)
label4 = tk.Label(window, background="yellow", fg="black", width=40, height=4, font=('Helvetica', 14, 'italic'))
label4.place(x=160, y=205)

takeImageBtn = tk.Button(window, command=takeImage, background="yellow", fg="black", text="CAPTURE IMAGE",
                         activebackground="red",
                         width=15, height=3, font=('Helvetica', 12))
takeImageBtn.place(x=50, y=360)
trainImageBtn = tk.Button(window, command=trainImage, background="yellow", fg="black", text="TRAINED IMAGE",
                          activebackground="red",
                          width=15, height=3, font=('Helvetica', 12))
trainImageBtn.place(x=300, y=360)
trackImageBtn = tk.Button(window, command=trackImage, background="yellow", fg="black", text="TRACK IMAGE", width=12,
                          activebackground="red", height=3, font=('Helvetica', 12))
trackImageBtn.place(x=550, y=360)

window.mainloop()
