import tkinter as tk
from PIL import Image, ImageTk
import random
import time
import threading
import math
import random
import winsound
from objects import *


def update_game(main_window):
    pass

def run_game():
    game_window = tk.Tk()
    game_window.title("Monkey: Primer Proyecto Programado")
    game_window.resizable(False, False) # No se puede cambiar el tamaño de la ventana
    game_window.wm_attributes("-topmost", 1) #Poner esta ventana enfrente de todas las demas 
    game_canvas = tk.Canvas(game_window, width=1000, height=700, borderwidth =0, highlightthickness=0, bg = "#000000")
    game_canvas.pack()
    
    imagen_escalera = tk.PhotoImage(file="escalera.png")
    game_canvas.create_image(250,580, image=imagen_escalera) 

    rojoNaranja = "#FF4500"
    cian = "#00FFFF"
    azul = "#0000FF"
    amarillo = "#FFFF00"
    white = "#FFFFFF"
    black = "#000000"

    paddle_list = [
        Paddle(game_canvas, 0, 640, 1000, 650, rojoNaranja),
        Paddle(game_canvas, 100, 510, 1000, 520, rojoNaranja),
        Paddle(game_canvas, 0, 380, 900, 390, rojoNaranja),
        Paddle(game_canvas, 100, 250, 1000, 260, rojoNaranja),
        Paddle(game_canvas, 0, 120, 900, 130, rojoNaranja)
    ]
            
    
    mario = Mario(game_canvas, paddle_list, white)

    update_game(game_canvas)


    tk.mainloop()

        
if __name__ == "__main__":
    run_game()