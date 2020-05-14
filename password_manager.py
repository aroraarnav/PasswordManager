# PASSWORD MANAGER APPLICATION BY ARNAV ARORA
# CUSTOMISABLE GUI, MADE WITH TKINTER

from tkinter import *
from tkinter import messagebox

didComeFirstTime = True 
password_file = "/Users/arnavarora/Desktop/Py Projects/Password Manager/PasswordManager/passwords.txt" # Passwords file Path Here
secret_file = "/Users/arnavarora/Desktop/Py Projects/Password Manager/PasswordManager/secret.txt" # Secret file path here
no_password = "ysahjvsdvhdvsadbvh" # Random Verification Code, Make sure user won't enter this as passcode.

# Initialising only the main View
root = Tk() 
root.title("Create A Master Password")
root2 = None
root3 = None

def mainFunc ():

    def setPasswords (service, password):
        if service.strip() == "" or password.strip() == "":
            messagebox.showerror("Notice", "Please fill in all fields and try again.")
        else:
            with open (password_file, 'a') as passFile:
                passFile.write("\nYour password for " + "'" + service + "'" + " is " + "'" + password + "'")
        
        messagebox.showinfo("Success!", "Your password has been added and saved! You can now retrieve it whenever you want.")


    def retrievePasswords ():
        with open (password_file, 'r') as passFile:

            passwords = passFile.readlines()
            if passwords == [] or passwords == [""]:
                messagebox.showerror('Notice', "You haven't saved any passwords yet. Save some passwords to view them.")
            else:
                messagebox.showinfo("Your Passwords", "\n".join(passwords))

    # Main Window
    if didComeFirstTime == False:
        root3.destroy()

    global root2 
    root2 = Tk()
    root2.title("Welcome to Password Manager")
    canvas2 = Canvas (root2, height = 500, width = 500)
    canvas2.pack()

    # Design for Main Screen

    frame = Frame(root2, bg = '#80c1ff', bd = 10)
    frame.place(relwidth = 0.75, relheight = 0.2, relx = 0.5, rely = 0.1, anchor = 'n')

    label = Label(frame, text = "Welcome To The Password Manager!", font = ('Courier', 18))
    label.place(relwidth = 1, relheight = 1)

    lower_frame = Frame(root2, bg = '#80c1ff', bd = 10)
    lower_frame.place(relx = 0.5, rely = 0.35, relwidth = 0.75, relheight = 0.6, anchor = "n")

    creditLabel = Label(lower_frame, text = "By Arnav Arora", font = ('Courier', 18), bg = '#80c1ff')
    creditLabel.place(relx = 0.8, rely = 0.95, anchor = "n", relwidth = 1.35)

    serviceLabel = Label(lower_frame, text = "Name of Service:", font = ("Courier", 18), bg = '#80c1ff')
    serviceLabel.place(rely = 0.05, relwidth = 1)

    serviceEntry = Entry(lower_frame, font = ('Courier', 16))
    serviceEntry.place(rely = 0.15, relwidth = 0.7, relx = 0.15, relheight = 0.12)

    passLabel = Label(lower_frame, text = "Password:", font = ("Courier", 18), bg = '#80c1ff')
    passLabel.place(rely = 0.32, relwidth = 1)

    passEntry = Entry(lower_frame, font = ('Courier', 16))
    passEntry.place(rely = 0.42, relwidth = 0.7, relx = 0.15, relheight = 0.12)

    addButton = Button(lower_frame, font = ("Courier", 16), text = "Add Password", command = lambda: setPasswords(serviceEntry.get(), passEntry.get()))
    addButton.place(rely = 0.6, relwidth = 0.7, relx = 0.15, relheight = 0.1)

    retrieveButton = Button(lower_frame, font = ("Courier", 16), text = "Retrieve Passwords", command = lambda: retrievePasswords())
    retrieveButton.place(rely = 0.75, relwidth = 0.7, relx = 0.15, relheight = 0.1)

    root2.mainloop()

def askForPassword ():
    # Ask for password window
    root.destroy()
    global root3
    root3 = Tk()
    root3.title("Log In With Master Password")
    canvas3 = Canvas (root3, height = 400, width = 450)
    canvas3.pack()

    # Main Frame And Label
    frame = Frame(root3, bg = '#80c1ff', bd = 10)
    frame.place(relwidth = 0.75, relheight = 0.2, relx = 0.5, rely = 0.1, anchor = 'n')

    label = Label(frame, text = "Please Enter Master\nPassword To Login & Proceed.", font = ('Courier', 18))
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
                    mainFunc()

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

    # Define Submit Button
    button = Button(lower_frame, text = "Submit", font = ("Courier", 18), command = lambda: submitPasscode(entry.get()))
    button.place (relheight = 0.12, relwidth = 0.5, rely = 0.7, relx = 0.26)

    root.mainloop()

with open(secret_file, 'r') as passFile:
    password = passFile.readline()

    if password == no_password:
        isLoggedIn()
    else:
        didComeFirstTime = False
        askForPassword()