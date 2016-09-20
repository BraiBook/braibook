import tkinter as tk
from tkinter.font import Font
from tkinter.constants import RADIOBUTTON

class Braibook_GUI:
    'Simulates Braibooks Braille cell given its output'
    
    def __init__(self):
        self.root = tk.Tk()
        
        'GUI declaration'
        top_frame = tk.Frame(self.root)
        top_frame.pack(side = tk.TOP)
        top_frame.grab_set()
        
        self.rVar = []
        self.rButtons = []
        
        def radioCallback(event):
            pass
            event.widget.setvar(0)
        for i in range(8):
            self.rVar.append(tk.IntVar())
            self.rButtons.append(tk.Radiobutton(top_frame,
                                  variable=self.rVar[i], value=1))
            self.rButtons[i].bind("<Button>", radioCallback)
            
        for j in range(2):
            for i in range(3):
                self.rButtons[i+j*3].grid(column=j, row=i)
                
        for i in range(2):
            self.rButtons[i+6].grid(column=i, row=3)
    

        charLabel = tk.Label(top_frame,
                             anchor=tk.CENTER, 
                             text="A",
                             font=("Helvetica", 40),
                             width=1)
        charLabel.grid(column=2, row=0, rowspan=4)
        
        
        bottom_frame = tk.Frame(self.root)
        bottom_frame.pack(side = tk.BOTTOM)
        txtMessage = tk.Message(bottom_frame,
                                text="The last 20 characters",
                                width=200)
        txtMessage.pack(side=tk.BOTTOM)
        
        self.root.mainloop()
        
    #def __init_rButtons(self):
    

    def update_plot(self, output):
        'output must be an 8 char string being each char the state of a dot'
        'representar en formato string, e ir caracter a caracter variando rVar
        

if __name__ == '__main__':
    test_gui = Braibook_GUI()
    #test_gui.update_plot('00110101')
    #test_gui.update_plot('10010101')
