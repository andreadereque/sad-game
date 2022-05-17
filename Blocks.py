import pygame
from Block import Block
import constants
import random
import brickblock
from Objects import Objects


class Blocks(pygame.sprite.Group):
    def __init__(self):

        pygame.sprite.Group.__init__(self)
        numBlocks = 0
        posWidth = 0
        posLarge = 20
        listToads = []
        list = []
        if brickblock.levelOfTheGame == '1':
            blocks_number = random.randint(50, 100)
        elif brickblock.levelOfTheGame == '2':
            blocks_number = random.randint(100, 150)
        elif brickblock.levelOfTheGame == '3':
            blocks_number = random.randint(150, 200)

        for i in range(blocks_number):
            list.append(random.randint(0, 1))
            numBlocks = len(list)

            block = Block((posWidth, posLarge))

            if list[i] == 1:
                self.add(block)
                posWidth += block.rect.width

                if posWidth >= constants.WIDTH:
                    posWidth = 0
                    posLarge += block.rect.height
                else:
                    posWidth += block.rect.width
            else:
                if posWidth >= constants.WIDTH:
                    posWidth = 0
                    posLarge += block.rect.height
                else:
                    posWidth += block.rect.width
        posWidth = 0
        posLarge = 20

        for i in range(blocks_number):
            listToads.append(random.randint(0, 100))
            toad = Objects((posWidth, posLarge))
            if list[i] == 1:
                if listToads[i] == 10 or listToads[i] == 20 or listToads[i] == 30 or listToads[i] == 40:
                    self.add(toad)
                    posWidth += toad.rect.width

                    if posWidth >= constants.WIDTH:
                        posWidth = 0
                        posLarge += toad.rect.height
                    else:
                        posWidth += toad.rect.width
            else:
                if posWidth >= constants.WIDTH:
                    posWidth = 0
                    posLarge += toad.rect.height
                else:
                    posWidth += toad.rect.width
