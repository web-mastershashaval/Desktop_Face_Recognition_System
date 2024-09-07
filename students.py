from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from datetime import datetime
import cv2
import os 

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        # ========variables=======
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_id = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_std_name = StringVar()
        self.var_std_id = StringVar()
        self.var_semister = StringVar()
        self.var_phone = StringVar()
        self.var_gender = StringVar()
        self.var_roll = StringVar()
        self.var_div = StringVar()
        self.var_dob = StringVar()
        self.var_year = StringVar()
        self.var_teacher = StringVar()
        self.var_semisterradio = StringVar()

        # Setup for images
        self.setup_images()
        # Setup for GUI
        self.setup_ui()

    def setup_images(self):
        # Image paths
        image_path = "./images/theimg.jpg"

        # Background image
        self.bg_image = Image.open(image_path)
        self.bg_image = self.bg_image.resize((1530, 790), Image.LANCZOS)
        self.photo_bg = ImageTk.PhotoImage(self.bg_image)

    def setup_ui(self):
        # Background image
        background_label = Label(self.root, image=self.photo_bg)
        background_label.place(x=0, y=0, width=1530, height=790)

        # Title label
        title_lbl = Label(background_label, text="STUDENTS MANAGEMENT SYSTEM", font=("Times New Roman", 35, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Main frame
        main_frame = Frame(background_label, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1500, height=650)

        # Left label frame for information
        Left_Frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Students Details", font=("times new roman", 12, "bold"))
        Left_Frame.place(x=10, y=10, width=760, height=580)
       
        # Current courses (Moved up)
        Current_Course_Frame = LabelFrame(Left_Frame, bd=2, bg="white", relief=RIDGE, text="Current Course", font=("times new roman", 12, "bold"))
        Current_Course_Frame.place(x=5, y=10, width=740, height=150)  # Adjusted y position

        # Department
        dep_label = Label(Current_Course_Frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        dep_combo = ttk.Combobox(Current_Course_Frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"), width=17, state="active")
        dep_combo["values"] = ("Select Department", "Engineering", "ICT", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=5, sticky=W)

        # Courses
        course_label = Label(Current_Course_Frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        course_combo = ttk.Combobox(Current_Course_Frame, textvariable=self.var_course, font=("times new roman", 12, "bold"), width=17, state="active")
        course_combo["values"] = ("Select Course", "Software Engineering", "Computer Science", "Mechanical Eng", "Media")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=5, sticky=W)

        # Year
        year_label = Label(Current_Course_Frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        year_combo = ttk.Combobox(Current_Course_Frame, textvariable=self.var_year, font=("times new roman", 12, "bold"), width=17, state="active")
        year_combo["values"] = ("Select Year", "2020-21", "2020-22", "2020-23", "2020-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=5, sticky=W)

        # Semester
        semester_label = Label(Current_Course_Frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        semester_combo = ttk.Combobox(Current_Course_Frame, textvariable=self.var_semister, font=("times new roman", 12, "bold"), width=17, state="active")
        semester_combo["values"] = ("Select Semester", "Semester-1", "Semester-2", "Semester-3", "Semester-4")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=5, sticky=W)

        # Class student information
        Class_Student_Frame = LabelFrame(Left_Frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        Class_Student_Frame.place(x=5, y=170, width=740, height=400)  # Adjusted y position

        # student id
        studentId_label = Label(Class_Student_Frame, text="StudentID:", font=("times new roman", 12, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, sticky=W)
        student_entry = ttk.Entry(Class_Student_Frame, textvariable=self.var_std_id, font=("times new roman", 12, "bold"))
        student_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # student Name
        studentName_label = Label(Class_Student_Frame, text="Student Name:", font=("times new roman", 12, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        studetName_entry = ttk.Entry(Class_Student_Frame, textvariable=self.var_std_name, font=("times new roman", 12, "bold"))
        studetName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class division
        Class_div_label = Label(Class_Student_Frame, text="Class Division:", font=("times new roman", 12, "bold"), bg="white")
        Class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        # Class_div_entry = ttk.Entry(Class_Student_Frame, textvariable=self.var_div, font=("times new roman", 12, "bold"))
        # Class_div_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        Class_div_combo = ttk.Combobox(Class_Student_Frame, textvariable=self.var_div, font=("times new roman", 12, "bold"), width=17, state="active")
        Class_div_combo["values"] = ("Select Class Division", "A", "B", "C")
        Class_div_combo.current(0)
        Class_div_combo.grid(row=1, column=1, padx=2, pady=5, sticky=W)

        # roll number
        Roll_no_label = Label(Class_Student_Frame, text="Roll No:", font=("times new roman", 12, "bold"), bg="white")
        Roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        Roll_no_entry = ttk.Entry(Class_Student_Frame, textvariable=self.var_roll, font=("times new roman", 12, "bold"))
        Roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(Class_Student_Frame, text="Gender:", font=("times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        # gender_entry = ttk.Entry(Class_Student_Frame, textvariable=self.var_gender, font=("times new roman", 12, "bold"))
        # gender_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(Class_Student_Frame, textvariable=self.var_gender, font=("times new roman", 12, "bold"), width=17, state="active")
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=2, pady=5, sticky=W)

        # DOB
        dob_label = Label(Class_Student_Frame, text="DOB:", font=("times new roman", 12, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        dob_entry = ttk.Entry(Class_Student_Frame, textvariable=self.var_dob, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(Class_Student_Frame, text="Email:", font=("times new roman", 12, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        email_entry = ttk.Entry(Class_Student_Frame, textvariable=self.var_email, font=("times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone
        phone_label = Label(Class_Student_Frame, text="Phone:", font=("times new roman", 12, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        phone_entry = ttk.Entry(Class_Student_Frame, textvariable=self.var_phone, font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(Class_Student_Frame, text="Address:", font=("times new roman", 12, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        address_entry = ttk.Entry(Class_Student_Frame, textvariable=self.var_address, font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher
        teacher_label = Label(Class_Student_Frame, text="Teacher:", font=("times new roman", 12, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        teacher_entry = ttk.Entry(Class_Student_Frame, textvariable=self.var_teacher, font=("times new roman", 12, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # Radiobuttons for photo sample status
        self.var_radio1 = StringVar()
        self.var_radio1.set("No")  # Set a default value

        radiobtn1 = ttk.Radiobutton(Class_Student_Frame, text="Take photo sample", variable=self.var_radio1, value="yes")
        radiobtn1.grid(row=6, column=0)

        radiobtn2 = ttk.Radiobutton(Class_Student_Frame, text="No photo sample", variable=self.var_radio1, value="No")
        radiobtn2.grid(row=6, column=1)

                # button frames
        btn_frame=Frame(Class_Student_Frame,relief=RIDGE,bg="grey")
        btn_frame.place(x=0,y=200,width=725,height=35)

        # save btn
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=20,font=("times new roman", 12, "bold"), bg="blue")
        save_btn.grid(row=0,column=0)
                # update btn
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=20,font=("times new roman", 12, "bold"), bg="blue")
        update_btn.grid(row=0,column=1)
                # dlete btn
        delete_btn=Button(btn_frame,text="Delete", command=self.delete_data,width=20,font=("times new roman", 12, "bold"), bg="blue")
        delete_btn.grid(row=0,column=2)
                # Reset btn
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data, width=20,font=("times new roman", 12, "bold"), bg="blue")
        reset_btn.grid(row=0,column=3)


        btn_frame1=Frame(Class_Student_Frame,relief=RIDGE,bg="grey")
        btn_frame1.place(x=0,y=235,width=725,height=35)

                        # Reset btn
        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset, width=40,font=("times new roman", 12, "bold"), bg="blue")
        take_photo_btn.grid(row=0,column=0)
    
                        # Reset btn
        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=40,font=("times new roman", 12, "bold"), bg="blue")
        update_photo_btn.grid(row=0,column=1)



        # Right label frame
        Right_Frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Students Details", font=("times new roman", 12, "bold"))
        Right_Frame.place(x=780, y=10, width=660, height=580)

        # ===== Search System =====
        Search_Frame = LabelFrame(Right_Frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        Search_Frame.place(x=5, y=10, width=640, height=70)  

        Search_label = Label(Search_Frame, text="Search By:", font=("times new roman", 15, "bold"), bg="red", fg="white")
        Search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        Search_combo = ttk.Combobox(Search_Frame, font=("times new roman", 12, "bold"), width=17, state="active")
        Search_combo["values"] = ("Select", "Roll_No", "Phone_No")
        Search_combo.current(0)
        Search_combo.grid(row=0, column=1, padx=2, pady=5, sticky=W)

        Search_entry = ttk.Entry(Search_Frame, font=("times new roman", 12, "bold"))
        Search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(Search_Frame, text="Search", width=5, font=("times new roman", 12, "bold"), bg="blue")
        search_btn.grid(row=0, column=3, padx=10, pady=5)

        showAll_btn = Button(Search_Frame, text="Show All", width=7, font=("times new roman", 12, "bold"), bg="blue")
        showAll_btn.grid(row=0, column=4, padx=10, pady=5)

        # Table frames
        table_frame = Frame(Right_Frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=90, width=640, height=250)  

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame, columns=("id", "name", "dep", "course", "year", "sem", "roll", "gender", "dob","email", "phone", "address", "teacher", "photo","div"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # Pack scrollbars
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        
        # Initialize UI components here     
        self.student_table.heading("dep", text="Depertment")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photo Status")
        self.student_table["show"] = "headings"

        # Configure columns
        self.student_table.column("dep", width=100, anchor=W)
        self.student_table.column("course", width=100, anchor=W)
        self.student_table.column("year", width=100, anchor=W)
        self.student_table.column("sem", width=100, anchor=W)
        self.student_table.column("id", width=100, anchor=W)
        self.student_table.column("name", width=150, anchor=W)
        self.student_table.column("div", width=100, anchor=W)
        self.student_table.column("roll", width=100, anchor=W)
        self.student_table.column("gender", width=100, anchor=W)
        self.student_table.column("dob", width=100, anchor=W)
        self.student_table.column("email", width=150, anchor=W)
        self.student_table.column("phone", width=100, anchor=W)
        self.student_table.column("address", width=150, anchor=W)
        self.student_table.column("teacher", width=150, anchor=W)
        self.student_table.column("photo", width=100, anchor=W)

        self.student_table.pack(fill=BOTH, expand=True)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        """
        Add data to the database and update the Treeview widget.
        """
        try:
            # Print the values to debug
            print(f"Department: '{self.var_dep.get()}'")
            print(f"Student Name: '{self.var_std_name.get()}'")
            print(f"Student ID: '{self.var_std_id.get()}'")
            print(f"DOB: '{self.var_dob.get()}'")
            print(f"Email: '{self.var_email.get()}'")
            print(f"Phone: '{self.var_phone.get()}'")
            print(f"Address: '{self.var_address.get()}'")
            print(f"Teacher: '{self.var_teacher.get()}'")

            # Check if all required fields are filled
            if (self.var_dep.get().strip() == "Select Department" or
                self.var_std_name.get().strip() == "" or
                self.var_std_id.get().strip() == "" or
                self.var_dob.get().strip() == "" or
                self.var_email.get().strip() == "" or
                self.var_phone.get().strip() == "" or
                self.var_address.get().strip() == "" or
                self.var_teacher.get().strip() == ""):
                    
                messagebox.showerror("Error", "All fields are required", parent=self.root)
                return

            # Get the date of birth from the entry field
            dob_str = self.var_dob.get().strip()  # Ensure no extra spaces
            dob_date = dob_str if dob_str else None  # Handle as needed if no DOB is provided

            # Connect to the database
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="",
                database="desktop_face_recognition",
                port=3306
            )
            my_cursor = conn.cursor()

            photo_status = self.var_radio1.get() if self.var_radio1.get() in ["yes", "No"] else None
            
            # Perform the insertion
            my_cursor.execute(
                "INSERT INTO students (name, department, course, year, semester, roll_no, gender, dob, email, phone, address, teacher, Photo, division) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    self.var_std_name.get().strip(),
                    self.var_dep.get().strip(),
                    self.var_course.get().strip(),
                    self.var_year.get().strip(),
                    self.var_semister.get().strip(),
                    self.var_roll.get().strip(),
                    self.var_gender.get().strip(),
                    dob_date,
                    self.var_email.get().strip(),
                    self.var_phone.get().strip(),
                    self.var_address.get().strip(),
                    self.var_teacher.get().strip(),
                    photo_status,
                    self.var_div.get().strip()
                )
            )
            conn.commit()
            self.fetch_data()  # Update Treeview with the new data
            conn.close()
            messagebox.showinfo("Success", "Student Details Added Successfully", parent=self.root)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database Error: {err}", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Error: {str(es)}", parent=self.root)

    def fetch_data(self):
        """
        Fetch data from the database and display it in the Treeview widget.
        """
        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="",
                database="desktop_face_recognition",
                port=3306
            )
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM students")
            data = my_cursor.fetchall()

            # Clear existing data in Treeview
            for item in self.student_table.get_children():
                self.student_table.delete(item)

            # Insert new data into Treeview
            if len(data) != 0:
                for row in data:
                    self.student_table.insert("", "end", values=row)

            conn.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database Error: {err}", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Error: {str(es)}", parent=self.root)    

    def get_cursor(self, event=""):
        try:
            cursor_focus = self.student_table.focus()  # Fix method name
            content = self.student_table.item(cursor_focus)
            data = content["values"]

            # Ensure that the data length matches the number of columns
            if len(data) == 15:
                self.var_dep.set(data[0])
                self.var_course.set(data[1])
                self.var_std_name.set(data[2])
                self.var_year.set(data[3])
                self.var_semister.set(data[4])
                self.var_roll.set(data[5])
                self.var_gender.set(data[6])
                self.var_dob.set(data[7])
                self.var_email.set(data[8])
                self.var_phone.set(data[9])
                self.var_address.set(data[10])
                self.var_teacher.set(data[11])
                self.var_div.set(data[12])
                self.var_std_id.set(data[13])
                self.var_radio1.set(data[14])
            else:
                messagebox.showerror("Error", "Unexpected data format", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Error in get_cursor: {str(e)}", parent=self.root)
    
    def update_data(self):
        """
        Update student details in the database.
        """
        # Check if all required fields are filled
        if (self.var_dep.get() == "Select Department" or
            self.var_std_name.get() == "" or
            self.var_std_id.get() == "" or
            self.var_dob.get() == "" or
            self.var_email.get() == "" or
            self.var_phone.get() == "" or
            self.var_address.get() == "" or
            self.var_teacher.get() == ""):
            
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        # Ask for confirmation to update
        update = messagebox.askyesno("Update", "Do you want to update the student's details?", parent=self.root)
        if update:
            try:
                # Connect to the database
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="",
                    database="desktop_face_recognition",
                    port=3306
                )
                my_cursor = conn.cursor()

                # Execute the update query
                my_cursor.execute(
                    "UPDATE students SET name=%s, department=%s, course=%s, year=%s, semester=%s, roll_no=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s, photo=%s, division=%s WHERE roll_no=%s",
                    (
                        self.var_std_name.get().strip(),
                        self.var_dep.get().strip(),
                        self.var_course.get().strip(),
                        self.var_year.get().strip(),
                        self.var_semister.get().strip(),
                        self.var_roll.get().strip(),
                        self.var_gender.get().strip(),
                        self.var_dob.get().strip(),
                        self.var_email.get().strip(),
                        self.var_phone.get().strip(),
                        self.var_address.get().strip(),
                        self.var_teacher.get().strip(),
                        self.var_radio1.get().strip(),  # Assuming this is for photo status
                        self.var_div.get().strip(),
                        self.var_std_id.get().strip()  # Assuming roll_no is unique for identifying the student
                    )
                )

                conn.commit()
                conn.close()
                self.fetch_data()  # Refresh data in the Treeview
                messagebox.showinfo("Success", "Student data updated successfully!", parent=self.root)
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database Error: {err}", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Error: {str(es)}", parent=self.root)
        else:
            return
        



    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID must be given", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Are you sure you want to delete the student's data?", parent=self.root)
                if delete:
                    # Connect to the database
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="",
                        database="desktop_face_recognition",
                        port=3306
                    )
                    my_cursor = conn.cursor()
                    
                    # SQL query to delete the student record
                    sql = "DELETE FROM students WHERE roll_no=%s"  # Adjust column name if necessary
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                    
                    conn.commit()
                    self.fetch_data()  # Refresh data in the Treeview
                    conn.close()
                    
                    messagebox.showinfo("Success", "Student details deleted successfully!", parent=self.root)
                else:
                    return
                
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database Error: {err}", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Error: {str(es)}", parent=self.root)
# Reset
    def reset_data(self):
                self.var_dep.set("Select Department")
                self.var_course.set("Select Course")
                self.var_year.set("Select Year")
                self.var_semister.set("Select Semester")
                self.var_std_id.set("")
                self.var_std_name.set("") 
                self.var_div.set("Select Division")               
                self.var_roll.set("")
                self.var_gender.set("Male")
                self.var_dob.set("")
                self.var_email.set("")
                self.var_phone.set("")
                self.var_address.set("")
                self.var_teacher.set("")               
                self.var_radio1.set("")

    def generate_dataset(self):
        # Check if all required fields are filled
        if (self.var_dep.get() == "Select Department" or
            self.var_std_name.get() == "" or
            self.var_std_id.get() == "" or
            self.var_dob.get() == "" or
            self.var_email.get() == "" or
            self.var_phone.get() == "" or
            self.var_address.get() == "" or
            self.var_teacher.get() == ""):
            
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        # Ask for confirmation to update
        update = messagebox.askyesno("Update", "Do you want to update the student's details?", parent=self.root)
        if not update:
            return

        try:
            # Connect to the database
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="",
                database="desktop_face_recognition",
                port=3306
            )
            my_cursor = conn.cursor()

            # Get the next ID for the student
            my_cursor.execute("SELECT COUNT(*) FROM students")
            result = my_cursor.fetchone()
            student_id = result[0] + 1  # Increment ID for the new student

            # Update student details with the new ID
            my_cursor.execute(
                "UPDATE students SET name=%s, department=%s, course=%s, year=%s, semester=%s, roll_no=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s, photo=%s, division=%s WHERE roll_no=%s",
                (
                    self.var_std_name.get().strip(),
                    self.var_dep.get().strip(),
                    self.var_course.get().strip(),
                    self.var_year.get().strip(),
                    self.var_semister.get().strip(),
                    self.var_roll.get().strip(),
                    self.var_gender.get().strip(),
                    self.var_dob.get().strip(),
                    self.var_email.get().strip(),
                    self.var_phone.get().strip(),
                    self.var_address.get().strip(),
                    self.var_teacher.get().strip(),
                    self.var_radio1.get().strip(),  # Assuming this is for photo status
                    self.var_div.get().strip(),
                    self.var_std_id.get().strip()  # Use roll_no for identifying the student
                )
            )
            conn.commit()
            conn.close()

            # Ensure the data directory exists
            data_dir = "data"
            if not os.path.exists(data_dir):
                os.makedirs(data_dir)

            # Load the Haar cascade for face detection
            face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
                if len(faces) == 0:
                    return None
                for (x, y, w, h) in faces:
                    return img[y:y+h, x:x+w]
                return None

            # Capture images for dataset
            cap = cv2.VideoCapture(0)
            img_id = 0
            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Failed to grab frame")
                    break

                face = face_cropped(frame)
                if face is not None:
                    img_id += 1
                    face_resized = cv2.resize(face, (450, 450))
                    face_gray = cv2.cvtColor(face_resized, cv2.COLOR_BGR2GRAY)
                    file_name_path = os.path.join(data_dir, f"user_face_{student_id}_{img_id}.jpg")
                    cv2.imwrite(file_name_path, face_gray)
                    cv2.putText(face_resized, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                    cv2.imshow("Cropped Face", face_resized)
                    print(f"Image saved: {file_name_path}")

                cv2.imshow("Camera Feed", frame)
                if cv2.waitKey(1) == 27 or img_id >= 100:
                    break

            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Generating dataset completed successfully!!!")
            self.reset_data()  # Assuming you have this method to clear/reset the form

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database Error: {err}", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Error: {str(es)}", parent=self.root)



if __name__ == "__main__":
    root = Tk()
    app = Student(root)
    root.mainloop()
# 0758063864