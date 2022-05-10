class Objects(pygame.sprite.Sprite):

    def __init__(self):

        #https://www.pygame.org/docs/ref/sprite.html
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('brickblocks/start.png')
        self.rect = self.image.get_rect()

        self.rect.centerx = constants.WIDTH / 2
        self.rect.centery = constants.LARGE / 2

        #add start speed
        self.speed = [3, 3]
