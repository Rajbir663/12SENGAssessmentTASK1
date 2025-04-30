from tkinter import* # imports alll symbols form the tkinter module in
import tkinter as tk
root = Tk()
import random
from tkinter import messagebox
from PIL import ImageTk, Image
root.title("Quick Times Challenge")
root.configure(background="darkblue") 

#Creating a difficulty state varibale 
difficulty = tk.StringVar(value="easy")

#Creating global variables for the quizz to keep on checking the user input and comparing with the answer.
question = ""
answer = 0
question_label = None
answer_entry = None
feedback_label = None
selected_label = None
content_frame = None

def create_home():
    #clearing all exisiting widgets 
    for widget in root.winfo_children():
        widget.destroy()
    Label(content_frame, text="Welcome To Quick Times Challenge", font=("Arial", 18), bg="darkblue", fg="white").pack(pady=50)

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

selection = StringVar()
def sel():
   difficulty_level = selection.get()


def start_quiz():
    global question_label, answer_entry, feedback_label

    for widget in root.winfo_children():
        widget.destroy()
    
    Button(root, text="Back", command=create_home).pack(anchor='nw', padx=10, pady=10)

    #Difficulty selection section
    difficulty_frame = LabelFrame(root, text="Select Difficulty", font=("Arial", 12), fg="white", bg="darkblue", bd=2, relief="groove", padx=10, pady=10, labelanchor="n")
    difficulty_frame.pack(pady=10)

    #Creating radio buttons for the difficulty selection
    Radiobutton(difficulty_frame, text="Easy", variable=difficulty, value="easy",  command=sel, state="active",
                bg='darkblue', fg='white', font=("Arial", 11)).pack(anchor='w')
    Radiobutton(difficulty_frame, text="Medium", variable=difficulty, value="medium", command=sel,
                bg='darkblue', fg='white', font=("Arial", 11)).pack(anchor='w')
    Radiobutton(difficulty_frame, text="Hard", variable=difficulty, value="hard", command=sel,
                bg='darkblue', fg='white',font=("Arial", 11)).pack(anchor='w')
    
    question_label = Label(root, text="", font=("Arial", 14), fg="white", bg="darkblue")
    question_label.pack(pady=10)

    answer_entry = Entry(root, font=("Arial", 14))
    answer_entry.pack()

    Button(root, text="Submit", command=check_answer).pack(pady=10)
    feedback_label = Label(root, text="", font=("Arial", 12), fg='yellow', bg='darkblue')
    feedback_label.pack()

    next_question()

def next_question():
    global question, answer

    max_table = 4 if difficulty.get() == 'easy' else 8 if difficulty.get() == 'medium' else 12 
    a = random.randint(1, max_table)
    b = random.randint(1, 12)
    answer = a * b
    question = f"What is {a} x {b}?"
    question_label.config(text=question)
    answer_entry.delete(0, END)
    feedback_label.config(text="")

def check_answer():
    user_input = answer_entry.get()
    if user_input.isdigit():  # Check if the input is a number
        user_answer = int(user_input)
        if user_answer == answer:
            feedback_label.config(text="Correct! 🎉")
        else:
            feedback_label.config(text=f"Wrong! The answer was {answer}.")
        root.after(1500, next_question)
    else:
        messagebox.showerror("Invalid Input", "Please enter a number.")

#start app
create_home()
root.mainloop() 