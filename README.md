# STUDENT ATTENDANCE uSING FACIAL RECOGNITION SYSTEM OPENCV

#### This is an automatic student attendance system using face recognition. The aim is to automate the process of attendance maintenance.


## FACE RECOGNITION 
***

Face recognition is a biometric recognition technique.
Biometric recognition is an information system that allows the identification of a person based on some of its main physiological and behavioral characteristics.
Face recognition is a broad problem of identifying or verifying people in photographs and videos, a process comprised of detection, alignment, feature extraction, and a recognition task
It has 4 steps which are :
1. **Face Detection**: Look at the picture and find a face in it.
2. **Data Gathering**: Extract unique characteristics of Kirill’s face that it can use to differentiate him from another person, like eyes, mouth, nose, etc.
3. **Data Comparison**: Despite variations in light or expression, it will compare those unique features to all the features of all the people you know.
4. **Face Recognition:** It will determine “Hey, that’s my boy ”

## TECHONLOGY USED

* **OPENCV**
>OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library. 
OpenCV was built to provide a common infrastructure for computer vision applications and to accelerate the use of machine perception in the commercial products.

* **TKINTER**
>Tkinter is a Python binding to the Tk GUI toolkit. It is the standard Python interface to the Tk GUI toolkit, and is Python's de facto standard GUI.

* **HAARCASCADE CLASSIFIER**
> is an effective object detection approach,Haar classifiers are organized in sequences called stages (classification stages). The stage value is the sum of its classifier values.

* **LocalBinaryPatternHistogram (LBPH) recognizer**
> It is an openCV recognizer, is a simple yet very efficient texture operator which labels the pixels of an image by thresholding the neighborhood of each pixel and considers the result as a binary number.

* **trainner
>file detect specific face using python and opencv

***
## HOW THE SYSTEM WORKS?

1. **DATA COLLECTION**:


![capture](https://github.com/memudualimatou/STUDENT-ATTENDANCE-USING-FACIAL-RECOGNITION-SYSTEM-OPENCV/blob/master/Docs/Images/Capture12.PNG)



The student interact with the system through the graphical user interface(GUI) above.
The first step the student has to enter his details(Name and ID) this details will be stored in a csv file **'StudentDetailss.csv'**, the ID is Matric Number on the GUI.
second step, the student will click on the **CAPTURE IMAGE** button to capture his faces, here 50pictures of the student will be taken and stored in the **TrainingImages** Folder.  The **haar-cascadeclassifier** file to detect faces through the video stream while the student face is being captured.
the notification board will print ou the student details after a succesfull data collection.

![capture2](https://github.com/memudualimatou/STUDENT-ATTENDANCE-USING-FACIAL-RECOGNITION-SYSTEM-OPENCV/blob/master/Docs/Images/555.PNG)


2. **IMAGE TRAINED**

The student has to click on the  **TRAIN IMAGE** button which will link his details, face features to the **LBPHrecognizer** to ease further face recognition,
the recognizer will save the face features in the **trainner.yml** and "IMAGE TRAINED" will be printed on the GUI notification board after a successfull linkage.


3. **FACE TRACKING**

The student has to click on the **TRACK IMAGE** button to allow the face recognizer to track his face through a video stream, when trhe system successfully recognize the student face, his details will show and "ATTENDANCE UPDATED" will be printed out otherwise , the ID will be Unkown and "ID UNKOWN, ATTENDANCE NOT UPDATED" will be printed out.
Simustenously, a csv file **AttendanceFile.csv'** will be updated with the ID,NAME of the student and DATE Aand TIME at which his face has recognized.


![capture3](https://github.com/memudualimatou/STUDENT-ATTENDANCE-USING-FACIAL-RECOGNITION-SYSTEM-OPENCV/blob/master/Docs/Images/ezgif.com-gif-maker%20(1).gif)




check this link to view the trainner file.

https://bitbucket.org/memudu_alimatou/facial-recognition-opencv/src/master/

