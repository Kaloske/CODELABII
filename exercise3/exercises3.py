from tkinter import *
import random

class StudentManager:
    def __init__(self, root):
        self.root = root
        self.total_students = 0
        self.average_percentage_marks = 0
        self.button_frame = Frame(self.root)
        self.button_frame.pack()

        self.content_frame = Frame(self.root)
        self.content_frame.pack()

        self.main_menu_frame = Frame(self.content_frame)
        self.main_menu_frame.pack()

        self.all_student_frame = Frame(self.content_frame)
        self.summary_frame = Frame(self.content_frame)


        back_b = Button(self.button_frame,text="Back", command=self.go_back)
        back_b.pack()


        #our current frame
        self.active_frame = self.main_menu_frame

        self.root.geometry("700x600")
        self.root.title("Student Manager")

    def view_all_records(self):
        #update our current menu
        self.clean_screen()
        self.active_frame = self.all_student_frame
        self.all_student_frame.pack()
        with open("studentMarks.txt") as f:
            #create the header first.
            self.display_header()

            for current_line, line in enumerate(f, start=1):
                if current_line == 1:
                    #first line has the number of total students
                    print(current_line)
                    self.total_students = int(line.strip())
                else:
                    #read the individual student records now
                    stu_id, stu_name, course1, course2, course3, exam_score = self.read_student_record(line)
                    exam_score = int(exam_score)
                    course_total = int(course1) + int(course2) + int(course3)
                    overall_percentage = ((course_total + exam_score) / 160) * 100

                    #add the individual marks to the average percentage variable so we can divide it later
                    self.average_percentage_marks += overall_percentage

                    #call function to display the record
                    self.display_record_row(current_line,
                                            stu_id,
                                            stu_name,
                                            course_total,
                                            exam_score,
                                            overall_percentage,
                                            self.grade_from_int(overall_percentage))

            #display summary
            self.average_percentage_marks = self.average_percentage_marks / self.total_students

            self.summary_frame.pack()
            self.display_summary(self.total_students+2)
            print(self.average_percentage_marks)

    def read_student_record(self, record):
        #takes a signle line from the dataset and then turns it into a list
        student_record_list = record.split(",")
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


    def display_record_row(self, current_row, stu_id, stu_name, course_total, exam_score, overall_percentage, grade):
        #given data displays the columns for a single row
        entry_l = Label(self.all_student_frame, text=current_row)
        entry_l.grid(row=current_row, column=0, pady=10, padx=10, sticky="e")

        id_l = Label(self.all_student_frame, text=stu_id)
        id_l.grid(row=current_row, column=1, pady=10, padx=10, sticky="e")

        name_l = Label(self.all_student_frame, text=stu_name)
        name_l.grid(row=current_row, column=2, pady=10, padx=10, sticky="e")

        course_total_l = Label(self.all_student_frame, text=course_total)
        course_total_l.grid(row=current_row, column=3, pady=10, padx=10, sticky="e")

        exam_score_l = Label(self.all_student_frame, text=exam_score, bg="red")
        exam_score_l.grid(row=current_row, column=4, pady=10, padx=10, sticky="e")

        overall_percentage_l = Label(self.all_student_frame, text=f"{overall_percentage:.2f}%")
        overall_percentage_l.grid(row=current_row, column=5, pady=10, padx=10, sticky="e")

        stu_grade = Label(self.all_student_frame, text=grade, bg="red")
        stu_grade.grid(row=current_row, column=6, pady=10, padx=10, sticky="e")

    def display_header(self):
        #displays the header, row 0 is always the header
        entry_l = Label(self.all_student_frame, text="Entry")
        entry_l.grid(row=0, column=0, pady=10, padx=10, sticky="e")

        id_l = Label(self.all_student_frame, text="ID")
        id_l.grid(row=0, column=1, pady=10, padx=10, sticky="e")

        name_l = Label(self.all_student_frame, text="Name")
        name_l.grid(row=0, column=2, pady=10, padx=10, sticky="e")

        course_total_l = Label(self.all_student_frame, text="Course Total")
        course_total_l.grid(row=0, column=3, pady=10, padx=10, sticky="e")

        exam_score_l = Label(self.all_student_frame, text="Exam Score", bg="red")
        exam_score_l.grid(row=0, column=4, pady=10, padx=10, sticky="e")

        overall_percentage_l = Label(self.all_student_frame, text="Overall Percentage")
        overall_percentage_l.grid(row=0, column=5, pady=10, padx=10, sticky="e")

        stu_grade = Label(self.all_student_frame, text="Grade", bg="red")
        stu_grade.grid(row=0, column=6, pady=10, padx=10, sticky="e")

    def display_summary(self, sum_row):
        total_students_l = Label(self.summary_frame,
                                 text=f"There are {self.total_students} in the class.")
        total_students_l.pack()

        average_l = Label(self.summary_frame,
                          text=f"The percentage average was {self.average_percentage_marks} in the class.")
        average_l.pack()

    def clean_screen(self):
        #this function cleans the current screen to prepare transition to a new frame.
        #this should be called before displaying a new frame to avoid any visual bugs.
        print("changing")
        print(self.active_frame)
        for frame in self.content_frame.winfo_children():
            #make sure the screen is clear before we do anything
            self.clear_frame(frame)
            #self.clear_frame(self.active_frame)
            frame.forget()
            #self.active_frame.forget()

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def display_main_menu(self):
        self.active_frame = self.main_menu_frame
        self.main_menu_frame.pack()
        view_all_records_b = Button(self.main_menu_frame, text="View All Records",
                                    command=lambda:self.view_all_records()
                                    )
        view_all_records_b.pack()

    def go_back(self):
        self.clean_screen()
        self.display_main_menu()


root = Tk()

manager = StudentManager(root)

manager.display_main_menu()

print(manager.read_student_record("8439,Jake Hobbs,10,11,10,43"))

root.mainloop()
