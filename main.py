import tkinter as tk
from tkinter import filedialog, messagebox, ttk

# Declare entry_num1, result_label, and window_calculator as global variables
entry_num1 = None
result_label = None
window_calculator = None

def calculate():
    try:
        expression = entry_num1.get()
        result = eval(expression)
        result_label.config(text=f"Result: {result}")

    except Exception as e:
        messagebox.showerror("Error", f"Invalid expression: {e}")

def open_file():
    file_path = filedialog.askopenfilename(title="Open File", filetypes=[("Text Files", "*.txt")])

    if file_path:
        try:
            with open(file_path, 'r') as file:
                content = file.read().strip()
                entry_num1.delete(0, tk.END)
                entry_num1.insert(0, content)
        except Exception as e:
            messagebox.showerror("Error", f"Error reading file: {e}")

# Login Page
def login():
    global entry_num1, result_label, window_calculator  # Reference the global variables

    entered_username = entry_username.get()
    entered_password = entry_password.get()

    if entered_username and entered_password:
        messagebox.showinfo("Login Successful", "Welcome, " + entered_username)
        window_login.destroy()
        open_calculator()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Calculator Page
def open_calculator():
    global entry_num1, result_label, window_calculator  # Reference the global variables
    window_calculator = tk.Tk()
    window_calculator.title("Simple Calculator")

    entry_num1 = tk.Entry(window_calculator, width=20, font=('Arial', 14))
    entry_num1.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="news")

    entry_num1.bind('<Return>', lambda event=None: calculate())  # Bind Enter key to calculate function

    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+'
    ]

    row_val = 1
    col_val = 0

    for button in buttons:
        tk.Button(window_calculator, text=button, font=('Arial', 14), command=lambda b=button: entry_num1.insert(tk.END, b)).grid(row=row_val, column=col_val, padx=5, pady=5, sticky="news")
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

    tk.Button(window_calculator, text="Calculate", command=calculate, font=('Arial', 14)).grid(row=row_val, column=0, columnspan=2, padx=10, pady=10, sticky="news")
    tk.Button(window_calculator, text="Next", command=open_feedback, font=('Arial', 14)).grid(row=row_val, column=2, columnspan=2, padx=10, pady=10, sticky="news")

    result_label = tk.Label(window_calculator, text="Result: ", font=('Arial', 14))
    result_label.grid(row=row_val + 1, column=0, columnspan=4, pady=10, sticky="news")

    # Configure row and column weights
    for i in range(6):
        window_calculator.grid_rowconfigure(i, weight=1)
        window_calculator.grid_columnconfigure(i, weight=1)

    window_calculator.mainloop()

# Feedback Page
def open_feedback():
    global window_calculator  # Reference the global variable
    window_calculator.destroy()  # Close the calculator window

    window_feedback = tk.Tk()
    window_feedback.title("Feedback Page")

    feedback_frame = tk.Frame(window_feedback)
    feedback_frame.pack(padx=20, pady=20)

    feedback_label = tk.Label(feedback_frame, text="Feedback:")
    feedback_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

    feedback_entry = tk.Text(feedback_frame, height=4, width=30)
    feedback_entry.grid(row=0, column=1, padx=5, pady=5)

    rating_label = tk.Label(feedback_frame, text="Rating:")
    rating_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

    rating_var = tk.IntVar()
    rating_stars = ttk.Combobox(feedback_frame, textvariable=rating_var, values=[1, 2, 3, 4, 5], state="readonly")
    rating_stars.grid(row=1, column=1, padx=5, pady=5)
    rating_stars.current(0)

    def submit_feedback():
        rating = rating_var.get()
        feedback = feedback_entry.get("1.0", tk.END)

        messagebox.showinfo("Feedback Submitted", f"Rating: {rating} stars\nFeedback: {feedback}")

    submit_feedback_button = tk.Button(feedback_frame, text="Submit Feedback", command=submit_feedback)
    submit_feedback_button.grid(row=2, columnspan=2, pady=10)

    window_feedback.mainloop()

# Login Page
window_login = tk.Tk()
window_login.title("Login Page")

login_frame = tk.Frame(window_login, padx=20, pady=20)
login_frame.pack()

label_username = tk.Label(login_frame, text="Username:")
label_username.grid(row=0, column=0, padx=5, pady=5, sticky="e")

entry_username = tk.Entry(login_frame)
entry_username.grid(row=0, column=1, padx=5, pady=5)

label_password = tk.Label(login_frame, text="Password:")
label_password.grid(row=1, column=0, padx=5, pady=5, sticky="e")

entry_password = tk.Entry(login_frame, show="*")
entry_password.grid(row=1, column=1, padx=5, pady=5)

entry_password.bind('<Return>', lambda event=None: login())  # Bind Enter key to login function

login_button = tk.Button(login_frame, text="Login", command=login)
login_button.grid(row=2, columnspan=2, pady=10)

# Run the Tkinter even8t loop for login page
window_login.mainloop()
