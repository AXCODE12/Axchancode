from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    lol = Tk()
    # Hide the window using the window's .withdraw() method
    lol.withdraw()
    # 1. Ask the user if they know how to write code.
    us = simpledialog.askstring('Question','Do you know how to write code?')
    # 2. If they say "yes", tell them they will rule the world in a message box pop-up.
    if us == 'yes':
        messagebox.showinfo('Message','YOU WILL RULE THE WORLD!')
    # 3. Otherwise, tell them to sign up for classes at The League in an error box pop-up.
    else:
        messagebox.showinfo('Recommendation','sign up for classes at The League')
    # Run the window's .mainloop() method
    lol.mainloop()