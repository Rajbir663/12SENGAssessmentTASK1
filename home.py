from tkinter import* # imports alll symbols form the tkinter module in
import tkinter as tk
root = Tk()
root.geometry("400x400") # make the window 400 x 400 size 
# root.resizeable(False,False) # make the wind non-resizebale
root.title("Quick Times Challenge")
root.configure(background="darkblue") 

Label1 = Label(root,text="Hello and Welcome to Quick Times Challenge",
               font =("Arial", 18),
               bg ="lightblue",
               fg ="darkblue",
               padx = 20, # adds horizontal space to the left and right of a widget
               pady = 10, # adds vertical space to the top and bottom of the widget
               relief ="flat",
               borderwidth= 2) # creating a label widget wiht options
Label1.pack() # shoving the label on to the screen
Label1 = Label(root,text="Please chose your option from below",
               font =("Arial", 18),
               bg ="lightblue",
               fg ="darkblue",
               padx = 20, # adds horizontal space to the left and right of a widget
               pady = 10, # adds vertical space to the top and bottom of the widget
               relief ="flat",
               borderwidth= 2) # creating a label widget wiht options
Label1.pack() # shoving the label on to the screen

button1 = Button(root,text="Times Table Resource", width=20, height=10, bg="lightblue", fg="darkblue")
button1.place(x=500, y=250)

button2 = Button(root,text="Times Table Quiz", width=20, height=10, bg="lightblue", fg="darkblue")
button2.place(x=890, y=250)


root.mainloop() 