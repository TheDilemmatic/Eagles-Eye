#import tkinter
from tkinter import*
from tkinter import Tk 
from tkinter import ttk
from PIL import *
from PIL import Image, ImageTk
from PIL.Image import ANTIALIAS
import mysql.connector as sqltor


class Entry_exit_detls:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x780+0+0")
        self.root.title("Entry exit details")

        img = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\graph.png")
        img = img.resize((1380,200),ANTIALIAS)
        self.photo = ImageTk.PhotoImage(img)
        m_img = Label(root, image = self.photo)
        m_img.place(x =0, y = 0, height = 200, width = 1380)

        Heading = Label(root, bg = "dark blue", height = 15, width = 1350, text = 'SCAN REPORT (can be viewed by admin only)', font = ("Algerian", 18, "bold"), fg = "white")
        Heading.place(x = 0, y = 180, height = 40, width = 1380)

        m_frame = LabelFrame(root, bd = 3, bg= "silver", relief = RIDGE, text = "Total Details Collected:", font = ('Algerian', 12, "bold", "italic", "underline") )
        m_frame.place(x = 7, y = 220, width = 1350, height = 510)

        # Frame_bg
        fram_bg = Image.open(r"C:\Users\T13126CNS\Desktop\project_gallery\bg_main.gif")
        fram_bg = fram_bg.resize((1340, 518), Image.ANTIALIAS)
        self.pic = ImageTk.PhotoImage(fram_bg)
        bgimg_lbl = Label(m_frame, image=self.pic)
        bgimg_lbl.place(x=0, y=0)

        # Entry and Exit details:
        in_frame2 = LabelFrame(m_frame, bd = 3, bg = "silver", relief = RIDGE, text = "Details of the Employee (who has accessed the door) :",font=('Algerian', 10, "bold", "italic", "underline"))
        in_frame2.place(x = 70, y = 65, width = 1200, height = 400)

        x_scrl_bar2 = ttk.Scrollbar(in_frame2, orient = "horizontal")
        y_scrl_bar2 = ttk.Scrollbar(in_frame2, orient = "vertical")

        self.Emplo_table = ttk.Treeview(in_frame2, columns = (0, 1, 2, 3, 4, 5, 6, 7, 8), xscrollcommand = x_scrl_bar2.set, yscrollcommand= y_scrl_bar2.set, height = 22)

        x_scrl_bar2.pack(side = BOTTOM, fill = X)
        x_scrl_bar2.config(command = self.Emplo_table.xview)
        y_scrl_bar2.pack(side = RIGHT, fill = Y)
        y_scrl_bar2.config(command = self.Emplo_table.yview)
        
        self.Emplo_table.column(0,width=180,anchor='c')
        self.Emplo_table.column(1,width=180,anchor='c')
        self.Emplo_table.column(2,width=180,anchor='c')
        self.Emplo_table.column(3,width=180,anchor='c')
        self.Emplo_table.column(4,width=180,anchor='c')
        self.Emplo_table.column(5,width=180,anchor='c')
        self.Emplo_table.column(6,width=180,anchor='c')
        self.Emplo_table.column(7,width=180,anchor='c')
        self.Emplo_table.column(8,width=180,anchor='c')
    
        
        self.Emplo_table.heading(0, text="Date(scan)")
        self.Emplo_table.heading(1, text="Time(scan)")
        self.Emplo_table.heading(2, text="Status")
        self.Emplo_table.heading(3, text = "Employee code")
        self.Emplo_table.heading(4, text = "Name")
        self.Emplo_table.heading(5, text = "Gender")
        self.Emplo_table.heading(6, text = "Department")
        self.Emplo_table.heading(7, text = "Post held")
        self.Emplo_table.heading(8, text = "Phone")

        mycon = sqltor.connect(host = "localhost", user = "root", password = "mera_sql", database = "cbse_compsci_proj")
        if mycon.is_connected():
            print("success!")
        cursor = mycon.cursor()
        cmd = "SELECT * from scan_report"
        cursor.execute(cmd)
        xitdetls = cursor.fetchall()
        print(xitdetls)
        cursor.close()

        for id in range(len(xitdetls)):
            print(id)
            record = xitdetls[id]
            self.Emplo_table.insert("",'end',iid= id,values= record)
        #id=19
        #while id<len(xitdetls):
            
            #record = xitdetls[id]
            #self.Emplo_table.insert("",'end',iid= id,values= record)
            #id=id+19
       
        self.Emplo_table.pack(fill = BOTH, pady = 10)


if __name__ == "__main__":
    root = Tk()
    obj = Entry_exit_detls(root)
    root.mainloop()





        
