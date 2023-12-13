import tkinter as tk
from tkinter import scrolledtext


def run_code():
    code = code_text.get("1.0", tk.END)
    try:
        exec(code)
    except Exception as e:
        result_text.insert(tk.END, f"Error: {e}\n")


# Create the main window
window = tk.Tk()
window.title("Simple Python IDE")

# Create a text widget for code input
code_text = scrolledtext.ScrolledText(window, width=80, height=20)
code_text.pack(pady=10)

# Create a button to run the code
run_button = tk.Button(window, text="Run Code", command=run_code)
run_button.pack()

# Create a text widget for displaying results
result_text = scrolledtext.ScrolledText(window, width=80, height=10)
result_text.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
