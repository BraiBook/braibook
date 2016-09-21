"""
A simple display to show Braille characters.
"""
from tkinter import Canvas
from itertools import product
from collections import deque

from .tables import LATIN


def create_dot(canvas, x, y, r, fill=False):
    return canvas.create_oval(x - r, y + r, x + r, y - r)


class Display(Canvas):
    def __init__(self, root, width=200, height=200):
        super().__init__(root, width=width, height=height)
        self.pack()
        self.dots = {}
        self.buffer = deque(maxlen=15)
        for j, i in product(range(4), range(2)):
            dot = create_dot(self, 30 * (i + 1), 30 * (j + 1), 9)
            self.dots[i + j * 2] = dot
        self.char = self.create_text(130, 75, text='',
                                     font=("liberation serif", 60))
        self.sentence = self.create_text(100, 160, text=self.buffer,
                                         font=("liberation mono", 10),
                                         width=160)

    def show(self, char):
        for dot in range(1, 9):
            fill = '#000000' if str(dot) in str(LATIN[char]) else '#ffffff'
            self.itemconfig(self.dots[dot-1], fill=fill)
        self.buffer.append(char)
        self.itemconfig(self.char, text=char)
        self.itemconfig(self.sentence, text=''.join(self.buffer))
        self.update()
