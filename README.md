# STUDENT-ATTENDANCE-USING-FACIAL-RECOGNITION-SYSTEM-OPENCV

this is an automatic student attendance system using face recognition.
all the processes of this system are run through a graphical user interface(GUI) built using tkInter.
the first step is the data entry, the student has to enter his details(Name and ID) this details will be stored in a csv file 'StudentDetails.csv'
second step, the student will click on the TAKE IMAGE button to capture his faces, here 60 pictures of the student will be taken and for face detection er used the harr-cascade classfier. this pictures are stored in a folder TrainImages
the third step, the student has to click on the TRAIN IMAGE button to link his face to the details and finally the student has to click on the TRACK IMAGE button to make the attendance.
when clicking the button, the camera will be open if his face is recognized, his details will show on the camera and they will be automatically added to a csv file ('Attendance.csv') with the exact time and time of the event if not the student's pictures will be added to the Unknown faces folder.

check this link to view the code.

https://bitbucket.org/memudu_alimatou/facial-recognition-opencv/src/master/

