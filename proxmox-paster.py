import keyboard
from tkinter import Tk

while True:
    keyboard.wait("ctrl+f12")
    cb = Tk().clipboard_get()
    keyboard.write(cb)