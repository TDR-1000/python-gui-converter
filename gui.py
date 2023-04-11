import os

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def binnary():
    window.destroy()  
    os.system('python binnary.py')

def decimal():
    window.destroy()  
    os.system('python decimals.py')

def octal():
    window.destroy()  
    os.system('python octal.py')

def hexa():
    window.destroy()  
    os.system('python hexa.py')

def ascii():
    window.destroy()  
    os.system('python ascii.py')

window = Tk()
# Get screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate position x and y for the window to be centered
pos_x = int(screen_width / 2 - 381 / 2)
pos_y = int(screen_height / 2 - 552 / 2)

# Set the position of the window
window.geometry(f"381x552+{pos_x}+{pos_y}")
window.configure(bg = "#3F4148")


window.title("Converter By xrafff.code")


canvas = Canvas(
    window,
    bg = "#3F4148",
    height = 552,
    width = 381,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    65.0,
    25.0,
    anchor="nw",
    text="Pilih Menu Converter",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 24 * -1)
)

button_image_bin = PhotoImage(
    file=relative_to_assets("btn_bin.png"))
button_bin = Button(
    image=button_image_bin,
    borderwidth=0,
    highlightthickness=0,
    command=binnary,
    relief="flat"
)
button_bin.place(
    x=16.0,
    y=87.0,
    width=349.0,
    height=60.0
)

button_image_dec = PhotoImage(
    file=relative_to_assets("btn_dec.png"))
button_dec = Button(
    image=button_image_dec,
    borderwidth=0,
    highlightthickness=0,
    command=decimal,
    relief="flat"
)
button_dec.place(
    x=16.0,
    y=172.0,
    width=349.0,
    height=60.0
)

button_image_octal = PhotoImage(
    file=relative_to_assets("btn_octal.png"))
button_octal = Button(
    image=button_image_octal,
    borderwidth=0,
    highlightthickness=0,
    command=octal,
    relief="flat"
)
button_octal.place(
    x=16.0,
    y=257.0,
    width=349.0,
    height=60.0
)

button_image_hexa = PhotoImage(
    file=relative_to_assets("btn_hexa.png"))
button_hexa = Button(
    image=button_image_hexa,
    borderwidth=0,
    highlightthickness=0,
    command=hexa,
    relief="flat"
)
button_hexa.place(
    x=16.0,
    y=342.0,
    width=349.0,
    height=60.0
)

button_image_ascii = PhotoImage(
    file=relative_to_assets("btn_asci.png"))
button_ascii = Button(
    image=button_image_ascii,
    borderwidth=0,
    highlightthickness=0,
    command=ascii,
    relief="flat"
)
button_ascii.place(
    x=16.0,
    y=427.0,
    width=349.0,
    height=60.0
)
window.resizable(False, False)
window.mainloop()
