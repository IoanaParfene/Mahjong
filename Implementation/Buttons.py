import pygame
import random
import TileArrangement
# Remaining uses of certain buttons
remaining_uses_undo = 3
remaining_uses_shuffle = 1

class Button:
    # Button width in pixels
    pixels = 60
    # Prefix of button standard images
    icon_outline = 2
    # Prefix of button standard images
    icon_pref = 'Scroll'
    # Prefix of button hover images
    hover_pref = 'PopUp'

    def __init__(self, button_type, icon_pos, hover_pos_add, screen, *varg):
        """ Initialize button attributes """
        # Prefix of button standard images
        self.button_type = button_type
        # Permanent button image loading, transforming and rectangle
        self.icon_pos = icon_pos
        self.image = pygame.image.load('Icons/' + str(self.icon_pref) + str(self.icon_outline) + button_type + '.png')
        self.image = pygame.transform.scale(self.image, (self.pixels, self.pixels))
        self.icon_rect = self.image.get_rect(topleft=self.icon_pos)
        # Hover button labels loading, transforming and rectangle
        self.hover_position = ([list(self.icon_pos)[0] + hover_pos_add[0], list(self.icon_pos)[1] + hover_pos_add[1]])
        self.hover_image = pygame.image.load('Icons/' + str(self.hover_pref) + button_type + '.png')
        self.hover_image = pygame.transform.scale(self.hover_image, (self.pixels, self.pixels))
        self.hover_rect = self.hover_image.get_rect(topleft=self.hover_position)
        # The pygame screen
        self.screen = screen
        # Special extra custom variables for different buttons
        self.varg = list(varg)

    def on_click(self, event):
        """ On-click button action function"""
        if event.button == 1:
            if self.icon_rect.collidepoint(event.pos):
                function_name = str(self.button_type) + '_button_action'
                eval(function_name)(self)


def MusicOn_button_action(button):
    """Turn music volume on and off"""
    if not button.varg[0]:
        # Turn music volume on if the custom extra argument is False
        button.image = pygame.image.load('Icons/' + str(button.icon_pref) + str(button.icon_outline) + 'MusicOn.png')
        button.image = pygame.transform.scale(button.image, (button.pixels, button.pixels))
        button.screen.blit(button.image, button.icon_rect)
        button.varg[0] = True
        button.varg[1].set_volume(0.1)
    else:
        # Turn music volume on if the custom extra argument is True
        button.image = pygame.image.load('Icons/' + str(button.icon_pref) + str(button.icon_outline) + 'MusicOff.png')
        button.image = pygame.transform.scale(button.image, (button.pixels, button.pixels))
        button.screen.blit(button.image, button.icon_rect)
        button.varg[0] = False
        button.varg[1].set_volume(0.0)


def Undo_button_action(button):
    """Undo the last move"""
    global remaining_uses_undo
    # Check if any moves were executed
    if(TileArrangement.executed_moves):
        # Check if the player has any undo uses left
        if(remaining_uses_undo>0):
            # Get both pieces' array positions
            values = TileArrangement.executed_moves.pop(-1)
            # Add the pieces back on the board
            TileArrangement.tile_array[values[0][0]][values[0][1]][values[0][2]][0] = True
            TileArrangement.tile_array[values[1][0]][values[1][1]][values[1][2]][0] = True
            # Remove one usage of undo
            remaining_uses_undo -= 1


def Shuffle_button_action(button):
    """Shuffle remaining pieces"""
    global remaining_uses_shuffle
    # Check if the player has any shuffle uses left
    if(remaining_uses_shuffle>0):
        # Array of all the pieces remaining as their types
        remaining_piece_types = []
        for piece in TileArrangement.pieces:
            # Check of the piece still exists on the board
            if TileArrangement.tile_array[piece.matrix_position[0]][piece.matrix_position[1]][piece.matrix_position[2]][0]:
                remaining_piece_types.append(piece.tile_number)
        # Shuffle the remaining Piece Types
        random.shuffle(remaining_piece_types)
        # Reassign the remaining Piece Types
        for piece in TileArrangement.pieces:
            if TileArrangement.tile_array[piece.matrix_position[0]][piece.matrix_position[1]][piece.matrix_position[2]][0]:
                piece.tile_number = remaining_piece_types.pop()
        # Remove one usage of shuffle
        remaining_uses_shuffle -= 1


def NewGame_button_action(button):
    """Shuffle remaining pieces"""
    # Add the available button uses back
    global remaining_uses_undo
    global remaining_uses_shuffle
    remaining_uses_undo = 3
    remaining_uses_shuffle = 1
    #
    TileArrangement.current_piece = None
    for move in TileArrangement.executed_moves:
        TileArrangement.executed_moves.pop()
    # Array of all the pieces remaining as their types
    remaining_piece_types = []
    for piece in TileArrangement.pieces:
        # Check of the piece still exists on the board
        TileArrangement.tile_array[piece.matrix_position[0]][piece.matrix_position[1]][piece.matrix_position[2]][0] = True
        piece.image = 'default'
        remaining_piece_types.append(piece.tile_number)
    # Shuffle the remaining Piece Types
    random.shuffle(remaining_piece_types)
    # Reassign the remaining Piece Types
    for piece in TileArrangement.pieces:
        if TileArrangement.tile_array[piece.matrix_position[0]][piece.matrix_position[1]][piece.matrix_position[2]][0]:
            piece.tile_number = remaining_piece_types.pop()




