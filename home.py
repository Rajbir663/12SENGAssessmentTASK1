from tkinter import* # imports alll symbols form the tkinter module in
import tkinter as tk
root = Tk()
import random
from tkinter import messagebox
from PIL import ImageTk, Image
root.geometry("400x400") # make the window 400 x 400 size 
# root.resizeable(False,False) # make the wind non-resizebale
root.title("Quick Times Challenge")
root.configure(background="darkblue") 

#Creating a difficulty state varibale 
difficulty = tk.StringVar(value="easy")

#Creating global variables for the quizz to keep on checking the user input and comparing with the answer.
question = ""
answer = 0

#Creating widgets for the quizz (also done golbally so they can be accessed later)
questio_label = None
answer_entry = None
feedback_label = None

def create_home():
    #clearing all exisiting widgets 
    for widget in root.winfo_children():
        widget.destroy()

    Label1 = Label(root,text="Hello and Welcome to Quick Times Challenge",
               font =("Arial", 18),
               bg ="lightblue",
               fg ="darkblue",
               padx = 20, # adds horizontal space to the left and right of a widget
               pady = 10, # adds vertical space to the top and bottom of the widget
               relief ="flat",
               borderwidth= 2) # creating a label widget wiht options
    Label1.pack() # shoving the label on to the screen
    Label2 = Label(root,text="Please chose your option from below",
               font =("Arial", 18),
               bg ="lightblue",
               fg ="darkblue",
               padx = 20, # adds horizontal space to the left and right of a widget
               pady = 10, # adds vertical space to the top and bottom of the widget
               relief ="flat",
               borderwidth= 2) # creating a label widget wiht options
    Label2.pack() # shoving the label on to the screen

    Button(root, text="Times Table Resource", width=20, height=10, bg="lightblue", fg="darkblue", font=("Arial", 14), command=show_resource).place(x=400, y=250)
    Button(root, text="Times Table Quiz", width=20, height=10, bg="lightblue", fg="darkblue", font=("Arial", 14)).place(x=900, y=250)

def show_resource():
    #show 1 to 15 times tables 
    for widget in root.winfo_children():
        widget.destroy()

    Button(root, text="BACK", command=create_home).pack(anchor='nw', padx=10, pady=10)
    Label(root, text="Times Tables from 1 to 12", font=("Arial",14), fg="white", bg="darkblue").pack(pady=10)

    tk.Label(text="Multiplication Chart", font=("Arial", 16, "bold"), bg="#00bfff", fg="white").pack(pady=10)
    res_img = ImageTk.PhotoImage(Image.open("resource.jpg"))
    chart_label = tk.Label(image=res_img, bg="#00bfff")
    chart_label.image = res_img  # Keep a reference to the image
    chart_label.pack()


#start app
create_home()
root.mainloop() 