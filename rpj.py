"""
This is a desktop program used to sort pictures of racers according to their name variable.
Created by Brad Remy for JARCO Photo. October 2019
"""
import os
import time

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
        self.root.geometry('1100x600+200+150')
        self.root.configure(background='black')
        self.root.resizable(False, False)
        self.root.title('JARCO //PHOTO')

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
        # Create main canvas
        self.main_canvas = tk.Canvas(
            self.root, width=1100, height=600, background='black', highlightthickness=0, cursor='target')
        self.main_canvas.pack()

        # Background image
        with Image.open('assets\\gui_background.png') as gui_background:
            gui_background = ImageTk.PhotoImage(gui_background)
            gui_background.photo = gui_background
        self.main_canvas.create_image(550, 300, image=gui_background)

        # Main title image
        with Image.open('assets\\title_logo.gif') as title_logo:
            title_logo = ImageTk.PhotoImage(title_logo)
            title_logo.photo = title_logo
        title_logo = self.main_canvas.create_image(
            550, 250, image=title_logo, tag='title_logo')

        # Button to select working directory and fire up the main program
        self.dir_button_frame = tk.Frame(
            self.main_canvas,  highlightthickness=2)
        self.dir_button_frame.place(relx=0.5, y=500, anchor='center')
        tk.Button(self.dir_button_frame, text='SELECT IMAGE DIRECTORY...', font=(
            'courier', 18, 'bold'), command=self.select_working_directory).grid(row=0, column=0, padx=5, pady=5)
        self.subdirectory_check = tk.IntVar(value=1)
        tk.Checkbutton(self.dir_button_frame, text='Include Subdirectories',  variable=self.subdirectory_check, onvalue=1, offvalue=0).grid(
            row=1, column=0, padx=5, pady=(0, 5))
        return

    def select_working_directory(self):
        '''
        This pops up a window to select a directory with image files
        '''
        # Open selection window
        self.working_directory = str(askdirectory()).replace('/', '\\') + '\\'

        # Create image list of images in directory and subdirectories
        if self.subdirectory_check == 1:
            files = []
            start_dir = self.working_directory
            pattern = '*.jpg'

            for dir, _, _ in os.walk(start_dir):
                files.extend(glob(os.path.join(dir, pattern.lower())))
            self.image_list = natsorted(files)

        # Create image list of images just in main directory
        else:
            self.image_list = natsorted(os.listdir(self.working_directory))

        # Check for valid images in image list
        for notpic in self.image_list:
            if not (notpic.lower().endswith('jpg')):
                self.image_list.remove(notpic)

        print(len(self.image_list))

        # Check for images in list
        if len(self.image_list) > 0:
            self.main_canvas.delete('title_logo')
            self.dir_button_frame.destroy()
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
