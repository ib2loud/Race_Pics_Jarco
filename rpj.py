"""
This is a desktop program used to sort pictures of racers according to their name variable.
Created by Brad Remy for JARCO Photo. October 2019
"""
import os

from glob import glob
from natsort import natsorted
from PIL import Image, ImageTk
from tkinter import messagebox, ttk
from tkinter.filedialog import askdirectory
from ttkthemes import ThemedTk

import tkinter as tk


class Jarco:
    def __init__(self):
        # Create main window
        self.root = tk.Tk()
        self.root.geometry('1200x800+200+150')
        self.root.configure(background='white')
        self.root.resizable(False, False)
        self.root.title('JARCO //PICS')

        # Call function to create title screen
        self.start_page()

        # Run main loop
        self.root.mainloop()

    def __repr__(self):
        return 'GOTTA GO FAST!'

    def start_page(self):
        '''
        This creates the start page with the big logo and the directory selection widget
        '''
        # Create frame to hold widgets
        self.title_window = tk.Frame(
            self.root, width=800, height=600, background='white')
        self.title_window.place(relx=0.5, rely=0.5, anchor='center')

        # Show title image
        with Image.open('assets\\title_logo.png') as title_logo:
            title_logo = ImageTk.PhotoImage(title_logo)
            title_logo.photo = title_logo
        tk.Label(self.title_window, image=title_logo,
                 borderwidth=0).grid(row=0, column=0)
        tk.Button(self.title_window, text='SELECT IMAGE DIRECTORY...',
                  font=('courier', 18), command=self.select_working_directory).grid(row=1, column=0, pady=20)
        return

    def select_working_directory(self):
        '''
        This pops up a window to select a directory with image files
        '''
        # Open selection window
        self.working_directory = str(askdirectory()).replace('/', '\\') + '\\'

        # Create image list of images in directory and subdirectories
        files = []
        start_dir = self.working_directory
        pattern = '*.JPG'

        for dir, _, _ in os.walk(start_dir):
            files.extend(glob(os.path.join(dir, pattern.upper())))
        self.image_list = natsorted(files)

        if len(self.image_list) > 0:
            self.title_window.destroy()
            self.create_windows()
        else:
            messagebox.showerror(
                'No Photos', f'No photos were found in {self.working_directory}.')
        return

    def create_windows(self):
        '''
        This creates the main program windows and widgets
        '''
        return


# Run program
if __name__ == '__main__':
    Jarco()
