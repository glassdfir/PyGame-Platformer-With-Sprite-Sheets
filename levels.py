import pygame

import constants
import platforms
import cookie
import random

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    platform_list = None
    cookie_list = None

    # Background image
    background = None

    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = -5500
    block_size = 70
    gap = block_size * 4
    low = 500
    medium = 400
    high = 250
    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.cookie_list = pygame.sprite.Group()
        self.player = player

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.cookie_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.BLUE)
        screen.blit(self.background,(self.world_shift // 3,0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.cookie_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """
        if self.world_shift + shift_x > 0: shift_x = 0
        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for cookie in self.cookie_list:
            cookie.rect.x += shift_x
    def stone_platform(self,x,y,size):
        out = [[platforms.STONE_PLATFORM_LEFT, x, y]]
        for i in range(size-1):
                out += [[platforms.STONE_PLATFORM_MIDDLE, x+(70*(i+1)), y]]
        out += [[platforms.STONE_PLATFORM_RIGHT, x+(70*(size)), y]]
        return out
    def grass_platform(self,x,y,size):
        out = [[platforms.GRASS_LEFT, x, y]]
        for i in range(size-1):
                out += [[platforms.GRASS_MIDDLE, x+(70*(i+1)), y]]
        out += [[platforms.GRASS_RIGHT, x+(70*(size)), y]]
        return out
    def random_treat(self):
        a = [cookie.CHOCOLATECHIP,cookie.CANDYCANE,cookie.COTTONCANDY,cookie.POPTART,cookie.MARSHMELLOW]
        num = random.randrange(0,5)
        return a[num]
    def random_platform(self, previous):
        num = random.randrange(0,2)
        if previous == self.low: 
            a = [self.low,self.medium]
        elif previous == self.high:
            a = [self.high,self.medium]
        else:
            a = [self.low,self.medium,self.high]
            num = random.randrange(0,3)
        return a[num]
    def insert_up_down(self,x,y):
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = x
        block.rect.y = y
        block.boundary_top = random.randrange(100,250)
        block.boundary_bottom = random.randrange(550,600)
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_01.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -9000

        # Array with type of platform, and x, y location of the platform.
        level = []
        counter = 500
        cookies =[
            [self.random_treat(),counter,self.low - 61]
        ]
        level += self.grass_platform(counter,self.low,4)
        counter += self.block_size * 4 + self.gap
        cookies.append([self.random_treat(),counter,self.medium - 61])
        level += self.stone_platform(counter,self.medium,4)
        counter += self.block_size * 4 + self.gap * 2
        cookies.append([self.random_treat(),counter,self.high - 61])
        cookies.append([self.random_treat(),counter,self.low - 61])
        level += self.grass_platform(counter,self.high,4)

        counter += self.block_size * 4 + self.gap * 2
        for i in range(13):
            level += self.stone_platform(counter,self.low,1)
            if (i % 2) == 0:
                cookies.append([self.random_treat(),counter,self.low - 61])
            counter += self.gap
        
        level += self.grass_platform(counter,self.low,2)
        counter += self.gap
        level += self.grass_platform(counter,self.medium,2)
        counter += self.gap
        level += self.grass_platform(counter,self.high,2)
        counter += self.gap
        cookies.append([self.random_treat(),counter,self.high - 61])
        counter += self.gap
        cookies.append([self.random_treat(),counter,self.medium - 61])
        counter += self.gap
        cookies.append([self.random_treat(),counter,self.low - 61])

        
        for cookieobj in cookies:
            block = cookie.Treat(cookieobj[0])
            block.rect.x = cookieobj[1]
            block.rect.y = cookieobj[2]
            block.player = self.player
            self.cookie_list.add(block)

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


# Create platforms for the level
class Level_02(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_02.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -9000

        # Array with type of platform, and x, y location of the platform.
        level = []
        counter = 500
        cookies =[]
        cookies.append([self.random_treat(),counter,self.medium - 61])
        level += self.grass_platform(counter,self.medium,4)
        counter += self.block_size * 4 + self.gap
        cookies.append([self.random_treat(),counter,self.medium - 61])
        level += self.stone_platform(counter,self.medium,4)
        counter += self.block_size * 4 + self.gap
        cookies.append([self.random_treat(),counter,self.high - 61])
        cookies.append([self.random_treat(),counter,self.low - 61])
        level += self.grass_platform(counter,self.high,4)

        counter += self.block_size * 4 + self.gap
        level += self.stone_platform(counter,self.low,3)
        counter += self.gap * 2
        prev = self.low
        for i in range(24):
            plat = self.random_platform(prev)
            prev = plat
            level += self.stone_platform(counter,plat,1)
            if (i % 2) == 0:
                cookies.append([self.random_treat(),counter,plat - 61])
            counter += self.gap

        
        for cookieobj in cookies:
            block = cookie.Treat(cookieobj[0])
            block.rect.x = cookieobj[1]
            block.rect.y = cookieobj[2]
            block.player = self.player
            self.cookie_list.add(block)

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 300
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

class Level_03(Level):
    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_03.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -9000
        counter = 500
        cookies =[]
        for i in range(55):
            self.insert_up_down(counter,random.randrange(450,500))
            if (i % 2) == 0:
                cookies.append([self.random_treat(),counter,random.randrange(250,500)])
            counter += self.block_size * 2
        for cookieobj in cookies:
            block = cookie.Treat(cookieobj[0])
            block.rect.x = cookieobj[1]
            block.rect.y = cookieobj[2]
            block.player = self.player
            self.cookie_list.add(block)
class Level_04(Level):
    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_04.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -9000
        counter = 500
        cookies =[]
        level = []
        for i in range(10):
            self.insert_up_down(counter,random.randrange(450,500))
            if (i % 2) == 0:
                cookies.append([self.random_treat(),counter,random.randrange(250,500)])
            counter += self.block_size * 2
        level += self.stone_platform(counter,self.low,2)
        counter += self.block_size * 4
        level += self.stone_platform(counter,self.medium,2)
        counter += self.block_size * 4
        level += self.stone_platform(counter,self.high,2)
        counter += self.block_size * 4

        prev = self.low
        for i in range(10):
            plat = self.random_platform(prev)
            prev = plat
            level += self.stone_platform(counter,plat,1)
            if (i % 2) == 0:
                cookies.append([self.random_treat(),counter,plat - 61])
            counter += self.gap
        
        for i in range(20):
            self.insert_up_down(counter,random.randrange(450,500))
            if (i % 2) == 0:
                cookies.append([self.random_treat(),counter,random.randrange(250,500)])
            counter += self.block_size * 2
        
        
        for cookieobj in cookies:
            block = cookie.Treat(cookieobj[0])
            block.rect.x = cookieobj[1]
            block.rect.y = cookieobj[2]
            block.player = self.player
            self.cookie_list.add(block)
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
