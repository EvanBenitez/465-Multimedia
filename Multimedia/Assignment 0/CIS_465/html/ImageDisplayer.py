# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 17:11:54 2021

@author: Evan Benitez
"""

import tkinter as tk
from PIL import Image, ImageTk

def Display():
    load = Image.open(pathBox.get())
    print(load)
    load = load.resize((200,200))
    render = ImageTk.PhotoImage(load)
    print(render)
    picture = tk.Label(app, image=render)
    print(picture)
    picture.image = render
    picture.place(x=150,y=70)

app = tk.Tk()
app.title("Image Displayer")
app.geometry("500x300")

textInstruction = tk.Label(app, font="size 13", text="Enter image file Path")
textInstruction.place(x=160, y=20)

pathBox = tk.Entry(app, width=25)
pathBox.place(x=160, y=40)
pathBox.insert(0, "images/CSU_Logo.jpg")

btn = tk.Button(app, text="Dispaly", width="10", command=Display)
btn.place(x=317, y=36)

picture = tk.Label(app)


if __name__ == "__main__":
    app.mainloop()
    
