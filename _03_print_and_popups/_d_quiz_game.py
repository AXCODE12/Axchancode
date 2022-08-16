from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    bro = Tk()
    # Hide the window using the window's .withdraw() method
    bro.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    an = simpledialog.askinteger('question', 'What is 5*2?')
    #      // 3.  Use an if statement to check if their answer is correct
    if an == 10:
    #      // 4.  if the user's answer was correct, add one to their score 
        score +=1
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    bl = simpledialog.askinteger('question', 'What is 2+2?')
    if bl == 4:
        score +=1
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    score = str(score)
    print(score)
    # Run the window's .mainloop() method
    bro.mainloop()