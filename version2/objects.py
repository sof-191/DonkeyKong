import time
import tkinter as tk


class Paddle:
    def __init__(self, canvas, x1, y1, x2, y2, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(x1, y1, x2, y2, fill = color)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color


class Fruit:
    def __init__(self, canvas, x1, y1, x2, y2, color):
        self.canvas = canvas
        self.id = canvas.create_oval(x1, y1, x2, y2, fill = color)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color



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
        
    def draw(self):
        
        if self.is_jumping: # Para saltar sobre las frutas, hay que agregarle algun "delay"
            step = 5
            limit = 120

            pos = self.canvas.coords(self.id)
            if 0 <= pos[2] <= 100: 
                while step <= limit:
                    self.canvas.move(self.id, self.x + 1, step)
                    step += 5
                    
                    print(step)
                while step >= 5:
                    self.canvas.move(self.id, self.x + 1, -step)
                    step -= 5
                    print(step)
                self.is_jumping = False
            if 900 <= pos[0] <= 1000: 
                while step <= limit:
                    self.canvas.move(self.id, self.x - 1, step)
                    step += 5
                    
                    print(step)
                while step >= 5:
                    self.canvas.move(self.id, self.x - 1, -step)
                    step -= 5
                    print(step)
                self.is_jumping = False
        #self.canvas.move(self.id, self.x, self.y)

        pos = self.canvas.coords(self.id)
        #print(pos)


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

    def turn_up(self, evt):
        pos = self.canvas.coords(self.id)
        if 260 >= pos[0] >= 200 and 640 >= pos[1] >= 480: 
            self.canvas.move(self.id, 0, -10)
            self.en_escalera = True

        elif 810 >= pos[0] >= 750 and 520 >= pos[1] >= 350:
            self.canvas.move(self.id, 0, -10)
            self.en_escalera = True

        elif 410 >= pos[0] >= 350 and 390 >= pos[1] >= 220:
            self.canvas.move(self.id, 0, -10)
            self.en_escalera = True

        elif 660 >= pos[0] >= 600 and 260 >= pos[1] >= 90:
            self.canvas.move(self.id, 0, -10)
            self.en_escalera = True

        elif 100 >= pos[0] >= 50 and 0 >= pos[1] >= 120:
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
        if 260 >= pos[0] >= 200 and 640 > pos[3] >= 480: 
            self.canvas.move(self.id, 0, 10)
            self.en_escalera = True

        elif 810 >= pos[0] >= 750 and 520 > pos[3] >= 350:
            self.canvas.move(self.id, 0, 10)
            self.en_escalera = True

        elif 410 >= pos[0] >= 350 and 390 > pos[3] >= 220:
            self.canvas.move(self.id, 0, 10)
            self.en_escalera = True

        elif 660 >= pos[0] >= 600 and 260 > pos[3] >= 90:
            self.canvas.move(self.id, 0, 10)
            self.en_escalera = True

        elif 100 >= pos[0] >= 50 and 0 > pos[3] >= 120:
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





if __name__ == "__main__":
    print("Please execute: run.py")