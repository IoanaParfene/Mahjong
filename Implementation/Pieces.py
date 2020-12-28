# Height of a piece in pixels
PIECE_PIXELS = 75

# Array of loaded tile images
piece_images = []
# Array of loaded clicked tile images
clicked_piece_images = []

# Array of 144 tile number names, 4 of each of the 36 pieces
tile_array = []
# Array of Piece type objects containing all tiles
pieces = []

# The current valid, selected tile for matching
current_piece = None

# Executed move list
executed_moves = []


class Piece:
    # If the piece has one of the 4 special pieces as a neighbour and it bends the rules
    special_neighbour = False
    # If the piece was clicked or not
    image = 'default'

    def __init__(self, matrix_position, tile_number, screen_position):
        # 3D array position of piece of type [level,line,column]
        self.matrix_position = matrix_position
        # int in [1,36] representing a certain tile image
        self.tile_number = tile_number
        # left corner, screen position tuple (width, height)
        self.screen_position = screen_position
        # occupied rectangle for said piece at said screen position
        self.rect = piece_images[0].get_rect(topleft=self.screen_position)

    def set_special_neighbour(self, special_neighbour):
        """ Set list of type [expected_neighbour, actual_neighbour_to_check]
            Special neighbour = one of the 4 special tiles that break screen position rules
        """
        self.special_neighbour = special_neighbour

    def available(self):
        """ Checks if said piece is available for clicking
            Avaiable = a piece has True at said location in 3D array,
                       a piece is not covered by upper level pieces,
                       a piece has at least one free side edge(no left/right neighbour)
        """
        available = True

        # Checks if the piece has True at its location in the 3D array
        # True means that the piece exists and was not taken yet
        if not tile_array[self.matrix_position[0]][self.matrix_position[1]][self.matrix_position[2]][0]:
            available = False

        # Checks if the piece is not covered by upper level pieces
        # True if the piece has never had neighbours, or if they were all taken
        for level in range(self.matrix_position[0] + 1, 5):
            # If the piece has one of the 4 special neighbours, check if that one is on top
            # Made for the 4 pieces in layer 4 covered by the top-most level 5 tile
            if self.special_neighbour is not False:
                if (self.special_neighbour[0][0] == level and
                        self.special_neighbour[0][1] == self.matrix_position[1] and
                        self.special_neighbour[0][2] == self.matrix_position[2]):
                    location = tile_array[self.special_neighbour[1][0]][self.special_neighbour[1][1]][
                        self.special_neighbour[1][2]]
                    if location[0]:
                        available = False
            else:
                location = tile_array[level][self.matrix_position[1]][self.matrix_position[2]]
                if location[0]:
                    available = False

        # Add-ons for getting the side neigbours (column+1 or column-1)
        side_neighbours = [1, -1]
        # Total of side neighbour, 0-2
        total_side_neighbours = 0
        # If at least one side is free, then the piece can be taken
        for column in side_neighbours:
            if 1 <= self.matrix_position[2] + column <= 15:
                # If the piece has one of the 4 special neighbours, check if that one is on the side
                # Made for the 3 pieces in layer 0 sided by the right-most/left-most special pieces
                if self.special_neighbour is not False:
                    if (self.special_neighbour[0][0] == self.matrix_position[0] and
                            self.special_neighbour[0][1] == self.matrix_position[1] and
                            self.special_neighbour[0][2] == self.matrix_position[2] + column):
                        if tile_array[self.special_neighbour[1][0]][self.special_neighbour[1][1]][
                            self.special_neighbour[1][2]][0]:
                            total_side_neighbours += 1
                if tile_array[self.matrix_position[0]][self.matrix_position[1]][self.matrix_position[2] + column][0]:
                    total_side_neighbours += 1

        # If the piece is blocked on both sides, it can not be taken
        if total_side_neighbours > 1:
            available = False

        return available

    def on_click(self, event):
        """ Action if the tile was clicked """

        # The current valid, selected tile for matching
        global current_piece

        # If clicked inside the rectangle area of the tile
        if event.button == 1:
            if self.rect.collidepoint(event.pos):
                # If the tile is available
                if self.available():
                    print(self.matrix_position[0], "Available")
                    # If there is no piece selected, select that one
                    if current_piece is None:
                        current_piece = [self.matrix_position[0],
                                         self.matrix_position[1],
                                         self.matrix_position[2]]
                        self.image = 'clicked'
                    else:
                        # If the current piece type is the same as the already selected piece
                        if (self.tile_number == pieces[tile_array[current_piece[0]]
                        [current_piece[1]]
                        [current_piece[2]][1]].tile_number):
                            # If the selected piece is itself, de-select
                            if (self.matrix_position[0] == current_piece[0]
                                    and self.matrix_position[1] == current_piece[1]
                                    and self.matrix_position[2] == current_piece[2]):
                                self.image = 'default'
                                current_piece = None
                            else:
                                # Put False in the 3D array at both of the pieces' locations
                                # They disappear as neighbours and don't blit anymore
                                tile_array[current_piece[0]][current_piece[1]][current_piece[2]][0] = False
                                tile_array[self.matrix_position[0]][self.matrix_position[1]][self.matrix_position[2]][
                                    0] = False
                                pieces[tile_array[current_piece[0]][current_piece[1]][current_piece[2]][1]].image = 'default'
                                executed_moves.append([[current_piece[0], current_piece[1], current_piece[2]],
                                                       [self.matrix_position[0], self.matrix_position[1],
                                                        self.matrix_position[2]]])
                                current_piece = None
                        else:
                            # If the pieces are different with different types
                            # De-select the last one and select the new one
                            pieces[
                                tile_array[current_piece[0]][current_piece[1]][current_piece[2]][1]].image = 'default'
                            current_piece = [self.matrix_position[0],
                                             self.matrix_position[1],
                                             self.matrix_position[2]]
                            self.image = 'clicked'
                else:
                    print(self.matrix_position[0], "Unavailable")
