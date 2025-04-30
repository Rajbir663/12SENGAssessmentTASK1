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
    for widget in content_frame.winfo_children():
        widget.destroy()
    Label(content_frame, text="Welcome To Quick Times Challenge", font=("Arial", 18), bg="darkblue", fg="white").pack(pady=50)

def steup_layout():
    global content_frame

    #Creating the sidebar
    sidebar = Frame(root, bg="lightblue", width=200)
    sidebar.pack(side=LEFT, fill=Y)

    tk.Label(sidebar, text="MENU", font=("Arial", 16, "bold"), bg="lightblue", fg="darkblue").pack(pady=20)

    Button(sidebar, text="HOME", width=20, height=2, bg="lightblue", fg="darkblue", font=("Arial", 12), command=create_home).pack(pady=10)
    Button(sidebar, text="Times Table Resource", width=20, height=2, bg="lightblue", fg="lightblue", font=("Arial", 12), command=show_resource).pack(pady=10)
    Button(sidebar, text="Times Table Quiz", width=20, height=2, bg="lightblue", fg="darkblue", font=("Arial", 16), command=start_quiz)

    #Creating content area
    content_frame = Frame(root, bg="darkblue")
    content_frame.pack(side=RIGHT, fill=BOTH, expand=TRUE)

    create_home()

def show_resource():
    #show 1 to 15 times tables 
    for widget in content_frame.winfo_children():
        widget.destroy()
    Label(content_frame, text="Times Tables from 1 to 12", font=("Arial", 14), fg="white", bg="darkblue").pack(pady=10)

    Label(content_frame, text="Multiplication Chart", font=("Arial", 16, "bold"), bg="#00bfff", fg="white").pack(pady=10)

    try:
        res_img = ImageTk.PhotoImage(Image.open("resource.jpg"))
        chart_label = tk.Label(content_frame, image=res_img, bg="#00bfff")
        chart_label.image = res_img
        chart_label.pack()
    except Exception as e:
        Label(content_frame, text="Resource image not found.", font=("Arial", 14), bg="darkblue", fg="red").pack(pady=10)

def update_selected_label():
    selected_label.config(text=f"Difficulty: {difficulty.get().capitalize()}")

def start_quiz():
    global question_label, answer_entry, feedback_label

    for widget in content_frame.winfo_children():
        widget.destroy()
    
    #creating a frame for the difficulty selection part
    difficulty_frame = LabelFrame(content_frame, text="Select Difficulty", font=("Arial", 12), fg="white", bg="darkblue", bd=2, relief="groove", padx=10, pady=10, labelanchor="n")
    difficulty_frame.pack(pady=10, fill=X, padx=20)

    #Difficulty selection section
    difficulty_frame = LabelFrame(root, text="Select Difficulty", font=("Arial", 12), fg="white", bg="darkblue", bd=2, relief="groove", padx=10, pady=10, labelanchor="n")
    difficulty_frame.pack(pady=10)

    #positioning the buttons in the difficulty selection frame 
    difficulty_buttons_frame = Frame(difficulty_frame, bg="darkblue")
    difficulty_buttons_frame.pack(side=LEFT)

    #Creating radio buttons for the difficulty selection
    Radiobutton(difficulty_buttons_frame, text="Easy", variable=difficulty, value="easy", command=update_selected_label,
                bg='darkblue', fg='white', font=("Arial", 11)).pack(anchor='w')
    Radiobutton(difficulty_buttons_frame, text="Medium", variable=difficulty, value="medium", command=update_selected_label,
                bg='darkblue', fg='white', font=("Arial", 11)).pack(anchor='w')
    Radiobutton(difficulty_buttons_frame, text="Hard", variable=difficulty, value="hard", command=update_selected_label,
                bg='darkblue', fg='white', font=("Arial", 11)).pack(anchor='w')
    
    #making a label for the selected difficulty
    selected_label = Label(difficulty_frame, text=f"Difficulty: {difficulty.get().capitalize()}", font=("Arial", 12),
                            fg="yellow", bg="darkblue")
    selected_label.pack(side=RIGHT, padx=20)

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