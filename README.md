# Eagles-Eye
A face recognition door security system which is capable of tracking the entry and exit details...
----A project by The_Dilemmatic(Derrick Rj.)----

This project titled “Eagle’s eye” is a Face Recognition Security System it aims to use various powerful libraries in Python and the data management skills of My SQL to create a software to provide Door entry security through Facial recognition and record the output of the face recogniser for future reference.
Note: We’ll be using the entry access system for the employees of a company to access the conference hall’s main door in this project. 

The project can be divided into three parts:

-> Graphical User Interface:
The GUI part of this project has been implimented using Tkinter and Pillow, it is very user friendly and helps the user to efficiently use this recogniser without any troubles the major parts of the GUI and the functional parts of it are implimented through Tkinter and Pillow is used to insert high quality images and give an attractive look to the GUI.
There are separete interfaces created for Administrator and the User to keep to ensure better security and giving only the Administrator the ability to manipulate the face regognizer and the all the databases and keepking the user completely away from it.

–>Database management:
The Database management part deals with managing datas from two different sources using MySQL, firstly it deals with accepting and storing the various information of the employee in a company who has to access the door, secondly it stores the data regarding the date, time and details of the person who has accessed the door. All functionalities for editing the database to satisfy all the needs of changing and manipulating this project has been successfully implimented using mysql and mysql-connector.

–>Facial recognition:
The Facial recognition part of this project deals with the code to figure out the encodings of each face given to it in form of an image, which differntiates that face form others(recognition) and the coordinates to locate the face(detection). All this is possible because of powerful python libraries like Deepface and OpenCV-python. Face recognition has been success fully achieved in this project through deepface(as mentioned earlier) this library has helped us gain acess to few of the most poweful face detectors like opencv, retina face mtcnn, opencv etc.. and face recognition models like Facenet,VGG-face,D-lib etc..(I recommend using mtcnn and Google Facenet since these are the most accurate one) and directly using them in our code with just a few lines of code, because of which we are able to provide users to choose options of vide variety of dectors and models while training the images captured.

Opencv is used to  accept input(which are images or real time video) for deepface, display output(real time video/live video) and manipulate it in the required manner so that the output given by deepface could easily understood by a User. Using this library data collected initially in sql database will also later be used to display the details of a person on the vieo out put when he or she will be recognized. The input is taken through live recording webcam and the out put will be the recorded video with a red rectangle plotted with a title 'unidentified' for unrecognised faces and a green frame around the face with name and his/her employee code will be displayed, if the face happens to be recognised. Opencv also plays a crucial role in taking fresh photo samples (i.e, writing the image) using the webcam and store them.
The os module in python is another library which plays a very inportant role for the face recognition it helps in creating and opening specific folders to save fresh photosamples and also opening already saved image files. Moreover the os module is also used to work with the 'path' to important directries so as to obtain important information regarding these directries as these are really important data for the recogniser.

When all these parts of this project functions together we have The EAGLE'S EYE ready to provide security....



