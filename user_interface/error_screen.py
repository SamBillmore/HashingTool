from tkinter import Frame
from tkinter import Button
from tkinter import Label

from user_interface.resource_path import ResourcePath

class ErrorScreen(Frame,ResourcePath):
    """
    Screen for showing errors in data import
    """
    
    def __init__(self, parent, controller, background_col, foreground_col, font):
        """
        Initialise the error screen
        """
        Frame.__init__(self, parent, bg=background_col)
        self.controller = controller
        self.parent = parent

        self.intro_label = Label (self, text='There has been an error generating the file containing the hash.\nPlease ensure you do not have the file open.', bg=background_col, fg=foreground_col, font=font, justify='left')
        self.back_button = Button (self, text='Back', width=19, command=lambda: self.controller.show_frame('HomeScreen'))

        self.intro_label.grid(row=0, column=0, sticky='W', padx=25, pady=20, columnspan=2)
        self.back_button.grid(row=1, column=0, sticky='W', padx=25, pady = 20)