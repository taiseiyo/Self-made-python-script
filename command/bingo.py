#!/usr/local/bin/python3.7
import sys
import pygame
import pyautogui
from pygame.locals import KEYUP, KEYDOWN, K_ESCAPE, K_SPACE, K_UP, QUIT
import random
import time
pygame.init()

x, y = 800, 600
font = pygame.font.Font(None, 300)
sur = pygame.display.set_mode((x, y))
fps = pygame.time.Clock()


def getnum():
    x = [i for i in range(1, 73)]
    return x


def change_number(sur, nums):  # nums[1-72]
    random.seed()
    num = random.sample(nums, 1)[0]
    text = font.render(str(num), True, (255, 255, 255))
    sur.blit(text, [x / 2 - 100, y / 2 - 100])
    pygame.display.update()


def callchange_number(sur, nums, call):
    if(call == True):
        change_number(sur, nums)
    else:
        num = random.sample(nums, 1)[0]
        text = font.render(str(num), True, (255, 255, 255))
        sur.blit(text, [x / 2 - 100, y / 2 - 100])


def mainloope(nums, call=None):
    while True:
        sur.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_SPACE:
                    call = False
                elif event.key == K_UP:
                    call = True
        callchange_number(sur, nums, call)
        fps.tick(30)


def main():
    nums = getnum()
    mainloope(nums)


main()
