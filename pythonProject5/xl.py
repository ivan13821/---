import pygame
import sys
from func import score
screen = pygame.display.set_mode((300, 200))
mas = [
    [1, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
BLUE = (0, 0, 255)
pygame.font.init()
text_score = pygame.font.SysFont('arial', 100)
text2 = text_score.render(f'You score: {score(mas)}', False, BLUE)
text_rect = text2.get_rect()
screen.blit(text2, (10, 50))
pygame.display.update()

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()