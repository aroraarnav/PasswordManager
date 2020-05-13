#PASSWORD MANAGER APPLICATION BY ARNAV ARORA

from tkinter import *
from tkinter import messagebox

secret_file = "/Users/arnavarora/Desktop/Py Projects/Password Manager/PasswordManager/secret.txt"
no_password = "ysahjvsdvhdvsadbvh" # Random Verification Code

root = Tk()

# Define Background Image


def createImage():
    background_image = PhotoImage(file = "") # Image Path Here
    background_label = Label(root, image = background_image)
    background_label.place (relwidth = 1, relheight = 1)


def mainFunc ():
    # Main Window
    root.destroy()
    root2 = Tk()
    canvas2 = Canvas (root2, height = 600, width = 600)
    canvas2.pack()

    root2.mainloop()

def askForPassword ():
    # Ask for password window
    root.destroy()
    root3 = Tk()
    canvas3 = Canvas (root3, height = 400, width = 450)
    canvas3.pack()

    # Main Frame And Label
    frame = Frame(root3, bg = '#80c1ff', bd = 10)
    frame.place(relwidth = 0.75, relheight = 0.2, relx = 0.5, rely = 0.1, anchor = 'n')

    label = Label(frame, text = "Please Enter Master\nPassword To Continue", font = ('Courier', 18))
    label.place(relwidth = 1, relheight = 1)

    # Password Frame and Label
    frame2 = Frame(root3, bg = '#80c1ff', bd = 10)
    frame2.place(relwidth = 0.75, relheight = 0.35, relx = 0.5, rely = 0.5, anchor = 'n')

    # Submit Button
    button = Button(frame2, text = "Submit", font = ("Courier", 18), command = lambda: checkPass(entry.get()))
    button.place(relheight = 0.3, relwidth = 0.6, rely = 0.6, relx = 0.2)

    entry = Entry(frame2, font = ('Courier', 18))
    entry.place(relwidth = 1, relheight = 0.4)
    entry.config(show = "*")

    def checkPass (enteredPasscode):
            with open (secret_file, 'r') as passfile:
                passcode = passfile.readline()  

                if passcode != enteredPasscode:
                    messagebox.showerror("Notice", "Your passcode is incorrect, please try again.")
                else:
                    print ("This worked")



    root3.mainloop()

def submitPasscode(passcode):
    # Perform password security checks
    if len(passcode) <= 8:
        messagebox.showerror("Notice", "For security reasons, make sure your password is at least 8 characters long!")
    else:
        # Try to write to the local file
        open(secret_file, 'w').close()

        with open(secret_file, 'w') as passFile:
            passFile.write(passcode)
        root.destroy()
        mainFunc ()
          
def isLoggedIn ():
    # Main root object
    

    # Define the canvas
    canvas = Canvas(root, height = 500, width = 600)
    canvas.pack()   

    lower_frame = Frame(root, bg = '#80c1ff', bd = 10)
    lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = "n")

    # Define Credit Label
    creditLabel = Label(lower_frame, text = "By Arnav Arora", font = ('Courier', 18), bg = '#80c1ff')
    creditLabel.place(relx = 0.8, rely = 0.95, anchor = "n", relwidth = 1.35)

    pleaseLabel = Label(lower_frame, text = "Please create a master\npassword below:", bg = '#80c1ff', font = ('Courier', 22), anchor = 'nw', justify = 'left', bd = 5)
    pleaseLabel.place (relwidth = 1, relheight = 0.2)

    # Define Text Entry
    entry = Entry(lower_frame, font = ("Courier" , 18))
    entry.place(relheight = 0.15, relwidth = 0.8, rely = 0.4, relx = 0.11)
    entry.config(show = "*")

    # Main Frame and Main Label
    frame = Frame(root, bg = '#80c1ff', bd = 10)
    frame.place(relwidth = 0.75, relheight = 0.1, relx = 0.5, rely = 0.1, anchor = 'n')

    label = Label(frame, text = "Welcome To The Password Manager", font = ('Courier', 18))
    label.place(relwidth = 1, relheight = 1)

    createImage()

    # Define Submit Button
    button = Button(lower_frame, text = "Submit", font = ("Courier", 18), command = lambda: submitPasscode(entry.get()))
    button.place (relheight = 0.12, relwidth = 0.5, rely = 0.7, relx = 0.26)

    

    root.mainloop()

    

with open(secret_file, 'r') as passFile:
    password = passFile.readline()

    if password == no_password:
        isLoggedIn()
    else:
        askForPassword()
