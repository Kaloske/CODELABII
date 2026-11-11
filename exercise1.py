import tkinter
import random
from tkinter import *

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

        #create frames
        self.difficulty_frame = Frame(self.root)
        self.difficulty_frame.pack()
        self.problem_frame = Frame(self.root)
        self.problem_frame.pack()

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

    def displayProblem(self):
            current_attempt = 1
            num_a = self.randomInt()
            num_b = self.randomInt()
            operation = self.decideOperation()

            question_l = Label(self.problem_frame,
                               text=f"Q{self.current_question}. {num_a} {operation} {num_b}",)
            question_l.pack()

            user_answer = Entry(self.problem_frame)
            user_answer.pack()

            submit = Button(self.problem_frame,
                            text="Submit Answer",
                            command=lambda: self.isCorrect(user_answer.get(),num_a,num_b,operation))
            submit.pack()


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

    def isCorrect(self, answer, num_a, num_b, operation):
        #Try turning the answer into an int, if it has an error it means it wasn't an integer.
        try:
            answer = int(answer)
        except ValueError:
            print("Answer not a number")

        #Match operation string with the appropriate operation
        match operation:
            case "+":
                if answer == num_a + num_b:
                    print("Correct")
                    output = Label(self.problem_frame, text="Addition problem answered correctly!")
                    output.pack()
            case "-":
                if answer == num_a - num_b:
                    print("Correct")
                    output = Label(self.problem_frame, text="Subtraction problem answered correctly!")
                    output.pack()
            case _:
                #if no matches it was wrong, return false.
                print("Incorrect answer")



mathquiz = MathQuiz(root)

mathquiz.displayMenu()

root.mainloop()