import tkinter as tk
from PIL import Image, ImageTk
import random
import time
import threading
import math
import random
import winsound
from objects import *
import constants
from constants import *
from threading import Thread
from splash_animado_listo import *


def update_game(main_window):
    pass

def run_game(nivel):
    
    game_window = tk.Tk()
    game_window.title("Monkey: Primer Proyecto Programado")
    game_window.resizable(False, False) # No se puede cambiar el tamaño de la ventana
    game_window.focus_force()
    #game_window.wm_attributes("-topmost", 1) #Poner esta ventana enfrente de todas las demas 
    game_canvas = tk.Canvas(game_window, width=1000, height=700, borderwidth =0, highlightthickness=0, bg = "#000000")
    game_canvas.pack()
    
    imagen_escalera = tk.PhotoImage(file="escalera.png")
    imagen_monkey = tk.PhotoImage(file="monkey1.png")
    imagen_princesa = tk.PhotoImage(file="princesa.png")

    game_canvas.create_image(100,70, image=imagen_monkey)
    game_canvas.create_image(200,70, image=imagen_princesa)


    paddle_img900 = tk.PhotoImage(file="BarraMario900.png")
    paddle_img1000 = tk.PhotoImage(file="BarraMario1000.png")
    
    constants.score_det = Label(game_canvas, text = "Score = 0", font = ("Haettenschweiler", 20), bg="#000000", fg=white)
    constants.score_det.place(x = 870, y = 10)


    if nivel == 1:
        paddle_list = [
            Paddle(game_canvas, 0, 640, 1000, 650, paddle_img900, paddle_img1000),
            Paddle(game_canvas, 100, 510, 1000, 520, paddle_img900, paddle_img1000),
            Paddle(game_canvas, 0, 380, 900, 390, paddle_img900, paddle_img1000),
            Paddle(game_canvas, 100, 250, 1000, 260, paddle_img900, paddle_img1000),
            Paddle(game_canvas, 0, 120, 900, 130, paddle_img900, paddle_img1000)
        ]

        escalera_list = [
            game_canvas.create_image(250,580, image=imagen_escalera),
            game_canvas.create_image(800,450, image=imagen_escalera) ,
            game_canvas.create_image(400,320, image=imagen_escalera) ,
            game_canvas.create_image(650,190, image=imagen_escalera)        
        ]

    if nivel == 2:
        paddle_list = [
            Paddle(game_canvas, 0, 641, 1000, 651, paddle_img900, paddle_img1000),
            Paddle(game_canvas, 100, 548, 1000, 558, paddle_img900, paddle_img1000),
            Paddle(game_canvas, 0, 455, 1000, 465, paddle_img900, paddle_img1000),
            Paddle(game_canvas, 100, 362, 1000, 372, paddle_img900, paddle_img1000),
            Paddle(game_canvas, 0, 269, 900, 279, paddle_img900, paddle_img1000),
            Paddle(game_canvas, 100, 176, 1000, 186, paddle_img900, paddle_img1000),
            Paddle(game_canvas, 0, 120, 900, 130, paddle_img900, paddle_img1000)
        ]

        escalera_list = [
            game_canvas.create_image(250,580, image=imagen_escalera),
            game_canvas.create_image(800,450, image=imagen_escalera) ,
            game_canvas.create_image(400,320, image=imagen_escalera) ,
            game_canvas.create_image(650,190, image=imagen_escalera)        
        ]


    
    
    barrel_list = [

        Barrel(game_canvas, 130, 90, 150, 110, "#FFFF00"),
        Barrel(game_canvas, 130, 90, 150, 110, "#FFFF00"),
        Barrel(game_canvas, 130, 90, 150, 110, "#FFFF00"),
        Barrel(game_canvas, 130, 90, 150, 110, "#FFFF00"),
        Barrel(game_canvas, 130, 90, 150, 110, "#FFFF00")
    ]
    
    Barrel.start_barrels(game_canvas, barrel_list, paddle_list, 0)
    
    # b1.move_barrel(paddle_list, -1)
    
    mario = Mario(game_canvas, escalera_list, paddle_list, white)
    
    
    update_game(game_canvas)
    tk.mainloop()
    

        
if __name__ == "__main__":
    splash_animation()
    run_game(1)


