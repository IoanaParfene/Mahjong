import pygame
import random
import Pieces
from Pieces import Piece
import time

# Starting time of every game
start_time = time.time()

# Height of a piece in pixels
PIECE_PIXELS = Pieces.PIECE_PIXELS

# Array of loaded tile images
piece_images = Pieces.piece_images
# Array of loaded clicked tile images
clicked_piece_images = Pieces.clicked_piece_images

# Array of 144 tile number names, 4 of each of the 36 pieces
tile_array = Pieces.tile_array
# Array of Piece type objects containing all tiles
pieces = Pieces.pieces

# The current valid, selected tile for matching
current_piece = Pieces.current_piece

# Executed move list
executed_moves = Pieces.executed_moves


def load_piece_images():
    """ Load normal piece images and clicked piece images in separate arrays """

    # Height of a piece in pixels
    global PIECE_PIXELS
    # Tuple of piece rectangle width x height
    tileSize = (int(PIECE_PIXELS * 0.75), PIECE_PIXELS)

    for i in range(0, 37):
        # Load normal piece images
        normal_image = pygame.transform.scale(pygame.image.load('Icons/Pieces/Tile' + str(i) + '.png'), tileSize)
        piece_images.append(normal_image)
        # Load clicked piece images
        clicked_image = pygame.transform.scale(pygame.image.load('Icons/Pieces/TileS' + str(i) + '.png'), tileSize)
        clicked_piece_images.append(clicked_image)


def create_tile_array():
    """ Make 3D array of free tile spaces of type [level][line][column] """
    for level in range(0, 5):
        level = []
        for line in range(0, 9):
            line = []
            for column in range(0, 16):
                # 1st element = the existence/availability of a piece in said 3D array space
                # 2nd element(optional) = position(index in [1-144]) of said piece in the piece array
                pieceInfo = [False]
                line.append(pieceInfo)
            level.append(line)
        tile_array.append(level)


def piece_position(level, line, column, special):
    """ Calculations for the screen-positions of the pieces
        Based on 3D array level,line,column and type of piece (normal/special)
    """
    # Height of a piece in pixels
    global PIECE_PIXELS

    # If the piece belongs to the 4 special ones that exceed 3D array rules
    if special:
        x_coord = column * int(PIECE_PIXELS * 0.75) + 180 - column * 5 - level * 5
        y_coord = 3.5 * PIECE_PIXELS + 80 - 5 - level * 5
    else:
        x_coord = column * int(PIECE_PIXELS * 0.75) + 180 - 5 * level - column * 5
        y_coord = line * PIECE_PIXELS + 25 - 5 * level - line * 5

    # Tuple of screen position of said piece
    return x_coord, y_coord


def get_all_pieces():
    """ 144 integers in [1...36] - each repeating 4 times = 2 pairs of each tile """
    queue = []
    for i in range(1, 37):
        for j in range(0, 4):
            queue.append(i)
    # shuffle piece number order
    random.shuffle(queue)
    return queue


