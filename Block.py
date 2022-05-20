import pygame



class Block(pygame.sprite.Sprite):
    def __init__(self, position):
        # Sprire es un objeto visible en la pantalla
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('brickblocks/block.png')
        # realiza las operaciones con sprites a través de rectangulos con coordenadas
        self.rect = self.image.get_rect()
        self.rect.topleft = position
