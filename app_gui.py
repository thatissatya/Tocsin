import tkinter as tk
from tkinter import Canvas, NW, END, messagebox
from PIL import ImageTk, Image
from videoFeed import dest
from resource_Access import create_resource

def gui():
    master = tk.Tk()
    master.geometry("700x500")  # Size of the Windows
    master.title('Interface')
    # master.configure(background="#FBF985")
    canvas = Canvas(master, width=200, height=109)
    image = ImageTk.PhotoImage(Image.open("b1.jpg"))  # Logo for the Applications
    canvas.create_image(0, 0, anchor=NW, image=image)
    canvas.grid(row=0, column=1, padx=10, pady=10)
    OPTIONS = ["Hybernation", "Shutdown", "Suspend0", "Hybrid Sleep"]  # Various Options for the System Status
    tk.Label(master, text="System State:", font=("Helvetica", 12)).grid(row=2, column=0)
    variable = tk.StringVar(master)
    variable.set(OPTIONS[0])  # default value
    w = tk.OptionMenu(master, variable, *OPTIONS)
    w.grid(row=2, column=1, padx=10, pady=10)
    e1 = tk.Entry(master)
    e1.insert(END, 15)
    tk.Label(master, text="Camera Frequency(min):", font=("Helvetica", 12)).grid(row=3, column=0)
    e1.grid(row=3, column=1, padx=10, pady=10)
    e2 = tk.Entry(master)
    e2.insert(END, 5)
    tk.Label(master, text="User minimum inactive(min):", font=("Helvetica", 12)).grid(row=4, column=0)
    e2.grid(row=4, column=1, padx=10, pady=10)
    e3 = tk.Entry(master)
    e3.insert(END, 2)
    tk.Label(master, text="Allow Sleep(counter):", font=("Helvetica", 12)).grid(row=5, column=0)
    e3.grid(row=5, column=1, padx=10, pady=10)
    e4 = tk.Entry(master)
    e4.insert(END, '/home')
    tk.Label(master, text="Screen Capture Folder:", font=("Helvetica", 12)).grid(row=6, column=0)
    e4.grid(row=6, column=1, padx=10, pady=10)
    tk.Button(master, text='Tocsin 1.O',
              command=lambda: create_resource(ti=int(e1.get()), v=variable.get(), inac=int(e2.get()),
                                              asleep=int(e3.get()),
                                              fold=str(e4.get()))).grid(row=7, column=1, sticky=tk.W, padx=10, pady=10)
    # tk.Button(master, text='Tocsin', command=create_resource).pack(side=TOP, anchor=W, fill=X, expand=YES)
    tk.Button(master, text='Quit', command=dest).grid(row=7, column=2, sticky=tk.W, padx=10, pady=10)
    msg = tk.Message(master, text="Press 'q' for kill the Tocsin")
    msg.config(bg='lightgreen', font=('times', 12, 'italic'))
    msg.grid()
    master.bind("<Escape>", lambda q: master.destroy())
    master.mainloop()  # Infinite running