def standard_arrangement():
    """ Model the standard 5-level arrangement of the Mahjong Game in the 3D position array
        Add the pieces to a 1D array and assign the tiles
        There are 144 total tiles( two pairs of each of the 36 existing tiles)
    """
    # The height of a tile on-screen
    global PIECE_PIXELS
    # The total number of pieces on half of the lines of each level
    level_line_total_pieces = [[12, 8, 10, 12], [6, 6, 6], [4, 4], [2, 2]]
    # 1D array of 144 tile numbers (4 of [1...36])
    available_pieces = get_all_pieces()

    # Assign the normal pieces on 4 levels on a 3D array and add to a piece array
    for level in range(0, 5):

        # Add the UPPER half of the 4 levels of tiles
        for line in range(1 + level, 5):
            # Starting and ending column positions of the tiles in the line
            start = 8 - level_line_total_pieces[level][line - level - 1] // 2
            end = start + level_line_total_pieces[level][line - level - 1]
            for column in range(start, end):
                # (matrix_position, next queue tile number, screen_position)
                pieces.append(Piece([level, line, column],
                                    available_pieces.pop(),
                                    piece_position(level, line, column, False)))
                # (piece exists/is available to use, index of piece in pieces array)
                tile_array[level][line][column] = [True, len(pieces) - 1]

        # Add the LOWER half of the 4 levels of tiles
        for line in range(5, 9 - level):
            # Starting and ending column positions of the tiles in the line
            start = 8 - level_line_total_pieces[level][8 - line - level] // 2
            end = start + level_line_total_pieces[level][8 - line - level]
            for column in range(start, end):
                # (matrix_position, next queue tile number, screen_position)
                pieces.append(Piece([level, line, column],
                                    available_pieces.pop(),
                                    piece_position(level, line, column, False)))
                # (piece exists/is available to use, index of piece in pieces array)
                tile_array[level][line][column] = [True, len(pieces) - 1]

    # Hardcode the 4 special pieces that exist in-between the 3D array elements on the screen
    pieces.append(Piece([0, 4, 1], available_pieces.pop(), piece_position(0, 4, 1, True)))
    tile_array[0][4][1] = [True, len(pieces) - 1]
    pieces.append(Piece([0, 5, 14], available_pieces.pop(), piece_position(0, 5, 14, True)))
    tile_array[0][5][14] = [True, len(pieces) - 1]
    pieces.append(Piece([0, 5, 15], available_pieces.pop(), piece_position(0, 5, 15, True)))
    tile_array[0][5][15] = [True, len(pieces) - 1]
    pieces.append(Piece([4, 5, 8], available_pieces.pop(), piece_position(4, 5, 7.5, True)))
    tile_array[4][5][8] = [True, len(pieces) - 1]

    # Hardcode the neighbours of the 4 special pieces that exceed 3D array bounds
    # 1st element = the expected neighbour, 2nd element = the actual neighbour
    pieces[tile_array[0][5][2][1]].set_special_neighbour([[0, 5, 1], [0, 4, 1]])
    pieces[tile_array[0][4][13][1]].set_special_neighbour([[0, 4, 14], [0, 5, 14]])
    pieces[tile_array[3][4][8][1]].set_special_neighbour([[4, 4, 8], [4, 5, 8]])
    pieces[tile_array[3][4][7][1]].set_special_neighbour([[4, 4, 7], [4, 5, 8]])
    pieces[tile_array[3][5][7][1]].set_special_neighbour([[4, 5, 7], [4, 5, 8]])


def render_pieces(screen):
    """ Blit piece images on screen based on existing/available/clicked """
    for level in range(0, 5):
        for line in range(0, 9):
            for column in range(0, 16):
                if tile_array[level][line][column][0]:
                    if pieces[tile_array[level][line][column][1]].image == 'default':
                        screen.blit(piece_images[pieces[tile_array[level][line][column][1]].tile_number],
                                    pieces[tile_array[level][line][column][1]].screen_position)
                    else:
                        screen.blit(clicked_piece_images[pieces[tile_array[level][line][column][1]].tile_number],
                                    pieces[tile_array[level][line][column][1]].screen_position)


def init_piece_arrangement():
    """ Initialize the pieces and the arrangement """
    load_piece_images()
    create_tile_array()
    standard_arrangement()


def check_win():
    """ Check if th game was won, lost or it can be continued"""
    # Get the remaining pieces
    remaining_piece_types = dict()
    lost = True
    # Get the remaining pieces on the board and their types
    for piece in pieces:
        if piece.available():
            if piece.tile_number not in remaining_piece_types.keys():
                remaining_piece_types[piece.tile_number] = 1
            else:
                remaining_piece_types[piece.tile_number] += 1
            # Lost if there are no available pairs on the board
            if remaining_piece_types[piece.tile_number] == 2:
                lost = False
    # If there are no pieces left on the board, the game is won
    if not remaining_piece_types:
        return "Won"
    elif lost is True:
        return "Lost"
    else:
        return "Continue"
