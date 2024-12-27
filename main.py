import customtkinter
import webbrowser
import requests
from PIL import Image
from io import BytesIO

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("600x500")
app.title("To-Do App")

task_widgets = []

canvas = customtkinter.CTkCanvas(master=app, height=250, width=550)
canvas.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

scrollbar = customtkinter.CTkScrollbar(master=app, orientation="vertical", command=canvas.yview)
scrollbar.place(relx=0.95, rely=0.5, relheight=0.5, anchor=customtkinter.CENTER)

canvas.configure(yscrollcommand=scrollbar.set)

tasks_frame = customtkinter.CTkFrame(master=canvas, fg_color="transparent")
canvas.create_window((0, 0), window=tasks_frame, anchor="nw")

title_label = customtkinter.CTkLabel(master=app, text="TODO LIST APP", font=("Arial", 24, "bold"))
title_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

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
add_button.place(relx=0.3, rely=0.85, anchor=customtkinter.CENTER)

remove_button = customtkinter.CTkButton(master=app, text="Remove Last Task", command=remove_task)
remove_button.place(relx=0.7, rely=0.85, anchor=customtkinter.CENTER)

def open_github():
    webbrowser.open("https://github.com/nstimumbai06/TODO-List")

footer_frame = customtkinter.CTkFrame(master=app, fg_color="transparent", height=50)
footer_frame.place(relx=0.5, rely=0.95, anchor=customtkinter.CENTER)

image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4ExGUTEwAQn95uM4KUU-OZ7Zz1n2lDrnXfw&s"
response = requests.get(image_url)

github_icon = Image.open(BytesIO(response.content))
github_icon = github_icon.resize((30, 30))

github_ctk_icon = customtkinter.CTkImage(light_image=github_icon, dark_image=github_icon, size=(30, 30))

github_label = customtkinter.CTkLabel(master=footer_frame, image=github_ctk_icon, text="", width=40, height=40)
github_label.grid(row=0, column=0, padx=10)
github_label.bind("<Button-1>", lambda e: open_github())

copyright_label = customtkinter.CTkLabel(master=footer_frame, text="© n0step_", font=("Arial", 12), anchor="w")
copyright_label.grid(row=0, column=1, padx=10, sticky="w")

app.mainloop()