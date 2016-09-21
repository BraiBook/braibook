import time
import random
from tkinter import Tk

from braibook.display import Display


if __name__ == '__main__':
    main = Tk()
    display = Display(main, width=200, height=200)
    for c in 'Hello world! this is a braille display test...':
        display.show(c)
        time.sleep(0.5)
