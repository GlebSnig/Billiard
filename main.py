import random
import time
import tkinter as tk
import math

class Ball:
    def __init__(self):
        self.r = 10
        self.x0 = 300
        self.y0 = 200
        self.vx = None
        self.vy = None
        self.moveFlag = False

def drawTable():
    luzs = [(30, 30, 60, 60), (620, 30, 650, 60), (30, 380, 60, 410), (620, 380, 650, 410), (325, 30, 355, 60), (325, 380, 355, 410)]
    window.create_rectangle(40, 40, 640, 400, fill='white')
    for i in range(6):
        window.create_oval(luzs[i], fill='green')
    window.create_oval(ball.x0 - ball.r, ball.y0 - ball.r, ball.x0 + ball.r, ball.y0 + ball.r, fill='black')

def ballSpawn():
    ball.x0 = random.randint(80, 600)
    ball.y0 = random.randint(80, 360)

def inLuzs(testBall):
    #luz1
    if testBall.x0 > 40 and testBall.x0 < 50 and testBall.y0 > 40 and testBall.y0 < 50:
        return True
    # luz2
    if testBall.x0 > 335 and testBall.x0 < 345 and testBall.y0 > 40 and testBall.y0 < 50:
        return True
    # luz3
    if testBall.x0 > 630 and testBall.x0 < 640 and testBall.y0 > 40 and testBall.y0 < 50:
        return True
    # luz4
    if testBall.x0 > 40 and testBall.x0 < 50 and testBall.y0 > 390 and testBall.y0 < 400:
        return True
    # luz5
    if testBall.x0 > 335 and testBall.x0 < 345 and testBall.y0 > 390 and testBall.y0 < 400:
        return True
    # luz6
    if testBall.x0 > 630 and testBall.x0 < 640 and testBall.y0 > 390 and testBall.y0 < 400:
        return True

    return False

def proschet():
    angles = []
    xyLuzs = [(45, 45), (340, 45), (635, 45), (45, 395), (340, 395), (635, 395)]
    for i in range(5, 2, -1):
        c = math.dist(xyLuzs[i], (ball.x0, ball.y0))
        b = xyLuzs[i][0] - ball.x0
        angles.append(round((math.acos(b / c)) * 180 / math.pi))
    for i in range(0, 3):
        c = math.dist(xyLuzs[i], (ball.x0, ball.y0))
        b = xyLuzs[i][0] - ball.x0
        angles.append(round((2 * math.pi - math.acos(b / c)) * 180 / math.pi))
    lAng.config(text= angles, background= "white")

wx = 1100
wy = 680
ball = Ball()
root = tk.Tk()
root.title("Бильярд")
maxStrike = None

window = tk.Canvas(root, width=wx, height=wy, background="grey")

btSp = tk.Button(text="Spawn ball", command=ballSpawn)
btSp.place(x=70, y=450)

btAp = tk.Button(text="Просчет траектории", command= proschet)
btAp.place(x=200, y=450)

label1 = tk.Label(text="Углы (отсчитываются по часовой стрелке с правой нижней лузы)")
label1.place(x=200, y=490)

lAng = tk.Label(text=None, background= "grey")
lAng.place(x=200, y=520)

while True:
    window.delete('all')
    drawTable()
    window.pack()
    if ball.moveFlag:
        ball.x0 += ball.vx
        ball.y0 += ball.vy
    root.update()
    time.sleep(0.001)
root.mainloop()