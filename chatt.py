import tkinter 
from tkinter import *
import os
from PIL import Image, ImageDraw, ImageTk, ImageFont
from log import *
# Designing window for registration
 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    opening(main_screen)
    main_screen.mainloop()
 
main_account_screen()