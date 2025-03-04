import random
import tkinter as tk
from tkinter import messagebox

terms_and_definitions = {
    "This is where you enter your term": "This is where you enter its definition",
    "This is where you enter your term": "This is where you enter its definition",
    "This is where you enter your term": "This is where you enter its definition"
}

# Separate the terms and definitions for easier access
terms = list(terms_and_definitions.keys())
definitions = list(terms_and_definitions.values())

# Shuffle the terms and definitions
random.shuffle(terms)
random.shuffle(definitions)

# Track areas to work on
areas_to_improve = []

# Function for the term-matching quiz
def term_matching_quiz():
    # Create a Tkinter window
    window = tk.Tk()
    window.title("Term Matching Quiz")

    # Frame for quiz content
    frame = tk.Frame(window)
    frame.pack(padx=20, pady=20)

    # Variable to track which question we are on
    term_matching_index = 0
    total_term_matching = len(terms)

    # Function to update the question and options
    def show_question():
        nonlocal term_matching_index

        # Clear previous content
        for widget in frame.winfo_children():
            widget.destroy()

        # Show current term
        term = terms[term_matching_index]
        correct_definition = terms_and_definitions[term]

        tk.Label(frame, text=f"Match this term to its definition: {term}", font=("Arial", 14), wraplength=600).pack(pady=10)

        # Select random definitions and add the correct one
        choices = random.sample(definitions, 3)  # Random 3 incorrect definitions
        choices.append(correct_definition)
        random.shuffle(choices)  # Shuffle them so the correct one isn't always last

        var = tk.StringVar()
        var.set(None)  # No option selected initially

        # Show options (definitions)
        for definition in choices:
            tk.Radiobutton(frame, text=definition, variable=var, value=definition, font=("Arial", 12), wraplength=600,
                           justify="left").pack(anchor='w')

        # Function to check the answer
        def check_answer():
            nonlocal term_matching_index

            selected_definition = var.get()
            if selected_definition == correct_definition:
                messagebox.showinfo("Correct", "Correct! Moving to the next question.")
                term_matching_index += 1
                if term_matching_index < total_term_matching:
                    show_question()  # Proceed to the next term-matching question
                else:
                    messagebox.showinfo("Quiz Complete", "You have completed the quiz!")
                    window.quit()
            else:
                messagebox.showerror("Incorrect", "Incorrect! Try again.")

        tk.Button(frame, text="Submit", command=check_answer, font=("Arial", 12)).pack(pady=10)

    show_question()

    window.mainloop()

# Run the term-matching quiz
if __name__ == "__main__":
    term_matching_quiz()
