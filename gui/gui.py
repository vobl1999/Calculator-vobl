import tkinter as tk
from tkinter import messagebox
from calculator.functions.functions import add, subtract, multiply, divide, power, sqrt

# Initialize history list
history = []

def update_history(history_listbox):
    history_listbox.delete(0, tk.END)
    for record in history:
        history_listbox.insert(tk.END, record)

def add_command(entry1, entry2, history_listbox):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = add(num1, num2)
        history.append(f"{num1} + {num2} = {result}")
        update_history(history_listbox)
        messagebox.showinfo("Result", f"The result is: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numbers only.")

def subtract_command(entry1, entry2, history_listbox):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = subtract(num1, num2)
        history.append(f"{num1} - {num2} = {result}")
        update_history(history_listbox)
        messagebox.showinfo("Result", f"The result is: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numbers only.")

def multiply_command(entry1, entry2, history_listbox):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = multiply(num1, num2)
        history.append(f"{num1} * {num2} = {result}")
        update_history(history_listbox)
        messagebox.showinfo("Result", f"The result is: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numbers only.")

def divide_command(entry1, entry2, history_listbox):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            messagebox.showerror("Error", "Division by zero is not allowed.")
        else:
            result = divide(num1, num2)
            history.append(f"{num1} / {num2} = {result}")
            update_history(history_listbox)
            messagebox.showinfo("Result", f"The result is: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numbers only.")

def power_command(entry1, entry2, history_listbox):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = power(num1, num2)
        history.append(f"{num1} ^ {num2} = {result}")
        update_history(history_listbox)
        messagebox.showinfo("Result", f"The result is: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numbers only.")

def sqrt_command(entry1, history_listbox):
    try:
        num1 = float(entry1.get())
        result = sqrt(num1)
        history.append(f"sqrt({num1}) = {result}")
        update_history(history_listbox)
        messagebox.showinfo("Result", f"The result is: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numbers only.")

def create_gui():
    # Create the main window
    root = tk.Tk()
    root.title("Calculator - vobl制作")

    # Create and place the widgets
    tk.Label(root, text="Enter first number:").grid(row=0, column=0)
    entry1 = tk.Entry(root)
    entry1.grid(row=0, column=1)

    tk.Label(root, text="Enter second number:").grid(row=1, column=0)
    entry2 = tk.Entry(root)
    entry2.grid(row=1, column=1)

    tk.Button(root, text="Add", command=lambda: add_command(entry1, entry2, history_listbox)).grid(row=2, column=0)
    tk.Button(root, text="Subtract", command=lambda: subtract_command(entry1, entry2, history_listbox)).grid(row=2, column=1)
    tk.Button(root, text="Multiply", command=lambda: multiply_command(entry1, entry2, history_listbox)).grid(row=3, column=0)
    tk.Button(root, text="Divide", command=lambda: divide_command(entry1, entry2, history_listbox)).grid(row=3, column=1)
    tk.Button(root, text="Power", command=lambda: power_command(entry1, entry2, history_listbox)).grid(row=4, column=0)
    tk.Button(root, text="Square Root", command=lambda: sqrt_command(entry1, history_listbox)).grid(row=4, column=1)

    # Create and place the history listbox
    tk.Label(root, text="History:").grid(row=5, column=0, columnspan=2)
    history_listbox = tk.Listbox(root, width=40, height=10)
    history_listbox.grid(row=6, column=0, columnspan=2)

    # Start the main event loop
    root.mainloop()

if __name__ == "__main__":
    create_gui()
