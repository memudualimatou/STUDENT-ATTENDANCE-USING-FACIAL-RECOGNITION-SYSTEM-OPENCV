# STUDENT ATTENDANCE uSING FACIAL RECOGNITION SYSTEM OPENCV

## This is an automatic student attendance system using face recognition.
***

## FACE RECOGNITION 
***

Face recognition is a biometric recognition technique.
Biometric recognition is an information system that allows the identification of a person based on some of its main physiological and behavioral characteristics. It is based on hardware systems for data acquisition that integrate the software components that allow, through mathematical algorithms, to perform data analysis and reconstruct the identity of a person and recognize it.
Face recognition is a broad problem of identifying or verifying people in photographs and videos, a process comprised of detection, alignment, feature extraction, and a recognition task

it has 4 steps which are :
1.Face Detection: Look at the picture and find a face in it.
2.Data Gathering: Extract unique characteristics of Kirill’s face that it can use to differentiate him from another person, like eyes, mouth, nose, etc.
3.Data Comparison: Despite variations in light or expression, it will compare those unique features to all the features of all the people you know.
4.Face Recognition: It will determine “Hey, that’s my boy Kirill!”

## TECHONLOGY USED
***
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


The student interact with the system through a graphical user interface(GUI) built using tkInter.
the first step is the data entry, the student has to enter his details(Name and ID) this details will be stored in a csv file 'StudentDetails.csv'
second step, the student will click on the TAKE IMAGE button to capture his faces, here 60 pictures of the student will be taken and for face detection er used the harr-cascade classfier. this pictures are stored in a folder TrainImages
the third step, the student has to click on the TRAIN IMAGE button to link his face to the details and finally the student has to click on the TRACK IMAGE button to make the attendance.
when clicking the button, the camera will be open if his face is recognized, his details will show on the camera and they will be automatically added to a csv file ('Attendance.csv') with the exact time and time of the event if not the student's pictures will be added to the Unknown faces folder.

check this link to view the code.

https://bitbucket.org/memudu_alimatou/facial-recognition-opencv/src/master/

