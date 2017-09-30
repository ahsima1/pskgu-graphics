import tkinter as tk
from tkinter import ttk
import canvas

class MainWindow:
    def __init__(self, master, canvas):
        self.master = master
        self.canvas = canvas
        self.frame = tk.Frame(self.master)
        self.frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)

        self.expr = tk.StringVar()
        self.leftx = tk.StringVar()
        self.rightx = tk.StringVar()
        self.x_left = tk.StringVar()
        self.x_right = tk.StringVar()
        self.unitx = tk.StringVar()

        self.unitx_entry = ttk.Entry(self.frame, width=50,
                                    textvariable=self.unitx)
        self.unitx_entry.grid(column=1, row=2, sticky=(tk.W, tk.E))
        self.unitx_label = ttk.Label(self.frame,
                                     text="Единичный отрезок оси х:")
        self.unitx_label.grid(column=1, row=1, sticky=(tk.W, tk.E))

        self.x_left_label = ttk.Label(self.frame,
                                     text="Левый предел оси х:")
        self.x_left_label.grid(column=1, row=3, sticky=(tk.W, tk.E))
        self.x_right_label = ttk.Label(self.frame,
                                      text="Правый предел оси х:")
        self.x_right_label.grid(column=2, row=3, sticky=(tk.W, tk.E))

        self.x_left_entry = ttk.Entry(self.frame, width=50,
                                    textvariable=self.x_left)
        self.x_left_entry.grid(column=1, row=4, sticky=(tk.W, tk.E))
        self.x_right_entry = ttk.Entry(self.frame, width=50,
                                    textvariable=self.x_right)
        self.x_right_entry.grid(column=2, row=4, sticky=(tk.W, tk.E))

        self.leftx_label = ttk.Label(self.frame,
                                     text="Начальное значение х:")
        self.leftx_label.grid(column=1, row=5, sticky=(tk.W, tk.E))
        self.rightx_label = ttk.Label(self.frame,
                                      text="Конечное значение х:")
        self.rightx_label.grid(column=2, row=5, sticky=(tk.W, tk.E))


        self.leftx_entry = ttk.Entry(self.frame, width=50,
                                    textvariable=self.leftx)
        self.leftx_entry.grid(column=1, row=6, sticky=(tk.W, tk.E))
        self.rightx_entry = ttk.Entry(self.frame, width=50,
                                    textvariable=self.rightx)
        self.rightx_entry.grid(column=2, row=6, sticky=(tk.W, tk.E))

        self.rightx_label = ttk.Label(self.frame,
                                      text="Введите формулу графика функции:")
        self.rightx_label.grid(column=1, row=7, sticky=(tk.W, tk.E))

        self.expr_entry = ttk.Entry(self.frame, width=50,
                                    textvariable=self.expr)
        self.expr_entry.grid(column=1, row=8, sticky=(tk.W, tk.E))
        self.button1 = tk.Button(self.frame, text = 'Построить график',
                                 width = 25, command = self.add_graph)
        self.button1.grid(column=2, row=8, sticky=(tk.W, tk.E))
        for child in self.frame.winfo_children(): child.grid_configure(padx=5, pady=5)
        self.master.bind('<Return>', self.add_graph)
        self.is_initialized = False

    def add_graph(self, *args):
        if not self.is_initialized:
            self.canvas.init_settings(float(self.x_left.get()),
                                      float(self.x_right.get()),
                                      float(self.unitx.get()))
            self.canvas.init_graph()
            self.is_initialized = True
        self.canvas.build_graph(self.expr.get(),
                                self.leftx.get()
                                , self.rightx.get())



