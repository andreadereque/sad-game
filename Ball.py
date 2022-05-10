import pygame
import constants

class Ball(pygame.sprite.Sprite):

    def __init__(self):

        #https://www.pygame.org/docs/ref/sprite.html
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('brickblocks/start.png')
        self.rect = self.image.get_rect()

        self.rect.centerx = constants.WIDTH / 2
        self.rect.centery = constants.LARGE / 2

        #add start speed
        self.speed = [3, 3]

    def updateBallPosition(self):

        if self.rect.right >= constants.WIDTH or self.rect.left <= 0:
            self.speed[0] = -self.speed[0]
        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]


        self.rect.move_ip((self.speed))