from tkinter import *

class chatroom:
    def __init__(self):
        # creates and sets up the window
        self.root = Tk()
        self.root.geometry("320x500")
        self.root.title("Chatroom")
        self.root.resizable(width=False, height=False)

        # Sets the photo as the background and the title
        picture = PhotoImage(file=r"C:\Users\333589885\Desktop\dribbble.png")
        self.background = Label(image=picture).place(x=0, y=0)
        self.Title = Label(self.root, font="arial", bg="lightgreen", text="Welcome To The Chatroom", ).place(y=8, x=65)

        # Creates the scrollbar
        self.TextScroll = Scrollbar(self.root)
        self.TextScroll.pack(fill=BOTH, side=RIGHT)

        # Creates the output message box
        self.TextBox = Text(self.root, yscrollcommand=self.TextScroll.set, wrap=WORD, height=25, width=36,
                       highlightbackground="darkorange", highlightcolor="darkorange", highlightthickness=3,
                       state=DISABLED)
        self.TextBox.place(x=2, y=35)

        # Creates an inputbox
        self.userinput = StringVar()
        self.Inputbox = Entry(self.root, width=33, textvariable=self.userinput)
        self.Inputbox.place(x=3, y=455)

        # Creates the sendbutton
        Sendbutton = Button(self.root, relief=GROOVE, text="Send", bg="darkorange", fg="white", height=2, width=10,
                            activebackground="orange", command=self.GetInput).place(x=210, y=450)

        self.root.mainloop()


     # prints a message on the output messagebox
    def PrintMessage(self,message):
         message = "Oi"
         self.TextBox.config(state=NORMAL)
         self.TextBox.insert(END, message + "\n\n")
         self.TextBox.config(state=DISABLED)


     # gets the input and stores it in a variable
    def GetInput(self):
         message = self.userinput.get()
         self.Inputbox.delete(0, 'end')
         self.PrintMessage(message)



room = chatroom()

