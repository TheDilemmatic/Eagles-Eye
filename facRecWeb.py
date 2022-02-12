
from ast import While
import cv2
import face_recognition 
import numpy as np
import os
from tkinter import *

def webCamRecog():
    TrainedEncode = np.load(r'C:\Users\Administrator\Desktop\compsci_proj\Features.npy', allow_pickle = True)
    print(TrainedEncode)

    DIR = r"C:\Users\Administrator\Desktop\Train"
    Folder = os.listdir(DIR)
   

    #Statement and loop control Variables
    whitelist = []
    webCamRecog.status = None
    webCamRecog.loopNo = 0


    vid = cv2.VideoCapture(0)
    while True:

        success, frame = vid.read()
        width = int(frame.shape[1]*0.50)
        height = int(frame.shape[0]*0.50)
        resizd1 = cv2.resize(frame, (width, height), interpolation = cv2.INTER_AREA)
        rgbFrame = cv2.cvtColor(resizd1, cv2.COLOR_BGR2RGB)
        currlocs = face_recognition.face_locations(rgbFrame) #the face aint fixd bruh and evrytime u move ur freakin face loc changes
        currEncods = face_recognition.face_encodings(rgbFrame, currlocs) #we aint planin to stresss the reconzr, so helpin a bit.
    
        #for facEncode, facLoc in zip(currEncods, currlocs):
        for facLoc in currlocs:
            result = face_recognition.compare_faces(TrainedEncode, currEncods)

            #Core variables
            name = None
            totalFile = 0
            maxFiles = 0
            compareList = []
            countChk1 = 0
            countChk2 = 0
            xPrev = 0
            yPrev = 0
            var = len(compareList)
            refined = None
            indices = []

            for file in Folder:
                path = os.path.join(DIR, file)
                currFile = os.listdir(path)
                maxFiles += len(currFile)
                print("total no. files:", maxFiles)

            fold1count = len(os.listdir(os.path.join(DIR,Folder[0])))
            indices.append(0)
            for k in range(fold1count):
                if result[k] == True:
                    countChk1 += 1
                if k == fold1count-1:
                    compareList.append(countChk1)
            print(compareList)

            for i in range(len(Folder)-1):
                print("i=",i)
                x = len(os.listdir(os.path.join(DIR, Folder[i])))
                y = len(os.listdir(os.path.join(DIR, Folder[i+1])))
                print(y)
                print(x+y)
                a = (x+xPrev)
                indices.append(a)
                b = (y+yPrev)
                xPrev += x
                yPrev += y
                c = b+y
                for j in range(a, c):
                    print('j=',j)
                    print(a,c, end='')
                    print()
                    if result[j] == True:
                        countChk2 += 1
                    if j == c-1:
                        compareList.append(countChk2)
                        countChk2 = 0
            print(compareList)

            compareLisEdt = compareList.copy()
            compareLisEdt.sort(reverse = True)
            print(compareLisEdt)
            print(indices)
            
        
            for item in compareList:
                if item != 0 and item == compareLisEdt[0]:
                    almstpure = compareList.index(item)
                    resultAssgn = len(os.listdir(os.path.join(DIR,Folder[almstpure])))
                    if compareLisEdt[0] == resultAssgn:
                        refined = almstpure
                    break
                else:
                    name = "Unidentified"
                    color = (0,0,225)
            print("refined assigned")

            if refined != None:
                print(Folder[refined])
            else:
                print(name)
            
            if refined != None:
                if refined == len(Folder)-1:
                    resultAssgn1 = indices[refined]
                    resultAssgn2 = len(os.listdir(os.path.join(DIR,Folder[refined])))
                    
                    if compareLisEdt[0] != resultAssgn2 :
                        name =  'Unidentified'
                        color = (0,0,255)
                    
                    else:                                                                              #len(os.listdir(os.path.join(DIR,Folder[refined])))
                        for outputs in result:
                            if outputs in result[resultAssgn1:]:
                                name =  Folder[refined]
                                color = (0,255,0)
                                whitelist.append('whitelisted')
                        

                else:
                    resultAssgn1 = indices[refined]         #len(os.listdir(os.path.join(DIR,Folder[refined])))
                    resultAssgn2 = len(os.listdir(os.path.join(DIR,Folder[refined])))
                    
                    if compareLisEdt[0] != resultAssgn2:
                        name =  'Unidentified'
                        color = (0,0,255)
                    
                    else:
                        for outputs in result:
                            if outputs in result[resultAssgn1:(resultAssgn1 + resultAssgn2)]:
                                name =  Folder[refined]
                                color = (0,255,0)
                                whitelist.append("whitelisted")
                        


            drawnFace = cv2.rectangle(resizd1, (facLoc[3], facLoc[0]), (facLoc[1], facLoc[2]), color, thickness = 2);
            #cv2.putText(drawnFace, name, (40,48), cv2.FONT_HERSHEY_COMPLEX, 1, color, 1)
            #txtrect = cv2.rectangle(resizd1, (facLoc[3], facLoc[0]-20), (facLoc[3]+180, facLoc[0]), color, thickness = -2);
            cv2.putText(resizd1, name, (facLoc[3], facLoc[0]-3), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color)
            cv2.imshow("Recognized", drawnFace);


            if len(whitelist) >= 20:
                webCamRecog.status = "You are  successfully recognized, entry permitted."
                webCamRecog.txtcolr = 'green'
            else:
                webCamRecog.status = "You are not recognized, entry restricted."
                webCamRecog.txtcolr = 'red'
        
            #Every time we reach here your face is scanned 1 time...
            webCamRecog.loopNo +=1
            cv2.waitKey(20)

        if webCamRecog.loopNo == 20:
            print("You face has been scanned:",webCamRecog.loopNo,"times.")
            break
    #cv2.destroyAllWindows()
    print(webCamRecog.status)
     

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
       

