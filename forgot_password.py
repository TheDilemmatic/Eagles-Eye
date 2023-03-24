import PIL
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector as ms
from secret_questions import secret_questions




def forgot_pass():
    con = ms.connect(host = "localhost",user = "root",password="mera_sql",database="cbse_compsci_proj")
    cursor1 = con.cursor()
    cursor1.execute("select * from secret_questions")
    recordlist = cursor1.fetchall()

    root = Toplevel()
    root.title("Forgot Password")
    root.geometry("1350x780+0+0")
        
        # login background
    bg = ImageTk.PhotoImage(image=PIL.Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\login_bg2.jpg"))
    lbl_bg = Label(root, image=bg)
    lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
        
        # login frame
    frame = Frame(root, bg="black")
    frame.place(x=500, y=170, width=340, height=450)
    get_str = Label(frame, text="Forgot Password", font=("times new roman", 20, "bold"), fg="white", bg="black")
    get_str.place(x=70, y=90)

    admin_no = Label(frame, text="Admin UID", font=("times new roman", 15, "bold"), fg="white", bg="black")
    admin_no.place(x=38, y=155)
    txtuesr = ttk.Entry(frame, font=("times new roman", 15, "bold"))
    txtuesr.place(x=40, y=180, width=270)
        
    def proceed():
        inp = txtuesr.get()
        print(inp)
        for records in recordlist:
            print(records)
            if inp in records:
                secret_questions(inp)
                quit()
            #elif inp not in records  and recordlist.index(records) != len(recordlist)-1:
                #pass
            #else:
                #messagebox.showerror("Error", "Invalid Admin UID")
                #quit()
            
    proceednbtn = Button(frame, command=proceed, text="Proceed", font=("times new roman", 15, "bold"), bd=3,relief=RIDGE, fg="black", bg="white", activeforeground="black", activebackground="white")
    proceednbtn.place(x=110, y=300, width=120, height=35)

    root.mainloop()
        
#file_h.close()

if __name__ == "__main__":
    forgot_pass()