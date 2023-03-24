from ast import Pass
from tkinter import font, ttk
from tkinter import *

import PIL
from PIL import Image, ImageTk


class capture_photos:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x500")
        self.varName = StringVar()
        self.picNo = IntVar()

        # frame
        self.bg = ImageTk.PhotoImage(image=PIL.Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\lock.jpg"))
        lbl_bg = Label(self.root, image=self.bg)

        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black", bd=8, relief=RIDGE).place(x=200, y=60, width=330, height=350)
        img1 = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\login.png")
        img1 = img1.resize((60, 60), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=320, y=70, width=90, height=90)
        self.root.title("Capture Sample")

        def set_val():
            self.varName.get()
            self.picNo.get()

        get_str = Label(frame, text="Fill in the details", font=("algerian", 15, "bold"), fg="white", bg="black").place(x=270, y=150)
        name = Label(frame, text="Name", font=("times new roman", 15, "bold"), fg="white", bg="black").place(x=220, y=240)
        txt_name = Entry(self.root, textvariable = self.varName,font=("times new roman", 15), fg="black", bg="white").place(x=280, y=240, width=210,height=30)
        sample = Label(frame, text="No.of Photo samples", font=("times new roman", 15), fg="white", bg="black").place(x=220, y=290)
        sam_no = ttk.Combobox(self.root, text="No.of Photo samples", textvariable = self.picNo , font=("times new roman", 15), state = "readonly")
        sam_no['values']=("7", "14", "28")
        sam_no.place(x=390, y=290, width=100, height=30)

        ok = Button(self.root, command = set_val, text="Ok").place(x=330, y=340, width=60, height=40)

    def setNamePic(self):
        name = self.varName.get()
        picno = self.picNo.get()
        return (name, picno)




if __name__ == "__main__":
    pass
    root = Tk()
    obj = capture_photos(root)
    root.mainloop()

    funcout = obj.setNamePic()
    print(funcout)




