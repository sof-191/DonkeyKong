

class Paddle:
    def __init__(self, canvas, x1, y1, x2, y2, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(x1, y1, x2, y2, fill = color)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color




class Mario:
    def __init__(self, x, y, canvas, paddle1, paddle2, paddle3, paddle4, paddle5, color):
        self.canvas = canvas
        self.id = canvas.create_oval(100, 600, 140, 640, fill = color)
        self.canvas.move(self.id, 0, 0)
        self.x = 0
        self.y = 0
        self.jump = False
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)
        self.canvas.bind_all("<KeyPress-Up>", self.turn_up)
        self.canvas.bind_all("<KeyPress-Down>", self.turn_down)
        self.canvas.bind_all("<KeyPress-a>", self.enter)
        
    def draw(self):
        if self.jump == True:
            step = 5
            limit = 140
            while step <= limit:
                self.canvas.move(self.id, self.x + 10, step)
                step += 5
                print(step)
            while step >= 5:
                self.canvas.move(self.id, self.x + 10, -step)
                step -= 5
                print(step)
            self.jump = False
        self.canvas.move(self.id, self.x, self.y)
        self.x = 0
        self.y = 0
        pos = self.canvas.coords(self.id)
        print(pos)
        if pos[0] <= 0:
            self.canvas.move(self.id, 10, 0)
        if pos[1] <= 0:
            self.canvas.move(self.id, 0, 10)
        if pos[2] >= self.canvas_width:
            self.canvas.move(self.id, -10, 0)
        if 650 >= pos[3] >= 640 and pos[2] <= 1000:
            self.canvas.move(self.id, 0, -10)
        if 520 >= pos[3] >= 510 and 100 <= pos[2] <= 1000:
            self.canvas.move(self.id, 0, -10)
        if 390 >= pos[3] >= 380 and pos[2] <= 900:
            self.canvas.move(self.id, 0, -10)
        if 260 >= pos[3] >= 250 and 100 <= pos[2] <= 1000:
            self.canvas.move(self.id, 0, -10)
        if 130 >= pos[3] >= 120 and pos[2] <= 900:
            self.canvas.move(self.id, 0, -10)
        if 650 >= pos[1] >= 640 and pos[2] <= 1000:
            self.canvas.move(self.id, 0, 10)
        if 520 >= pos[1] >= 510 and 100 <= pos[2] <= 1000:
            self.canvas.move(self.id, 0, 10)
        if 390 >= pos[1] >= 380 and pos[2] <= 900:
            self.canvas.move(self.id, 0, 10)
        if 260 >= pos[1] >= 250 and 100 <= pos[2] <= 1000:
            self.canvas.move(self.id, 0, 10)
        if 130 >= pos[1] >= 120 and pos[2] <= 900:
            self.canvas.move(self.id, 0, 10)

    def turn_left(self, evt):
        self.x = -10
        
    def turn_right(self, evt):
        self.x = 10

    def turn_up(self, evt):
        self.y = -10
        
    def turn_down(self, evt):
        self.y = 10
        
    def enter(self, evt):
        self.jump = True