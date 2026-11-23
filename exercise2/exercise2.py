from tkinter import *
import random

class alexaJoke:
    def __init__(self, root):
        self.root = root
        self.root.title("Alexa Joke")
        #track current joke and punchline
        self.current_joke_line = None
        #variable to check if joke and punchline have been displayed
        self.joke_displayed = False
        self.punchline_displayed = False
        #frame for buttons
        self.buttonFrame = Frame(self.root)
        self.buttonFrame.pack(pady=20)
        #create frame for jokes
        self.jokeFrame = Frame(self.root)
        self.jokeFrame.pack(pady=30)

        self.joke_b = Button(self.buttonFrame,
                        text="Play Alexa Joke",
                        command=lambda: self.display_joke(),
                        font=("Arial", 15)
                        )
        self.joke_b.grid(row=0, column=0, padx=10)

        self.punchL_b = Button(self.buttonFrame,text="Show Punchline",
                               command=lambda: self.display_punchline(self.current_punchline),
                               font=("Arial", 15),
                               state=DISABLED
        )
        self.punchL_b.grid(row=0, column=1, padx=10)

        self.next_joke_b = Button(self.buttonFrame,
                                  text="Next Joke",
                                  command=lambda: self.next_joke(),
                                  font=("Arial", 15),
                                  state=DISABLED)
        self.next_joke_b.grid(row=0, column=2, padx=10)

        self.quit_b = Button(self.buttonFrame,
                             text="Quit",
                             command=lambda: self.root.destroy(),
                             font=("Arial", 15)
                             )
        self.quit_b.grid(row=0, column=3, padx=10)

        #labels for the joke and punchline
        self.joke_l = Label(self.jokeFrame, text="", font=("Arial", 15))
        self.joke_l.grid(row=0, column=0)

        self.punch_l = Label(self.jokeFrame, text="", font=("Arial", 15))
        self.punch_l.grid(row=1, column=0)


    def display_joke(self):
        #check if joke has already been displayed, return if it has.
        if self.joke_displayed:
            return

        self.joke_displayed = True

        #get random joke
        joke, punchline = self.rand_joke()
        joke, punchline = joke.strip(), punchline.strip()

        #set our variables
        self.current_punchline = punchline
        self.joke_l.config(text=f"{joke}?")
        self.joke_b.config(state=DISABLED)

        self.punchL_b.config(state=NORMAL)
        self.next_joke_b.config(state=NORMAL)
        print(joke)
        print(punchline)

    def display_punchline(self, punchline):
        #check if punchline is already displayed
        if self.punchline_displayed:
            return

        self.punchline_displayed = True
        self.punch_l.config(text=punchline)
        self.punchL_b.config(state=DISABLED)

    def next_joke(self):
        #reset tracker
        self.joke_displayed = False
        self.punchline_displayed = False

        self.joke_l.config(text="")
        self.punch_l.config(text="")

        self.joke_b.config(state=NORMAL)
        self.punchL_b.config(state=DISABLED)
        self.next_joke_b.config(state=DISABLED)


    def rand_joke(self):
        #instead of just using readlines I wanted to use a for loop.
        print("reading a random joke")
        joke_line = None
        #open file
        #open with utf-8 encoding because there are some weird formatting bugs without it.
        with open("randomJokes.txt", encoding="utf-8") as f:
            #we use a loop here because we want to pick another joke if it is the same joke as the current one.
            while True:
                #pick a random line
                rand_line = random.randint(1, 37)
                #iterate until we get to the target line
                for current_line, line in enumerate(f, start=1):
                    #if it is our target line we strip the joke line
                    if current_line == rand_line:
                        #we check to make sure it is not the same joke as the current one...
                        if line.strip() != self.current_joke_line:
                            print("found new joke")
                            #we break the loop by giving joke_line a value and update our current joke line
                            joke = line.split("?")
                            self.current_joke_line = joke_line
                            return joke

root = Tk()
root.geometry("700x500")

alexajoke = alexaJoke(root)


root.mainloop()
