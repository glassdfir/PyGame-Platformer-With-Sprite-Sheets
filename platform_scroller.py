"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/

Main module for platform scroller example.

From:
http://programarcadegames.com/python_examples/sprite_sheets/

Explanation video: http://youtu.be/czBDKWJqOao

Part of a series:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example.py
http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py
http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
http://programarcadegames.com/python_examples/sprite_sheets/

Game art from Kenney.nl:
http://opengameart.org/content/platformer-art-deluxe

"""

import pygame

import constants
import levels

from player import Player

def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Ellie's Big Adventure!!!")



    #Loop until the user clicks the close button.


    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    font_name = pygame.font.match_font('arial')
    def draw_text(surf, text, size, x, y,color):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)


    def title_screen():
        title_done = False

        while not title_done:
            screen.fill(constants.WHITE)
            draw_text(screen, "Ellie's Big Adventure", 70, constants.SCREEN_WIDTH / 2, 200, constants.RED)
            draw_text(screen, "Help Ellie collect treats!", 50, constants.SCREEN_WIDTH / 2, 270, constants.BLACK)
            draw_text(screen, "Press ANY key to Play or ESC to Quit", 50, constants.SCREEN_WIDTH / 2, 340, constants.BLACK)
            draw_text(screen, "Press left and right to move and SPACE to jump.", 50, constants.SCREEN_WIDTH / 2, 410, constants.BLACK)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # If user clicked close
                    title_done = True
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    title_done = True
        game()

    def end_screen(score):
        end_done = False
        while not end_done:
            screen.fill(constants.WHITE)
            draw_text(screen, "WOW! You collected " + str(score) + " treats!", 70, constants.SCREEN_WIDTH / 2, 200, constants.RED)
            draw_text(screen, "Press SPACE to play again or", 50, constants.SCREEN_WIDTH / 2, 270, constants.BLACK)
            draw_text(screen, "press ESC to Quit.", 50, constants.SCREEN_WIDTH / 2, 340, constants.BLACK)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # If user clicked close
                    end_done = True
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            end_done = True
                            pygame.quit()
                        if event.key == pygame.K_SPACE:
                            game()





    def game():
        # -------- Main Program Loop -----------
        # Create the player
        player = Player()

        # Create all the levels
        level_list = []
        level_list.append(levels.Level_01(player))
        level_list.append(levels.Level_02(player))
        level_list.append(levels.Level_03(player))
        level_list.append(levels.Level_04(player))

        # Set the current level
        current_level_no = 0
        current_level = level_list[current_level_no]

        active_sprite_list = pygame.sprite.Group()
        player.level = current_level

        player.rect.x = 340
        player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
        active_sprite_list.add(player)
        done = False
        while not done:
            for event in pygame.event.get(): # User did something

                if event.type == pygame.QUIT: # If user clicked close
                    done = True # Flag that we are done so we exit this loop

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = True
                    if event.key == pygame.K_LEFT:
                        player.go_left()
                    if event.key == pygame.K_RIGHT:
                        player.go_right()
                    if event.key == pygame.K_SPACE:
                        player.jump()
                    if event.key == pygame.K_UP                                               :
                        player.jump()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and player.change_x < 0:
                        player.stop()
                    if event.key == pygame.K_RIGHT and player.change_x > 0:
                        player.stop()

            # Update the player.
            active_sprite_list.update()

            # Update items in the level
            current_level.update()

            # If the player gets near the right side, shift the world left (-x)
            if player.rect.x >= 500:
                diff = player.rect.x - 500
                player.rect.x = 500
                current_level.shift_world(-diff)

            # If the player gets near the left side, shift the world right (+x)
            if player.rect.x <= 120:
                diff = 120 - player.rect.x
                player.rect.x = 120
                current_level.shift_world(diff)

            # If the player gets to the end of the level, go to the next level
            current_position = player.rect.x + current_level.world_shift
            if current_position < current_level.level_limit:
                player.rect.x = 120
                if current_level_no < len(level_list)-1:
                    current_level_no += 1
                    current_level = level_list[current_level_no]
                    player.level = current_level
                else:
                    done = True

            # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

            current_level.draw(screen)
            active_sprite_list.draw(screen)

            # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

            # Limit to 60 frames per second
            clock.tick(120)

            # Go ahead and update the screen with what we've drawn.
            draw_text(screen, "Treats found: " + str(player.score), 40, constants.SCREEN_WIDTH / 2, 10,constants.WHITE)

            pygame.display.flip()





        # Be IDLE friendly. If you forget this line, the program will 'hang'
        # on exit.
        end_screen(player.score)


    title_screen()

if __name__ == "__main__":
    main()
