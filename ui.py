THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

"""imported every class from the tkinter module"""
from tkinter import *

"""created QuizInterface class"""
class QuizInterface:

    def __init__(self):

        # window

        """created the window object"""
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # label

        """created the labelScore object"""
        self.labelScore = Label(text=f"Score: {0}", fg="white", bg=THEME_COLOR, font=("Arial", 15, "normal"))
        self.labelScore.grid(row=1, column=2)


        # canvas

        """created the canvas object"""
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.questionText = self.canvas.create_text(150, 125, text="Hello", font=FONT, fill=THEME_COLOR)
        self.canvas.grid(row=2, column=1, columnspan=2, pady=50)

        # button

        """created the buttonTrue object"""
        self.trueImg = PhotoImage(file="images/true.png")
        self.buttonTrue = Button(image=self.trueImg, highlightthickness=0, bd=0)
        self.buttonTrue.grid(row=3, column=1)

        """created the buttonFalse object"""
        self.falseImg = PhotoImage(file="images/false.png")
        self.buttonFalse = Button(image=self.falseImg, highlightthickness=0, bd=0)
        self.buttonFalse.grid(row=3, column=2)

        """loop to keep the window open"""
        self.window.mainloop()