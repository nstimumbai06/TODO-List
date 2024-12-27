import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("400x400")
app.title("To-Do App")

tasks = []

task_textbox = customtkinter.CTkTextbox(master=app, height=10, width=40)
task_textbox.place(relx=0.5, rely=0.35, anchor=customtkinter.CENTER)

task_entry = customtkinter.CTkEntry(master=app, placeholder_text="Enter a task", width=280)
task_entry.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

def add_task():
    task = task_entry.get().strip()
    if task:
        tasks.append(task)
        task_textbox.insert("end", task + "\n")
        task_entry.delete(0, "end")

def remove_task():
    if tasks:
        tasks.pop()
        task_textbox.delete("1.0", "end")
        task_textbox.insert("1.0", "\n".join(tasks))

add_button = customtkinter.CTkButton(master=app, text="Add Task", command=add_task)
add_button.place(relx=0.3, rely=0.75, anchor=customtkinter.CENTER)

remove_button = customtkinter.CTkButton(master=app, text="Remove Last Task", command=remove_task)
remove_button.place(relx=0.7, rely=0.75, anchor=customtkinter.CENTER)

app.mainloop()
