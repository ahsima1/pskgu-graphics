#!/usr/bin/env python

import tkinter as tk
import mainwindow, canvas

def main():
    root = tk.Tk()
    new_window = tk.Toplevel(root)
    my_canvas = canvas.MyCanvas(root)
    main_window = mainwindow.MainWindow(new_window, my_canvas)

    root.mainloop()

if __name__ == '__main__':
    main()
