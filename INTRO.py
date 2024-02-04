from tkinter import *
from PIL import Image,ImageTk,ImageSequence
import time
import pygame
from pygame import mixer
mixer.init()

root = Tk()
root.geometry("1400x800")

def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global img 
    img = Image.open("sachi.gif")
    lbl = Label(root)
    lbl.place(x=0,y=0)
    i=0
    mixer.music.load("sachi.mp3")
    mixer.music.play()
    
    for img in ImageSequence.Iterator(img):
        img = img.resize((1400,800))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
    root.destroy()
    
play_gif()
root.mainloop()