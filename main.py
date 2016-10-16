import time
import random
from tkinter import Tk
import types

from braibook.display import Display
from braibook.unicode_gen import str2brl
from braibook.signal_gen import signal_generator
from braibook.hv5522 import hv5522

hv5522 = hv5522()


def update_display(hv5522):
    if hv5522.get_enable():
        display.show_byte(hv5522.hv_out)

if __name__ == '__main__':
    main = Tk()
    display = Display(main, width=200, height=200)
    display2 = Display(main, width=200, height=200)
    hv5522.output_updated = types.MethodType(update_display, hv5522)

    signal_generator = signal_generator(hv5522)
    for code_point in str2brl('Hello world! This is a braille display test...', 'en-gb-g1.utb'):
        signal_generator.generate_braille(code_point)
        time.sleep(0.5)

    for c in 'Hello world! this is a braille display test...':
        display2.show(c)
        time.sleep(0.5)
