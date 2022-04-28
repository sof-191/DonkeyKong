from concurrent.futures.process import _ThreadWakeup
import time
import tkinter as tk
from constants import *
import constants
import random



class Paddle:


    def __init__(self, canvas, x1, y1, x2, y2, imagen900, imagen1000):
        self.canvas = canvas
        if (x2-x1) == 1000:
            self.img = canvas.create_image((x2+x1)//2, (y2+y1)//2, image=imagen1000)
        else:
            self.img = canvas.create_image((x2+x1)//2, (y2+y1)//2, image=imagen900)
            
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        


class Barrel:
    def __init__(self, canvas, x1, y1, x2, y2, color):
        self.canvas = canvas
        self.id = canvas.create_oval(x1, y1, x2, y2, fill = white)
        self.color = color
        self.moving = False

    def start_barrels(canvas, barrel_list, paddle_list, i, mario):
        delta_time = 1000
        chance_to_throw = 0.333
        if i >= len(barrel_list):
            canvas.after(delta_time, Barrel.start_barrels, canvas, barrel_list, paddle_list, 0, mario)
        else: 
            if (barrel_list[i].moving):
                canvas.after(delta_time, Barrel.start_barrels, canvas, barrel_list, paddle_list, i + 1, mario)
            else:
                if (random.random() < chance_to_throw):
                    barrel_list[i].moving = True
                    barrel_list[i].move_barrel(paddle_list, -1, mario)
                    canvas.after(delta_time, Barrel.start_barrels, canvas, barrel_list, paddle_list, i + 1, mario)
                else:
                    canvas.after(delta_time, Barrel.start_barrels, canvas, barrel_list,paddle_list, i, mario)
    
        
    def move_barrel(self, paddle_list, i, mario):
        
        barrel_x1, barrel_y1, barrel_x2, barrel_y2 = self.canvas.coords(self.id)
        distance = 10
        delta_time = 10

        menos_i = i * - 1
        if (len(paddle_list) == menos_i) and \
            ((barrel_x1 < 0) or (barrel_x2 > 1000) or (barrel_y1 < 0) or (barrel_y2 > 700)):
            self.canvas.move(self.id, 130 - barrel_x1, 90- barrel_y1)
           # self.canvas.after(delta_time, self.move_barrel, paddle_list, -1, mario)
            self.moving = False
            constants.score += constants.score_gain
            constants.score_det.configure(text= ("Score = " + str(constants.score)) )
            
        else:

            if  menos_i % 2 == 0:
                if barrel_x1 <= 0:
                    self.canvas.move(self.id, 0, distance)
                else:
                    self.canvas.move(self.id, -distance, 0)
            else:
                if barrel_x2 >= 1000:
                    self.canvas.move(self.id, 0, distance)
                else:
                    self.canvas.move(self.id, distance, 0)

            barrel_x1, barrel_y1, barrel_x2, barrel_y2 = self.canvas.coords(self.id)
            mario_x1, mario_y1, mario_x2, mario_y2 = self.canvas.coords(mario.id)
            if ((mario_x1 < barrel_x2) and (mario_y1 < barrel_y2) and (mario_x2 > barrel_x1) and (mario_y2 > barrel_y1)):
                constants.lifes -= 1
                if constants.lifes == 0:
                    constants.lose = True


            


            if (len(paddle_list) != menos_i) and (barrel_y2 >= paddle_list[i-1].y1):
                i = i - 1 # Actualizo el paddle en el cual me encuentro

            self.canvas.after(delta_time, self.move_barrel, paddle_list, i, mario)
        

class Mario:
    def __init__(self, game_canvas, escalera_list, paddle_list, color, x1 = 100, y1 = 600, x2 = 140, y2 = 640):
        self.canvas = game_canvas
        self.id = game_canvas.create_oval(x1, y1, x2, y2, fill = color)
        self.escaleras_list = escalera_list
        self.en_escalera = False
        self.is_jumping = False
        self.paddle_list = paddle_list
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)
        self.canvas.bind_all("<KeyPress-Up>", self.turn_up)
        self.canvas.bind_all("<KeyPress-Down>", self.turn_down)
        self.canvas.bind_all('<Return>', self.enter)
        
   

    def turn_left(self, evt):
        if not self.en_escalera:
            self.canvas.move(self.id, -10, 0)
            mario_x1, _, _ , _ = self.canvas.coords(self.id)
            current_paddle_i = self.get_current_paddle(0)

            if current_paddle_i != -1:
                current_paddle = self.paddle_list[ current_paddle_i ]
                paddle_x1 = current_paddle.x1
                if mario_x1 < paddle_x1:
                    self.canvas.move(self.id, paddle_x1 - mario_x1, 0)


    def turn_right(self, evt):
        if not self.en_escalera:
            self.canvas.move(self.id, 10, 0)
            _, _, mario_x2, _ = self.canvas.coords(self.id)
            current_paddle_i = self.get_current_paddle(0)

            if current_paddle_i != -1:
                current_paddle = self.paddle_list[ current_paddle_i ]
                paddle_x2 = current_paddle.x2
                if mario_x2 > paddle_x2:
                    self.canvas.move(self.id, paddle_x2 - mario_x2, 0)


    def i_am_in_a_stair(self, i, going_up):
        if i >= len(self.escaleras_list):
            return False
        
        STAIR_WIDTH = 100
        STAIR_HEIGHT = 120

        STAIR_WIDTH_HALF = STAIR_WIDTH // 2
        STAIR_HEIGHT_HALF = STAIR_HEIGHT // 2

        mario_x1, mario_y1, mario_x2, mario_y2 = self.canvas.coords(self.id)
        
        MARIO_HEIGHT = (mario_y2 - mario_y1)

        escalera_x, escalera_y = self.canvas.coords(self.escaleras_list[i])
        escalera_x1, escalera_y1, escalera_x2, escalera_y2 =                 \
            escalera_x - STAIR_WIDTH_HALF, escalera_y - STAIR_HEIGHT_HALF - MARIO_HEIGHT,   \
            escalera_x + STAIR_WIDTH_HALF, escalera_y + STAIR_HEIGHT_HALF

        if not going_up:
            escalera_y1 -= 10
            escalera_y2 -= 10

        if (mario_x1 >= escalera_x1) and (mario_x2 <= escalera_x2) and \
             (mario_y1 >= escalera_y1) and (mario_y2 <= escalera_y2):
            return True

        else:
            return self.i_am_in_a_stair(i + 1, going_up)



    def turn_up(self, evt):
        pos = self.canvas.coords(self.id)

        if self.i_am_in_a_stair(0, True):
            self.canvas.move(self.id, 0, -10)
            self.en_escalera = True


        #Si estoy en algún paddle, entonces no estoy en la escalera porque ya termine de subir.
        if self.get_current_paddle(0) != -1: 
            self.en_escalera = False





        


    def get_current_paddle(self, i):
        """
        |   Verifica en cuál paleta/paddle estoy
        |
        |   i : contador de la paleta actual a verificar, empieza en 0
        """
        _, _, _ , mario_y2 = self.canvas.coords(self.id)
        if i >= len(self.paddle_list):
            return -1
        elif self.paddle_list[i].y1 == mario_y2:
            return i
        else:
            return self.get_current_paddle(i+1)
            

    def turn_down(self, evt):
        pos = self.canvas.coords(self.id)
        if self.i_am_in_a_stair(0, False):
            self.canvas.move(self.id, 0, 10)
            self.en_escalera = True
        
        #Si estoy en algún paddle, entonces no estoy en la escalera porque ya termine de subir.
        if self.get_current_paddle(0) != -1: 
            self.en_escalera = False
   
    
    def jump(self, step, going_up):
        
        limit = 5
        if going_up:
            speed = -10
        else:
            speed = 10
        if step <= limit:
            self.canvas.move(self.id, 0, speed)
        else:
            going_up = False
            step = 0
       
        if  (going_up == False and step >= limit): #Ya llegue de vuelta al piso
            self.canvas.move(self.id, 0, speed)
            self.is_jumping = False
        else:
            self.canvas.after(30, self.jump, step + 1, going_up)
     
        


    def enter(self, evt):
       if self.is_jumping == False:
           self.jump(0, True)




