import tkinter
import random
from tkinter import *
from traceback import clear_frames

root = Tk()
root.geometry("300x300")

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
        self.difficulty_frame.pack()

        self.problem_frame = Frame(self.root)
        self.problem_frame.pack()

        self.results_frame = Frame(self.root)
        self.results_frame.pack()

    def change_difficulty(self, difficulty):
        #set the difficulty here, print output for debugging
        #Also hides the difficulty frame
        self.chosen_difficulty.set(difficulty)
        self.difficulty_frame.forget()
        self.displayProblem()

        print(self.chosen_difficulty.get())

    def displayMenu(self):
        #create the menu for the difficulties
        l1 = Label(self.difficulty_frame, text="Choose your difficulty.")
        l1.pack()

        b_easy = Button(self.difficulty_frame, text="1. Easy", command=lambda: self.change_difficulty("easy"))
        b_easy.pack()

        b_medium = Button(self.difficulty_frame, text="2. Moderate", command=lambda: self.change_difficulty("moderate"))
        b_medium.pack()

        b_hard = Button(self.difficulty_frame, text="3. Advanced", command=lambda: self.change_difficulty("advanced"))
        b_hard.pack()

    def displayResults(self):
        #displays the results
        score_l = Label(self.results_frame, text=f"Score: {self.user_score}/{self.number_of_questions * 10}")
        score_l.pack()

    def displayProblem(self):
            #generate required values and operation
            num_a = self.randomInt()
            num_b = self.randomInt()
            operation = self.decideOperation()

            #create label, entry, and button
            question_l = Label(self.problem_frame,
                               text=f"Q{self.current_question}. {num_a} {operation} {num_b}",)
            question_l.pack()

            user_answer = Entry(self.problem_frame)
            user_answer.pack()

            #submit button runs isCorrect() function
            submit = Button(self.problem_frame,
                            text="Submit Answer",
                            command=lambda: self.isCorrect(user_answer.get(),num_a,num_b,operation))
            submit.pack()

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
        self.clearFrame(self.problem_frame)

        if self.current_question <= self.number_of_questions:
            #runs display problem again for a new question
            self.displayProblem()
        else:
            #hide problem frame
            self.problem_frame.forget()
            #go to results
            self.displayResults()

    def clearFrame(self, frame):
        #this clears the frame
        for widget in frame.winfo_children():
            widget.destroy()

    def isCorrect(self, answer, num_a, num_b, operation):
        #Try turning the answer into an int, if it has an error it means it wasn't an integer.
        try:
            answer = int(answer)
        except ValueError:
            print("Answer not a number")

        #Match operation string with the appropriate operation
        if ((operation == "+" and answer == num_a + num_b)or (operation == "-" and answer == num_a - num_b)
                and (self.attempt <= 2)):
            print("Correct")
            self.correct_answers += 1
            output = Label(self.problem_frame, text="Problem answered correctly!")
            output.pack()

            #award score based on attempt count
            if self.attempt == 1:
                self.user_score += 10
            else:
                self.user_score += 5

            next_question = Button(self.problem_frame,text="Next Question", command=lambda:self.update_question())
            next_question.pack()

        else:
            #if no matches it was wrong, return false.
            print("Incorrect answer")
            print(self.attempt)
            if self.attempt == 1:
                output = Label(self.problem_frame, text="Incorrect answer, last attempt.")
                output.pack()
                self.attempt += 1

            elif self.attempt == 2:
                self.attempt += 1
                #if its over 2 it doesn't do anything so the user has to go to the next question.

                output = Label(self.problem_frame, text="Wrong answer.")
                output.pack()

                next_question = Button(self.problem_frame, text="Next", command=lambda: self.update_question())
                next_question.pack()







mathquiz = MathQuiz(root)

mathquiz.displayMenu()

root.mainloop()