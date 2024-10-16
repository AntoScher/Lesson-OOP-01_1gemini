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

    # ... (остальные методы класса TaskManager)

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

    # ... (остальные методы delete_task, edit_task, mark_task, populate_fields_for_edit, check_task_deadline)
