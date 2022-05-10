import pygame
import constants


class Platform(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('brickblocks/platform.png')
        self.rect = self.image.get_rect()

        # center the platform
        self.rect.midbottom = (constants.WIDTH / 2, constants.LARGE - 20)

        self.speed = [0, 0]

    def updatePlatformPosition(self, movement):

        if movement.key == pygame.K_LEFT and self.rect.left > 0:
            self.speed = [-20, 0]

        elif movement.key == pygame.K_RIGHT and self.rect.right < constants.WIDTH:
            self.speed = [20, 0]

        else:
            self.speed = [0, 0]

        self.rect.move_ip((self.speed))
