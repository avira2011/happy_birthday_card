import pygame
import time

pygame.init()

WIDTH = 600
HEIGHT = 600    

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Birthday Card Animation By:Avira')

img = pygame.image.load('birthday_card/birthday1.jpg')
img2 = pygame.image.load('birthday_card/birthday2.jpg')
img3 = pygame.image.load('birthday_card/birthday3.jpg')
image = pygame.transform.scale(img, (WIDTH, HEIGHT))
image2 = pygame.transform.scale(img2, (WIDTH, HEIGHT))
image3 = pygame.transform.scale(img3, (WIDTH, HEIGHT))

while True: 
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()

    font = pygame.font.SysFont("Times New Roman", 50)
    text = font.render("Happy Birthday", True, 'black')

    screen.fill('black')
    screen.blit(image, (0,0))
    screen.blit(text, (150, 300))
    
    pygame.display.update()
    time.sleep(3)

    text2 = font.render("Enjoy getting old", True, 'black')

    screen.fill('black')
    screen.blit(image2, (0,0))
    screen.blit(text2, (50, 50))

    pygame.display.update()
    time.sleep(3)

    text3 = font.render("Enjoy :)", True, 'black')

    screen.fill('black')
    screen.blit(image3, (0,0))
    screen.blit(text3, (0, 50))

    pygame.display.update()
    time.sleep(3)




