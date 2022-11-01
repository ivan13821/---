import pygame
import sys
from func import *

def draw_interfase():
    pygame.draw.rect(screen, WHITE, title_rec)
    font = pygame.font.SysFont('arial', 70)
    pretty_print(mas)
    for row in range(blocks):
        for col in range(blocks):
            value = mas[row][col]
            text = font.render(f'{value}', True, WHITE)
            w = col * size_block + (col + 1) * margin
            h = row * size_block + (row + 1) * margin + 110
            pygame.draw.rect(screen, colours[value], (w, h, size_block, size_block))
            if value != 0:
                font_w, font_h = text.get_size()
                text_w = w + (size_block - font_w) / 2
                text_h = h + (size_block - font_h) / 2
                screen.blit(text, (text_w, text_h))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GREY = (130, 130, 130)

colours = {
    0: (130, 130, 130),
    2: (128, 0, 0),
    4: (255, 160, 122),
    8: (220,20,60),
    16: (205,92,92),
    32: (255, 160, 122),
    64: (255, 215,0),
    128:(238, 232, 170),
    256: (128,128,0),
    512: (107, 142,35),
    1028: (0,100,0),
    2056: (0,250,154),

}

pygame.init()
mas = [[0]*blocks for i in range(blocks)]
size_block = 110
margin = 10
weight = size_block * blocks + margin*(blocks+1)
height = size_block * blocks + margin*(blocks+1) + 110
title_rec = pygame.Rect(0, 0, weight, 110)

mas[1][2] = 2
mas[3][0] = 4
print(get_empty_list(mas))
pretty_print(mas)


screen = pygame.display.set_mode((weight, height))
pygame.display.set_caption('2048')

draw_interfase()

text_score = pygame.font.SysFont('arial', 40)
text2 = text_score.render(f'You score: {score(mas)}', True, BLACK)
text_rect = text2.get_rect()
screen.blit(text2, (10, 30))
pygame.display.update()

pygame.display.update()
while is_zero_in_mas(mas) or can_move(mas):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mas = move_left(mas)
            elif event.key == pygame.K_RIGHT:
                mas = move_right(mas)
            elif event.key == pygame.K_UP:
                mas = move_up(mas)
            elif event.key == pygame.K_DOWN:
                mas = move_down(mas)
            pygame.draw.rect(screen, WHITE, title_rec)
            font = pygame.font.SysFont('arial', 70)
            pretty_print(mas)
            for row in range(blocks):
                for col in range(blocks):
                    value = mas[row][col]
                    text = font.render(f'{value}', True, WHITE)
                    w = col*size_block + (col + 1)*margin
                    h = row * size_block + (row + 1) * margin + 110
                    pygame.draw.rect(screen, colours[value], (w, h, size_block, size_block))
                    if value != 0:
                        font_w, font_h = text.get_size()
                        text_w = w + (size_block - font_w)/2
                        text_h = h + (size_block - font_h) / 2
                        screen.blit(text, (text_w, text_h))

            empty = get_empty_list(mas)
            random.shuffle(empty)
            num = empty.pop()
            x, y = get_index_from_number(num)
            mas = insert_2_or_4(mas, x, y)
            print(f'Мы заполнили элемент под номером {num}')
            draw_interfase()

            text_score = pygame.font.SysFont('arial', 40)
            text2 = text_score.render(f'You score: {score(mas)}', True, BLACK)
            text_rect = text2.get_rect()
            screen.blit(text2, (10, 30))
            pygame.display.update()
