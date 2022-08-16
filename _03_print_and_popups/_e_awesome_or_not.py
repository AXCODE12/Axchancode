from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    so = Tk()
    # Hide the window using the window's .withdraw() method
    so.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    var = random.randint(0,3)
    # 2. Print your variable to the console
    print(var)
    # 3. Get the user to enter something that they think is awesome
    awe = simpledialog.askstring('q', 'Type something that is awesome')
    # 4. If your variable is  0
        # -- tell the user whatever they entered is awesome!
    if var == 0:
        messagebox.showinfo('feedback', 'Awesome')
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    if var == 1:
        messagebox.showinfo('feedback', 'ok')
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    if var == 2:
        messagebox.showinfo('feedback', 'boring')
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
    if var == 3:
        messagebox.showinfo('feedback', 'cool')
    # Run the window's .mainloop() method
    so.mainloop()