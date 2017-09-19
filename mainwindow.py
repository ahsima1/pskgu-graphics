import tkinter as tk
from tkinter import ttk
import canvas

class MainWindow:
    def __init__(self, master, canvas):
        self.master = master
        self.canvas = canvas
        self.frame = tk.Frame(self.master)
        self.expr = tk.StringVar()
        self.expr_entry = ttk.Entry(self.frame, width=50,
                                    textvariable=self.expr)
        self.button1 = tk.Button(self.frame, text = 'Построить график',
                                 width = 25, command = self.add_graph)
        self.expr_entry.pack()
        self.button1.pack()
        self.frame.pack()
        self.master.bind('<Return>', self.add_graph)

    def add_graph(self, *args):
        self.canvas.build_graph(self.expr.get())



