from tkinter import *
import random

class alexaJoke:
    def __init__(self, root):
        self.root = root
        self.root.title("Alexa Joke")
        #track current joke and punchline
        self.current_joke_line = None
        self.current_punchline = None

        #frame for buttons
        self.buttonFrame = Frame(self.root)
        self.buttonFrame.pack(pady=20)
        #create frame for jokes
        self.jokeFrame = Frame(self.root)
        self.jokeFrame.pack(pady=30)

        #Create buttons for the button frame
        self.joke_b = Button(self.buttonFrame,
                        text="Play Alexa Joke",
                        command=self.display_joke,
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
                                  command=self.next_joke,
                                  font=("Arial", 15),
                                  state=DISABLED)
        self.next_joke_b.grid(row=0, column=2, padx=10)

        quit_b = Button(self.buttonFrame,
                             text="Quit",
                             command=self.root.destroy,
                             font=("Arial", 15)
                             )
        quit_b.grid(row=0, column=3, padx=10)

        #Create labels for the joke and punchline
        self.joke_l = Label(self.jokeFrame, text="", font=("Arial", 15))
        self.joke_l.grid(row=0, column=0)

        self.punch_l = Label(self.jokeFrame, text="", font=("Arial", 15))
        self.punch_l.grid(row=1, column=0)


    def display_joke(self):
        #get random joke
        joke, punchline = self.rand_joke()
        #Strip any unwanted characters here
        joke, punchline = joke.strip(), punchline.strip()

        #set our punchline for the joke as a variable
        self.current_punchline = punchline
        #Configure the buttons here
        self.joke_l.config(text=f"{joke}?")
        self.joke_b.config(state=DISABLED)

        self.punchL_b.config(state=NORMAL)
        self.next_joke_b.config(state=NORMAL)

    def display_punchline(self, punchline):
        #Show the punchline, we also disable the punchline button.
        self.punch_l.config(text=punchline)
        self.punchL_b.config(state=DISABLED)

    def next_joke(self):
        #reset the labels
        self.joke_l.config(text="")
        self.punch_l.config(text="")
        #Reset the button states
        self.joke_b.config(state=NORMAL)
        self.punchL_b.config(state=DISABLED)
        self.next_joke_b.config(state=DISABLED)

    def get_total_jokes(self):
        #simple function to iterate and count the number of jokes.
        with open("randomJokes.txt", "r") as f:
            total_jokes = 0
            for i, line in enumerate(f, start=1):
                total_jokes += 1
            return total_jokes

    def rand_joke(self):
        #instead of just using .readlines() I wanted to use a for loop.
        total_jokes = self.get_total_jokes()
        index = total_jokes
        #open with utf-8 encoding because there are some weird formatting bugs without it.
        with open("randomJokes.txt", encoding="utf-8") as f:
            #pick a random line
            rand_line = random.randint(1, total_jokes)
            previous_line = None
            #iterate until we get to the target line
            for current_line, line in enumerate(f, start=1):
                #First we store the previous line, so if it isn't our target line we assign it.
                if current_line != rand_line or not previous_line:
                    previous_line = line

                #we check if its the same as the line we've randomly chosen
                if current_line == rand_line:
                    #if its the same joke we change it
                    if self.current_joke_line == line.strip():
                        #if we are at the very end of the line we pick the previous joke
                        if current_line == total_jokes:
                            self.current_joke_line = previous_line.strip()
                            return previous_line.split("?")
                        else:
                            #if we arent at the end of the line we just add one to rand_line so we go to the next line
                            rand_line += 1
                            #continue loop to the nextl ine
                            continue
                    else:
                        #if the line isn't the same as the current joke we can select it
                        joke = line.split("?")
                        self.current_joke_line = line.strip()
                        return joke

root = Tk()
root.geometry("700x500")

alexajoke = alexaJoke(root)


root.mainloop()
