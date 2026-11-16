from tkinter import *
from tkinter import messagebox
import random

class StudentManager:
    def __init__(self, root):
        self.root = root
        self.total_students = 0
        self.average_percentage_marks = 0

        #create frame for buttons
        self.button_frame = Frame(self.root, bg="#D3D3D3")
        self.button_frame.pack(side="left", fill="y")
        back_b = Button(self.button_frame, text="Home", command=lambda: self.display_main_menu(),
                        font=("Arial", 15))
        back_b.pack(fill="x")

        view_all_records_b = Button(self.button_frame, text="View All Records",
                                    command=lambda:self.view_all_records(),
                                    font=("Arial", 15)
                                    )
        view_all_records_b.pack(fill="x")

        view_individual_record = Button(self.button_frame, text="Search Student",
                                        command=lambda:self.display_individual_record(),
                                        font=("Arial", 15)
                                        )
        view_individual_record.pack(fill="x")



        self.content_frame = Frame(self.root)
        self.content_frame.pack(side="left", fill="both", expand=TRUE)

        self.header_frame = Frame(self.content_frame)
        self.header_frame.pack(pady=(0, 20))

        self.header_l = Label(self.header_frame, text="Header", font=("Arial", 15))
        self.header_l.pack(side="top")

        self.main_menu_frame = Frame(self.content_frame)

        self.all_student_frame = Frame(self.content_frame)
        self.summary_frame = Frame(self.content_frame)

        self.individual_student_frame = Frame(self.content_frame)

        #our current frame
        self.active_frame = self.main_menu_frame

        self.root.geometry("800x600")
        self.root.title("Student Manager")

    def view_all_records(self):
        #update our current frame
        self.clean_screen()
        self.active_frame = self.all_student_frame
        self.all_student_frame.pack()

        self.header_l.configure(text="All Students")


        with open("studentMarks.txt") as f:
            #create the header first.
            self.display_header(self.all_student_frame)

            for current_line, line in enumerate(f, start=1):
                if current_line == 1:
                    #first line has the number of total students
                    print(current_line)
                    self.total_students = int(line.strip())
                else:
                    #call function to display the record
                    self.display_record_row(self.all_student_frame, current_line, line)

            #display summary
            self.average_percentage_marks = self.average_percentage_marks / self.total_students

            self.summary_frame.pack()
            self.display_summary(self.total_students+2)
            print(self.average_percentage_marks)

    def read_student_record(self, record):
        #takes a signle line from the dataset and then turns it into a list. Numbers are returned as integers.
        student_record_list = record.split(",")

        #Its easier if we just convert the string numbers into integers so we dont have to worry about converting them
        for i in student_record_list:
            try:
                index = student_record_list.index(i)
                student_record_list[index] = int(i)
            except ValueError:
                pass
        return student_record_list

    def grade_from_int(self, grade_int):
        if grade_int >= 90:
            return "A"
        elif 90 > grade_int >= 80:
            return "B"
        elif 80 > grade_int >= 70:
            return "C"
        elif 70 > grade_int >= 60:
            return "D"
        else:
            return "F"


    def display_record_row(self, frame, current_row, record_line):
        # read the individual student records now
        stu_id, stu_name, course1, course2, course3, exam_score = self.read_student_record(record_line)
        course_total = course1 + course2 + course3
        overall_percentage = ((course_total + exam_score) / 160) * 100
        grade = self.grade_from_int(overall_percentage)
        print(grade)

        # add the individual marks to the average percentage variable so we can divide it later
        self.average_percentage_marks += overall_percentage

        #given data displays the columns for a single row
        entry_l = Label(frame, text=current_row)
        entry_l.grid(row=current_row, column=0, pady=10, padx=10, sticky="e")

        id_l = Label(frame, text=stu_id)
        id_l.grid(row=current_row, column=1, pady=10, padx=10, sticky="e")

        name_l = Label(frame, text=stu_name)
        name_l.grid(row=current_row, column=2, pady=10, padx=10, sticky="e")

        course_total_l = Label(frame, text=course_total)
        course_total_l.grid(row=current_row, column=3, pady=10, padx=10, sticky="e")

        exam_score_l = Label(frame, text=exam_score)
        exam_score_l.grid(row=current_row, column=4, pady=10, padx=10, sticky="e")

        overall_percentage_l = Label(frame, text=f"{overall_percentage:.2f}%")
        overall_percentage_l.grid(row=current_row, column=5, pady=10, padx=10, sticky="e")

        stu_grade = Label(frame, text=grade)
        stu_grade.grid(row=current_row, column=6, pady=10, padx=10, sticky="e")

    def display_header(self, frame):
        #displays the header, row 0 is always the header
        entry_l = Label(frame, text="Entry")
        entry_l.grid(row=0, column=0, pady=10, padx=10, sticky="e")

        id_l = Label(frame, text="ID")
        id_l.grid(row=0, column=1, pady=10, padx=10, sticky="e")

        name_l = Label(frame, text="Name")
        name_l.grid(row=0, column=2, pady=10, padx=10, sticky="e")

        course_total_l = Label(frame, text="Course Total")
        course_total_l.grid(row=0, column=3, pady=10, padx=10, sticky="e")

        exam_score_l = Label(frame, text="Exam Score")
        exam_score_l.grid(row=0, column=4, pady=10, padx=10, sticky="e")

        overall_percentage_l = Label(frame, text="Overall Percentage")
        overall_percentage_l.grid(row=0, column=5, pady=10, padx=10, sticky="e")

        stu_grade = Label(frame, text="Grade")
        stu_grade.grid(row=0, column=6, pady=10, padx=10, sticky="e")

    def display_summary(self, sum_row):
        total_students_l = Label(self.summary_frame,
                                 text=f"There are {self.total_students} in the class.")
        total_students_l.pack()

        average_l = Label(self.summary_frame,
                          text=f"The percentage average was {self.average_percentage_marks:.2f}% in the class.")
        average_l.pack()

    def clean_screen(self):
        #this function cleans the current screen to prepare transition to a new frame.
        #this should be called before displaying a new frame to avoid any visual bugs.
        print("changing")
        print(self.active_frame)

        for frame in self.content_frame.winfo_children():
            #make sure the screen is clear before we do anything
            if frame != self.header_frame:
                self.clear_frame(frame)
                frame.forget()
                self.active_frame.forget()

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def display_main_menu(self):
        #switch screens
        self.clean_screen()
        self.active_frame = self.main_menu_frame
        self.main_menu_frame.pack()

        self.header_l.configure(text="Home Menu")
        menu_l = Label(self.main_menu_frame,text="Press the buttons on the sidebar to navigate menus! \n"
                                                 "You can view all the student records or search via name or ID.",
                       font=("Arial", 12)
                       )
        menu_l.pack()

    def search_student(self, query):
        #clear the screen of anything previously displayed.

        match = None
        with open('studentMarks.txt', 'r') as f:
            for current_line, line in enumerate(f, start=1):
                if current_line > 1:
                    stu_id, stu_name, course1, course2, course3, exam_score = self.read_student_record(line)
                    try:
                        if int(query) == stu_id:
                            match = line
                    except ValueError:
                        #we try to match the name instead. Normalize it first to avoid any bugs
                        if query.lower() == stu_name.lower():
                            match = line

            if match:
                self.clear_frame(self.active_frame)
                self.display_header(self.individual_student_frame)
                self.display_record_row(self.individual_student_frame, 1, match)
            else:
                #we can show an error here
                messagebox.showerror("Student Not Found! ","Type a valid ID or Name.")




    def display_individual_record(self):
        #create frame for input

        self.clean_screen()
        self.active_frame = self.individual_student_frame
        student_input_frame = Frame(self.content_frame)
        student_input_frame.pack()
        self.individual_student_frame.pack()

        #this is the header
        self.header_l.configure(text="Search Student Record")


        student_entry = Entry(student_input_frame)
        student_entry.grid(row=0, column=0, pady=10, sticky="e")

        enter_b = Button(student_input_frame, text="Search",
                         command=lambda:self.search_student(student_entry.get()))
        enter_b.grid(row=0, column=1, pady=10, sticky="e")

        # create frame that will have grid and row
        self.individual_student_frame.pack()






root = Tk()

manager = StudentManager(root)

manager.display_main_menu()

root.mainloop()
