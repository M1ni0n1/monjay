from tkinter import *
from time import *
# Create the main window
win = Tk()
#win geometry
win.geometry("400x200")


#window name
win.title("WinLocker :)")

# Create a Label widget
label = Label(win, text="it's a virus)")
label.pack()# Place the Label widget in the window


# Create the label
label = Label(win, text="Enter Winlocker Code:")
label.pack()

# Create the entry box
entry = Entry(win, show="*")
entry.pack()

# Create the submit button
submit = Button(win, text="Submit")
submit.pack()

# Create the wrong password message
wrong_password = Label(win, text="Wrong Password!")

# prevent window from closing
win.protocol("WM_DELETE_WINDOW", lambda: None)

# Function to check if the password is correct
def check_password():
    if entry.get() == "12":
        win.destroy()
    else:
        wrong_password.pack()

# Bind the submit button to the check_code function
submit.config(command=check_password)

# Run the main loop
win.mainloop()