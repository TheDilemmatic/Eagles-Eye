
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector as ms
mycon=ms.connect(host='localhost',user='root',password='mera_sql',database='cbse_compsci_proj')
mycursor=mycon.cursor()

class Delete_id:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x780+0+0")
        self.root.title("Delete id")
        #image1
        img = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\del0.jpg")
        img = img.resize((460, 135),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x = 0, y = 0, width = 460, height = 135)
        
        #image2
        img1 = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\del2.jpg")
        img1= img1.resize((480, 135),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root,image = self.photoimg1)
        f_lbl1.place(x = 460, y = 0, width = 480, height = 135)
        
        #image3
        img2 = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\del3.jpg")
        img2 = img2.resize((460, 135),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.root,image = self.photoimg2)
        f_lbl2.place(x = 940, y = 0, width = 460, height = 135)

        #backround
        img3 = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\fac4.gif")
        img3 = img3.resize((1370, 655),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root,image = self.photoimg3)
        bg_img.place(x = 0, y = 135, width = 1370, height = 655) 
        
        title_lbl=Label(bg_img, text = "DELETE AN EMPLOYEE ID HERE", font = ("Algerian", 29,'bold'), bg = "dark blue", fg = "white")
        title_lbl.place(x = 0, y = 5, width = 1370, height = 35 )

        m_frame = Frame(bg_img, bd = 2)
        m_frame.place(x = 20, y = 48, width = 1320, height = 550)


        l_frame = LabelFrame(m_frame, bd = 10, relief = RIDGE, text = "SEARCH AND DELETE:", font = ('Algerian', 18, "bold", "italic", "underline") )
        l_frame.place(x = 15, y = 15, width= 1280, height = 528)

        #Frame_bg
        fram_bg = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\cap3.jpg")
        fram_bg = fram_bg.resize((1258,528),Image.ANTIALIAS)
        self.pic = ImageTk.PhotoImage(fram_bg)
        bgimg_lbl = Label(l_frame, image = self.pic)
        bgimg_lbl.place(x = 0, y = 0)
        
        #inserting values
        def dele():
            q="Select * from employee_details where Employee_code='{}'".format(srch_entry.get())
            mycursor.execute(q)
            r=mycursor.fetchall()
            self.Emplo_table.insert(parent='', index=0, iid=0, values=r[0])


        #search_frame
        srch_frame = LabelFrame(l_frame, bg = "silver", relief = RIDGE, text = "SEARCH FOR AN EMPLOYEE HERE:", font = ('Algerian', 14, "italic", "underline"))
        srch_frame.place(x = 130, y = 30, width = 1000, height = 100)
        srch_header = Label(srch_frame, bg = "silver", text = "Search by employee code:", font = ('Times New Roman', 18, "bold"), fg = "dark blue")
        srch_header.grid( row = 0, column = 0, padx = 60, pady = 20)
        srch_entry = ttk.Entry(srch_frame, width = 50, font = ("times new roman", 10))
        srch_entry.grid(row = 0, column = 1, padx = 0)
        search_btn = Button(srch_frame, command=dele,bg = "blue", height = 1, width = 14, text = "Search", font = ("Times New Roman", 12, "bold"), fg = "white")
        search_btn.grid(row = 0, column = 2, padx = 45)

        #Table_frame
        tabl_frame = LabelFrame(l_frame, bd=3, bg="silver", relief=RIDGE,text = "Details of the Employee (whose id you want to delete):", font = ('Algerian', 12, "bold", "italic", "underline"))
        tabl_frame.place(x=230, y=143, width= 800, height=245)
        x_scrl_bar = ttk.Scrollbar(tabl_frame, orient="horizontal")
        y_scrl_bar = ttk.Scrollbar(tabl_frame, orient="vertical")
        self.Emplo_table = ttk.Treeview(tabl_frame, columns=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),xscrollcommand=x_scrl_bar.set, yscrollcommand=y_scrl_bar.set)

        x_scrl_bar.pack(side=BOTTOM, fill=X)
        x_scrl_bar.config(command=self.Emplo_table.xview)
        y_scrl_bar.pack(side=RIGHT, fill=Y)
        y_scrl_bar.config(command=self.Emplo_table.yview)

        self.Emplo_table.heading(0, text="Name")
        self.Emplo_table.heading(1, text="Gender")
        self.Emplo_table.heading(2, text="Department")
        self.Emplo_table.heading(3, text="Post held")
        self.Emplo_table.heading(4, text="Employee code")
        self.Emplo_table.heading(5, text="Salary")
        self.Emplo_table.heading(6, text="Phone")
        self.Emplo_table.heading(7, text="E-mail")
        self.Emplo_table.heading(8, text="Qualifications")
        self.Emplo_table.heading(9, text="Achievements")
        self.Emplo_table.heading(10, text="Experience")
        self.Emplo_table.heading(11, text="Ratings")

        self.Emplo_table.pack(fill=BOTH, pady=10)


        inner_frame3 = LabelFrame(l_frame, bd = 3, bg = "silver", relief = RIDGE, font = ('Algerian', 12, "bold", "italic", "underline") )
        inner_frame3.place(x = 230, y = 401, width = 800, height = 80)
        
        
        def dbtn():
            q="delete from employee_details where Employee_code='{}'".format(srch_entry.get())
            mycursor.execute(q)
            mycon.commit()
        def sav():
            subroot=Tk()
            subroot.geometry("500x100")
            ler=Label(subroot,bg="black",text = "Successfully Deleted", font = ("Algerian", 24,'bold'),fg="white")
            ler.pack(fil = BOTH,expand=True)
            root.destroy()
        #Delete_button
        change_btn = Button(inner_frame3,command=dbtn ,bg = "dark red", height = 2, width = 10, text = "Delete", cursor = "hand2", font = ("Times New Roman", 15, "bold"), fg = "white")
        change_btn.grid(row = 2, column = 0, padx = 44, pady = 6)

        #Save_button
        save_btn = Button(inner_frame3,command=sav, bg = "dark green", height = 2, width = 10, text = "Save", cursor = "hand2", font = ("Times New Roman", 15, "bold"), fg = "white")
        save_btn.grid(row = 2, column = 1, padx = 395, pady = 0)
        
           
        
       
if __name__ == "__main__":
    root = Tk()
    obj = Delete_id(root)
    root.mainloop()





