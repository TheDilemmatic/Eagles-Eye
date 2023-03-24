 #Decting a face in the given video...
from logging import root
from operator import and_
import cv2
import os.path
from tkinter import *
from tkinter import ttk
from capture_samples import capture_photos
import PIL
from PIL import Image, ImageTk
from os import path

#pop up window 
def capture_photos(root):
    root.geometry("800x500")
    root.title("Photo Samples")
        
    #Setting a bg image:
    bg = ImageTk.PhotoImage(image=PIL.Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\lock.jpg"))
    lbl_bg = Label(root, image=bg)
    lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
        
    #Setting up a labelframe (and items inside):
    lbl_frm = LabelFrame(root, width = 350, height =  350, bd = 8, relief= RIDGE, bg = 'black', fg = 'white')
    lbl_frm.place(x = 220, y = 80)

    #person_icon
    img1 = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\login.png")
    img1 = img1.resize((60, 60), Image.ANTIALIAS)
    photoimage1 = ImageTk.PhotoImage(img1)
    lblimg1 = Label(lbl_frm, image=photoimage1, bg="black", borderwidth=0)
    lblimg1.place(x=130, y=20, width=90, height=90)

    #Label text:
    #lbl1_txt = Label(lbl_frm, bg = 'black', text = "Fill the following details:", font = ('algerian', 14, 'bold'), fg = 'white')
    #lbl1_txt.place(x = 20, y = 60)
    #Making the buttons functional 
    varName = StringVar()
    picNo = IntVar()
    
    def set_val():
        varName.get()
        picNo.get()

    def xit_windo():
        root.destroy()
  
    name = Label(lbl_frm, bg="black", text="Employee code", font=("times new roman", 14, "bold"), fg="white")
    name.place(x=40, y=140)

    #Enter name(entry):
    txt_name = Entry(lbl_frm, textvariable = varName,font=("times new roman", 15), fg="black", bg="white")
    txt_name.place(x=190, y=140, width=130,height=25)

    sample = Label(lbl_frm, text="No.of Photo samples", font=("times new roman", 13), fg="white", bg="black")
    sample.place(x=40, y=200)

    #no. of photos(combobox)
    sam_no = ttk.Combobox(lbl_frm, text="No. of Photo samples", textvariable = picNo , font=("times new roman", 12, 'bold'), state = "readonly")
    sam_no['values']=("7", "14", "28")
    sam_no.place(x= 200, y=200, width=100, height=25)

    #ok button
    okbtn = Button(lbl_frm, bg = "white", command = set_val, text="OK", font=("times new roman", 14, "bold"), bd=6 )
    okbtn.place(x=80, y=260, width=50, height=30)

    #exit button
    xitbtn = Button(lbl_frm, bg = "white", command = xit_windo, text="Save", font=("times new roman", 14, "bold"), bd=6 )
    xitbtn.place(x=210, y=260, width=50, height=30)

    def setNamePic():
        Name = varName.get()
        Picno = picNo.get()
        return (Name, Picno)
    
    root.mainloop()
    

    # Code behind Button's functionality 
    
    values = setNamePic()
    code = values[0]
    picno = values[1]
    Code = code
    shotsNum = picno
      
    #Locaction to create a new directry
    DIR = r"C:\Users\T13126CNS\Desktop\cbse_compsci\faces"
    loc2create = os.path.join(DIR, Code)
    os.mkdir(loc2create)

    pic_no = 0

    #wbecam settings:
    vid = cv2.VideoCapture(0) #setting camera
    #dimensions of camera view
    vid.set(3, 400)
    vid.set(4, 1250)      
    #start recording
    while True:
        passed, frame = vid.read()
        reqpath = "C:\\Users\\T13126CNS\\Desktop\\cbse_compsci\\faces\\" + Code + "\\" + "img" + str(pic_no) + '.jpg'
        cv2.imwrite(reqpath, frame)
        #stord = cv2.imread(reqpath)
        #cv2.imshow("Image taken & strored:", stord)
        pic_no += 1
        print("no. of pictures", pic_no)

        #stop recording
        if pic_no == shotsNum:
             break

    
    cv2.destroyAllWindows()
    #root.destroy()

def displayScreen():
    sideroot = Tk()
    sideroot.geometry("500x100")
    lablfrm1 = Label(sideroot, bg = "black", text = "All pictures taken successfully.", font = ("Times New Roman",16, "bold"), fg = "white" )
    lablfrm1.pack(fil = BOTH, expand = True)
    sideroot.mainloop()


    
if __name__ == "__main__":
    root = Tk()
    capture_photos(root)
    displayScreen()
    
 
