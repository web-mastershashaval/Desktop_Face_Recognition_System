from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from students import Student
import os
from time import strftime
from datetime import datetime
import numpy as np
from tkinter import messagebox
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

# ==============main window============

# =======================first window=================

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Load and set the images
        self.setup_images()

        # Setup UI components
        self.setup_ui()

    def setup_images(self):
        # Image paths
        image_path = "./images/theimg.jpg"

        # Top images
        self.img1 = Image.open(image_path)
        self.img1 = self.img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(self.img1)

        self.img2 = Image.open(image_path)
        self.img2 = self.img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(self.img2)

        self.img3 = Image.open(image_path)
        self.img3 = self.img3.resize((500, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(self.img3)

        # Background image
        self.bg_image = Image.open(image_path)
        self.bg_image = self.bg_image.resize((1530, 790), Image.LANCZOS)
        self.photo_bg = ImageTk.PhotoImage(self.bg_image)

        # Button images
        self.img4 = Image.open("./images/students.jpg")
        self.img4 = self.img4.resize((220, 220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(self.img4)

        self.img5 = Image.open("./images/face.jpg")
        self.img5 = self.img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(self.img5)

        self.img6 = Image.open("./images/attendance.jpg")
        self.img6 = self.img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(self.img6)

        self.img7 = Image.open("./images/help.jpg")
        self.img7 = self.img7.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(self.img7)

        self.img8 = Image.open("./images/ai.jpg")
        self.img8 = self.img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(self.img8)

        self.img9 = Image.open("./images/photos.jpg")
        self.img9 = self.img9.resize((220, 220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(self.img9)

        self.img10 = Image.open("./images/developers.jpg")
        self.img10 = self.img10.resize((220, 220), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(self.img10)

        self.img11 = Image.open("./images/exit.jpg")
        self.img11 = self.img11.resize((220, 220), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(self.img11)

    def setup_ui(self):
        # Top images
        Label(self.root, image=self.photoimg1).place(x=0, y=0, width=500, height=130)
        Label(self.root, image=self.photoimg2).place(x=500, y=0, width=500, height=130)
        Label(self.root, image=self.photoimg3).place(x=1000, y=0, width=530, height=130)

        # Background image
        background_label = Label(self.root, image=self.photo_bg)
        background_label.place(x=0, y=0, width=1530, height=790)

        # Title label
        title_lbl = Label(background_label, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("Times New Roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=('times new roman', 14, 'bold'), background='white', foreground="green")
        lbl.place(x=0, y=0, width=110, height=50)
        time()    

        # Main buttons
        self.create_button(background_label, self.photoimg4, "Student Details", 200, 100, self.student_details)
        self.create_button(background_label, self.photoimg5, "Face Detector", 500, 100, self.detect_faces)
        self.create_button(background_label, self.photoimg6, "Attendance", 800, 100, self.attendance)
        self.create_button(background_label, self.photoimg7, "Help Menu", 1100, 100, self.help_menu)
        self.create_button(background_label, self.photoimg8, "Train Model", 200, 380, self.train_data)
        self.create_button(background_label, self.photoimg9, "Photos", 500, 380, self.open_img)
        self.create_button(background_label, self.photoimg10, "Developers", 800, 380, self.developers)
        self.create_button(background_label, self.photoimg11, "Exit", 1100, 380, self.iExit)

        # Taskbar
        self.create_taskbar(background_label)

    def create_button(self, parent, image, text, x, y, command):
        # Button with image
        button = Button(parent, image=image, command=command, cursor="hand2")
        button.place(x=x, y=y, width=220, height=220)

        # Button with text
        button_text = Button(parent, text=text, cursor="hand2", font=("Times New Roman", 15, "bold"), bg="darkblue", fg="red", command=command)
        button_text.place(x=x, y=y + 220, width=220, height=40)

    def create_taskbar(self, parent):
        # Taskbar frame
        taskbar_frame = Frame(parent, bg="gray", height=60)
        taskbar_frame.place(x=0, y=730, width=1530)

        # Taskbar buttons
        taskbar_buttons = [
            ("Student Details", self.photoimg4, self.student_details),
            ("Face Detector", self.photoimg5, self.detect_faces),
            ("Attendance", self.photoimg6, self.attendance),
            ("Help Menu", self.photoimg7, self.help_menu),
            ("Train Model", self.photoimg8, self.train_data),
            ("Photos", self.photoimg9, self.open_img),
            ("Developers", self.photoimg10, self.developers),
            ("Exit", self.photoimg11, self.iExit)
        ]

        for i, (text, image, command) in enumerate(taskbar_buttons):
            Button(taskbar_frame, image=image, command=command, cursor="hand2").pack(side=LEFT, padx=10, pady=10)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        exit_confirm = messagebox.askyesno("Warning", "Are you sure you want to Exit the System!", parent=self.root)
        if exit_confirm:
            self.root.destroy()

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def detect_faces(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def help_menu(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def developers(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

if __name__ == "__main__":
    root = Tk()
    app = Face_Recognition_System(root)
    root.mainloop()
