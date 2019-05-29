from tkinter import *



# prints a message on the output messagebox
def PrintMessage(message):

    TextBox.config(state=NORMAL)
    TextBox.insert(END, message + "\n\n")
    TextBox.config(state=DISABLED)


# gets the input and stores it in a variable
def GetInput():
     message = userinput.get()
     Inputbox.delete(0,'end')








# creates and sets up the window
root = Tk()
root.geometry("320x500")
root.title("Chatroom")
root.resizable(width=False, height=False)




# Sets the photo as the background and the title
picture = PhotoImage(file=r"C:\Users\333589885\Desktop\dribbble.png")
background = Label(image=picture).place(x=0,y=0)
Title = Label(root, font= "Times",bg = "lightgreen",  text= "Welcome To The Chatroom",).place(y=8,x=65)

# Creates the scrollbar
TextScroll = Scrollbar(root)
TextScroll.pack(fill=BOTH,side=RIGHT)

# Creates the output message box
TextBox = Text(root,yscrollcommand=TextScroll.set,wrap=WORD,height=25,width=36,highlightbackground="darkorange",highlightcolor="darkorange",highlightthickness=3,state=DISABLED)
TextBox.place(x=2,y=35)

# Creates an inputbox
userinput = StringVar()
Inputbox = Entry(root, width=33, textvariable=userinput)
Inputbox.place(x=3,y=455)


# Creates the sendbutton
Sendbutton = Button(root,relief=GROOVE,text= "Send", bg = "darkorange", fg= "white",height=2, width=10, activebackground="orange",command=GetInput).place(x=210,y=450)












root.mainloop()

