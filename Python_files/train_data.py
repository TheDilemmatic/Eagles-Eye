
from tkinter import *
from tkinter import ttk
import PIL
from PIL import Image, ImageTk
import pickle

def train_face( root):
    root.geometry("750x450")
    root.title("Train_face")
    lbl_frm = LabelFrame(root, width = 750, height =  450, bd = 8, text = 'Train Photos', font=("Algerian", 30), relief= RIDGE, bg = 'dark grey', fg = 'black')
    lbl_frm.place(x =0, y = 0)
    bg = ImageTk.PhotoImage(image=PIL.Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\lock.jpg"))
    lbl_bg = Label(lbl_frm, image=bg)
    lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
    lbl_frm2 = LabelFrame(root, width = 500, height =  280,text = 'Choose the following: ', font=("Algerian", 18), bd = 8, bg = 'black', fg = 'white')
    lbl_frm2.place(x =120, y = 120)
    txt_name = Label(lbl_frm2, text = 'Face Recognition model', font=("times new roman", 13), fg="black", bg="steel blue")
    txt_name.place(x=30, y=60, width=180,height=25)
    txt_name2 = Label(lbl_frm2, text = 'Face detector', font=("times new roman", 15), fg="black", bg="steel blue")
    txt_name2.place(x=30, y=130, width=180,height=25)
    
    varName1 = StringVar()
    varName2 = StringVar()
    def set_val():
        #varName1.get()
        #varName2.get()
        root.destroy()

    fac_mod = ttk.Combobox(lbl_frm2, text="face recognizers available",textvariable=varName1, font=("times new roman", 12, 'bold'), state = "readonly")
    fac_mod['values']=("VGG-Face", "Facenet", "OpenFace", "DeepFace", "DeepID", "Dlib", "ArcFace")
    fac_mod.place(x= 270, y=60, width=150, height=25)
    fac_det = ttk.Combobox(lbl_frm2, text="face recognizers available",textvariable=varName2, font=("times new roman", 12, 'bold'), state = "readonly")
    fac_det['values']=("opencv", "ssd", "mtcnn", "dlib", "retinaface")
    fac_det.place(x= 270, y=130, width=150, height=25)
    trnbtn = Button(lbl_frm2, bg = "silver", fg = 'black', command = set_val, text="Train", font=("times new roman", 14, "bold"), bd=6 )
    trnbtn.place(x=200, y= 190, width=90, height=40)
    root.mainloop()
    mod = varName1.get()
    det = varName2.get()
    rectup = (mod, det)
    print(rectup)
 
    with open('train_fac.dat', 'wb') as f_obj:
        pickle.dump(rectup, f_obj)
    
#def displaymsg():
    #tkinter.Tk()
if __name__ == "__main__":
    root = Tk()
    train_face(root)
    