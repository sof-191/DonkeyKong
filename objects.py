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
    def __init__(self, game_canvas, paddle_list, color, x1 = 100, y1 = 600, x2 = 140, y2 = 640):
        self.canvas = game_canvas
        self.id = game_canvas.create_oval(x1, y1, x2, y2, fill = color)
    
        self.current_paddle = 0

        #self.delta_x = 0
        #self.delta_y = 0
        self.jump = False
        self.paddle_list = paddle_list
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)
        self.canvas.bind_all("<KeyPress-Up>", self.turn_up)
        self.canvas.bind_all("<KeyPress-Down>", self.turn_down)
        self.canvas.bind_all("<KeyPress-a>", self.enter)
        
    def draw(self):
        
        if self.jump: # Para saltar sobre las frutas, hay que agregarle algun "delay"
            step = 5
            limit = 120
            self.x = 0
            self.y = 0
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
                self.jump = False
            if 900 <= pos[0] <= 1000: 
                while step <= limit:
                    self.canvas.move(self.id, self.x - 1, step)
                    step += 5
                    
                    print(step)
                while step >= 5:
                    self.canvas.move(self.id, self.x - 1, -step)
                    step -= 5
                    print(step)
                self.jump = False
        #self.canvas.move(self.id, self.x, self.y)
        self.x = 0
        self.y = 0
        pos = self.canvas.coords(self.id)
        #print(pos)
        if pos[0] <= 0:
            self.canvas.move(self.id, 10, 0)
        if pos[1] <= 0:
            self.canvas.move(self.id, 0, 10)
        if pos[2] >= 1000:
            self.canvas.move(self.id, -10, 0)
        if 650 >= pos[3] >= 640 and pos[2] <= 1000:
            self.canvas.move(self.id, 0, -10)
        if 520 >= pos[3] >= 510 and 100 <= pos[2] <= 200 or 260 <= pos[2] <= 1000:
            self.canvas.move(self.id, 0, -10)
        if 390 >= pos[3] >= 380 and 0 <= pos[2] <= 750 and 810 <= pos[2] <= 900:
            self.canvas.move(self.id, 0, -10)
        if 260 >= pos[3] >= 250 and 100 <= pos[2] <= 350 and 410<= pos[2] <= 1000:
            self.canvas.move(self.id, 0, -10)
        if 130 >= pos[3] >= 120 and 0 <= pos[2] <= 50 and 100 <= pos[2] <= 900:
            self.canvas.move(self.id, 0, -10)
        if 650 >= pos[1] >= 640 and pos[2]  <= 1000:
            self.canvas.move(self.id, 0, 10)
        if 520 >= pos[1] >= 510 and 100 <= pos[2] <= 200 or 260 <= pos[2] <= 1000:
            self.canvas.move(self.id, 0, 10)
        if 390 >= pos[1] >= 380 and 0 <= pos[2] <= 750 and 810 <= pos[2] <= 900:
            self.canvas.move(self.id, 0, 10)
        if 260 >= pos[1] >= 250 and 100 <= pos[2] <= 350 and 410<= pos[2] <= 1000:
            self.canvas.move(self.id, 0, 10)
        if 130 >= pos[1] >= 120 and 0 <= pos[2] <= 50 and 100 <= pos[2] <= 900:
            self.canvas.move(self.id, 0, 10)

    def turn_left(self, evt):
        self.canvas.move(self.id, -10, 0)
        
    def turn_right(self, evt):
        self.canvas.move(self.id, 10, 0)

    def turn_up(self, evt):
        self.x = 0
        self.y = 0
        pos = self.canvas.coords(self.id)
        if 260 >= pos[0] >= 200 and 640>= pos[1] >= 480: 
            self.canvas.move(self.id, 0, -10)
        elif 810 >= pos[0] >= 750 and 520 >= pos[1] >= 350:
            self.canvas.move(self.id, 0, -10)
        elif 410 >= pos[0] >= 350 and 390 >= pos[1] >= 220:
            self.canvas.move(self.id, 0, -10)
        elif 660 >= pos[0] >= 600 and 260 >= pos[1] >= 90:
            self.canvas.move(self.id, 0, -10)
        elif 100 >= pos[0] >= 50 and 0 >= pos[1] <= 120:
            self.canvas.move(self.id, 0, -10)


    def turn_down(self, evt):
        self.canvas.move(self.id, 0, 10)
        
    def enter(self, evt):
        self.jump = True

    def check_paddles(self):
        p0 = self.paddle_list[0]
        p1 = self.paddle_list[1]
        p2 = self.paddle_list[2]
        p3 = self.paddle_list[3]
        p4 = self.paddle_list[4]


if __name__ == "__main__":
    print("Please execute: run.py")