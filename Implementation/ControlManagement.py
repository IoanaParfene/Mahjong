import pygame
import Buttons

# Array of Button objects
buttons = []

def create_buttons(screen, gameVersion, bkmusic, volumeOn):
    ''' Create buttons and add them to a button object array '''
    buttons.append(Buttons.Button('Undo', (140, 445), [65, 0], screen))
    buttons.append(Buttons.Button('Info', (140, 640), [65, 0], screen))
    buttons.append(Buttons.Button('Shuffle', (140, 510), [65, 0], screen))
    buttons.append(Buttons.Button('NewGame', (140, 575), [65, 0], screen, gameVersion))
    buttons.append(Buttons.Button('MusicOn', (1000, 40), [-75,-5], screen, volumeOn, bkmusic))

def render_buttons(screen):
    ''' Show buttons on screen '''
    for index in range(0,len(buttons)):
        screen.blit(buttons[index].image, buttons[index].icon_rect)

def hover_buttons(screen):
    ''' Show button label on screen if hovered over '''
    for index in range(0,len(buttons)):
        if buttons[index].icon_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(buttons[index].hover_image, buttons[index].hover_rect)

def manage_buttons(screen):
    ''' Render buttons and check if hovered over '''
    render_buttons(screen)
    hover_buttons(screen)