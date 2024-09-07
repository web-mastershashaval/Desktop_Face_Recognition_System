from tkinter import *
from PIL import Image, ImageTk
import cv2
import numpy as np
from datetime import datetime
from tkinter import messagebox
import mysql.connector

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title label
        title_lbl = Label(self.root, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("Times New Roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Button
        button_text = Button(self.root, text="Scan Face", cursor="hand2", font=("Times New Roman", 15, "bold"), bg="green", fg="white", command=self.face_recog)
        button_text.place(x=350, y=380, width=650, height=40)

    def draw_boundry(self, img, classifier, scaleFactor, minNeighbour, color, text, clf):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbour)

        coord = []
        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x+w, y+h), color, 3)
            id, predict = clf.predict(gray_image[y:y+h, x:x+w])
            confidence = int(100 * (1 - predict / 300))

            try:
                # Connect to the database
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="desktop_face_recognition",
                    port=3306
                )
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Name FROM students WHERE id=%s", (id,))
                n = my_cursor.fetchone()
                n = n[0] if n else "Unknown"

                my_cursor.execute("SELECT Roll_no FROM students WHERE id=%s", (id,))
                r = my_cursor.fetchone()
                r = r[0] if r else "Unknown"

                my_cursor.execute("SELECT Department FROM students WHERE id=%s", (id,))
                d = my_cursor.fetchone()
                d = d[0] if d else "Unknown"

                my_cursor.execute("SELECT id FROM students WHERE id=%s", (id,))
                i = my_cursor.fetchone()
                i = i[0] if i else "Unknown"

                conn.close()

                if confidence > 77:
                    cv2.putText(img, f'id: {r}', (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f'Roll: {r}', (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f'Name: {n}', (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f'Department: {d}', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, 'Unknown person', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")
            
            coord = [x, y, w, h]
        return coord

    def recognize(self, img, clf, faceCascade):
        coord = self.draw_boundry(img, faceCascade, 1.1, 10, (255, 25, 255), "face", clf)
        return img

    # =================ATTENDANCE================
    def mark_attendance(self, i, r, n, d):
        with open("samba.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = [line.split(",")[0] for line in myDataList]

            if (i not in name_list) and (n not in name_list) and (r not in name_list) and (d not in name_list):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtstring = now.strftime("%H:%M:%S")
                f.write(f'{i},{r},{n},{d},{dtstring},{d1},present\n')

    def face_recog(self):
        try:
            faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")

            video_cap = cv2.VideoCapture(0)
            if not video_cap.isOpened():
                messagebox.showerror("Video Capture Error", "Unable to access the webcam.")
                return

            while True:
                ret, img = video_cap.read()
                if not ret:
                    messagebox.showerror("Video Capture Error", "Failed to capture image.")
                    break

                img = self.recognize(img, clf, faceCascade)
                cv2.imshow("Welcome to face recognition", img)

                if cv2.waitKey(1) == 13:  # Enter key
                    break

            video_cap.release()
            cv2.destroyAllWindows()

        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = Tk()
    app = Face_Recognition(root)
    root.mainloop()
