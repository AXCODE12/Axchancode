from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block 
if __name__ == '__main__':
    
    # Make a new window variable, window = Tk()
    win = Tk()
    # Hide the window using the window's .withdraw() method
    win.withdraw()
    # Ask the user for their name and save it to a variable
    # name = simpledialog.askstring(title='Greeter', prompt="What is your name?")
    alex = simpledialog.askstring(title='Greeter', prompt="What is your name?")
    # Show a message box with your message using the .showinfo() method
    messagebox.showinfo('info', 'Your name is?' + alex)
    # Print your message to the console using the print() function
    print('hello')
    # Show an error message using messagebox.showerror()
    messagebox.showerror()
    # Run the window's .mainloop() method
    win.mainloop()
    pass
