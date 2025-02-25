import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime
import time

class PDAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDA Touchscreen Interface")
        self.root.geometry("800x480")  # Set resolution for most touchscreens
        self.root.configure(bg="black")

        # Create tabs using ttk Notebook
        self.notebook = ttk.Notebook(root)
        
        # Create frames for each tab
        self.home_tab = tk.Frame(self.notebook, bg="black")
        self.todo_tab = tk.Frame(self.notebook, bg="black")
        self.notes_tab = tk.Frame(self.notebook, bg="black")
        self.settings_tab = tk.Frame(self.notebook, bg="black")
        
        # Add frames to the notebook as tabs
        self.notebook.add(self.home_tab, text="Home")
        self.notebook.add(self.todo_tab, text="To-Do List")
        self.notebook.add(self.notes_tab, text="Notes")
        self.notebook.add(self.settings_tab, text="Settings")

        self.notebook.pack(expand=True, fill="both")

        # Setup each tab
        self.setup_home_tab()
        self.setup_todo_tab()
        self.setup_notes_tab()
        self.setup_settings_tab()

    def setup_home_tab(self):
        font_large = ("Helvetica", 24, "bold")
        font_medium = ("Helvetica", 18)

        # Display time and date
        self.time_label = tk.Label(self.home_tab, font=font_large, fg="green", bg="black")
        self.date_label = tk.Label(self.home_tab, font=font_medium, fg="green", bg="black")

        # Update time and date
        self.update_time_and_date()

        self.time_label.pack(expand=True, fill="both")
        self.date_label.pack(expand=True, fill="both")

        # Battery Status (Placeholder)
        self.battery_label = tk.Label(self.home_tab, text="Battery: 100%", font=font_medium, fg="green", bg="black")
        self.battery_label.pack(pady=10)

    def update_time_and_date(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        
        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)
        
        # Update every second
        self.root.after(1000, self.update_time_and_date)

    def setup_todo_tab(self):
        font_medium = ("Helvetica", 16)

        # To-Do List Label
        self.todo_label = tk.Label(self.todo_tab, text="To-Do List", font=font_medium, fg="green", bg="black")
        self.todo_label.pack(pady=10)

        # Listbox to display tasks
        self.todo_listbox = tk.Listbox(self.todo_tab, height=10, font=font_medium, fg="green", bg="black", selectbackground="green")
        self.todo_listbox.pack(pady=10)

        # Entry to add new task
        self.todo_entry = tk.Entry(self.todo_tab, font=font_medium, fg="green", bg="black", insertbackground="green")
        self.todo_entry.pack(pady=5)

        # Buttons to add and remove tasks
        self.add_task_button = tk.Button(self.todo_tab, text="Add Task", command=self.add_task, font=font_medium, fg="green", bg="black")
        self.add_task_button.pack(pady=5)

        self.remove_task_button = tk.Button(self.todo_tab, text="Remove Task", command=self.remove_task, font=font_medium, fg="green", bg="black")
        self.remove_task_button.pack(pady=5)

    def add_task(self):
        task = self.todo_entry.get()
        if task:
            self.todo_listbox.insert(tk.END, task)
            self.todo_entry.delete(0, tk.END)

    def remove_task(self):
        selected_task = self.todo_listbox.curselection()
        if selected_task:
            self.todo_listbox.delete(selected_task)
        else:
            messagebox.showwarning("No Selection", "Please select a task to remove.")

    def setup_notes_tab(self):
        font_medium = ("Helvetica", 16)

        # Notes Label
        self.notes_label = tk.Label(self.notes_tab, text="Notes", font=font_medium, fg="green", bg="black")
        self.notes_label.pack(pady=10)

        # Text widget to enter and display notes
        self.notes_text = tk.Text(self.notes_tab, height=15, font=font_medium, fg="green", bg="black", insertbackground="green")
        self.notes_text.pack(pady=10)

        # Button to save note
        self.save_note_button = tk.Button(self.notes_tab, text="Save Note", command=self.save_note, font=font_medium, fg="green", bg="black")
        self.save_note_button.pack(pady=5)

    def save_note(self):
        note_content = self.notes_text.get("1.0", tk.END).strip()
        if note_content:
            messagebox.showinfo("Note Saved", "Your note has been saved.")
            self.notes_text.delete("1.0", tk.END)
        else:
            messagebox.showwarning("Empty Note", "Please enter some text to save.")

    def setup_settings_tab(self):
        font_medium = ("Helvetica", 16)

        # Settings Label
        self.settings_label = tk.Label(self.settings_tab, text="Settings", font=font_medium, fg="green", bg="black")
        self.settings_label.pack(pady=10)

        # Example button for brightness adjustment (placeholder functionality)
        self.brightness_button = tk.Button(self.settings_tab, text="Adjust Brightness", command=self.adjust_brightness, font=font_medium, fg="green", bg="black")
        self.brightness_button.pack(pady=10)

        # Example button for shutdown (placeholder functionality)
        self.shutdown_button = tk.Button(self.settings_tab, text="Shutdown PDA", command=self.shutdown, font=font_medium, fg="green", bg="black")
        self.shutdown_button.pack(pady=10)

    def adjust_brightness(self):
        # Placeholder function for adjusting brightness
        messagebox.showinfo("Brightness", "Brightness adjusted (placeholder).")

    def shutdown(self):
        # Placeholder function for shutting down
        confirm = messagebox.askyesno("Shutdown", "Are you sure you want to shut down?")
        if confirm:
            messagebox.showinfo("Shutdown", "Shutting down (placeholder).")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDAApp(root)
    root.mainloop()
