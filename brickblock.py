import sys
import time

import pygame
from Ball import Ball
from Blocks import Blocks
from Platform import Platform
import constants

pygame.init()


def start_game(level):
    global gameDisplay
    global points
    global lives
    global gamePointsList
    global levelOfTheGame


    gameDisplay = pygame.display.set_mode((constants.WIDTH, constants.LARGE))
    pygame.display.set_caption("Bricks Block Break Game")
    # para no tener que clicar el boton x veces para moverse hacia un lado
    pygame.key.set_repeat(30)  # https://www.pygame.org/docs/ref/key.html
    levelOfTheGame = level
    ball = Ball()
    platform = Platform()
    blocks = Blocks()
    clock = pygame.time.Clock()
    points = 0
    lives = 3
    gamePointsList = []
    timeBetweenLives = True
    while True:
        clock.tick(60)

        # events
        for movement in pygame.event.get():  # https://www.pygame.org/docs/ref/event.html
            if movement.type == pygame.QUIT:
                sys.exit()
            # buscar eventos del teclado
            # keydown evento al pulsar una tecla del teclado
            elif movement.type == pygame.KEYDOWN:
                platform.updatePlatformPosition(movement)
                if timeBetweenLives == True and movement.key == pygame.K_SPACE:
                    timeBetweenLives = False
                    if ball.rect.centerx < constants.WIDTH / 2:
                        if levelOfTheGame == '1':
                            ball.speed = [3, -3]
                        if levelOfTheGame == '2':
                            ball.speed = [4, -4]
                        if levelOfTheGame == '3':
                            ball.speed = [5, -5]
                    else:
                        if levelOfTheGame =='1':
                            ball.speed = [-3, -3]
                        if levelOfTheGame =='2':
                            ball.speed = [-4, -4]
                        if levelOfTheGame =='3':
                            ball.speed = [-5, -5]
        if timeBetweenLives == False:
            ball.updateBallPosition()
        else:
            ball.rect.midbottom = platform.rect.midtop

        if pygame.sprite.collide_rect(ball, platform):
            ball.speed[1] = -ball.speed[1]

        # para las colisiones con los ladrillos
        list = pygame.sprite.spritecollide(ball, blocks, False)
        if list:
            block = list[0]
            cx = ball.rect.centerx
            if cx < block.rect.left or cx > block.rect.right:
                ball.speed[0] = -ball.speed[0]
            else:
                ball.speed[1] = - ball.speed[1]
            blocks.remove(block)
            points += 10

        if ball.rect.top > constants.LARGE:
            lives -= 1
            timeBetweenLives = True
            if lives <= 0:
                end_game()

        # fondo
        gameDisplay.fill(constants.BGCOLOUR)
        showPoints()
        showLives()
        # blit sirve para dibujar una superficie sobre otra en la posición que le indicamos mediante coordenadas
        gameDisplay.blit(ball.image, ball.rect)
        gameDisplay.blit(platform.image, platform.rect)
        # dibujar el conjunto de bloques
        blocks.draw(gameDisplay)

        pygame.display.flip()  # crear pantalla que no se cierre durante el juego


def end_game():


    font = pygame.font.SysFont('Arial', 70)
    fontPoints = pygame.font.SysFont('Arial', 20)
    text = font.render('End game', True, constants.WHITECOLOUR)
    pointsString = fontPoints.render('Points', showPoints(), constants.WHITECOLOUR)
    points_rect = text.get_rect()
    text_rect = text.get_rect()
    points_rect.center = [constants.WIDTH/2, constants.LARGE/2 + 100]
    text_rect.center = [constants.WIDTH / 2, constants.LARGE / 2]
    gameDisplay.blit(text, text_rect)
    gameDisplay.blit(pointsString,points_rect)
    pygame.display.flip()
    time.sleep(3)
    sys.exit()


def showPoints():
    global points
    fonts = pygame.font.SysFont('Arial', 16)
    text = fonts.render(str(points).zfill(5), True, (constants.WHITECOLOUR))
    text_rect = text.get_rect()
    text_rect.topright = [constants.WIDTH, 0]
    gameDisplay.blit(text, text_rect)

def savePoints():
    global points
    global gamePointList
    gamePointList.append(points)
    return gamePointList



def showLives():
    global lives
    fonts = pygame.font.SysFont('Arial', 16)
    livesString = "Lives: " + str(lives).zfill(2)
    text = fonts.render(livesString, True, constants.WHITECOLOUR)
    text_rect = text.get_rect()
    text_rect.bottomright = [constants.WIDTH, constants.LARGE]
    gameDisplay.blit(text, text_rect)
