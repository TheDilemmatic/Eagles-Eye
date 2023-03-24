
#from imp import source_from_cache
import PIL
from tkinter import ttk
from tkinter import *
from PIL import Image,ImageTk 
from tkinter import messagebox
#from cv2 import sepFilter2D
from Admin_window import AdminWindow
from facRecWeb import webCamRecog ,outputScreen
from forgot_password import forgot_pass

import mysql.connector as ms
con = ms.connect(host = "localhost",user = "root",password="mera_sql",database="cbse_compsci_proj")
cursor1 = con.cursor()


def adminwind():
    AdminWindow(root)

#first window       
class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1350x780+0+0")
        self.bg=ImageTk.PhotoImage(image=PIL.Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\bg_login1.jpg"))
        lbl_bg1=Label(self.root,image=self.bg)
        lbl_bg1.place(x=0,y=0,relwidth=1,relheight=1)

        main_title=Label(lbl_bg1, text = "EAGLE'S EYE", font = ("Algerian", 35,'bold'), bg = "black", fg = "white")
        main_title.place(x = 440, y = 0, width = 450, height = 80 )
        
        title1_lbl=Label(lbl_bg1, text = "FACE RECOGNITION DOOR SECURITY SYSTEM", font = ("Georgia", 25,'bold'), bg = "steel blue", fg = "black")
        title1_lbl.place(x = 0, y = 60, width = 1370, height = 40 )

        title2_lbl=Label(lbl_bg1, text = "LOGIN WINDOW", font = ("Times New Roman", 20,'bold'), bg = "black", fg = "white")
        title2_lbl.place(x = 440, y = 100, width = 450, height = 40 )
        
        blkframe = Frame(lbl_bg1,height = 300 ,width= 350 , bg = 'black', bd = 10, relief=RAISED)
        blkframe.place(x=500,y=250,width=300,height=430)
        #logo
        img2=Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\logo2.jpg")
        img2=img2.resize((200,200))
        self.photoimage1=ImageTk.PhotoImage(img2)
        lblimg1=Label(self.root,image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=530,y=260,width=250,height=200)
        #drop box
        Language=ttk.Combobox(self.root,values=("Admin","User"),font=("times new roman",15,"bold"),state="readonly")
        Language.place(x=520,y=480,width=250,height=40)
            
        def get_data():
            if Language.get()=="Admin":
                app=Admin_window(root)
            elif Language.get()=="User":
                app=User_window(root)
        #button to check the choice
        btn=Button(self.root,text="Next",command=get_data, font = ("Algerian", 16, "bold"), bd = 6)
        btn.place(x=600,y=570,width=100,height=50)


#admin window
class Admin_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1350x780+0+0")

        #login background
        self.bg=ImageTk.PhotoImage(image=PIL.Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\login_bg2.jpg"))
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        #login frame
        frame=Frame(self.root,bg="black")
        frame.place(x=500,y=170,width=340,height=450)
        
        img1=Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\login.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=620,y=175,width=100,height=100)
        
        get_str=Label(frame,text="Login", font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=133,y=100)
        
       
        admin_no=Label(frame,text="Admin UID",font=("times new roman",15,"bold"),fg="white",bg="black")
        admin_no.place(x=38,y=155)
        
        self.txtuesr=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuesr.place(x=40,y=180,width=270)
        
        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=38,y=225)
        
        self.txtpass=ttk.Entry(frame,show = '*',font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #login button
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="white",activeforeground="black",activebackground="white")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #forgot password
        passwordbtn=Button(frame,command = forgot_pass, text="Forgot Password",font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="black",activebackground="white")
        passwordbtn.place(x=13,y=350,width=160)
    
    #to check admin login details  
    def login(self):
        uid = self.txtuesr.get()
        cursor1.execute("select * from secret_questions")
        recordlist = cursor1.fetchall()
        print(recordlist)
        D = None
        for record in recordlist:
            print(record)
            if uid in record:
                print(uid)
                print(record)
                D = recordlist.index(record)
                print(D)
                break

        if self.txtuesr.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("ERROR", "All fields required")
            quit()
        elif D == None or self.txtpass.get()!=recordlist[D][1]:
            messagebox.showerror("Error","Invalid Admin UID or Password")
            quit()
        elif self.txtuesr.get()==recordlist[D][0] and self.txtpass.get()==recordlist[D][1]:
            messagebox.showinfo("Success","Welcome to Eagle's Eye")
            adminwind()  
                           
