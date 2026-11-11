import tkinter
import random
from tkinter import *
from traceback import clear_frames

root = Tk()
root.geometry("400x300")

class MathQuiz:
    def __init__(self, root):
        self.root = root

        #set up initial variables
        self.chosen_difficulty = tkinter.StringVar()
        self.number_of_questions = 10
        self.current_question = 1
        self.correct_answers = 0
        self.user_score = 0
        self.attempt = 1

        #create frames
        self.difficulty_frame = Frame(self.root)
        self.difficulty_frame.pack(pady=20)

        self.problem_frame = Frame(self.root)
        self.problem_frame.pack(pady=20)

        self.output_frame = Frame(self.problem_frame)
        self.output_frame.pack(side="bottom")

        self.results_frame = Frame(self.root)
        self.results_frame.pack(pady=20)

        #formatting variables
        self.output_padding = 15

    def change_difficulty(self, difficulty):
        #set the difficulty here, print output for debugging
        #Also hides the difficulty frame
        self.chosen_difficulty.set(difficulty)
        self.difficulty_frame.forget()
        self.displayProblem()

        print(self.chosen_difficulty.get())

    def displayMenu(self):
        #create the menu for the difficulties
        l1 = Label(self.difficulty_frame, text="Choose your difficulty.", font=("Arial", 20))
        l1.pack()

        b_easy = Button(self.difficulty_frame,
                        text="1. Easy",
                        font=("Arial", 15),
                        anchor="w",
                        command=lambda: self.change_difficulty("easy")
                        )
        b_easy.pack(fill="x")

        b_medium = Button(self.difficulty_frame,
                          text="2. Moderate", font=("Arial", 15),
                          anchor="w",
                          command=lambda: self.change_difficulty("moderate")
                          )
        b_medium.pack(fill="x")

        b_hard = Button(self.difficulty_frame,
                        text="3. Advanced",
                        font=("Arial", 15),
                        anchor="w",
                        command=lambda: self.change_difficulty("advanced")
                        )
        b_hard.pack(fill="x")

    def displayResults(self):
        #initialize variable
        grade = None

        #determine grade rating from the score
        if self.user_score >= 90:
            grade = "A"
        elif 80 <= self.user_score < 90:
            grade = "B"
        elif 70 <= self.user_score < 80:
            grade = "C"
        elif 60 <= self.user_score < 70:
            grade = "D"
        elif self.user_score < 60:
            grade = "F"

        #displays the results
        score_l = Label(self.results_frame,
                        text=f"Score: {self.user_score}/{self.number_of_questions * 10}",
                        font=("Arial", 20)
                        )
        score_l.pack()

        correct_q_l = Label(self.results_frame,
                        text=f"Correct Answers: {self.correct_answers}/{self.number_of_questions}",
                        font=("Arial", 20)
                        )
        correct_q_l.pack()

        grade_l = Label(self.results_frame,
                            text=f"Grade: {grade}",
                            font=("Arial", 20)
                        )
        grade_l.pack()


    def displayProblem(self):
            #generate required values and operation
            num_a = self.randomInt()
            num_b = self.randomInt()
            operation = self.decideOperation()

            #create label, entry, and button
            question_l = Label(self.problem_frame,
                               text=f"Q{self.current_question}: {num_a} {operation} {num_b}",
                               font=("Arial", 20)
                               )
            question_l.pack()

            user_answer = Entry(self.problem_frame,
                                font=("Arial", 15)
                                )
            user_answer.pack()

            #submit button runs isCorrect() function
            submit = Button(self.problem_frame,
                            text="Submit Answer",
                            command=lambda: self.isCorrect(user_answer.get(),num_a,num_b,operation),
                            font=("Arial", 15)
                            )
            submit.pack(pady=10)

            #increment current question



    def randomInt(self):
        #for my program I decided that moderate is only 2 digit numbers (to avoid getting single digits in both)
        rand_number = 0
        if self.chosen_difficulty.get() == "easy":
            rand_number = random.randint(1, 9)
        elif self.chosen_difficulty.get() == "moderate":
            rand_number = random.randint(10, 99)
        elif self.chosen_difficulty.get() == "advanced":
            rand_number = random.randint(1000, 9999)
        return rand_number

    def decideOperation(self):
        operations = ["+", "-"]
        return random.choice(operations)

    def update_question(self):
        #resets attempts and increments current question counter
        self.current_question += 1
        self.attempt = 1

        #clear problem_frame children
        self.clearProblemFrame(self.problem_frame)
        self.clearOutputFrame()

        if self.current_question <= self.number_of_questions:
            #runs display problem again for a new question
            self.displayProblem()
        else:
            #hide problem frame
            self.problem_frame.forget()
            #go to results
            self.displayResults()

    def clearProblemFrame(self, frame):
        #this clears the problem_frame
        for widget in frame.winfo_children():
            if not isinstance(widget, Frame):
                widget.destroy()

    def clearOutputFrame(self):
        for widget in self.output_frame.winfo_children():
            widget.destroy()

    def isCorrect(self, answer, num_a, num_b, operation):
        #First we clear the output frame to remove any loose widgets
        self.clearOutputFrame()

        #Try turning the answer into an int, if it has an error it means it wasn't an integer.
        try:
            answer = int(answer)
            # Match operation string with the appropriate operation

            #initialize variable for now
            correct_answer = None

            match operation:
                case "+":
                    correct_answer = num_a + num_b
                case "-":
                    correct_answer = num_a - num_b

            if answer == correct_answer and self.attempt <= 2:
                #increment correct answer
                self.correct_answers += 1

                #display output
                output = Label(self.output_frame, text="Problem answered correctly!",
                               font=("Arial", 20),
                               fg="green")
                output.pack(pady = self.output_padding)

                # award score based on attempt count
                if self.attempt == 1:
                    self.user_score += 10
                else:
                    self.user_score += 5

                next_question = Button(self.output_frame,
                                       text="Next",
                                       font=("Arial", 15),
                                       command=lambda: self.update_question())
                next_question.pack(pady = self.output_padding)

            else:
                # if no matches it was wrong, return false.
                print("Incorrect answer")
                print(self.attempt)
                if self.attempt == 1:
                    output = Label(self.output_frame,
                                   text="Incorrect answer! \nLast attempt.",
                                   font=("Arial", 20),
                                   fg="red"
                                   )
                    output.pack(pady = self.output_padding)
                    self.attempt += 1

                elif self.attempt == 2:
                    self.attempt += 1
                    # if its over 2 it doesn't do anything so the user has to go to the next question.

                    output = Label(self.output_frame,
                                   text=f"The correct answer was:\n{correct_answer}",
                                   font=("Arial", 20),
                                   fg="red"
                                   )
                    output.pack(pady = self.output_padding)

                    next_question = Button(self.output_frame,
                                           text="Next",
                                           font=("Arial", 15),
                                           command=lambda: self.update_question())
                    next_question.pack()
        except ValueError:
            #something went wrong so we don't count the attempt.
            output = Label(self.output_frame,
                           text="Enter a valid number! \nAttempt not counted.",
                           font=("Arial", 20),
                           fg="red")
            output.pack(pady = self.output_padding)










mathquiz = MathQuiz(root)

mathquiz.displayMenu()

root.mainloop()