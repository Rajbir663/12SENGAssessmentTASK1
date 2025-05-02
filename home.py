from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import random
from tkinter import messagebox

root = Tk()
root.title("Quick Times Challenge")
root.configure(background="darkblue")

difficulty = tk.StringVar(value="easy")

# Global variables
question = ""
answer = 0
question_label = None
answer_entry = None
feedback_label = None
selected_label = None
content_frame = None

#creating home page
def create_home():
    for widget in content_frame.winfo_children():
        widget.destroy()

    Label(content_frame, text="Welcome to Quick Times Challenge", font=("Arial", 18), bg="darkblue", fg="white").pack(pady=50)

    # Load and place the background image
    bg_image = tk.PhotoImage(file="HOME_PAGE1.png")
    background_label = tk.Label(content_frame, image=bg_image)
    background_label.image = bg_image  # Keep a reference!
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

#creating the layout of the app page
def setup_layout():
    global content_frame

    # Sidebar
    sidebar = Frame(root, bg="lightblue", width=200)
    sidebar.pack(side=LEFT, fill=Y)

    tk.Label(sidebar, text="MENU", font=("Arial", 16, "bold"), bg="lightblue", fg="darkblue").pack(pady=20)

    Button(sidebar, text="Home", width=20, height=2, bg="lightblue", fg="darkblue", font=("Arial", 12), command=create_home).pack(pady=10)
    Button(sidebar, text="Times Table Resource", width=20, height=2, bg="lightblue", fg="darkblue", font=("Arial", 12), command=show_resource).pack(pady=10)
    Button(sidebar, text="Times Table Quiz", width=20, height=2, bg="lightblue", fg="darkblue", font=("Arial", 12), command=start_quiz).pack(pady=10)

    # Content Area
    content_frame = Frame(root, bg="darkblue")
    content_frame.pack(side=RIGHT, fill=BOTH, expand=True)

    create_home()

#showing the resource image 
def show_resource():
    for widget in content_frame.winfo_children():
        widget.destroy()

    Label(content_frame, text="Times Tables from 1 to 12", font=("Arial", 14), fg="white", bg="darkblue").pack(pady=10)
    try:
        res_img = tk.PhotoImage(file="resource2.png")
        chart_label = tk.Label(content_frame, image=res_img, bg="#00bfff")
        chart_label.image = res_img
        chart_label.pack()
    except Exception as e:
        Label(content_frame, text="Resource image not found.", font=("Arial", 14), bg="darkblue", fg="red").pack(pady=10)

def update_selected_label():
    selected_label.config(text=f"Difficulty: {difficulty.get().capitalize()}")

#starting the quiz and creating the quiz page 
def start_quiz():
    global question_label, answer_entry, feedback_label, selected_label

    for widget in content_frame.winfo_children():
        widget.destroy()

    difficulty_frame = LabelFrame(content_frame, text="Select Difficulty", font=("Arial", 12), fg="white", bg="darkblue", bd=2, relief="groove", padx=10, pady=10, labelanchor="n")
    difficulty_frame.pack(pady=10, fill=X, padx=20)

    difficulty_buttons_frame = Frame(difficulty_frame, bg="darkblue")
    difficulty_buttons_frame.pack(side=LEFT)

    Radiobutton(difficulty_buttons_frame, text="Easy", variable=difficulty, value="easy", command=update_selected_label,
                bg='darkblue', fg='white', font=("Arial", 11)).pack(anchor='w')
    Radiobutton(difficulty_buttons_frame, text="Medium", variable=difficulty, value="medium", command=update_selected_label,
                bg='darkblue', fg='white', font=("Arial", 11)).pack(anchor='w')
    Radiobutton(difficulty_buttons_frame, text="Hard", variable=difficulty, value="hard", command=update_selected_label,
                bg='darkblue', fg='white', font=("Arial", 11)).pack(anchor='w')

    selected_label = Label(difficulty_frame, text=f"Difficulty: {difficulty.get().capitalize()}", font=("Arial", 12),
                            fg="yellow", bg="darkblue")
    selected_label.pack(side=RIGHT, padx=20)

    question_label = Label(content_frame, text="", font=("Arial", 14), fg="white", bg="darkblue")
    question_label.pack(pady=10)

    answer_entry = Entry(content_frame, font=("Arial", 14))
    answer_entry.pack()

    Button(content_frame, text="Submit", command=check_answer).pack(pady=10)

    feedback_label = Label(content_frame, text="", font=("Arial", 12), fg='yellow', bg='darkblue')
    feedback_label.pack()

    next_question()

#creating the questions for the quiz to display and creating the feedback label
def next_question():
    global question, answer

    max_table = 4 if difficulty.get() == 'easy' else 8 if difficulty.get() == 'medium' else 12
    a = random.randint(1, max_table)
    b = random.randint(1, max_table)
    answer = a * b
    question = f"What is {a} x {b}?"
    question_label.config(text=question)
    answer_entry.delete(0, END)
    feedback_label.config(text="")

def check_answer():
    user_input = answer_entry.get()
    if user_input.isdigit():
        user_answer = int(user_input)
        if user_answer == answer:
            feedback_label.config(text="Correct! 🎉")
        else:
            feedback_label.config(text=f"Wrong! The answer was {answer}.")
        root.after(1500, next_question)
    else:
        messagebox.showerror("Invalid Input", "Please enter a number.")

# Run the setup
setup_layout()
root.mainloop()