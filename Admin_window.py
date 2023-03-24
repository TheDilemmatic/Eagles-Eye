import tkinter
from tkinter import*
from tkinter import Tk 
from tkinter import ttk
from PIL import Image, ImageTk
from create_new_id import Create_id
from scan_report import Entry_exit_detls
from update_id import Update_id
from delete_id import Delete_id
from train_data import train_face
from facRecWeb import webCamRecog, outputScreen
from sample_shots import capture_photos, displayScreen
import cv2

class AdminWindow:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x780")
        self.root.title("Admin window")
        
        #image1
        img = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\topbg_1.jpg")
        img = img.resize((460, 180),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x = 0, y = 0, width = 460, height = 180)
        
        #image2
        img1 = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\topbg_2.jpg")
        img1= img1.resize((480, 180),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root,image = self.photoimg1)
        f_lbl1.place(x = 460, y = 0, width = 480, height = 180)
        
        #image3
        img2 = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\topbg_3.jpg")
        img2 = img2.resize((460, 180),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.root,image = self.photoimg2)
        f_lbl2.place(x = 940, y = 0, width = 460, height = 180)

        #backround
        img3 = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\bg_main.gif")
        img3 = img3.resize((1370, 610),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root,image = self.photoimg3)
        bg_img.place(x = 0, y = 170, width = 1370, height = 610)
        

        main_title=Label(bg_img, text = "EAGLE'S EYE", font = ("Algerian", 35,'bold'), bg = "black", fg = "white")
        main_title.place(x = 440, y = 0, width = 450, height = 80 )
        
        title1_lbl=Label(bg_img, text = "FACE RECOGNITION DOOR SECURITY SYSTEM", font = ("Georgia", 25,'bold'), bg = "dark blue", fg = "white")
        title1_lbl.place(x = 0, y = 60, width = 1370, height = 40 )

        title2_lbl=Label(bg_img, text = "ADMINISTRATOR WINDOW", font = ("Times New Roman", 20,'bold'), bg = "black", fg = "white")
        title2_lbl.place(x = 440, y = 100, width = 450, height = 40 )
        

        #Create_id
        img4 = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\img00.jpg")
        img4 = img4.resize((125, 125),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(bg_img, image = self.photoimg4, command = self.create_id, cursor = "hand2")
        b1.place(x = 50, y = 180, width = 125, height = 125)
        b1_txt = Label(bg_img, text = "Create id", font = ("Ariel", 10,'bold'), bg = "purple", fg = "white")
        b1_txt.place(x = 50, y = 305, width = 125, height = 35)

        #Capture_samples
        img5 = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\photo4.png")
        img5 = img5.resize((125, 125),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b2 = Button(bg_img, image = self.photoimg5, command = self.take_pics, cursor = "hand2")
        b2.place(x = 125, y = 375, width = 125, height = 125)
        b2_txt = Label(bg_img, text = "Capture samples", font = ("Ariel", 10,'bold'), bg = "purple", fg = "white")
        b2_txt.place(x = 125, y = 500, width = 125, height = 35)

        #Update
        img6 = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\photo1.png")
        img6 = img6.resize((125, 125),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b3 = Button(bg_img, image = self.photoimg6, command = self.update_id, cursor = "hand2")
        b3.place(x = 400, y = 180, width = 125, height = 125)
        b3_txt = Label(bg_img, text = "Update details", font = ("Ariel", 10,'bold'), bg = "purple", fg = "white")
        b3_txt.place(x = 400, y = 305, width = 125, height = 35)

        #Train data
        img7 = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\img003.jpg")
        img7 = img7.resize((125, 125),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b4 = Button(bg_img, image = self.photoimg7, cursor = "hand2", command = self.TrainFace)
        b4.place(x = 475, y = 375, width = 125, height = 125)
        b4_txt = Label(bg_img, text = "Train data", font = ("Ariel", 10,'bold'), bg = "purple", fg = "white")
        b4_txt.place(x = 475, y = 500, width = 125, height = 35) 

        #Scan_report
        img8 = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\report.png")
        img8 = img8.resize((125, 125),Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b5 = Button(bg_img, image = self.photoimg8, command = self.ntry_xit, cursor = "hand2")
        b5.place(x = 750, y = 180, width = 125, height = 125)
        b5_txt = Label(bg_img, text = "Scan report", font = ("Ariel", 9,'bold'), bg = "purple", fg = "white")
        b5_txt.place(x = 750, y = 305, width = 125, height = 35)

        #Face_Recognition
        img9 = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\recognizeface.jpg")
        img9 = img9.resize((125, 125),Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b6 = Button(bg_img, image = self.photoimg9, command = self.recognise_face, cursor = "hand2")
        b6.place(x = 825, y = 375, width = 125, height = 125)
        b6_txt = Label(bg_img, text = "Recognize face", font = ("Ariel", 10,'bold'), bg = "purple", fg = "white")
        b6_txt.place(x = 825, y = 500, width = 125, height = 35)

        #Delete_id
        img10 = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\photo3.png")
        img10 = img10.resize((125, 125),Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b7 = Button(bg_img, image = self.photoimg10, command = self.delete_id, cursor = "hand2")
        b7.place(x = 1100, y = 180, width = 125, height = 125)
        b7_txt = Label(bg_img, text = "Delete id", font = ("Ariel", 10,'bold'), bg = "purple", fg = "white")
        b7_txt.place(x = 1100, y = 305, width = 125, height = 35)

        #Exit
        img11 = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\exit.jpg")
        img11 = img11.resize((125, 125),Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b8 = Button(bg_img, image = self.photoimg11, command = self.close_window, cursor = "hand2")
        b8.place(x = 1185, y = 375, width = 125, height = 125)
        b8_txt = Label(bg_img, text = "Exit", font = ("Ariel", 10,'bold'), bg = "purple", fg = "white")
        b8_txt.place(x = 1185, y = 500, width = 125, height = 35)

#==========================================================================================================================================#
    
    def create_id(self):
        self.new_window1 = Toplevel(self.root)
        self.app1 = Create_id(self.new_window1)

    def update_id(self):
        self.new_window2 = Toplevel(self.root)
        self.app2 = Update_id(self.new_window2)

    def ntry_xit(self):
        self.new_window3 = Toplevel(self.root)
        self.app3 = Entry_exit_detls(self.new_window3)

    def delete_id(self):
        self.new_window4 = Toplevel(self.root)
        self.app4 = Delete_id(self.new_window4)

    def take_pics(self):
        root = Toplevel(self.root)
        self.app5 = capture_photos(root)
        displayScreen()

    def TrainFace(self):
        root = Toplevel(self.root)
        train_face(root)
    
    def recognise_face(self):
        webCamRecog()
        outputScreen()
    
    def close_window(self):
        exit()


if __name__ == "__main__":
    root = Tk()
    obj = AdminWindow(root)
    root.mainloop()



