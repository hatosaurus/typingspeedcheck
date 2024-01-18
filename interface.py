from tkinter import *
from tkinter import filedialog, ttk, messagebox


class Main(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master, padding=10)
        self.master = master
        self.grid(sticky="nsew")
        self.master.title("Typing Speed Calculator")
        self.master.geometry("1200x700")
        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.master.grid_rowconfigure((0, 1), weight=1)
        self.master.grid_columnconfigure((0, 1, 2, 3), weight=1)

    def create_widgets(self, word_list):
        self.label = ttk.Label(self.master, text=word_list)
        self.label.config(font=("Arial", 18, "bold"), justify="center")
        self.label.grid(column=1, row=0, columnspan=2)

        self.typing = ttk.Entry(self.master, justify="center")
        self.typing.config(font=("Arial", 18, "bold"))
        self.typing.grid(column=1, row=1, columnspan=2, sticky="ew")

