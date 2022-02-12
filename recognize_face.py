

import cv2
import face_recognition 
import numpy as np
import os

TrainedEncode = np.load(r'C:\Users\Administrator\Desktop\compsci_proj\Features.npy', allow_pickle = True)
print(TrainedEncode)

DIR = r"C:\Users\Administrator\Desktop\Train"
Folder = os.listdir(DIR)




#label = np.load(r'C:\Users\Administrator\Desktop\compsci_proj\Labels.npy', allow_pickle = True)

toCheck = face_recognition.load_image_file(r"C:\Users\Administrator\Desktop\testfold\yngdk.jpg");
toCheck = cv2.cvtColor(toCheck, cv2.COLOR_BGR2RGB); 

encodeCheck = face_recognition.face_encodings(toCheck)[0];
checkLoc = face_recognition.face_locations(toCheck)[0];

result = face_recognition.compare_faces(TrainedEncode, encodeCheck);
print(result);

#print("______________________________")
#print(TrainedEncode)
#print(encodeBilly)
#print("___________________________________")

#Core Variables
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

print("loop for 1st folder started.\n")

for file in Folder:
    path = os.path.join(DIR, file)
    currFile = os.listdir(path)
    maxFiles += len(currFile) 
print("total no. files:", maxFiles)

fold1count = len(os.listdir(os.path.join(DIR,Folder[0])))
for k in range(fold1count):
    if result[k] == True:
        countChk1 += 1
    if k == fold1count-1:
        compareList.append(countChk1)
        indices.append(0)
print(compareList)

print("loop through 2nd folder t0 last folder has started:\n")

for i in range(len(Folder)-1):
    print("i=",i)
    x = len(os.listdir(os.path.join(DIR, Folder[i])))
    y = len(os.listdir(os.path.join(DIR, Folder[i+1]) ))
    print('y:',y)
    print('x+y:',x+y)
    a = (x+xPrev)
    indices.append(a)
    b = (y+yPrev)
    xPrev += x
    yPrev += y

    c = b+y

    print('xPrev:', xPrev)
    print('yPrev:', yPrev)
    print()
    print('a:', a)
    print('b:', b)
    print('c:', c)

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
        refined = compareList.index(item)
        break
    else:
        name = "Unidentified"
        color = (0,0,225)

        
print("refined assigned")

print(refined)
if refined != None:
    print(Folder[refined])
else:
    print(name)

if refined != None:
    if refined == len(Folder)-1:
        resultAssgn = len(os.listdir(os.path.join(DIR,Folder[refined])))
        resultAssgn1 =  indices[refined]                   #len(os.listdir(os.path.join(DIR,Folder[refined])))
        print(result[resultAssgn1:])
        for outputs in result:
            if outputs in result[resultAssgn1:]:
                name =  Folder[refined]
                color = (0,255,0)
            elif compareLisEdt[0] != resultAssgn:
                name = "Unidentified"
                color = (0,0,225)

    else:
        resultAssgn1 = indices[refined]
        resultAssgn2 = len(os.listdir(os.path.join(DIR,Folder[refined])))                            #len(os.listdir(os.path.join(DIR,Folder[refined+1])))
        print(result[resultAssgn1:(resultAssgn1+resultAssgn2)])
        for outputs in result:
            if outputs in result[resultAssgn1:(resultAssgn1+resultAssgn2)]:
                name =  Folder[refined]
                color = (0,255,0)
            elif compareLisEdt[0] != resultAssgn2:
                name = "Unidentified"
                color = (0,0,225)

# (facLoc[3], facLoc[0]), (facLoc[1], facLoc[2])
drawnFace = cv2.rectangle(toCheck, (checkLoc[3], checkLoc[0]), (checkLoc[1], checkLoc[2]), color, thickness = 2);
txtrect = cv2.rectangle(toCheck, (checkLoc[3], checkLoc[0]-20), (checkLoc[3]+180, checkLoc[0]), color, thickness = -2);
cv2.putText(txtrect, name, (checkLoc[3], checkLoc[0]-3), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0))
cv2.imshow("detected1", drawnFace);
cv2.waitKey(0)
