import PIL
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector as ms

con = ms.connect(host="localhost", user="root", password="mera_sql", database="cbse_compsci_proj")
cursor1 = con.cursor()
cursor1.execute("select * from secret_questions")
recordlist = cursor1.fetchall()
print(recordlist)


def secret_questions(uid):
    D = None
    for record in recordlist:
        print(record)
        if uid in record:
            print(uid)
            print(record)
            D = recordlist.index(record)
            print(D)
            break
    
    root = Toplevel()
    root.title("Forgot Password")
    root.geometry("1350x780+0+0")

    bg = ImageTk.PhotoImage(image=PIL.Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\login_bg2.jpg"))
    lbl_bg = Label(root, image=bg)
    lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
    
    # login frame
    frame = Frame(root, bg="black")
    frame.place(x=500, y=170, width=350, height=450)

    get_str = Label(frame, text="Secret Questions", font=("times new roman", 20, "bold","underline"), fg="white", bg="black")
    get_str.place(x=70, y=90)
    
    ques1 = Label(frame, text= recordlist[D][2], font=("times new roman", 15, "bold"), fg="white", bg="black")
    ques1.place(x=38, y=155)

    txtuesr = ttk.Entry(frame, font=("times new roman", 15, "bold") )
    txtuesr.place(x=40, y=190, width=270)

    ques2 = Label(frame, text= recordlist[D][4], font=("times new roman", 15, "bold"), fg="white", bg="black")
    ques2.place(x = 38,y = 235)

    txtuesr2 = ttk.Entry(frame, font=("times new roman", 15, "bold") )
    txtuesr2.place(x=40, y=270, width=270)


    def proceed():
        
        passwd = recordlist[D][1]
        inp = txtuesr.get()
        inp2 = txtuesr2.get()
        
        if inp == recordlist[D][3] and inp2 == recordlist[D][5]:
            messagebox.showinfo("Success","Your password is: "+ passwd)
        elif inp != recordlist[D][3] and inp2 != recordlist[D][5]:
            messagebox.showerror("Error", "Wrong answer")
        
    enter = Button(frame, command=proceed, text="confirm", font=("times new roman", 12, "bold"),borderwidth=0, fg="black", bg="white", activeforeground="black", activebackground="white")
    enter.place(x=110, y=350, width=120)
    root.mainloop()
    #file_h.close()

if __name__ == "__main__":
    secret_questions('7654321')
