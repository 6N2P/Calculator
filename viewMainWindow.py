import tkinter as tk
from tkinter import ttk


class View(tk.Tk):
    "Class View"
    PAD = 10
    maxButtonPerRow = 4
    buttonCaptions = [
        'C',  '+/-', '%', '/',
        7, 8, 9, '*',
        4, 5, 6, '-',
        1, 2, 3, '+',
        0, '.', '='
    ]

    def __init__(self, controller):
        super().__init__()
        self.title("Kalkulator")
        self.controller = controller
        self.value_var = tk.StringVar()
        self.makeMainFrame()
        self.makeEntry()
        self.makeButtons()


    def main(self):
        self.mainloop()

    def makeMainFrame(self):
        self.main_frm = ttk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)

    def makeEntry(self):
        ent = ttk.Entry(
            self.main_frm, justify="right" ,textvariable=self.value_var,
            state='disabled'
        )
        ent.pack(fill='x')

    def makeButtons(self):
        outer_frm = ttk.Frame(self.main_frm)
        outer_frm.pack()

        frm = ttk.Frame(outer_frm)
        frm.pack()

        buttons_in_row = 0

        for caption in self.buttonCaptions:

            if buttons_in_row == self.maxButtonPerRow:
                frm = ttk.Frame(outer_frm)
                frm.pack()
                buttons_in_row = 0

            btn = ttk.Button(frm, text=caption)
            btn.pack(side='left')

            buttons_in_row +=1


