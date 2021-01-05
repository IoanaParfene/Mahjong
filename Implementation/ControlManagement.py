import pygame
import Buttons

# Array of Button objects
buttons = []


def create_buttons(screen, background_music, volumeOn):
    """ Create buttons and add them to a button object array """
    buttons.append(Buttons.Button('Undo', (135, 470), [65, 0], screen))
    buttons.append(Buttons.Button('Shuffle', (135, 535), [65, 0], screen))
    buttons.append(Buttons.Button('Hint', (135, 405), [65, 0], screen))
    buttons.append(Buttons.Button('NewGame', (135, 600), [65, 0], screen, buttons[0], buttons[1], buttons[2]))
    buttons.append(Buttons.Button('Info', (135, 665), [65, 0], screen))
    buttons.append(Buttons.Button('MusicOn', (970, 40), [-75, -5], screen, volumeOn, background_music))


def render_buttons(screen):
    """ Show buttons on screen """
    for index in range(0, len(buttons)):
        screen.blit(buttons[index].image, buttons[index].icon_rect)


def hover_buttons(screen):
    """ Show button label on screen if hovered over """
    for index in range(0, len(buttons)):
        if buttons[index].icon_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(buttons[index].hover_image, buttons[index].hover_rect)


def try_shuffling(button):
    """ Shuffle tiles if possible when game is lost"""
    return Buttons.shuffle_button_action(button)


def restart_game(button):
    """ Shuffle tiles if possible when game is lost"""
    return Buttons.newgame_button_action(button)