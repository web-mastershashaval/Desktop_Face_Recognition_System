from tkinter import *
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import csv
import os
from tkinter import messagebox

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        self.setup_images()
        self.ui_setup()

    def setup_images(self):
        image_path = "./images/help.jpg"
        samba_path="./images/sambaman.jpg"
        full_dev="./images/fullstk.jpg"
        try:
            self.bg_image = Image.open(image_path)
            self.bg_image = self.bg_image.resize((1530, 790), Image.LANCZOS)
            self.photo_bg = ImageTk.PhotoImage(self.bg_image)

            self.dv_image = Image.open(samba_path)
            self.dv_image = self.dv_image.resize((200, 200), Image.LANCZOS)
            self.photo_bg2 = ImageTk.PhotoImage(self.dv_image)

            self.fstk_image = Image.open(full_dev)
            self.fstk_image = self.fstk_image.resize((480, 250), Image.LANCZOS)
            self.photo_bg3 = ImageTk.PhotoImage(self.fstk_image)
        except IOError:
            messagebox.showerror("Error", "Image file not found.")


    def ui_setup(self):
            background_label = Label(self.root, image=self.photo_bg)
            background_label.place(x=0, y=0, width=1530, height=790)
            
            title_lbl = Label(self.root, text="HELP", font=("Times New Roman", 35, "bold"), bg="white", fg="BLACK")
            title_lbl.place(x=0, y=0, width=1530, height=45)












if __name__ == "__main__":
    root =Tk()
    app = Help(root)
    root.mainloop()
