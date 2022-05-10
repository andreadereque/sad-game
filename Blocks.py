import pygame
from Block import Block
import constants
import random
import brickblock

class Blocks(pygame.sprite.Group ):
    def __init__(self):
        pygame.sprite.Group.__init__(self)
        posWidth = 0
        posLarge = 20
        if brickblock.levelOfTheGame == '1':
            blocks_number = random.randint(50,100)
        elif brickblock.levelOfTheGame == '2':
            blocks_number = random.randint(100, 150)
        elif brickblock.levelOfTheGame == '3':
            blocks_number = random.randint(150,200)


        for i in range(blocks_number):
            block = Block((posWidth, posLarge))
            self.add(block)
            posWidth += block.rect.width
            if posWidth >= constants.WIDTH:
                posWidth = 0
                posLarge += block.rect.height