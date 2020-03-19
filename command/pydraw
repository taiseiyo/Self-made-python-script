#!/usr/bin/env python3
# Copyright (c) 2020, Suzuki Taisei.
# All rights reserved.
#
# $Id: kg_lib.py,v 1.32 2020/03/25 07:50:31 suzuki

import sys
import pygame as pg
from pygame.locals import QUIT, MOUSEBUTTONDOWN, MOUSEMOTION, MOUSEBUTTONUP, KEYDOWN, K_SPACE, K_ESCAPE, K_UP, K_LEFT, K_RIGHT, K_DOWN
import pyautogui
import subprocess

window_x, window_y = pyautogui.size()
window = (int(window_x/2), window_y)
surface = pg.display.set_mode((window))
white = (255, 255, 255)
pg.init()


def draw(mousepos):
    fpsclock = pg.time.Clock()
    for i, j in mousepos:
        pg.draw.circle(surface, (255, 0, 0), (i, j), 5)
    fpsclock.tick(25)
    pg.display.update()


def erase_draw(mousepos):
    fpsclock = pg.time.Clock()
    for i, j in mousepos:
        pg.draw.circle(surface, white, (i, j), 12)
    fpsclock.tick(30)
    pg.display.update()


def mainloope(mousepos, mouse=False, mode=True):
    count = 0
    while True:
        for get in pg.event.get():

            if(get.type == KEYDOWN):
                if(get.key == K_SPACE):
                    surface.fill(white)
                elif(get.key == K_ESCAPE):
                    pg.quit()
                    sys.exit()
                elif(get.key == K_UP):
                    cmd = "scrot photo" + str(count)+".png"
                    subprocess.call(cmd.split())
                    count = count + 1
                elif(get.key == K_RIGHT):
                    mode = True
                elif(get.key == K_LEFT):
                    mode = False

            if(get.type == MOUSEBUTTONDOWN):
                mouse = True
            elif(get.type == MOUSEBUTTONUP):
                mouse = False
                mousepos.clear()
            elif(get.type == MOUSEMOTION
                 and mouse):
                mousepos.append(get.pos)

        draw(mousepos) if mode == True else erase_draw(mousepos)


def main():
    mousepos = []
    surface.fill(white)
    mainloope(mousepos)


main()
