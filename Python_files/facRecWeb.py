
from deepface import DeepFace
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
import cv2
import face_recognition 
import numpy as np
import os
from tkinter import *
import mysql.connector as sqltor
import pandas as pd
import pickle



def webCamRecog():

    with open (r"C:\Users\T13126CNS\Desktop\cbse_compsci\train_fac.dat",'rb') as f_obj:
        rectup = pickle.load(f_obj)
        print(rectup)

    DIR = r"C:\Users\T13126CNS\Desktop\cbse_compsci\faces"
    m_folder = os.listdir(DIR)
    imageDict = {}
    for code in m_folder:
        f_path = os.path.join(DIR, code)
        imageDict[code]=f_path
        #f_list = os.listdir(f_path)
        #images = []
        #for file in f_list:
            #img_path = os.path.join(f_path, file)
            #images.append(img_path)
        #imageDict[folder]=images
    print(imageDict)


    #Statement and loop control Variables
    #whitelist = 0
    
    #CORE VARIABLES
    name = None
    color = None
    code = None 
    webCamRecog.status = None
    webCamRecog.loopNo = 0
    check = 0
    count = 0
    
    vid = cv2.VideoCapture(0)
    while True:
        #Accessing a video frame by fram...
        success, frame = vid.read()
        width = int(frame.shape[1]*1.25)
        height = int(frame.shape[0]*1.25)
        resizd = cv2.resize(frame, (width, height), interpolation = cv2.INTER_AREA)
        #pic = cv2.cvtColor(resizd, cv2.COLOR_BGR2RGB)
        #create the dector, using default weights
        detector = MTCNN()
        #DETECT FACES IN THE IMAGE...
        faces = detector.detect_faces(resizd)
        for face in faces:
            result = face
            print(face)
        #coordinates
        x, y, width, height = result['box']
        
        imgpath = r"C:\Users\T13126CNS\Desktop\cbse_compsci\vid_bg\photo.jpg"
        captured = cv2.imwrite(imgpath, resizd)
        
        for code,folder in  imageDict.items():
            df = DeepFace.find(img_path = imgpath, db_path = folder, model_name= rectup[0], detector_backend = rectup[1])
            print(df.values.tolist())
            
            if df.values.tolist() != []:
                cosine = df.values.tolist()[0][1]
            #if (cosine >= 0.0 and cosine <= 0.38 ):
                color = (0,170,0)
                _status_ = 'RECOGNIZED'
                print(code) 
                
                mycon = sqltor.connect(host = "localhost", user = "root", passwd = "mera_sql", database = "cbse_compsci_proj")
                if mycon.is_connected():
                    print("success!")
                cursor = mycon.cursor()
                cmd = "select employee_name from employee_details where employee_code = " + "'"+code+"'"
                cursor.execute(cmd)
                name = cursor.fetchone()[0]
                print(name)
                cursor.close()
                
                mycon = sqltor.connect(host = "localhost", user = "root", passwd = "mera_sql", database = "cbse_compsci_proj")
                if mycon.is_connected():
                    print("success!")
                cursor3 = mycon.cursor()
                cmd3 = "SELECT employee_code, employee_name, gender, department, post_held, phone from employee_details where employee_code = " + "'"+code+"'"
                cursor3.execute(cmd3)
                employee_code, employee_name, gender, department, post_held, phone = cursor3.fetchone()
                print(employee_code, employee_name, gender, department, post_held, phone)
                cursor3.close()

                mycon = sqltor.connect(host = "localhost", user = "root", passwd = "mera_sql", database = "cbse_compsci_proj")
                if mycon.is_connected():
                    print("success!")
                cursor1 = mycon.cursor()
                cmd1 = "SELECT current_date()"
                cursor1.execute(cmd1)
                date_of_scan = cursor1.fetchone()[0]
                print(date_of_scan)
                cursor1.close()

                mycon = sqltor.connect(host = "localhost", user = "root", passwd = "mera_sql", database = "cbse_compsci_proj")
                if mycon.is_connected():
                    print("success!")
                cursor2 = mycon.cursor()
                cmd2 = "SELECT current_time()"
                cursor2.execute(cmd2)
                time_of_scan = cursor2.fetchone()[0]
                print(time_of_scan)
                cursor2.close()

                mycon = sqltor.connect(host = "localhost", user = "root", passwd = "mera_sql", database = "cbse_compsci_proj")
                if mycon.is_connected():
                    print("success!")
                print(_status_)
                cursor4 = mycon.cursor()
                cmd4 = "INSERT INTO SCAN_REPORT(date_of_scan, time_of_scan, _status_, employee_code, employee_name, gender, department, post_held, phone)\
                        VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {})"\
                    .format(date_of_scan, time_of_scan, _status_, employee_code, employee_name, gender, department, post_held, phone)
                cursor4.execute(cmd4)
                mycon.commit()
                cursor4.close()
                check +=1

                drawnFace = cv2.rectangle(resizd, (x, y, width, height), color, thickness = 2);
                #drawnFace1 = cv2.rectangle(resizd, (x, y, width, height-300), color, thickness = -1);
                cv2.putText(resizd, (name+'('+code+')'), (x+10, y-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,color);
                cv2.imshow("Recognized", resizd);
                cv2.waitKey(0)
                break

            elif df.values.tolist() == []:
                count += 1
                if count <= (len(imageDict)-1):
                    name = "Scanning..."
                    color = (225,0,0)
                    addefect = resizd.copy()
                    drawnFace = cv2.rectangle(addefect, (x, y, width, height), color, thickness = 2);
                    cv2.putText(drawnFace, name, (x+10, y-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,color);
                    cv2.imshow("Recognized",drawnFace);
                    cv2.waitKey(600);
                    cv2.destroyAllWindows()
                else:   
                    name = "Unidentified"
                    color = (0,0,225)

                    _status_ = "UNRECOGNIZED"
                    employee_code = "Unknown"
                    employee_name = "Unknown" 
                    gender = "Unknown"
                    department = "Unknown"
                    post_held = "Unknown"
                    phone = 000000000

                    mycon = sqltor.connect(host = "localhost", user = "root", passwd = "mera_sql", database = "cbse_compsci_proj")
                    if mycon.is_connected():
                            print("success!")
                    cursor1 = mycon.cursor()
                    cmd1 = "SELECT current_date()"
                    cursor1.execute(cmd1)
                    date_of_scan = cursor1.fetchone()[0]
                    print(date_of_scan)
                    cursor1.close()

                    mycon = sqltor.connect(host = "localhost", user = "root", passwd = "mera_sql", database = "cbse_compsci_proj")
                    if mycon.is_connected():
                        print("success!")
                    cursor2 = mycon.cursor()
                    cmd2 = "SELECT current_time()"
                    cursor2.execute(cmd2)
                    time_of_scan = cursor2.fetchone()[0]
                    print(time_of_scan)
                    cursor2.close()

                    mycon = sqltor.connect(host = "localhost", user = "root", passwd = "mera_sql", database = "cbse_compsci_proj")
                    if mycon.is_connected():
                        print("success!")
                    print(_status_)
                    cursor4 = mycon.cursor()
                    cmd4 = "INSERT INTO SCAN_REPORT(date_of_scan, time_of_scan, _status_, employee_code, employee_name, gender, department, post_held, phone)\
                            VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {})"\
                        .format(date_of_scan, time_of_scan, _status_, employee_code, employee_name, gender, department, post_held, phone)
                    cursor4.execute(cmd4)
                    mycon.commit()
                    cursor4.close()     
            
                    drawnFace = cv2.rectangle(resizd, (x, y, width, height), color, thickness = 2);
                    #drawnFace1 = cv2.rectangle(resizd, (x, y, width, height-300), color, thickness = -1);
                    cv2.putText(drawnFace, name, (x+10, y-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,color);
                    cv2.imshow("Recognized", drawnFace);
                    cv2.waitKey(0);
        
        #Every time we reach here your face is scanned 1 time...
        webCamRecog.loopNo +=1

        if check >= 1:
            print("no. of successful scans: ",check)
            webCamRecog.status = "You are  successfully recognized, entry permitted."
            webCamRecog.txtcolr = 'green'
        else:
            print("no. of successful scans: ",check)
            webCamRecog.status = "You are not recognized, entry restricted."
            webCamRecog.txtcolr = 'red'
        

        if webCamRecog.loopNo >=1:
            print("You face has been scanned: ",webCamRecog.loopNo,"times.")
            cv2.destroyAllWindows()
            print(webCamRecog.status)
            break
            
     

def outputScreen():
    sideroot = Tk()
    sideroot.geometry("500x100")
    lablfrm1 = Label(sideroot, bg = "black", text = "You face hs been scanned: "+str(webCamRecog.loopNo)+" times.", font = ("Times New Roman",16, "bold"), fg = "white" )
    lablfrm1.pack(fil = BOTH, expand = True)
    lablfrm2 = Label(sideroot, bg = "black", text = webCamRecog.status, font = ("Times New Roman",14, "bold"), fg = webCamRecog.txtcolr)
    lablfrm2.pack(fil = BOTH, expand = True)
    sideroot.mainloop()

if __name__ == "__main__":
    webCamRecog()
    outputScreen()
       

