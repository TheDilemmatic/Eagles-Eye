from msilib.schema import Feature
import cv2
import face_recognition 
import os
import numpy as np
from tkinter import *


def train_face():

    DIR = r"C:\Users\Administrator\Desktop\Train"
    Folder = os.listdir(DIR)
    print(Folder)
    Features = []
    #Labels = []

    for File in Folder:
        path = os.path.join(DIR, File)
        #label = Folder.index(File)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            read = cv2.imread(img_path)
            cv2.imshow("Trained pic", read)
            RGB_img = cv2.cvtColor(read, cv2.COLOR_BGR2RGB)
            #FacLoc = face_recognition.face_locations(RGB_img)[0]
            FacEncode = face_recognition.face_encodings(RGB_img)[0]

            Features.append(FacEncode)
            #Labels.append(label)
    
    print("_______OK________")
    

    np.array(Features)
    #np.array(Labels)

    np.save('Features.npy', Features)
    #np.save('Labels.npy',  Labels)

    print("_______OK________")

def displaymsg():
    sideroot = Tk()
    sideroot.geometry("500x100")
    lablfrm1 = Label(sideroot, bg = "black", text = "All pictures trained successfully.", font = ("Times New Roman",16, "bold"), fg = "white" )
    lablfrm1.pack(fil = BOTH, expand = True)
    sideroot.mainloop()


if __name__ == "__main__":
    train_face()
    displaymsg()