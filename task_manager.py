import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

class TaskManager:
    def __init__(self, master):
        self.master = master
        master.title("Task List")
        master.configure(background="HotPink")

        self.tasks = []

        # UI элементы
        self.create_ui()

    def create_ui(self):
        # Ввод задачи
        tk.Label(self.master, text="Введите задачу", bg="HotPink").pack(pady=5)
        self.task_entry = tk.Entry(self.master, width=30, bg="DeepPink1", fg="black", font=("Helvetica", 12))
        self.task_entry.pack(pady=10, padx=10)

        # Ввод даты выполнения
        tk.Label(self.master, text="Введите дату выполнения (ДД.ММ.ГГГГ ЧЧ:ММ)", bg="HotPink").pack(pady=5)
        self.date_entry = tk.Entry(self.master, width=30, bg="DeepPink1", fg="black", font=("Helvetica", 12))
        self.date_entry.pack(pady=10, padx=10)

        # Кнопки
        tk.Button(self.master, text="Добавить задачу", command=self.add_task).pack(padx=5, pady=5)
        tk.Button(self.master, text="Удалить задачу", command=self.delete_task).pack(padx=5, pady=5)
        tk.Button(self.master, text="Редактировать задачу", command=self.edit_task).pack(padx=5, pady=5)
        tk.Button(self.master, text="Отметить выполненную задачу", command=self.mark_task).pack(padx=5, pady=5)
        tk.Button(self.master, text="Выбрать задачу для редактирования", command=self.populate_fields_for_edit).pack(padx=5, pady=5)

        # Список задач
        tk.Label(self.master, text="Список задач:", bg="HotPink").pack(pady=5)
        self.task_listBox = tk.Listbox(self.master, height=10, width=50, bg="LightPink1", fg="black", font=("Helvetica", 12))
        self.task_listBox.pack(padx=10, pady=10)

        # Запуск проверки срока выполнения задач
        self.check_task_deadline()

    def add_task(self):
        task = self.task_entry.get()
        date_str = self.date_entry.get()

        try:
            due_date = datetime.strptime(date_str, '%d.%m.%Y %H:%M')
            current_time = datetime.now()
            if due_date < current_time:
                messagebox.showerror("Ошибка", "Дата выполнения задачи не может быть в прошлом!")
                return

            if task:
                self.task_listBox.insert(tk.END, f"{task} (до: {due_date.strftime('%d.%m.%Y %H:%M')})")
                self.task_entry.delete(0, tk.END)
                self.date_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректную дату в формате ДД.ММ.ГГГГ ЧЧ:ММ")

    def delete_task(self):
        try:
            selected_index = self.task_listBox.curselection()[0]
            self.task_listBox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def edit_task(self):
        try:
            selected_index = self.task_listBox.curselection()[0]
            task = self.task_entry.get()
            date_str = self.date_entry.get()

            try:
                due_date = datetime.strptime(date_str, '%d.%m.%Y %H:%M')
                self.task_listBox.delete(selected_index)
                self.task_listBox.insert(selected_index, f"{task} (до: {due_date.strftime('%d.%m.%Y %H:%M')})")
                self.task_entry.delete(0, tk.END)
                self.date_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Ошибка", "Введите корректную дату в формате ДД.ММ.ГГГГ ЧЧ:ММ")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to edit.")

    def mark_task(self):
        try:
            selected_index = self.task_listBox.curselection()[0]
            self.task_listBox.itemconfig(selected_index, {'bg': 'lightgreen'})
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark.")

    def populate_fields_for_edit(self):
        try:
            selected_index = self.task_listBox.curselection()[0]
            selected_task = self.task_listBox.get(selected_index)
            task_text = selected_task.split(" (до: ")[0]
            date_text = selected_task.split(" (до: ")[1][:-1]  # Remove parentheses
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(0, task_text)
            self.date_entry.delete(0, tk.END)
            self.date_entry.insert(0, date_text)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to edit.")

    def check_task_deadline(self):
        for i in range(self.task_listBox.size()):
            task_text = self.task_listBox.get(i)
            try:
                due_date_str = task_text.split(" (до: ")[1][:-1]
                due_date = datetime.strptime(due_date_str, '%d.%m.%Y %H:%M')
                if due_date < datetime.now():
                    self.task_listBox.itemconfig(i, {'bg': 'salmon'})
                else:
                    self.task_listBox.itemconfig(i, {'bg': 'LightPink1'})
            except IndexError:
                pass  # Skip tasks without a due date
        self.master.after(60000, self.check_task_deadline)  # Check every minute

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
