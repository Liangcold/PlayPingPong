import pygame as pg
from time import sleep
import sys

pg.init()  # initialize or error in wordfont & so on
scr = pg.display.set_mode((600, 550))  # set size of scr
pg.display.set_caption(("play pingpong"))  # set scr tit
pingpong = 255, 140, 0  # pinppong color
green = 0, 255, 0
white = 255, 255, 255
cs = 225, 121, 21

x = 120
y = 120
vx = 1
vy = 1
a = 200

zt1 = pg.font.SysFont('stkaiti', 24)
zt2 = pg.font.SysFont('stkaiti', 20)


def printtext(font, text, x, y, color):
    img = font.render(text, True, color)
    scr.blit(img, (x, y))


c = 0  # accelerate after 3times
pts = 0  # pts add score everytime catch
k = 1  # Base plus component

while True:
    scr.fill((199, 21, 133))
    for eve in pg.event.get():
        if eve.type == pg.QUIT:
            sys.exit()
    mx, my = pg.mouse.get_pos()  # get mouse loc
    a = mx  # mouse loc= pingpong board loc
    pg.draw.circle(scr, pingpong, (x, y), 40, 0)
    pg.draw.rect(scr, green, (a, 530, 100, 20), 0)
    x = x + vx
    y = y + vy
    if x > 550 or x < 40:
        vx = -vx
    if y < 40:
        vy = -vy
    if y > 510 and abs(a - x + 50) < 50:
        if vy > 0:
            vy = -vy
        else:
            pass
        c = c + 1  # accelerate after 3times
        pts = pts + k  # get pts
        if c >= 3:
            c = 0
            k = k + k  # dou pts af accelerate
            if vx > 0:  # accelerate
                vx = vx + 1
            else:
                vx = vx - 1
        else:
            pass
    elif y > 510 and abs(a - x + 50) > 50:
        break
    sleep(0.005)
    printtext(zt1, "移动鼠标控制乒乓板左右移动", 20, 30, white)
    printtext(zt2, "得分", 550, 12, cs)
    printtext(zt2, str(pts), 560, 32, cs)
    pg.display.update()

scr.fill((211, 21, 33))  # game over and catch color
zt3 = pg.font.SysFont('stkaiti', 120)
zt4 = pg.font.SysFont('stkaiti', 60)
printtext(zt3, "game over", 60, 120, white)
printtext(zt4, 'score: ' + str(pts), 120, 400, white)
pg.display.update()
sleep(2)
