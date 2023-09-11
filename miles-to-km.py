import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    userInput = entryVar.get()
    kmOutput = userInput * 1.61
    resultVar.set(f"{kmOutput}km")


window = ttk.Window(themename= "journal")
window.title("Miles to KM")
window.geometry("300x150")

titleLabel = ttk.Label(window, text= "Miles to Kilometers", font= "Calibri 24 bold")
titleLabel.pack()

inputUser = ttk.Frame(window)
entryVar = tk.IntVar()
entry = ttk.Entry(inputUser, textvariable= entryVar)
button = ttk.Button(inputUser, text= "Convert", command=convert)
entry.pack(side = "left", padx= 10)
button.pack(side = "left")
inputUser.pack(pady= 10)

resultVar = tk.StringVar()
resultLabel = ttk.Label(window, text= "Output", font= "Calibri 24 bold", textvariable=resultVar)
resultLabel.pack(pady=5)

window.mainloop()
