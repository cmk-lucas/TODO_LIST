import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Attention", "Veuillez entrer une tâche !")

def remove_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Attention", "Veuillez sélectionner une tâche à supprimer !")

def mark_done():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_task_index)
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(tk.END, f"✔ {task}")
    except IndexError:
        messagebox.showwarning("Attention", "Veuillez sélectionner une tâche à marquer comme terminée !")

# Création de la fenêtre principale
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Champ d'entrée de tâche
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Boutons d'action
add_button = tk.Button(root, text="Ajouter", command=add_task)
add_button.pack()

remove_button = tk.Button(root, text="Supprimer", command=remove_task)
remove_button.pack()

mark_done_button = tk.Button(root, text="Terminer", command=mark_done)
mark_done_button.pack()

# Liste des tâches
tasks_listbox = tk.Listbox(root, width=50, height=15)
tasks_listbox.pack(pady=10)

# Lancement de l'application
root.mainloop()
