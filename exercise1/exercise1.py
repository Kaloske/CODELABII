import tkinter
import random
from tkinter import *

class MathQuiz:
    def __init__(self, root):
        self.root = root

        #set up initial variables
        self.chosen_difficulty = tkinter.StringVar()
        self.number_of_questions = 10
        self.current_question = 0
        self.correct_answers = 0
        self.user_score = 0
        self.attempt = 1

        #create frames
        self.difficulty_frame = Frame(self.root)
        self.problem_frame = Frame(self.root)
        self.output_frame = Frame(self.problem_frame)
        self.output_frame.pack(side="bottom")
        self.results_frame = Frame(self.root)
        self.active_frame = self.difficulty_frame

        #create difficulty frame widgets
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

        #create problem frame widgets
        self.question_l = Label(self.problem_frame,
                           text=f"",
                           font=("Arial", 20)
                           )
        self.question_l.pack()

        self.user_answer = Entry(self.problem_frame,
                            font=("Arial", 15)
                            )
        self.user_answer.pack()

        # submit button runs isCorrect() function
        self.submit = Button(self.problem_frame,
                        text="Submit Answer",
                        font=("Arial", 15),
                        command=lambda: self.isCorrect(self.user_answer.get(), num_a=0, num_b=0, operation="+")
                        )
        self.submit.pack(pady=10)

        self.output = Label(self.output_frame, text="",
                       font=("Arial", 20),
                       fg="green")
        self.output.pack(pady=15)

        self.next_question = Button(self.output_frame,
                               text="Next",
                               font=("Arial", 15),
                               command= self.update_question,
                               state=DISABLED)
        self.next_question.pack(pady=15)

        ##create results frame widgets
        self.score_l = Label(self.results_frame,
                        text=f"",
                        font=("Arial", 20)
                        )
        self.score_l.pack()

        self.correct_q_l = Label(self.results_frame,
                            text=f"",
                            font=("Arial", 20)
                            )
        self.correct_q_l.pack()

        self.grade_l = Label(self.results_frame,
                        text=f"",
                        font=("Arial", 20)
                        )
        self.grade_l.pack()

        self.restart = Button(self.results_frame,
                         text="Play Again?",
                         command=lambda: self.start_quiz(),
                         font=("Arial", 15)
                         )
        self.restart.pack()

    def change_difficulty(self, difficulty):
        #set the difficulty here, print output for debugging
        #Also switches frame
        self.chosen_difficulty.set(difficulty)
        self.displayProblem()

        print(self.chosen_difficulty.get())

    def switch_frame(self, frame):
        self.active_frame.forget()
        self.active_frame = frame
        frame.pack()

    def displayMenu(self):
        #Switch the menu for the difficulty buttons
        self.switch_frame(self.difficulty_frame)

    def displayResults(self):
        #Switch the frame
        self.switch_frame(self.results_frame)
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
        self.score_l.config(text=f"Score: {self.user_score}/{self.number_of_questions * 10}")

        self.correct_q_l.config(text=f"Correct Answers: {self.correct_answers}/{self.number_of_questions}")

        self.grade_l.config(text=f"Grade: {grade}")

        self.restart.config(text="Play Again?")

    def displayProblem(self):
            #Switch frame to the problem frame
            self.switch_frame(self.problem_frame)
            #we remove output text
            self.user_answer.delete(0, END)
            self.output.config(text="")
            #generate required values and operation
            num_a = self.randomInt()
            num_b = self.randomInt()
            operation = self.decideOperation()

            #Configure label, entry, and button
            self.question_l.config(text=f"Q{self.current_question}: {num_a} {operation} {num_b}")

            #submit button runs isCorrect() function with the proper arguments
            self.submit.config(command=lambda:self.isCorrect(self.user_answer.get(),num_a,num_b,operation))


    def start_quiz(self):
        #reset counters for questions
        self.current_question = 1
        self.correct_answers = 0
        #hide results screen and re show menu

        self.switch_frame(self.difficulty_frame)

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
        #Increment the question counter and reset the attempt counter.
        self.current_question += 1
        self.attempt = 1
        print(f"current question: {self.current_question}")

        if self.current_question <= self.number_of_questions:
            # runs display problem again for a new question
            self.displayProblem()
            self.output.config(text="")
            self.next_question.config(state=DISABLED)

        elif self.current_question > self.number_of_questions:
            #hide problem_frame
            self.displayResults()

    def isCorrect(self, answer, num_a, num_b, operation):
        # return early if there are no more attempts, no need to run the rest of the code in this case.
        if self.attempt > 2:
            return

        #Try turning the answer into an int, if it has an error it means it wasn't an integer.
        try:
            answer = int(answer)
            # Match operation string with the appropriate operation

            #initialize variable for now
            correct_answer = None

            #calculate the correct answer given the operation as a character.
            match operation:
                case "+":
                    correct_answer = num_a + num_b
                case "-":
                    correct_answer = num_a - num_b

            if answer == correct_answer and self.attempt <= 2:
                #increment correct answer
                self.correct_answers += 1

                #display output
                self.output.config(text="Problem answered correctly!", fg="green")

                # award score based on attempt count
                if self.attempt == 1:
                    self.user_score += 10
                else:
                    self.user_score += 5

                self.next_question.config(state=NORMAL)
            else:
                # if no matches it was wrong, return false.
                print("Incorrect answer")
                print(self.attempt)
                if self.attempt == 1:
                    self.output.config(text="Incorrect answer! \nLast attempt.", fg="red")
                    self.attempt += 1

                elif self.attempt == 2:
                    self.attempt += 1
                    # if its over 2 it doesn't do anything so the user has to go to the next question.
                    self.output.config(text=f"The correct answer was:\n{correct_answer}", fg="red")

                    self.next_question.config(state=NORMAL)
        except ValueError:
            #something went wrong so we don't count the attempt.
            self.output.config(text="Enter a valid number! \nAttempt not counted.", fg="red")

root = Tk()
root.title("Math Quiz")
root.geometry("400x300")
mathquiz = MathQuiz(root)
mathquiz.start_quiz()

root.mainloop()