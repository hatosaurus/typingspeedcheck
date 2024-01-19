from tkinter import *
from tkinter import filedialog, ttk, messagebox


class Main(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master, padding=10)
        self.wordlist = None
        self.info = None
        self.master = master
        self.grid(sticky="nsew")
        self.master.title("Typing Speed Calculator")
        self.master.geometry("1200x700")
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.master.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.master.grid_columnconfigure((0, 1, 2, 3), weight=1)

    def create_widgets(self, word_list, retry_callback):
        if self.wordlist:
            self.wordlist.destroy()
        if self.info:
            self.info.destroy()

        self.wordlist = ttk.Label(self.master, text=word_list)
        self.wordlist.config(font=("Arial", 18, "bold"), justify="center")
        self.wordlist.grid(column=1, row=0, columnspan=2)

        self.typing = ttk.Entry(self.master)
        self.typing.config(font=("Arial", 18, "bold"), justify="center")
        self.typing.grid(column=1, row=1, columnspan=2, sticky="ew")

        self.info = ttk.Label(self.master, text="Type the words above.\nPress enter to see your results.", foreground="red")
        self.info.config(font=("Arial", 18, "bold"), justify="center")
        self.info.grid(column=2, row=2, columnspan=1, sticky="ew")

        self.retry_button = ttk.Button(text="Retry", command=lambda: retry_callback())
        self.retry_button.grid(column=1, row=3, columnspan=2, sticky="ew")

    def show_results(self, score, wpm):
        self.info.config(text=f"Accuracy: {score}%\nWords per minute: {wpm}.", font=("Arial", 18, "bold"), justify="center", foreground="green")
        self.info.grid(column=2, row=2, columnspan=1, sticky="ew")

    def retrieve_input(self):
        self.typing.config(state="disabled")
        input = self.typing.get()
        return input