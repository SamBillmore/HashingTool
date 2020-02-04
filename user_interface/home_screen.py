from tkinter import Frame
from tkinter import Button
from tkinter import Label
from tkinter import Entry
from tkinter import PhotoImage
import pyperclip

from user_interface.resource_path import ResourcePath
from hash_class.hash_file import FileHasher

class HomeScreen(Frame,ResourcePath):
    """
    The home screen for the program
    """

    def __init__(self, parent, controller, background_col, foreground_col, font):
        """
        Layout for the home screen
        """
        Frame.__init__(self, parent, bg=background_col)
        self.controller = controller
        self.parent = parent
        self.picture_path = './/user_interface//home_screen_pic.png'

        self.logo = PhotoImage(file=self.resource_path(self.picture_path))

        self.picture = Label (self, image=self.logo, borderwidth=0, highlightthickness=0)
        self.picture.image = self.logo
        self.description_label = Label (self, text="This tool uses the SHA-256 algorithm to generate a target file's hash value.\n\nIt saves details of the hashed file to a .txt file in the same location and sets the target file to \nread-only.", bg=background_col, fg=foreground_col, font=font, justify='left')
        self.file_label = Label (self, text='Select file for hashing: ', bg=background_col, fg=foreground_col, font=font)
        self.file_entry = Entry (self, width=55)
        self.file_button = Button (self, text='Browse', width=6, command=lambda: self.controller.browse_file(self.file_entry))
        self.hash_button = Button (self, text='Hash file', width=19, command=lambda: self.hash_file(self.file_entry.get()))
        self.hash_output_label = Label (self, text='Hash: ', bg=background_col, fg=foreground_col, font=font)
        self.copy_button = Button (self, text='Copy to clipboard', width=19, command=lambda: self.copy_to_clipboard(self.hashed_file))

        self.picture.grid(row=0, column=0, sticky='W', padx = 25, pady = 5, columnspan=3)
        self.description_label.grid(row=2, column=0, sticky='W', padx = 25, pady = 15, columnspan=3)
        self.file_label.grid(row=3, column=0, sticky='W', padx=25, pady=20)
        self.file_entry.grid(row=3, column=1, sticky='E', padx=0, pady=0)
        self.file_button.grid(row=3, column=2, sticky='E', padx=0, pady=0)
        self.hash_button.grid(row=4, column=1, sticky='E', padx=0, pady=15)
        self.hash_output_label.grid(row=5, column=0, sticky='W', padx=25, pady=15, columnspan=3)
        self.copy_button.grid(row=6, column=1, sticky='E', padx=0, pady=15)

    def hash_file(self, file_path):
        """
        Hash the file
        Update screen to show results
        """
        file_hasher = FileHasher()
        self.hashed_file = file_hasher.hash_file(file_path)
        txt_doc_created = file_hasher.save_to_txt(file_path,self.hashed_file)
        if txt_doc_created:
            self.hash_output_label['text'] = 'Hash: ' + self.hashed_file
        else:
            self.controller.show_frame('ErrorScreen')

    def copy_to_clipboard(self, string_to_copy):
        """
        Copies string to clipboard
        """
        pyperclip.copy(string_to_copy)