import tkinter as tk
from task_manager import TaskManager

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
