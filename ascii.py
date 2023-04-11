import os



from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, IntVar


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame1")




def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def back():
    window.destroy()  
    os.system('python gui.py')

def clear():
    entry_1.delete(0, 'end')

def convert():
    """Converts the given string to ascii"""
    try:
        string = entry_1.get()
        if string == "":
            messagebox.showerror("Error", "Mohon masukan string")
        else:
            ascii = [ord(c) for c in string]
            canvas.itemconfig(text, text=ascii)
    except ValueError:
        messagebox.showerror("Error", "Mohon masukan string")



window = Tk()
# Get screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate position x and y for the window to be centered
pos_x = int(screen_width / 2 - 381 / 2)
pos_y = int(screen_height / 2 - 552 / 2)

# Set the position of the window
window.geometry(f"381x552+{pos_x}+{pos_y}")
window.configure(bg = "#22252D")


window.title("Converter By xrafff.code")

canvas = Canvas(
    window,
    bg = "#22252D",
    height = 552,
    width = 381,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    122.0,
    25.0,
    anchor="nw",
    text="Konversi Ascii Ke String",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 16 * -1)
)

text = canvas.create_text(
    20.0,
    331.0,
    anchor="nw",
    text="Hasil",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 24 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    190.5,
    119.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#181818",
    fg="#FFF",
    font=("Poppins SemiBold", 16 * -1),
    highlightthickness=0
)
entry_1.place(
    x=25.0,
    y=87.0,
    width=331.0,
    height=62.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=clear,
    relief="flat"
)
button_1.place(
    x=16.0,
    y=182.0,
    width=91.0,
    height=64.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=convert,
    relief="flat"
)
button_2.place(
    x=113.0,
    y=182.0,
    width=252.0,
    height=64.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat"
)
button_3.place(
    x=16.0,
    y=18.0,
    width=38.0,
    height=38.0
)
window.resizable(False, False)
window.mainloop()
