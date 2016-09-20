"""
A simple display to show Braille characters.
"""
import time
import random
from tkinter import Canvas, Tk


def create_dot(canvas, x, y, r, fill=False):
    return canvas.create_oval(x - r, y + r, x + r, y - r)


class Display(Canvas):
    def __init__(self, root, width=500, height=500):
        super().__init__(root, width=width, height=height)
        self.pack()
        self.dots = {}

        for j in range(4):
            for i in range(2):
                dot = create_dot(self, 100 * (i + 1), 100 * (j + 1), 30)
                self.dots[i + j * 2] = dot

    def show(self, code):
        for key, value in zip(range(1, 9), code):
            fill = '#000000' if int(value) else '#ffffff'
            self.itemconfig(key, fill=fill)
        self.update()


if __name__ == '__main__':
    root = Tk()
    display = Display(root, 500, 500)
    for i in range(10):
        display.show(''.join(str(random.randint(0, 1)) for x in range(8)))
        time.sleep(1)
