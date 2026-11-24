#I used official documentation for tkinter (https://docs.python.org/3/library/tkinter.html)
#As well as w3schools's Python File handling section (https://www.w3schools.com/python/python_file_handling.asp) as
#References during the development of this code.

from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog


class StudentManager:
    def __init__(self, root):
        self.root = root
        self.total_students = 0
        self.total_marks = 0
        self.average_percentage_marks = 0

        # create frame for buttons
        side_frame = Frame(root, bg="#22396F")
        side_frame.pack(side="left", fill="y")
        side_frame_l = Label(side_frame, text="Student Menu", font=("Arial", 15), bg="#22396F", fg="white")
        side_frame_l.pack(fill="x")
        button_frame = Frame(side_frame)
        button_frame.pack(fill="x")

        #Create frame for the main content
        self.content_frame = Frame(self.root)
        self.content_frame.pack(side="left", fill="both", expand=TRUE)

        #Create header frame
        self.header_frame = Frame(self.content_frame)
        self.header_frame.pack(pady=(0, 20))



        #Create the main menu frame
        self.main_menu_frame = Frame(self.content_frame)

        #Create the frames displayed when viewing all records
        self.all_student_frame = Frame(self.content_frame)
        self.summary_frame = Frame(self.content_frame)

        #Create the frames for searching and displaying one student record
        self.individual_student_frame = Frame(self.content_frame)
        self.student_input_frame = Frame(self.content_frame)

        #Create the two frames used for highest and lowest mark student.
        self.highest_mark_frame = Frame(self.content_frame)
        self.lowest_mark_frame = Frame(self.content_frame)

        #Create the frames for the sort menu.
        self.sort_frame = Frame(self.content_frame, )
        self.sort_input_frame = Frame(self.content_frame)

        #Create frames for the update menu.
        self.update_frame = Frame(self.content_frame)
        self.update_input_frame = Frame(self.content_frame)
        self.update_radio_frame = Frame(self.content_frame)

        #Create header label here
        self.header_l = Label(self.header_frame, text="Header", font=("Arial", 15))
        self.header_l.pack(side="top")

        #Create buttons for the GUI
        back_b = Button(button_frame, text="Home", command=self.display_main_menu, font=("Arial", 15))
        back_b.pack(fill="x")

        view_all_records_b = Button(button_frame, text="View All Records",
                                    command=self.display_all_records,
                                    font=("Arial", 15),
                                    )
        view_all_records_b.pack(fill="x")

        view_individual_record_b = Button(button_frame, text="Search Student",
                                          command=self.display_individual_record,
                                          font=("Arial", 15)
                                          )
        view_individual_record_b.pack(fill="x")

        highest_mark_b = Button(button_frame, text="Highest Mark",
                                command=self.display_highest_mark,
                                font=("Arial", 15)
                                )
        highest_mark_b.pack(fill="x")

        lowest_mark_b = Button(button_frame, text="Lowest Mark",
                               command=self.display_lowest_mark,
                               font=("Arial", 15)
                               )
        lowest_mark_b.pack(fill="x")

        sort_b = Button(button_frame, text="Sort Records",
                        command=self.display_sort,
                        font=("Arial", 15)
                        )
        sort_b.pack(fill="x")

        add_record_b = Button(button_frame, text="Add Record",
                              command=self.add_student_record,
                              font=("Arial", 15)
                              )
        add_record_b.pack(fill="x")

        remove_record_b = Button(button_frame, text="Remove Record",
                                 command=self.remove_student_record,
                                 font=("Arial", 15)
                                 )
        remove_record_b.pack(fill="x")

        update_frame_b = Button(button_frame, text="Update Record",
                                command=self.display_update,
                                font=("Arial", 15)
                                )
        update_frame_b.pack(fill="x")

        #Home menu widgets
        menu_l = Label(self.main_menu_frame, text="Press the buttons on the sidebar to navigate menus! \n"
                                                  "You can view all the student records or search via name or ID.",
                       font=("Arial", 12)
                       )
        menu_l.pack()

        #View all records widget
        self.total_students_l = Label(self.summary_frame, text=f"There are {self.total_students} in the class.")
        self.total_students_l.pack()

        self.average_l = Label(self.summary_frame,
                               text=f"The percentage average was {self.average_percentage_marks:.2f}% in the class.")
        self.average_l.pack()

        # individual record widget and related values.
        individual_info_l = Label(self.student_input_frame, text="Enter Student ID or Name")
        individual_info_l.grid(row=0, column=0, sticky="e")
        individual_student_entry = Entry(self.student_input_frame)
        individual_student_entry.grid(row=1, column=0, pady=10, sticky="e")

        individual_enter_b = Button(self.student_input_frame, text="Search",
                                    command=lambda: self.display_individual_student(individual_student_entry.get()))
        individual_enter_b.grid(row=1, column=1, pady=10, sticky="e")

        # update_frame widgets
        update_field = StringVar(value="stu_id")

        update_info_l = Label(self.update_input_frame, text="Enter Student ID or Name")
        update_info_l.grid(row=0, column=0, sticky="e")

        update_student_entry = Entry(self.update_input_frame)
        update_student_entry.grid(row=1, column=0, sticky="e")

        update_enter_b = Button(self.update_input_frame, text="Update",
                                command=lambda: self.update(update_student_entry.get(), update_field.get()))
        update_enter_b.grid(row=1, column=1, sticky="e")

        student_id_r = Radiobutton(self.update_radio_frame, text="Student ID",
                                   variable=update_field,
                                   value="stu_id")
        student_id_r.grid(row=0, column=0, sticky="w")

        student_name_r = Radiobutton(self.update_radio_frame, text="Name",
                                     variable=update_field,
                                     value="stu_name")
        student_name_r.grid(row=0, column=1, sticky="w")

        course1_r = Radiobutton(self.update_radio_frame, text="Course 1 Marks",
                                variable=update_field,
                                value="course1")
        course1_r.grid(row=0, column=2, sticky="w")

        course2_r = Radiobutton(self.update_radio_frame, text="Course 2 Marks",
                                variable=update_field,
                                value="course2")
        course2_r.grid(row=1, column=0, sticky="w")

        course3_r = Radiobutton(self.update_radio_frame, text="Course 3 Marks",
                                variable=update_field,
                                value="course3")
        course3_r.grid(row=1, column=1, sticky="w")

        exam_r = Radiobutton(self.update_radio_frame, text="Exam Marks",
                             variable=update_field,
                             value="exam_score")
        exam_r.grid(row=1, column=2, sticky="w")

        # sort widgets
        sort_option = StringVar(value="student_id")
        order_option = StringVar(value="asc")

        student_id_r = Radiobutton(self.sort_input_frame, text="Student ID", variable=sort_option, value="student_id")
        student_id_r.grid(row=0, column=0, pady=10, sticky="e")

        course_total_r = Radiobutton(self.sort_input_frame, text="Course Total", variable=sort_option,
                                     value="course_total")
        course_total_r.grid(row=0, column=1, pady=10, sticky="e")

        exam_r = Radiobutton(self.sort_input_frame, text="Exam Score", variable=sort_option,
                                     value="exam_score")
        exam_r.grid(row=0, column=2, pady=10, sticky="e")

        overall_r = Radiobutton(self.sort_input_frame, text="Overall", variable=sort_option,
                                     value="overall")
        overall_r.grid(row=0, column=3, pady=10, sticky="e")

        asc_r = Radiobutton(self.sort_input_frame, text="Ascending", variable=order_option, value="asc")
        asc_r.grid(row=1, column=0, sticky="e")

        dsc_r = Radiobutton(self.sort_input_frame, text="Descending", variable=order_option, value="dsc")
        dsc_r.grid(row=1, column=1, sticky="e")

        sort_b = Button(self.sort_input_frame, text="Sort",
                        command=lambda: self.sort(sort_option.get(), order_option.get()))
        sort_b.grid(row=0, column=4, pady=10, sticky="e")

        # our current frame
        self.active_frame = self.main_menu_frame
        self.root.geometry("800x700")
        self.root.title("Student Manager")

    def display_all_records(self):
        # update our current frame
        self.switch_frame(self.all_student_frame, self.all_student_frame, self.summary_frame)
        #reset the table.
        self.clear_frame(self.all_student_frame)

        with open("studentMarks.txt", 'r') as f:
            # create the header first.
            self.display_header(self.all_student_frame)

            # Reset the average percentage mark and total marks.
            self.total_marks = 0
            self.average_percentage_marks = 0

            for current_line, line in enumerate(f):
                if current_line > 0:
                    # call function to display the record
                    self.display_record_row(self.all_student_frame, current_line, line)

            #It is possible to just get it directly since we are reading the file, but I decided on making a function
            #Just in case I needed to get the total in another unrelated menu.
            self.total_students = self.get_total()

            # display summary
            self.average_percentage_marks = self.total_marks / self.get_total()

            # update the summary labels
            self.total_students_l.config(text=f"There are {self.total_students} in the class.")
            self.average_l.config(text=f"The percentage average was {self.average_percentage_marks:.2f}% in the class.")

    def read_student_record(self, record):
        # takes a single line from the dataset and then turns it into a list. Numbers are returned as integers.
        student_record_list = record.split(",")

        # Its easier if we just convert the string numbers into integers so we dont have to worry about converting them
        for i in student_record_list:
            try:
                index = student_record_list.index(i)
                student_record_list[index] = int(i)
            except ValueError:
                #If we get an error it means we cant convert it, skip to the next iteration.
                continue
        return student_record_list

    def grade_from_int(self, grade_int):
        # very simple, just returns a grade from an integer
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

    def switch_frame(self, new_active_frame, *frames):
        # for switching frames.
        # clean the screen first
        self.clean_screen()
        # update active frame
        self.active_frame = new_active_frame
        #update header
        self.update_header()
        # note frame(s) are packed in order it is passed.
        for frame in frames:
            frame.pack()

    def display_highest_mark(self):
        # update our current frame
        self.switch_frame(self.highest_mark_frame, self.highest_mark_frame)

        with open('studentMarks.txt', 'r') as f:
            #Track out highest mark and its line
            highest_line = None
            highest_mark = None
            for i, line in enumerate(f):
                if i > 0:
                    # get values
                    stu_id, stu_name, course1, course2, course3, exam_score = self.read_student_record(line)
                    course_total = course1 + course2 + course3

                    # if we dont have any record or have a new higher mark we set it as our highest.
                    if not highest_mark or course_total > highest_mark:
                        highest_line = line
                        highest_mark = course_total

        # output the table
        self.display_header(self.highest_mark_frame)
        self.display_record_row(self.highest_mark_frame, 1, highest_line)

    def display_lowest_mark(self):
        # very similar to the highest mark function except it gets the lowest.
        # update our current frame
        self.switch_frame(self.lowest_mark_frame, self.lowest_mark_frame)

        with open('studentMarks.txt', 'r') as f:
            #Keep track of lowest mark and its line.
            lowest_line = None
            lowest_mark = None
            for i, line in enumerate(f):
                if i > 0:
                    # get values
                    stu_id, stu_name, course1, course2, course3, exam_score = self.read_student_record(line)
                    course_total = course1 + course2 + course3

                    # if we dont have any record or have a new higher mark we set it.
                    if not lowest_line or course_total < lowest_mark:
                        lowest_line = line
                        lowest_mark = course_total

        # output the table
        self.display_header(self.lowest_mark_frame)
        self.display_record_row(self.lowest_mark_frame, 1, lowest_line)

    def display_record_row(self, frame, current_row, record_line):
        # read the individual student records now by unpacking it first
        stu_id, stu_name, course1, course2, course3, exam_score = self.read_student_record(record_line)
        # calculate necessary values
        course_total = course1 + course2 + course3
        overall_percentage = ((course_total + exam_score) / 160) * 100
        # call function to get grade
        grade = self.grade_from_int(overall_percentage)

        # add the individual marks to the average percentage variable so we can divide it later to get an average
        self.total_marks += overall_percentage

        # given data displays the columns for a single row
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
        # displays the header, row 0 is always the header
        entry_l = Label(frame, text="Row")
        entry_l.grid(row=0, column=0, pady=10, padx=10, sticky="e")

        id_l = Label(frame, text="ID")
        id_l.grid(row=0, column=1, pady=10, padx=10, sticky="e")

        name_l = Label(frame, text="Name")
        name_l.grid(row=0, column=2, pady=10, padx=10, sticky="e")

        course_total_l = Label(frame, text="Course\nTotal")
        course_total_l.grid(row=0, column=3, pady=10, padx=10, sticky="e")

        exam_score_l = Label(frame, text="Exam Score")
        exam_score_l.grid(row=0, column=4, pady=10, padx=10, sticky="e")

        overall_percentage_l = Label(frame, text="Overall\nPercentage")
        overall_percentage_l.grid(row=0, column=5, pady=10, padx=10, sticky="e")

        stu_grade = Label(frame, text="Grade")
        stu_grade.grid(row=0, column=6, pady=10, padx=10, sticky="e")

    def clean_screen(self):
        # this function cleans the current screen to prepare transition to a new frame.
        # this should be called before displaying a new frame to avoid any visual bugs.
        for frame in self.content_frame.winfo_children():
            # make sure the screen is clear before we do anything
            if frame != self.header_frame:
                frame.forget()
                #self.active_frame.forget()

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def update_header(self):
        if self.active_frame == self.main_menu_frame:
            self.header_l.configure(text="Home Menu")
        elif self.active_frame == self.all_student_frame:
            self.header_l.configure(text="All Students Record")
        elif self.active_frame == self.individual_student_frame:
            self.header_l.configure(text="Individual Student Record")
        elif self.active_frame == self.highest_mark_frame:
            self.header_l.configure(text="Highest Mark Record")
        elif self.active_frame == self.lowest_mark_frame:
            self.header_l.configure(text="Lowest Mark Record")
        elif self.active_frame == self.sort_frame:
            self.header_l.configure(text="Sort Student Record")
        elif self.active_frame == self.update_frame:
            self.header_l.configure(text="Update Student Record")
    def display_main_menu(self):
        # switch screens
        self.switch_frame(self.main_menu_frame, self.main_menu_frame)

    def search_student_line(self, query):
        match = None
        with open('studentMarks.txt', 'r') as f:
            for current_line, line in enumerate(f, start=1):
                if current_line > 1:
                    stu_id, stu_name, course1, course2, course3, exam_score = self.read_student_record(line)
                    try:
                        if int(query) == stu_id:
                            match = line
                            break
                    except ValueError:
                        # we try to match the name instead. Normalize it first to avoid any bugs
                        if query.lower() == stu_name.lower():
                            match = line
                            break

            if match:
                return match
            else:
                return None

    def display_individual_student(self, query):
        match = self.search_student_line(query)
        if match:
            self.clear_frame(self.active_frame)
            self.display_header(self.individual_student_frame)
            self.display_record_row(self.individual_student_frame, 1, match)
        else:
            # we can show an error here
            messagebox.showerror("Student Not Found! ", "Type a valid ID or Name.")

    def display_individual_record(self):
        # create frame for input
        # Note we pass input frame first because we want it to be packed first.
        self.switch_frame(self.individual_student_frame, self.student_input_frame, self.individual_student_frame)
        # this is the header


    def get_total(self):
        with open('studentMarks.txt', 'r') as f:
            return int(f.readline().strip())

    def sort(self, sort_option, order):
        self.clear_frame(self.sort_frame)
        matched_line = None
        # I generally avoided loading the txt file into a declared list in this program as a bit of a self imposed challenge.
        # Here however it was much easier handling the sorting with two lists.
        unsorted_lines = []
        sorted_lines = []
        with open('studentMarks.txt', 'r') as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            if i > 0:
                unsorted_lines.append(line.strip())

        # first loop we iterate over the number of items
        for x in range(len(unsorted_lines)):
            previous_category = None
            # here we iterate to check if that particular item is the biggest or smallest value.
            for line in unsorted_lines:
                # read the individual student records now
                stu_id, stu_name, course1, course2, course3, exam_score = self.read_student_record(line)
                # calculate necessary values
                course_total = course1 + course2 + course3
                overall_percentage = ((course_total + exam_score) / 160) * 100

                match sort_option:
                    # whe match it with whatever order.
                    case "student_id":
                        if order == "asc":
                            if previous_category is None or stu_id > previous_category:
                                # we check if it has already been added to the sorted list.
                                if line in sorted_lines:
                                    continue
                                previous_category = stu_id
                                matched_line = line
                        if order == "dsc":
                            if previous_category is None or stu_id < previous_category:
                                # we check if it has already been added to the sorted list.
                                if line in sorted_lines:
                                    continue
                                previous_category = stu_id
                                matched_line = line

                    case "course_total":
                        if order == "asc":
                            if previous_category is None or course_total > previous_category:
                                # we check if it has already been added to the sorted list.
                                if line in sorted_lines:
                                    continue
                                previous_category = course_total
                                matched_line = line
                        if order == "dsc":
                            if previous_category is None or course_total < previous_category:
                                # we check if it has already been added to the sorted list.
                                if line in sorted_lines:
                                    continue
                                previous_category = course_total
                                matched_line = line

                    case "exam_score":
                        if order == "asc":
                            if previous_category is None or exam_score > previous_category:
                                # we check if it has already been added to the sorted list.
                                if line in sorted_lines:
                                    continue
                                previous_category = exam_score
                                matched_line = line
                        if order == "dsc":
                            if previous_category is None or exam_score < previous_category:
                                # we check if it has already been added to the sorted list.
                                if line in sorted_lines:
                                    continue
                                previous_category = exam_score
                                matched_line = line

                    case "overall":
                        if order == "asc":
                            if previous_category is None or overall_percentage > previous_category:
                                # we check if it has already been added to the sorted list.
                                if line in sorted_lines:
                                    continue
                                previous_category = overall_percentage
                                matched_line = line
                        if order == "dsc":
                            if previous_category is None or overall_percentage < previous_category:
                                # we check if it has already been added to the sorted list.
                                if line in sorted_lines:
                                    continue
                                previous_category = overall_percentage
                                matched_line = line

            sorted_lines.append(matched_line)
        # Here we create the table finally
        self.display_header(self.sort_frame)
        for index, i in enumerate(sorted_lines):
            self.display_record_row(self.sort_frame, index + 1, i)

    def display_sort(self):
        self.switch_frame(self.sort_frame, self.sort_input_frame, self.sort_frame)

    def add_student_record(self):
        student_id = simpledialog.askinteger(
            title="Input", prompt="Enter a Number for Student ID:"
        )
        #to make cancelling end the prompts early, we have guard clauses to return when cancelled.

        if not student_id:
            return

        student_name = simpledialog.askstring(
            title="Input", prompt="Enter Student Name:"
        )

        #here the condition is different. If a user continues but doesn't type anything it is assigned an empty '' string
        #The problem is that an empty string is evaluated as false
        #so we explicitly check if it is none here so that only pressing cancel (which assigns None) returns the func.
        if student_name is None:
            return

        course1 = simpledialog.askinteger(
            title="Input", prompt="Enter a Number for Course 1 Marks:"
        )

        if not course1:
            return

        course2 = simpledialog.askinteger(
            title="Input", prompt="Enter a Number for Course 2 Marks:"
        )

        if not course2:
            return

        course3 = simpledialog.askinteger(
            title="Input", prompt="Enter a Number for Course 3 Marks:"
        )

        if not course3:
            return

        exam = simpledialog.askinteger(
            title="Input", prompt="Enter a Number for Exam Marks:"
        )

        if not exam:
            return

        confirmation = messagebox.askyesno(
            title="Confirm Entry", message="Are you sure that you want to enter this record?"
        )

        # first we return here if we have no confirmation
        if not confirmation:
            return

        # check if anything is null
        if not student_name:
            messagebox.showerror("Invalid Input", "Null Names are not allowed.")
            return

        # guard clause here to avoid duplicated student IDs
        match = self.search_student_line(student_id)
        if match:
            messagebox.showerror("Duplicate ID", "Student IDs must be unique.")
            return

        with open('studentMarks.txt', 'r') as f:
            lines = f.readlines()

        with open('studentMarks.txt', 'w') as f:
            lines[0] = f"{int(lines[0]) + 1}\n"
            f.writelines(lines)

        with open('studentMarks.txt', 'a') as f:
            f.write(f"\n{student_id},{student_name},{course1},{course2},{course3},{exam}")

        self.display_all_records()

    def remove_student_record(self):
        query = simpledialog.askstring(
            title="Enter Search", prompt="Enter a name or student ID to remove:"
        )
        # guard clause to check if the query not a null value
        if not query:
            messagebox.showerror("Invalid Input", "Null Values are not allowed.")
            return
        # search for the student
        match = self.search_student_line(query)
        # guard clause to search for the student.
        if not match:
            messagebox.showerror("Student Not Found", "Enter a valid name or student ID.")
            return

        confirmation = messagebox.askyesno(
            title="Confirm Entry", message="Are you sure that you want to remove this record?")
        if confirmation:
            with open('studentMarks.txt', 'r') as f:
                lines = f.readlines()
            with open('studentMarks.txt', 'w') as f:
                #Update counts
                new_total = int(lines[0]) - 1
                for i, line in enumerate(lines):
                    if i == 0:
                        #we update the new total for the first line
                        f.write(f"{new_total}\n")
                    elif line.strip() != match:
                        #to remove it we write everything except that line we want to remove.
                        f.write(line.strip())
                        #if the index is equal to the new total we are at the end so we dont need to write a new line.
                        if i != new_total:
                            f.write("\n")

            # we'll go back to the frame with all the records.
            self.display_all_records()

    def update(self, query, update_field):
        # first we check if it not null
        if not query:
            messagebox.showerror("Null Error", "Null Values not Supported.")
            return

        match = self.search_student_line(query)

        # return if we have no match
        if not match:
            messagebox.showerror("Student Not Found", "Enter a valid name or student ID.")
            return

        if update_field in ("stu_id", "course1", "course2", "course3", "exam_score"):
            # try to convert the new value into an int if its a numeric field. An exception means its invalid.
            new_value = simpledialog.askinteger(
                title="Update Field", prompt="Enter new value to update:"
            )
        else:
            new_value = simpledialog.askstring(
                title="Update Field", prompt="Enter new value to update:"
            )

        # unpack the student line so we can edit fields individually.
        stu_id, stu_name, course1, course2, course3, exam_score = self.read_student_record(match)
        # we update the value here depending on what the user selected.
        match update_field:
            case "stu_id":
                stu_id = new_value
            case "stu_name":
                stu_name = new_value
            case "course1":
                course1 = new_value
            case "course2":
                course2 = new_value
            case "course3":
                course3 = new_value
            case "exam_score":
                exam_score = new_value

        # make our updated line
        updated_student_line = f"{stu_id},{stu_name},{course1},{course2},{course3},{exam_score}"

        with open('studentMarks.txt', 'r') as f:
            lines = f.readlines()
        # Now we can search for that line in the txt file and then replace it.
        for i, line in enumerate(lines):
            if line.strip() == match.strip():
                lines[i] = updated_student_line
                #if we are at the end of the text file we dont need the new line
                if i > len(lines):
                    lines[i] = lines[i] + "\n"
                # if we've found it we can break the loop
                break

        with open('studentMarks.txt', 'w') as f:
            # write it into the txt file
            f.writelines(lines)

    def display_update(self):
        self.switch_frame(self.update_frame, self.update_input_frame, self.update_radio_frame, self.update_frame)


root = Tk()

manager = StudentManager(root)

manager.display_main_menu()

root.mainloop()
