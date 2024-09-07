from tkinter import *
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import csv
import os

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        self.setup_images()
        self.ui_setup()

    def setup_images(self):
        image_path = "./images/theimg.jpg"
        try:
            self.bg_image = Image.open(image_path)
            self.bg_image = self.bg_image.resize((1530, 790), Image.LANCZOS)
            self.photo_bg = ImageTk.PhotoImage(self.bg_image)
        except IOError:
            messagebox.showerror("Error", "Image file not found.")

    def ui_setup(self):
        background_label = Label(self.root, image=self.photo_bg)
        background_label.place(x=0, y=0, width=1530, height=790)
        
        title_lbl = Label(self.root, text="STUDENTS ATTENDANCE SYSTEM SOFTWARE", font=("Times New Roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(background_label, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1500, height=650)

        Left_Frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Left_Frame.place(x=10, y=10, width=760, height=590)

        Left_insideFrame = LabelFrame(Left_Frame, bd=2, bg="white", relief=RIDGE, font=("times new roman", 12, "bold"))
        Left_insideFrame.place(x=10, y=10, width=719, height=300)

        # Label entries
        attendanceId_label = Label(Left_insideFrame, text="Attendance ID:", font=("times new roman", 12, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        self.attendance_entry = ttk.Entry(Left_insideFrame, font=("times new roman", 12, "bold"))
        self.attendance_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        rollLabel = Label(Left_insideFrame, text="Roll:", font=("times new roman", 12, "bold"), bg="white")
        rollLabel.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        self.atten_roll = ttk.Entry(Left_insideFrame, font=("times new roman", 12, "bold"))
        self.atten_roll.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        nameLabel = Label(Left_insideFrame, text="Name:", font=("times new roman", 12, "bold"), bg="white")
        nameLabel.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        self.atten_name = ttk.Entry(Left_insideFrame, font=("times new roman", 12, "bold"))
        self.atten_name.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        departmentLabel = Label(Left_insideFrame, text="Department:", font=("times new roman", 12, "bold"), bg="white")
        departmentLabel.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        self.atten_department = ttk.Entry(Left_insideFrame, font=("times new roman", 12, "bold"))
        self.atten_department.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        timeLabel = Label(Left_insideFrame, text="Time:", font=("times new roman", 12, "bold"), bg="white")
        timeLabel.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        self.atten_time = ttk.Entry(Left_insideFrame, font=("times new roman", 12, "bold"))
        self.atten_time.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        dateLabel = Label(Left_insideFrame, text="Date:", font=("times new roman", 12, "bold"), bg="white")
        dateLabel.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        self.atten_date = ttk.Entry(Left_insideFrame, font=("times new roman", 12, "bold"))
        self.atten_date.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        attendanceLabel = Label(Left_insideFrame, text="Attendance Status:", font=("times new roman", 12, "bold"), bg="white")
        attendanceLabel.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        self.atten_status = ttk.Combobox(Left_insideFrame, font=("times new roman", 12, "bold"), width=17, state="active")
        self.atten_status["values"] = ("Select Status", "Present", "Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        btn_frame = Frame(Left_insideFrame, relief=RIDGE, bg="grey")
        btn_frame.place(x=0, y=250, width=725, height=35)

        save_btn = Button(btn_frame, text="Import csv", command=self.importCsv, width=19, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Export csv", command=self.exportCsv, width=19, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Update", width=19, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", width=19, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        Right_Frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_Frame.place(x=790, y=10, width=660, height=583)

        table_Frame = LabelFrame(Right_Frame, bd=2, bg="white", relief=RIDGE, text="Attendance Table", font=("times new roman", 12, "bold"))
        table_Frame.place(x=5, y=10, width=640, height=400)

        # Scroll bars
        scroll_x = ttk.Scrollbar(table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_Frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_Frame, columns=("id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        # Set column headings and configuration
        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"
        
        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())  # Clear existing data
        for row in rows:
            if len(row) == len(self.AttendanceReportTable["columns"]):
                self.AttendanceReportTable.insert("", END, values=row)
            else:
                print("Warning: Row length mismatch.")
        if not rows:
            print("Warning: No data to display.")

    def importCsv(self):
        global mydata
        file_name = filedialog.askopenfilename(
            initialdir=os.getcwd(), 
            title="Open CSV", 
            filetypes=(("CSV file", "*.csv"), ("ALL file", "*.*")), 
            parent=self.root
        )
        if file_name:
            with open(file_name, newline='') as myfile:
                csvread = csv.reader(myfile, delimiter=",")
                mydata = [row for row in csvread]
                
                if mydata:
                    self.fetchData(mydata)
                else:
                    print("Warning: CSV file is empty.")

    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No data found to export", parent=self.root)
                return
            
            file_name = filedialog.asksaveasfilename(
                initialdir=os.getcwd(), 
                title="Save CSV", 
                filetypes=(("CSV file", "*.csv"), ("ALL file", "*.*")), 
                parent=self.root,
                defaultextension=".csv"
            )
            if file_name:
                with open(file_name, mode="w", newline="") as myfile:
                    exp_write = csv.writer(myfile, delimiter=",")
                    exp_write.writerows(mydata)
                    messagebox.showinfo("Success", "Data successfully exported to " + os.path.basename(file_name), parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Error: {str(es)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    app = Attendance(root)
    root.mainloop()
