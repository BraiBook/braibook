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
        self.buffer = deque(maxlen=15)
        dots = [create_dot(self, 30 * (x + 1), 30 * (y + 1), 9)
                for x, y in product(range(2), range(4))]
        self.dots = dict(zip((1, 2, 3, 7, 4, 5, 6, 8), dots))
        self.char = self.create_text(130, 75, text='',
                                     font=("liberation serif", 60))
        self.sentence = self.create_text(100, 160, text=self.buffer,
                                         font=("liberation mono", 10),
                                         width=160)

    def show(self, char):
        for dot in range(1, 9):
            fill = '#000000' if str(dot) in str(LATIN[char]) else '#ffffff'
            self.itemconfig(self.dots[dot], fill=fill)
        self.buffer.append(char)
        self.itemconfig(self.char, text=char)
        self.itemconfig(self.sentence, text=''.join(self.buffer))
        self.update()

    def show_byte(self, byte):
        bit_list = [(byte >> bit) & 1 for bit in range(7, -1, -1)]
        for dot in range(1, 9):
            fill = '#000000' if bit_list[dot-1] else '#ffffff'
            self.itemconfig(self.dots[dot], fill=fill)
        self.buffer.append('\b')
        self.itemconfig(self.char, text='\b')
        self.itemconfig(self.sentence, text=''.join(self.buffer))
        self.update()
