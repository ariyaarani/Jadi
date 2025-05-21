# Author: Mohammad Reza Arani

import csv

class Task:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def to_list(self):
        return [self.name, self.level]

class Todo:
    def __init__(self):
        self.list = []

    def add(self, name, level):
        self.list.append(Task(name, level))

    def show(self):
        if not self.list:
            print("No tasks available.")
        else:
            for i, task in enumerate(self.list, 1):
                print(f"{i}. {task.name} - level: {task.level}")

    def delete(self, index):
        if 0 <= index < len(self.list):
            removed = self.list.pop(index)
            print(f"Task '{removed.name}' deleted.")
        else:
            print("Invalid task number.")

    def save_csv(self, filename):
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for task in self.list:
                writer.writerow(task.to_list())

    def load_csv(self, filename):
        self.list.clear()
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 2:
                        self.add(row[0], row[1])
        except FileNotFoundError:
            print("CSV file not found.")

todo = Todo()

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add task")
    print("2. Show all tasks")
    print("3. Delete task")
    print("4. Save to CSV")
    print("5. Load from CSV")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter task name: ")
        level = input("Enter task level (high / medium / low): ")
        todo.add(name, level)

    elif choice == "2":
        todo.show()

    elif choice == "3":
        try:
            index = int(input("Enter task number to delete: ")) - 1
            todo.delete(index)
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":
        todo.save_csv("tasks.csv")
        print("Tasks saved to 'tasks.csv'.")

    elif choice == "5":
        todo.load_csv("tasks.csv")
        print("Tasks loaded from 'tasks.csv'.")

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
