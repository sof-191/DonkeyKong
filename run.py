import tkinter as tk
from tkinter import *
import tkinter as tk2
from PIL import Image, ImageTk
import random
import time
import threading
import math
import random
import winsound
from objects import *



def main():
    tk = Tk()
    tk.title("Monkey: Primer Proyecto Programado")
    tk.resizable(False, False) # No se puede cambiar el tamaño de la ventana
    tk.wm_attributes("-topmost", 1) #Poner esta ventana enfrente de todas las demas 
    canvas = Canvas(tk, width=1000, height=700, borderwidth =0, highlightthickness=0, bg = "#000000")
    canvas.pack()
    tk.update()


    rojoNaranja = "#FF4500"
    cian = "#00FFFF"
    azul = "#0000FF"
    amarillo = "#FFFF00"
    white = "#FFFFFF"
    black = "#000000"

    
            
    paddle1 = Paddle(canvas, 0, 640, 1000, 650, rojoNaranja)
    paddle2 = Paddle(canvas, 100, 510, 1000, 520, rojoNaranja)
    paddle3 = Paddle(canvas, 0, 380, 900, 390, rojoNaranja)
    paddle4 = Paddle(canvas, 100, 250, 1000, 260, rojoNaranja)
    paddle5 = Paddle(canvas, 0, 120, 900, 130, rojoNaranja)
    paddle6 = Paddle(canvas, 200, 640, 300, 520, cian)
    mario = Mario(200, 640, canvas, paddle1, paddle2, paddle3, paddle4, paddle5, white)



    while 1:
        mario.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)

main()