import pygame

import constants


class Objects(pygame.sprite.Sprite):

    def __init__(self, position):

        #https://www.pygame.org/docs/ref/sprite.html
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('brickblocks/thunder.png')

        self.rect = self.image.get_rect()
        self.rect.topleft = position



