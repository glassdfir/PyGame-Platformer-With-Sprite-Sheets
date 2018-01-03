import pygame
from spritesheet_functions import SpriteSheet
CHOCOLATECHIP = (0,0,61,57)
CANDYCANE = (61,0,61,57)
POPTART = (122,0,61,57)
COTTONCANDY = (183,0,61,57)
MARSHMELLOW = (244,0,61,57)

class Treat(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, sprite_sheet_data):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("cookie.png")
        # Grab the image for this platform
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])


        self.rect = self.image.get_rect()
