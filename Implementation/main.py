import pygame
import Buttons
import GameModel
import time

# Initialize the game
pygame.init()
gameVersion = 'standard'

# Title
pygame.display.set_caption("Mahjong")
icon = pygame.image.load('Icons/mahjong.png')
pygame.display.set_icon(icon)

# Create Window and Background
screen = pygame.display.set_mode((1200,770))
bg = pygame.image.load('Pictures/bk.png')

# Music and Sound
bkmusic = pygame.mixer.Sound('Sound/bkmusic.wav')
bkmusic.play(-1)
bkmusic.set_volume(0.1)
volumeOn = True

# buttons
buttons = []

def CreateButtons():
    buttons.append(Buttons.Button('Undo', (140, 445), [65, 0], screen))
    buttons.append(Buttons.Button('Info', (140, 640), [65, 0], screen))
    buttons.append(Buttons.Button('Shuffle', (140, 510), [65, 0], screen))
    buttons.append(Buttons.Button('NewGame', (140, 575), [65, 0], screen, gameVersion))
    buttons.append(Buttons.Button('SoundOn', (1000, 40), [-75,-5], screen, volumeOn, bkmusic))

def RenderButtons():
    for index in range(0,len(buttons)):
        screen.blit(buttons[index].image, buttons[index].iconRect)

def HoverButtons():
    for index in range(0,len(buttons)):
        if buttons[index].iconRect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(buttons[index].popUpImage, buttons[index].popUpRect)
            pygame.display.flip()

def main():

    # Initialize Buttons and Pieces
    CreateButtons()
    GameModel.InitPieceArrangement(gameVersion)

    # Running game loop
    running = True
    while running:

        # Render Screen
        screen.blit(bg, (0,0))
        GameModel.RenderPieces(screen)
        RenderButtons()
        HoverButtons()

        # Check if mouse clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    button.on_click(event)

        pygame.display.update()

main()