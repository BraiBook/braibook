from .hv5522 import hv5522


class signal_generator:

    def __init__(self, hv5522):
        self.input_char = ''
        if hv5522 is None:
            self.hv5522 = hv5522()
        else:
            self.hv5522 = hv5522

    def generate_braille(self, braille_unicode):
        for code_point in braille_unicode:
            self.unibits = self.get_byte(code_point)
            for bit in self.unibits:
                self.hv5522.data_in = bit
                self.hv5522.clock_cycle()
            self.hv5522.set_enable()
            self.hv5522.clear_enable()

    def get_byte(self, code_point):
        number = ord(code_point) - 0x2800
        return [(number >> bit) & 1 for bit in range(7, -1, -1)]
