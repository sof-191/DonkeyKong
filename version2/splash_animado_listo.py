
from tkinter import *
import random
import time

def splash_animation(): 
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


    class Ball:
        def __init__(self, x, y, r, canvas, color):
            self.canvas = canvas
            self.x = x
            self.y = y
            self.r = r
            self.id = canvas.create_oval(self.x, self.y, self.x + 2*self.r, self.y + 2*self.r, fill = color)
            self.canvas.move(self.id, 0, 0)

            self.canvas_height = self.canvas.winfo_height()
            self.canvas_width = self.canvas.winfo_width()

            
        def draw(self):
            self.x = 0
            self.y = 0
            #self.canvas.move(self.id, self.x, self.y)
            pos = self.canvas.coords(self.id)
            #print(pos)
            if pos[0] <= 850 and 0 <= pos[1] <= 50: #derecha
                self.canvas.move(self.id, 10, 0)
            elif 750 <= pos[0] <= 950 and 0 <= pos[1] <= 550: #baje
                self.canvas.move(self.id, 0, 10)
            elif 50 <= pos[0] <= 1050 and   pos[1] >= 500: #izquierda
                self.canvas.move(self.id, -10, 0)
            elif pos[0] <= 200 and pos[1] >= 50: #suba
                self.canvas.move(self.id, 0, -10)

    label1 = Label(canvas, text = "Monkey", font = ("Haettenschweiler", 200), bg="#000000", fg="#FFFF00")
    label1.place(x=165, y=200)


    ball = Ball(25, 25, 50, canvas, rojoNaranja)
    ball1 = Ball(175, 25, 50, canvas, cian)
    ball2 = Ball(325, 25, 50, canvas, white)
    ball3 = Ball(475, 25, 50, canvas, rojoNaranja)
    ball4 = Ball(625, 25, 50, canvas, cian)
    ball5 = Ball(775, 25, 50, canvas, white)
    ball6 = Ball(850, 150, 50, canvas, rojoNaranja)
    ball7 = Ball(850, 300, 50, canvas, cian)
    ball8 = Ball(850, 450, 50, canvas, white)
    ball9 = Ball(800, 550, 50, canvas, rojoNaranja)
    ball10 = Ball(650, 550, 50, canvas, cian)
    ball11 = Ball(500, 550, 50, canvas, white)
    ball12 = Ball(350, 550, 50, canvas, rojoNaranja)
    ball13 = Ball(200, 550, 50, canvas, cian)
    ball14 = Ball(25, 210, 50, canvas, white)
    ball15 = Ball(25, 360, 50, canvas, rojoNaranja)
    ball16 = Ball(25, 510, 50, canvas, cian)



    end_time = time.time() + 5
    is_running = time.time() <= end_time
    while is_running: 
        ball.draw()
        ball1.draw()
        ball2.draw()
        ball3.draw()
        ball4.draw()
        ball5.draw()
        ball6.draw()
        ball7.draw()
        ball8.draw()
        ball9.draw()
        ball10.draw()
        ball11.draw()
        ball12.draw()
        ball13.draw()
        ball14.draw()
        ball15.draw()
        ball16.draw()

        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
        is_running = time.time() <= end_time
    
    tk.destroy()

    return 