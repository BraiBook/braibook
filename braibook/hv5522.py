
class hv5522:
    'Defines behaviour of the HV5522 chip'

    def __init__(self):
        """
        Initialises signals defined in datasheet
        """
        self.hv_out = 0b0
        # hv_output before being inverted by polarity signal
        self.latch_out = 0b0
        self.shift_reg = 0b0
        self.data_in = 0
        self.__enable = 0
        self.__polarity = 0
        self.__blanking = 0
        self.__clk = 0

    def set_data_in(self, value):
        """
        Serial stream input. 1 or 0 integer expected
        """
        self.data_in = value

    def clock_cycle(self):
        self.__rising_edge()
        self.__falling_edge()

    def __clk_rising_edge(self):
        self.clk = 1

    def __clk_falling_edge(self):
        self.clk = 0
        self.shift_reg = self.data_in << 7 | self.shift_reg >> 1
        self.__update()

    def set_enable(self):
        self.__enable = 1
        self.__update()

    def clear_enable(self):
        self.__enable = 0

    def set_polarity(self):
        self.__polarity = 1
        self.__update()

    def clear_polarity(self):
        self.__polarity = 0
        self.__update()

    def set_blanking(self):
        self.__blanking = 1
        self.__update()

    def clear_blanking(self):
        self.__blanking = 0
        self.__update()

    def __update(self):
        if(self.__enable):
            self.latch_out = self.shift_reg

        if(self.__blanking):
            if(self.__polarity):
                self.hv_out = 0xFF
            else:
                self.hv_out = 0x00
        else:
            if(self.__polarity):
                self.hv_out = ~self.latch_out
            else:
                self.hv_out = self.latch_out
