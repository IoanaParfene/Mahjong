import pygame
import random
import TileArrangement
# Remaining uses of certain buttons
remaining_uses_undo = 3
remaining_uses_shuffle = 1
remaining_uses_hint = 3

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
                function_name = str(self.button_type).lower() + '_button_action'
                eval(function_name)(self)


def musicon_button_action(button):
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


def undo_button_action(button):
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
            # Add the 1 shuffle available image back
            button.hover_image = pygame.image.load(
                'Icons/' + str(button.hover_pref) + button.button_type + str(
                    remaining_uses_undo) + '.png')
            button.hover_image = pygame.transform.scale(button.hover_image, (button.pixels, button.pixels))


def shuffle_button_action(button):
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
        # Add the 1 shuffle available image back
        button.hover_image = pygame.image.load(
            'Icons/' + str(button.hover_pref) + button.button_type + str(
                remaining_uses_shuffle) + '.png')
        button.hover_image = pygame.transform.scale(button.hover_image, (button.pixels, button.pixels))


def newgame_button_action(button):
    """Start a new game"""
    # Add the available button uses back
    global remaining_uses_undo
    global remaining_uses_hint
    global remaining_uses_shuffle
    remaining_uses_hint = 3
    remaining_uses_undo = 3
    remaining_uses_shuffle = 1
    # Add all buttons uses left back
    button.varg[0].hover_image = pygame.image.load(
            'Icons/' + str(button.varg[0].hover_pref) + button.varg[0].button_type + '.png')
    button.varg[0].hover_image = pygame.transform.scale(button.varg[0].hover_image, (button.pixels, button.pixels))
    button.varg[1].hover_image = pygame.image.load(
        'Icons/' + str(button.varg[1].hover_pref) + button.varg[1].button_type + '.png')
    button.varg[1].hover_image = pygame.transform.scale(button.varg[1].hover_image, (button.pixels, button.pixels))
    button.varg[2].hover_image = pygame.image.load(
        'Icons/' + str(button.varg[2].hover_pref) + button.varg[2].button_type + '.png')
    button.varg[2].hover_image = pygame.transform.scale(button.varg[0].hover_image, (button.pixels, button.pixels))
    # Re-initialize variables
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


def hint_button_action(button):
    """Hint for an available move"""
    global remaining_uses_hint
    # If the player has any hints left
    if remaining_uses_hint > 0:
        # Count the available piece types with a dictionary
        remaining_piece_types = dict()
        for piece in TileArrangement.pieces:
            if piece.available():
                if piece.tile_number not in remaining_piece_types.keys():
                    remaining_piece_types[piece.tile_number] = 1
                else:
                    remaining_piece_types[piece.tile_number] += 1
                # Hint the first two piece found
                if remaining_piece_types[piece.tile_number] == 2:
                    remaining_pieces = 2
                    for piece2 in TileArrangement.pieces:
                        if piece2.available():
                            if(remaining_pieces>0):
                                if piece2.tile_number == piece.tile_number:
                                    piece2.image = "clicked"
                                    remaining_pieces -= 1
                            else:
                                break
                    # Remove one usage of hint
                    remaining_uses_hint -= 1
                    # Add the 1 shuffle available image back
                    button.hover_image = pygame.image.load(
                        'Icons/' + str(button.hover_pref) + button.button_type + str(
                            remaining_uses_hint) + '.png')
                    button.hover_image = pygame.transform.scale(button.hover_image, (button.pixels, button.pixels))
                    break








