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
root.geometry("500x500")
root.config(bg="#f2f2f2")  # Couleur de fond douce

# Police stylée
font_style = ("Helvetica", 12)

# Champ d'entrée de tâche avec bord arrondi et ombre légère
task_entry = tk.Entry(root, width=40, font=font_style, bd=2, relief="flat", bg="#f9f9f9", fg="#333")
task_entry.pack(pady=20)

# Boutons d'action avec effets modernes
add_button = tk.Button(root, text="Ajouter", command=add_task, font=font_style, bg="#4CAF50", fg="white", relief="flat", padx=20, pady=10)
add_button.pack(pady=10)

remove_button = tk.Button(root, text="Supprimer", command=remove_task, font=font_style, bg="#F44336", fg="white", relief="flat", padx=20, pady=10)
remove_button.pack(pady=10)

mark_done_button = tk.Button(root, text="Terminer", command=mark_done, font=font_style, bg="#2196F3", fg="white", relief="flat", padx=20, pady=10)
mark_done_button.pack(pady=10)

# Liste des tâches avec un joli fond et une bordure arrondie
tasks_listbox = tk.Listbox(root, width=40, height=10, font=font_style, bg="#ffffff", fg="#333", bd=2, relief="flat", selectmode=tk.SINGLE)
tasks_listbox.pack(pady=20)

# Lancement de l'application
root.mainloop()
