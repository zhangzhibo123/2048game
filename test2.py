import random
import sys
import pygame
from pygame.locals import *


PIXEL = 100  # block宽度
SCORE_PIXEL = 100
SIZE = 4

pygame.init()   # 初始化
screen = pygame.display.set_mode((PIXEL * SIZE, PIXEL * SIZE + SCORE_PIXEL)) # 创建屏幕对象 长,宽
pygame.display.set_caption("2048")  # 标题

block = [pygame.Surface((PIXEL, PIXEL)) for i in range(2)] # 创建2个surface block对象
# 设置颜色
block[0].fill((152, 251, 152))
block[1].fill((240, 255, 255))

score_block = pygame.Surface((PIXEL * SIZE, SCORE_PIXEL))# 创建一个分数显示surface对象
score_block.fill((175, 240, 240))
screen.blit(score_block, (0, PIXEL * SIZE))


for i in range(SIZE): # 左上角坐标为(0,0)
    for j in range(SIZE):
        # 背景颜色块 往屏幕上放置Surface block对象
        screen.blit(block[(i + j) % 2] , (PIXEL * j, PIXEL * i))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:# 右上角X
            pygame.quit()
            sys.exit()

    pygame.display.update()