import tkinter
from tkinter import*
from tkinter import Tk 
from tkinter import ttk
from PIL import *
from PIL import Image, ImageTk
from PIL.Image import ANTIALIAS


class Entry_exit_detls:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x780+0+0")
        self.root.title("Entry exit details")

        img = Image.open(r"C:\Users\Administrator\Desktop\project_galerry\impimg.jpg")
        img = img.resize((1380,200),ANTIALIAS)
        self.photo = ImageTk.PhotoImage(img)
        m_img = Label(root, image = self.photo)
        m_img.place(x =0, y = 0, height = 200, width = 1380)

        Heading = Label(root, bg = "dark blue", height = 15, width = 1350, text = 'ENTRY AND EXIT DETAILS OF EMPLOYEES (can be viewed by admin only)', font = ("Algerian", 18, "bold"), fg = "white")
        Heading.place(x = 0, y = 180, height = 40, width = 1380)

        m_frame = LabelFrame(root, bd = 3, bg= "silver", relief = RIDGE, text = "Total Details Collected:", font = ('Algerian', 12, "bold", "italic", "underline") )
        m_frame.place(x = 7, y = 220, width = 1350, height = 510)

        # Frame_bg
        fram_bg = Image.open(r"C:\Users\Administrator\Desktop\project_galerry\facda.jpg")
        fram_bg = fram_bg.resize((1340, 518), Image.ANTIALIAS)
        self.pic = ImageTk.PhotoImage(fram_bg)
        bgimg_lbl = Label(m_frame, image=self.pic)
        bgimg_lbl.place(x=0, y=0)

        # Entry and Exit details:
        in_frame1 = LabelFrame(m_frame, bd = 3, bg= "silver", relief = RIDGE, text = "Entry and Exit details:", font = ('Algerian', 10, "bold", "italic", "underline") )
        in_frame1.place(x = 70, y = 7, width = 1200, height = 230)

        x_scrl_bar1 = ttk.Scrollbar(in_frame1, orient="horizontal")
        y_scrl_bar1 = ttk.Scrollbar(in_frame1, orient="vertical")

        self.xit_ntry_table = ttk.Treeview(in_frame1, columns=(0, 1, 2, 3, 4, 5),xscrollcommand = x_scrl_bar1.set, yscrollcommand = y_scrl_bar1.set)

        x_scrl_bar1.pack(side=BOTTOM, fill=X)
        x_scrl_bar1.config(command=self.xit_ntry_table.xview)
        y_scrl_bar1.pack(side=RIGHT, fill=Y)
        y_scrl_bar1.config(command=self.xit_ntry_table.yview)

        self.xit_ntry_table.heading(0, text="Name")
        self.xit_ntry_table.heading(1, text="Purpose")
        self.xit_ntry_table.heading(2, text="Date(entry)")
        self.xit_ntry_table.heading(3, text="Time(entry)")
        self.xit_ntry_table.heading(4, text="Date(exit)")
        self.xit_ntry_table.heading(5, text="Time(exit)")

        self.xit_ntry_table.pack(fill=BOTH, pady=10)

        # Employee_details(with scrollbar):
        in_frame2 = LabelFrame(m_frame, bd = 3, bg = "silver", relief = RIDGE, text = "Details of the Employee (who has accessed the door) :",font=('Algerian', 10, "bold", "italic", "underline"))
        in_frame2.place(x = 70, y = 242, width = 1200, height = 245)

        x_scrl_bar2 = ttk.Scrollbar(in_frame2, orient = "horizontal")
        y_scrl_bar2 = ttk.Scrollbar(in_frame2, orient = "vertical")

        self.Emplo_table = ttk.Treeview(in_frame2, columns = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), xscrollcommand = x_scrl_bar2.set, yscrollcommand= y_scrl_bar2.set)

        x_scrl_bar2.pack(side = BOTTOM, fill = X)
        x_scrl_bar2.config(command = self.Emplo_table.xview)
        y_scrl_bar2.pack(side = RIGHT, fill = Y)
        y_scrl_bar2.config(command = self.Emplo_table.yview)

        self.Emplo_table.heading(0, text = "Name")
        self.Emplo_table.heading(1, text = "Gender")
        self.Emplo_table.heading(2, text = "Department")
        self.Emplo_table.heading(3, text = "Post held")
        self.Emplo_table.heading(4, text = "Employee code")
        self.Emplo_table.heading(5, text = "Salary")
        self.Emplo_table.heading(6, text = "Phone")
        self.Emplo_table.heading(7, text = "E-mail")
        self.Emplo_table.heading(8, text = "Qualifications")
        self.Emplo_table.heading(9, text = "Achievements")
        self.Emplo_table.heading(10, text = "Experience")
        self.Emplo_table.heading(11, text = "Ratings")
        
        self.Emplo_table.pack(fill = BOTH, pady = 10)


if __name__ == "__main__":
    root = Tk()
    obj = Entry_exit_detls(root)
    root.mainloop()





        
