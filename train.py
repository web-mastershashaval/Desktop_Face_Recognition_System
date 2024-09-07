from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from datetime import datetime
import cv2
import os 
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title label
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("Times New Roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)


        # Button
        button_text = Button(self.root, text="TRAIN DATA",command=self.train_classifier, cursor="hand2", font=("Times New Roman", 15, "bold"), bg="darkblue", fg="red")
        button_text.place(x=0, y=380, width=1530, height=40)

    def train_classifier(self):
        data_dir = "data"
        # List only files, exclude directories
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, file))]

        faces = []
        ids = []

        for image_path in path:
            try:
                img = Image.open(image_path).convert('L')  # Open and convert the image to grayscale
                image_np = np.array(img, 'uint8')

                # Extract ID from filename
                filename = os.path.split(image_path)[-1]
                basename, ext = os.path.splitext(filename)
                parts = basename.split('_')
                if len(parts) >= 3 and parts[-1].isdigit():  # Ensure the last part is a number
                    id = int(parts[-2])  # Use the second-to-last part as ID
                    faces.append(image_np)
                    ids.append(id)
                else:
                    print(f"Filename {filename} is not in the expected format.")
                    
                cv2.imshow("Training", image_np)
                if cv2.waitKey(1) == 27:  # ESC key to break
                    break
            except Exception as e:
                print(f"Error processing file {image_path}: {e}")

        ids = np.array(ids)

        # ================TRAIN THE CLASSIFIER AND THEN SAVE=======================
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Success", "Training dataset completed successfully", parent=self.root)








if __name__ == "__main__":
    root = Tk()
    app = Train(root)
    root.mainloop()