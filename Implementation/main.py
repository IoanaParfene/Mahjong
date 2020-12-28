import pygame
import TileArrangement
import ControlManagement
import time

# Initialize the game
pygame.init()

# Title and App Icon
pygame.display.set_caption("Mahjong")
icon = pygame.image.load('Icons/mahjong.png')
pygame.display.set_icon(icon)

# Create Window and Background
screen = pygame.display.set_mode((1200,770))
bg = pygame.image.load('Pictures/bk.png')
table = pygame.image.load('Pictures/WoodTable.jpg')
table = pygame.transform.scale(table, (1500,800))

# Music and Sound
background_music = pygame.mixer.Sound('Sound/bkmusic.wav')
background_music.play(-1)
background_music.set_volume(0.1)
volumeOn = True

def main():
    """ Initialize game elements and run main loop """
    # Initialize Buttons and Pieces
    ControlManagement.create_buttons(screen, background_music, volumeOn)
    TileArrangement.init_piece_arrangement()
    # Run game loop by frame
    running = True
    while running:
        # Render screen, buttons, check if button hover occurs
        screen.blit(table,(0,0))
        screen.blit(bg, (0,0))
        TileArrangement.render_pieces(screen)
        ControlManagement.manage_buttons(screen)
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Action if a certain button was clicked
                for button in ControlManagement.buttons:
                    button.on_click(event)
                # Action if a certain game tile was clicked
                for piece in TileArrangement.pieces:
                    piece.on_click(event)
        # Display the screen
        pygame.display.update()

main()