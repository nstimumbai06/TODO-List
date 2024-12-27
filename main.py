import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("600x500")
app.title("To-Do App")

task_widgets = []

canvas = customtkinter.CTkCanvas(master=app, height=250, width=550)
canvas.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

scrollbar = customtkinter.CTkScrollbar(master=app, orientation="vertical", command=canvas.yview)
scrollbar.place(relx=0.95, rely=0.6, relheight=0.5, anchor=customtkinter.CENTER)

canvas.configure(yscrollcommand=scrollbar.set)

tasks_frame = customtkinter.CTkFrame(master=canvas)
canvas.create_window((0, 0), window=tasks_frame, anchor="nw")

task_entry = customtkinter.CTkEntry(master=app, placeholder_text="Enter a task", width=400)
task_entry.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

def add_task():
    task = task_entry.get().strip()
    if task:
        task_frame = customtkinter.CTkFrame(master=tasks_frame, width=500, height=40)
        task_frame.pack(pady=5)

        task_label = customtkinter.CTkLabel(master=task_frame, text=task, width=480, anchor="w")
        task_label.pack(padx=10, pady=10, anchor="w")

        task_widgets.append(task_frame)

        task_entry.delete(0, "end")

        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

def remove_task():
    if task_widgets:
        last_task = task_widgets.pop()
        last_task.destroy()

        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

add_button = customtkinter.CTkButton(master=app, text="Add Task", command=add_task)
add_button.place(relx=0.3, rely=0.75, anchor=customtkinter.CENTER)

remove_button = customtkinter.CTkButton(master=app, text="Remove Last Task", command=remove_task)
remove_button.place(relx=0.7, rely=0.75, anchor=customtkinter.CENTER)

app.mainloop()
