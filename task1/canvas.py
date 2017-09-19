import tkinter as tk
from tkinter import ttk
import random as rnd
from math import *

class MyCanvas:
    def __init__(self, master):
        self.height = 1000
        self.width = 1000
        self.arrowshape = (16, 20, 6)
        self.bg = "white"
        self.graph_height_pos = 10
        self.graph_width_pos = 10
        self.graph_height_neg = 10
        self.graph_width_neg = 10
        self.graph_width = self.graph_width_neg + self.graph_width_pos
        self.graph_height = self.graph_height_neg + self.graph_height_pos
        self.master = master
        self.h = ttk.Scrollbar(master, orient=tk.HORIZONTAL)
        self.v = ttk.Scrollbar(master, orient=tk.VERTICAL)
        self.canvas = tk.Canvas(master, bg=self.bg, scrollregion=
                                (0, 0, self.height, self.width),
                                yscrollcommand=self.v.set,
                                xscrollcommand=self.h.set)
        self.h['command'] = self.canvas.xview
        self.v['command'] = self.canvas.yview
        ttk.Sizegrip(master).grid(column=1, row=1, sticky=(tk.S,tk.E))

        self.canvas.grid(column=0, row=0, sticky=(tk.N,tk.W,tk.E,tk.S))
        self.h.grid(column=0, row=1, sticky=(tk.W,tk.E))
        self.v.grid(column=1, row=0, sticky=(tk.N,tk.S))
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        self.draw_axis()





    def new_line(self, x1, y1, x2, y2):
        self.canvas.create_line(x1, y1, x2, y2)

    def build_graph(self, expr):
        lasty = 0
        for i in range(self.width):
            x = self.x_num(i)
            try:
                y = eval(expr)
            except ZeroDivisionError:
                pass
            except ValueError:
                pass
            else:
                if self.y_coord(lasty) == self.y_coord(y):
                    self.new_line(self.x_coord(x), self.y_coord(lasty),
                              self.x_coord(x), self.y_coord(y)+1)
                else:
                    self.new_line(self.x_coord(x), self.y_coord(lasty),
                              self.x_coord(x), self.y_coord(y))
                lasty = y

    def draw_axis(self):
        self.canvas.create_line(0, self.y_coord(0), self.width,
                                self.y_coord(0),
                                arrow=tk.LAST, arrowshape=self.arrowshape)
        self.canvas.create_line(self.x_coord(0), self.height,
                                self.x_coord(0), 0,
                                arrow=tk.LAST, arrowshape=self.arrowshape)
        self.canvas.create_text(self.width - 20, self.y_coord(0) + 20,
                                text="X")
        self.canvas.create_text(self.x_coord(0) - 20, 20,
                                text="Y")

    def x_coord(self, num):
        return round((num + self.graph_width_neg) * \
                (self.width / self.graph_width))

    def y_coord(self, num):
        return round(self.height - (num + self.graph_height_neg) * \
                (self.height / self.graph_height))

    def x_num(self, coord):
        return -self.graph_width_neg + coord * (self.graph_width / self.width)


    def y_num(self, coord):
        return self.graph_height_pos - coord * (self.graph_height / self.height)

