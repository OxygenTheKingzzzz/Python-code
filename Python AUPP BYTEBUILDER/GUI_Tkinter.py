"""
import tkinter as tk # Recommended import style
window=tk.Tk() # CReate main window
window.title('My first GUI') # Set window title 
window.geometry("300x200") # Set the size and position of the window (width x height + x + y)
# Keep the window visible until the user closes it
# Label wwidget for displaying static text
label=tk.Label(window,
               text="Enter your name:",
               fg='black', #fg=force ground
               font=('Helvetica',14))
label.place(x=30,y=30)
#another style 
# tk.Label(window,
#                text="Enter your name:",
#                fg='black',
#                font=('Helvetica',14)).place(x=30,y=30)

#Entry widget for user input
entry=tk.Entry(window, bd=10)
entry.place(x=30,y=80)

# Button widget for triggering an action
button = tk.Button(window, text="Greet Me!", fg='blue')
button.place(x=30, y=150)

window.mainloop()
"""

"""
import tkinter as tk

window = tk.Tk()
window.title("Using pack()")
window.geometry("300x150")

label = tk.Label(window, text="Username:")
label.pack(padx=10, pady=5)

entry = tk.Entry(window)
entry.pack(padx=10, pady=5)

button = tk.Button(window, text="Submit")
button.pack(padx=10, pady=10)

window.mainloop()
"""


# import tkinter as tk

# window = tk.Tk()
# window.title("Using grid()")
# window.geometry("300x150")

# # Username label and entry
# label_username = tk.Label(window, text="Username:")
# label_username.grid(row=0, column=0, padx=10, pady=10, sticky='e')

# entry_username = tk.Entry(window)
# entry_username.grid(row=0, column=1, padx=10, pady=10)

# # Password label and entry
# label_password = tk.Label(window, text="Password:")
# label_password.grid(row=1, column=0, padx=10, pady=10, sticky='e')

# entry_password = tk.Entry(window, show="*")
# entry_password.grid(row=1, column=1, padx=10, pady=10)

# # Submit button
# button_submit = tk.Button(window, text="Login")
# button_submit.grid(row=2, column=0, columnspan=2, pady=10)

# window.mainloop()

# import tkinter as tk
# from tkinter.ttk import Combobox

# window = tk.Tk()
# window.title("Selection Widgets")
# window.geometry("400x250")

# # ComboBox
# combo_label = tk.Label(window, text="Choose your option:")
# combo_label.place(x=20, y=20)

# combo = Combobox(window, values=["Yes", "No", "Maybe"])
# combo.place(x=150, y=20)

# # ListBox
# listbox_label = tk.Label(window, text="Select multiple options:")
# listbox_label.place(x=20, y=60)

# listbox = tk.Listbox(window, selectmode='multiple', height=4)
# for option in ["Python", "Java", "C++", "JavaScript"]:
#     listbox.insert(tk.END, option)
# listbox.place(x=150, y=60)

# # RadioButtons
# radio_label = tk.Label(window, text="Select gender:")
# radio_label.place(x=20, y=140)

# gender_var = tk.IntVar()
# gender_var.set(1)  # default selection

# male_rb = tk.Radiobutton(window, text="Male", variable=gender_var, value=1)
# female_rb = tk.Radiobutton(window, text="Female", variable=gender_var, value=2)

# male_rb.place(x=150, y=140)
# female_rb.place(x=220, y=140)

# window.mainloop()

import tkinter as tk

def greet():
    username = entry.get()  # Get text from entry box
    greeting_label.config(text=f"Hello, {username}!")

window = tk.Tk()
window.title("Greeting Application")
window.geometry("350x200")

# Label prompting for input
prompt_label = tk.Label(window, text="Enter your name:")
prompt_label.pack(pady=5)

# Entry box to take user input
entry = tk.Entry(window, bd=3)
entry.pack(pady=5)

# Button to trigger greeting
greet_button = tk.Button(window, text="Greet Me", command=greet)
greet_button.pack(pady=5)

# Label to display greeting
greeting_label = tk.Label(window, text="", font=("Arial", 14), fg="green")
greeting_label.pack(pady=20)

window.mainloop()



