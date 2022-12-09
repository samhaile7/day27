import tkinter

window = tkinter.Tk()

#Title of window
window.title('My First GUI Program')

# Minimum size of window
window.minsize(width= 500, height= 300)

# This creates a Label
my_label = tkinter.Label(text="This is a Label", font=("Arial", 24, "bold"))
#this displays and centers it
my_label.pack(expand=True)













# Method that keeps window open
window.mainloop()