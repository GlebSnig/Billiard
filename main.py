import random
import time
import tkinter as tk
import math
from threading import Thread


class Ball:
    def __init__(self):
        self.r = 10
        self.x0 = 300
        self.y0 = 200
        self.vx = None
        self.vy = None
        self.moveFlag = False


def drawTable():
    luzs = [(30, 30, 60, 60), (620, 30, 650, 60), (30, 380, 60, 410), (620, 380, 650, 410), (325, 30, 355, 60),
            (325, 380, 355, 410)]
    window.create_rectangle(40, 40, 640, 400, fill='white')
    for i in range(6):
        window.create_oval(luzs[i], fill='green')


def ballSpawn():
    global ballMark
    window.delete("all")
    drawTable()
    ball.x0 = random.randint(80, 600)
    ball.y0 = random.randint(80, 360)
    ballMark = window.create_oval(ball.x0 - ball.r, ball.y0 - ball.r, ball.x0 + ball.r, ball.y0 + ball.r, fill='black')


def inLuzs():
    if ball.x0 > 670 or ball.x0 < 10 or ball.y0 > 430 or ball.y0 < 10:
        return True
    # luz1
    if ball.x0 > 40 and ball.x0 < 50 and ball.y0 > 40 and ball.y0 < 50:
        return True
    # luz2
    if ball.x0 > 335 and ball.x0 < 345 and ball.y0 > 40 and ball.y0 < 50:
        return True
    # luz3
    if ball.x0 > 630 and ball.x0 < 640 and ball.y0 > 40 and ball.y0 < 50:
        return True
    # luz4
    if ball.x0 > 40 and ball.x0 < 50 and ball.y0 > 390 and ball.y0 < 400:
        return True
    # luz5
    if ball.x0 > 335 and ball.x0 < 345 and ball.y0 > 390 and ball.y0 < 400:
        return True
    # luz6
    if ball.x0 > 630 and ball.x0 < 640 and ball.y0 > 390 and ball.y0 < 400:
        return True
    return False


def setAng():
    global select_ang, angles
    if int(entry1.get()) in angles:
        select_ang = int(entry1.get())


def task():
    thr = Thread(target=move(ballMark), daemon=True)
    thr.start()


def move(ballMark):
    ball.vx = math.cos(select_ang)
    ball.vy = -math.sin(select_ang)
    while not inLuzs():
        window.delete(ballMark)
        ball.x0 += ball.vx
        ball.y0 += ball.vy
        ballMark = window.create_oval(ball.x0 - ball.r, ball.y0 - ball.r, ball.x0 + ball.r, ball.y0 + ball.r,
                                      fill='black')


def proschet():
    angles.clear()
    xyLuzs = [(45, 45), (340, 45), (635, 45), (45, 395), (340, 395), (635, 395)]
    for i in range(5, 2, -1):
        c = math.dist(xyLuzs[i], (ball.x0, ball.y0))
        b = xyLuzs[i][0] - ball.x0
        angles.append(round((math.acos(b / c)) * 180 / math.pi))
    for i in range(0, 3):
        c = math.dist(xyLuzs[i], (ball.x0, ball.y0))
        b = xyLuzs[i][0] - ball.x0
        angles.append(round((2 * math.pi - math.acos(b / c)) * 180 / math.pi))
    lAng.config(text=angles, background="white")


wx = 1100
wy = 680
select_ang = 0
angles = []
ball = Ball()
root = tk.Tk()
root.title("Бильярд")
window = tk.Canvas(root, width=wx, height=wy, background="grey")

entry1 = tk.Entry()
entry1.insert(0, "0")
entry1.place(x=270, y=540)

btSp = tk.Button(text="Создание шарика", command=ballSpawn)
btSp.place(x=70, y=450)

btSt = tk.Button(text="Удар", command=task)
btSt.place(x=70, y=530)

btAp = tk.Button(text="Просчет вектора скорости", command=proschet)
btAp.place(x=70, y=490)

btVv = tk.Button(text="Ввод", command=setAng)
btVv.place(x=400, y=537)

label1 = tk.Label(text="Углы (отсчитываются по часовой стрелке от правой нижней лузы)")
label1.place(x=270, y=450)

lAng = tk.Label(text=None, background="grey")
lAng.place(x=270, y=470)

label1 = tk.Label(text="Введите один из предложенных углов, под которым произойдет удар")
label1.place(x=270, y=510)

drawTable()
window.pack()
root.mainloop()