#userwindow   
class User_window:  
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x780+0+0")
        self.root.title("Eagle's Eye")
        #background images
        img1 =Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\win_bg.jpg")
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root,image = self.photoimg1,cursor="hand2")
        bg_img.place(x=0,y=0,width=1400,height=800)
        
        img2 = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\topbg_2.jpg")
        img2 = img2.resize((450, 200), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        photo1 = Label(self.root, image=self.photoimg2,cursor="hand2")
        photo1.place(x=450, y=0)
        
        img3 = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\topbg_3.jpg")
        img3 = img3.resize((450, 250), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        photo1 = Label(self.root, image=self.photoimg3)
        photo1.place(x=900, y=0)
        
        img4 = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\cap3.jpg")
        img4 = img4.resize((450, 250), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        photo1 = Label(self.root, image=self.photoimg4)
        photo1.place(x=0, y=0)
        
        lbl = Label(self.root,text="EAGLE'EYE",font = ("Algerian",20,"bold"),fg="white",bg ="Black" )
        lbl.place(x=450,y=200,height=50,width=450)

        lbl = Label(self.root,text="Face recognition door security system",font = ("Algerian",20,"bold"),fg="black",bg ="dark blue" )
        lbl.place(x=0,y=250,height=50,width=1350)
        lbl = Label(self.root,text="user window",font = ("Algerian",20,"bold"),fg="white",bg ="Black" )
        lbl.place(x=450,y=300,height=50,width=450)
        #developer details button
        img8 = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\developers.jpg")
        img8 = img8.resize((250,250),Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        photo8 = Label(self.root,image = self.photoimg8,cursor="hand2")
        photo8.place(x = 0, y = 300)
        developer_details = Button(self.root,text="Developer Details",command=self.dev_info,cursor="hand2",font=("Arial",20),fg="white",bg = "Black")
        developer_details.place(x=0,y=550,height=35,width = 255)
        
        #help desk button
        img5 = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\fac24.png")
        img5 = img5.resize((250,250),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        photo5 = Label(self.root,image = self.photoimg5,cursor="hand2")
        photo5.place(x = 380, y = 400)
        help_desk = Button(self.root,text="Helpdesk",command=self.helpdesk,cursor="hand2",font=("Arial",20),fg="white",bg = "Black")
        help_desk.place(x= 380,y=650,height=35,width=255)
        
        #recognize face button
        img6 = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\recognizeface.jpg")
        img6 = img6.resize((250,250),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        photo6 = Label(self.root,image = self.photoimg6,cursor="hand2")
        photo6.place(x = 720, y = 400)
        detect_face = Button(self.root,text="Detect Face",command= self.face_recog, cursor="hand2",font=("Arial",20),fg="white",bg = "Black")
        detect_face.place(x=720,y=650,height=35,width=255)
        #exit button
        img7 = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\exit.jpg")
        img7 = img7.resize((250,250),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        photo7 = Label(self.root,image = self.photoimg7,cursor="hand2")
        photo7.place(x = 1110, y = 300)
        exit_btn = Button(self.root,text="Exit",command=self.exit,cursor="hand2",font=("Arial",20),fg="white",bg = "Black")
        exit_btn.place(x=1110,y=550,height=35,width=255)
    
    # exit button
    def exit(self):
        quit()
    
    def face_recog(self):
        webCamRecog()
        outputScreen()
    
    #help desk window
    def helpdesk(self):
        global photoimg1,photoimg2,photoimg3,photoimg4
        Top= Toplevel()
        Top.geometry("1350x780+0+0")
        Top.title("Eagle's Eye")
        
        #background images
        img1 = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\lock.jpg")
        img1 = img1.resize((1400, 630), Image.ANTIALIAS)
        photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(Top,image=photoimg1)
        bg_img.place(x=0, y=150, width=1400, height=650)

        img2 = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\topbg_3.jpg")
        img2 = img2.resize((470, 200), Image.ANTIALIAS)
        photoimg2 = ImageTk.PhotoImage(img2)
        photo1 = Label(Top, image=photoimg2)
        photo1.place(x=0, y=0)
        
        img3 = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\topbg_2.jpg")
        img3 = img3.resize((450, 200), Image.ANTIALIAS)
        photoimg3 = ImageTk.PhotoImage(img3)
        photo1 = Label(Top, image=photoimg3)
        photo1.place(x=450, y=0)
        
        img4 = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\cap3.jpg")
        img4 = img4.resize((450, 200), Image.ANTIALIAS)
        photoimg4 = ImageTk.PhotoImage(img4)
        photo1 = Label(Top, image=photoimg4)
        photo1.place(x=900, y=0)
         
        lbl = Label(Top,text="HELP DESK", font=("Algerian", 20, "bold"), fg="white", bg="Black")
        lbl.place(x=450, y=200, height=55, width=450)
        lbl = Label(Top,text="If you are facing any issues \n contact any of the following email ids: \n prajin1619@gmail.com \n derrickraju3ty@gmail.com \n jchalakkal16@gmail.com", font=("Arial", 20, "bold"), fg="white", bg="black",pady=50,bd=10, relief=SUNKEN)
        lbl.place(x=200, y=350, width= 950)
   
    #developer details window
    def dev_info(self):
        global photoimg1,photoimg2,photoimg3,photoimg4
        Top =Toplevel()
        Top.geometry("1350x780+0+0")
        Top.title("Eagle's Eye")
        
        #background images
        img3 = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\bg_login1.jpg")
        img3 = img3.resize((1400, 780))
        photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(Top,image=photoimg3)
        bg_img.place(x=0, y=0, width=1400, height=780)

        img1 = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\codrIcon.jpg")
        img1 = img1.resize((200, 250))
        photoimg1 = ImageTk.PhotoImage(img1)
        photo = Label(Top,image=photoimg1)
        photo.place(x=180, y=200)

        img2 = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\codrIcon.jpg")
        img2 = img2.resize((200, 250))
        photoimg2 = ImageTk.PhotoImage(img2)
        photo1 = Label(Top,image=photoimg2)
        photo1.place(x=580, y=200)
    
        img4 = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\codrIcon.jpg")
        img4 = img4.resize((200, 250))
        photoimg4 = ImageTk.PhotoImage(img4)
        photo4 = Label(Top,image=photoimg4)
        photo4.place(x=980, y=200)
        #dev details
        lbl_1 = Label(Top,text="EAGLE'EYE", font=("Algerian", 20, "bold"), fg="white", bg="Black")
        lbl_1.place(x=450, y=0, height=50, width=450)


        lbl_2 = Label(Top,text="Face recognition door security system", font=("Algerian", 20, "bold"), fg="black",bg="dark blue")
        lbl_2.place(x=0, y=50, height=50, width=1350)

        lbl_3 = Label(Top,text="Developer Details", font=("Algerian", 20, "bold"), fg="white", bg="Black")
        lbl_3.place(x=450, y=100, height=50, width=450)

        lbl_4 = Label(Top,text="Created by THE_DEBUGGERS:\nEAGLE'S EYE is a Facial recognition door security system used for conference halls and labs \n It  was developed by group of codders called 'The_Debuggers' which consists of:\n Antony Prajin, Derrick Raju and Joseph Chalakkal from CHRIST ACADEMY JUNIOR COLLEGE.\nThis project was develeoped for their XII CBSE COMPUTER SCIENCE PROJECT ASSINGMENT.", font=("Arial", 12, "bold"),bg="black",fg="white",pady=50,bd=10, relief=SUNKEN)
        lbl_4.place(x=180, y=500, width= 1000, height = 200)
    
#first window         
if __name__=="__main__":
    root=Tk()
    app=Login_window(root)
    root.mainloop()
    
 
        

   





    

