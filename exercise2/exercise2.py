from tkinter import *
import random

class alexaJoke:
    def __init__(self, root):
        self.root = root
        self.root.title("Alexa Joke")
        #track current joke and punchline
        self.current_joke = None
        self.current_punchline = None
        #variable to check if joke and punchline have been displayed
        self.joke_displayed = False
        self.punchline_displayed = False
        #frame for buttons
        self.buttonFrame = Frame(self.root)
        self.buttonFrame.pack(pady=20)
        #create frame for jokes
        self.jokeFrame = Frame(self.root)
        self.jokeFrame.pack(pady=30)

    def play_game(self):
        joke_b = Button(self.buttonFrame,
                        text="Play Alexa Joke",
                        command=lambda: self.display_joke(),
                        font=("Arial", 10)
                        )
        joke_b.grid(row=0, column=0)

        punchL_b = Button(self.buttonFrame,
                          text="Show Punchline",
                          command=lambda: self.display_punchline(self.current_punchline),
                          font=("Arial", 10)
        )
        punchL_b.grid(row=0, column=1)

        next_joke_b = Button(self.buttonFrame,
                             text="Next Joke",
                             command=lambda: self.next_joke(),
                             font=("Arial", 10)
                             )
        next_joke_b.grid(row=0, column=2)

    def display_joke(self):
        #check if joke has already been displayed, return if it has.
        if self.joke_displayed:
            return

        self.joke_displayed = True

        #get random joke
        joke, punchline = self.rand_joke()

        #set our variables
        self.current_joke = joke
        self.current_punchline = punchline
        joke_l = Label(self.jokeFrame, text=self.current_joke, font=("Arial", 15))
        joke_l.grid(row=0, column=0)
        print(joke)
        print(punchline)

    def display_punchline(self, punchline):
        #check if punchline is already displayed
        if self.punchline_displayed:
            return

        self.punchline_displayed = True
        punch_l = Label(self.jokeFrame, text=punchline, font=("Arial", 15))
        punch_l.grid(row=1, column=0)

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def next_joke(self):
        self.clear_frame(self.jokeFrame)
        self.joke_displayed = False
        self.punchline_displayed = False


    def rand_joke(self):
        print("reading a random joke")
        joke_line = None

        #open file
        with open("randomJokes.txt") as f:
            #pick a random line
            rand_line = random.randint(1, 37)
            #iterate until we get to the target line
            for current_line, line in enumerate(f, start=1):
                if current_line == rand_line:
                    joke_line = line.strip()
                    break


        joke = joke_line.split("?")
        return joke




root = Tk()
root.geometry("500x500")

alexajoke = alexaJoke(root)

alexajoke.play_game()

root.mainloop()
