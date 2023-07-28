import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from tkcalendar import DateEntry
from ttkthemes import ThemedTk

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List App")

        # Initialize an empty list to store tasks
        self.tasks = []

        # Create the main frame
        self.main_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Create the Date and Time frame
        self.datetime_frame = tk.Frame(self.main_frame, bg="#ffffff")
        self.datetime_frame.pack(fill=tk.X, padx=10, pady=10)

        self.date_label = tk.Label(self.datetime_frame, text="", bg="#ffffff", fg="#555555", font=("Arial", 16, "bold"))
        self.date_label.pack(side=tk.LEFT)

        self.time_label = tk.Label(self.datetime_frame, text="", bg="#ffffff", fg="#555555", font=("Arial", 16, "bold"))
        self.time_label.pack(side=tk.RIGHT)

        # Create the Todo List frame
        self.list_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.list_frame.pack(fill=tk.BOTH, padx=10, pady=(0, 10), expand=True)

        self.task_list = tk.Listbox(self.list_frame, selectmode=tk.SINGLE, bg="#ffffff", font=("Arial", 14))
        self.task_list.pack(fill=tk.BOTH, expand=True)

        # Create the Add Task frame
        self.add_frame = tk.Frame(self.main_frame, bg="#ffffff")
        self.add_frame.pack(fill=tk.X, padx=10, pady=(10, 0))

        self.new_task_entry = tk.Entry(self.add_frame, font=("Arial", 14))
        self.new_task_entry.pack(padx=10, pady=5, fill=tk.X, expand=True)

        self.target_date_cal = DateEntry(self.add_frame, font=("Arial", 14), selectbackground="#a0a0a0", foreground="#555555")
        self.target_date_cal.pack(padx=10, pady=5, fill=tk.X, expand=True)

        self.add_button = tk.Button(self.add_frame, text="Add Task", bg="#4caf50", fg="#ffffff", font=("Arial", 14, "bold"), command=self.add_task)
        self.add_button.pack(pady=5)

        # Create the Mark as Completed frame
        self.mark_frame = tk.Frame(self.main_frame, bg="#ffffff")
        self.mark_frame.pack(fill=tk.X, padx=10, pady=5)

        self.mark_button = tk.Button(self.mark_frame, text="Mark Completed", bg="#2196f3", fg="#ffffff", font=("Arial", 14, "bold"), command=self.mark_task_completed)
        self.mark_button.pack(pady=5)

        # Create the Delete frame
        self.delete_frame = tk.Frame(self.main_frame, bg="#ffffff")
        self.delete_frame.pack(fill=tk.X, padx=10, pady=5)

        self.delete_button = tk.Button(self.delete_frame, text="Delete Task", bg="#f44336", fg="#ffffff", font=("Arial", 14, "bold"), command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Create the Refresh List frame
        self.refresh_frame = tk.Frame(self.main_frame, bg="#ffffff")
        self.refresh_frame.pack(fill=tk.X, padx=10, pady=(5, 10))

        self.refresh_button = tk.Button(self.refresh_frame, text="Refresh List", bg="#555555", fg="#ffffff", font=("Arial", 14, "bold"), command=self.display_tasks)
        self.refresh_button.pack(pady=5)

        # Update the Date and Time labels
        self.update_datetime()

        # Display the initial tasks
        self.display_tasks()

    def update_datetime(self):
        # Get the current date and time
        now = datetime.now()
        date_string = now.strftime("%A, %d %B %Y")
        time_string = now.strftime("%H:%M:%S")
        
        # Update the labels
        self.date_label.config(text=date_string)
        self.time_label.config(text=time_string)

        # Schedule the next update after 1 second (1000 milliseconds)
        self.root.after(1000, self.update_datetime)

    def display_tasks(self):
        self.task_list.delete(0, tk.END)
        if not self.tasks:
            self.task_list.insert(tk.END, "No tasks to display.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                status = "✓" if task['completed'] else " "
                description = task['description']
                target_date = task['target_date'].strftime("%Y-%m-%d")
                self.task_list.insert(tk.END, f"{idx}. [{status}] {description} (Target Date: {target_date})")

    def add_task(self):
        description = self.new_task_entry.get().strip()
        target_date = self.target_date_cal.get_date()

        if not description:
            messagebox.showwarning("Warning", "Please enter a task description.")
            return

        if not target_date:
            messagebox.showwarning("Warning", "Please select a target date.")
            return

        self.tasks.append({'description': description, 'completed': False, 'target_date': target_date})
        self.new_task_entry.delete(0, tk.END)
        self.target_date_cal.set_date(None)
        self.display_tasks()

    def mark_task_completed(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            task_idx = selected_index[0]
            self.tasks[task_idx]['completed'] = True
            self.display_tasks()

    def delete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            task_idx = selected_index[0]
            deleted_task = self.tasks.pop(task_idx)
            self.display_tasks()

def main():
    root = ThemedTk(theme="arc")  # Applying the "arc" theme from ttkthemes
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
