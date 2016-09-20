"""
A simple display to show Braille characters.
"""
import time
import random
from tables import LATIN
from tkinter import Canvas, Tk


def create_dot(canvas, x, y, r, fill=False):
    return canvas.create_oval(x - r, y + r, x + r, y - r)


class Display(Canvas):
    def __init__(self, root, width=200, height=200):
        super().__init__(root, width=width, height=height)
        self.pack()
        self.dots = {}
        self.last_chars = []

        for j in range(4):
            for i in range(2):
                dot = create_dot(self, 30 * (i + 1), 30 * (j + 1), 9)
                self.dots[i + j * 2] = dot
        self.char = self.create_text(100, 75, text='', font=("Default", 40))
        self.sentence = self.create_text(25, 150, text=self.last_chars,
                                         font=("Default", 12),
                                         anchor='w', width=160)   

    def show(self, char):
        code = LATIN[char]
        for dot in range(1,9):
            fill = '#000000' if str(dot) in str(code) else '#ffffff'
            self.itemconfig(self.dots[dot-1], fill=fill)
            
        self.delete(self.char)
        self.char = self.create_text(130, 75, text=char, font=("Default", 60))
        
        self.__update_last_chars(char)
        self.delete(self.sentence)
        self.sentence = self.create_text(25, 160, text=self.last_chars, font=("Default", 12),
                         anchor='w', width=160)      
        self.update()
        
    def __update_last_chars(self, char):
        self.last_chars.append(char)
        if len(self.last_chars) > 20:
            self.last_chars[:10] = []
            self.delete(self.sentence)
        

if __name__ == '__main__':
    root = Tk()
    display = Display(root, width=200, height=200)
    for i in range(50):
        display.show(chr(random.randrange(97, 122)))
        time.sleep(0.1)
