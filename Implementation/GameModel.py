import pygame
import random

piecePixels = 75

pieceImages = []
clickedPieceImages = []

tileArray = []

def LoadPieceImages():
    global piecePixels
    tileSize = (int(piecePixels * 0.75), piecePixels)
    for i in range(0,37):
        pieceImages.append(pygame.transform.scale(pygame.image.load('Icons/Pieces/Tile' + str(i) +'.png'), tileSize))
        clickedPieceImages.append(pygame.transform.scale(pygame.image.load('Icons/Pieces/TileS' + str(i) +'.png'), tileSize))

def CreateTileArray():

    for level in range(0,5):
        level = []
        for line in range(0,9):
            line = []
            for column in range(0,16):
                # existing, tile number, screen position, pieceGroup
                pieceInfo = [False, -1, (), []]
                line.append(pieceInfo)
            level.append(line)
        tileArray.append(level)

def PiecePosition(level, line, column, special):
    global piecePixels
    if(special == True):
        x_coord = column * int(piecePixels * 0.75) + 180 - column*5 - level*5
        y_coord = 3.5*piecePixels + 80 - 5 - level*5
    else:
        x_coord = column * int(piecePixels * 0.75) + 180 - 5 * level - column * 5
        y_coord = line * piecePixels + 25 - 5*level - line * 5
    return (x_coord, y_coord)

def StandardArrangement():

    global piecePixels
    columns = [[12,8,10,12],[6,6,6],[4,4],[2,2]]

    for level in range(0,5):
        for line in range(1+level,5):
            start = 8-columns[level][line-level-1]//2
            end = start + columns[level][line-level-1]
            for column in range(start,end):
                tileArray[level][line][column] = [True, random.randrange(1,37), PiecePosition(level,line,column,False), []]
        for line in range(5, 9-level):
            start = 8 - columns[level][8-line-level] // 2
            end = start + columns[level][8-line-level]
            for column in range(start, end):
                tileArray[level][line][column] = [True, random.randrange(1, 37), PiecePosition(level,line,column,False), []]

    tileArray[0][4][1] = [True, random.randrange(1, 37), PiecePosition(0, 4, 1, True), []]
    tileArray[0][5][14] = [True, random.randrange(1, 37), PiecePosition(0, 5, 14, True), []]
    tileArray[0][5][15] = [True, random.randrange(1, 37), PiecePosition(0, 5, 15, True), []]
    tileArray[4][5][8] = [True, random.randrange(1, 37), PiecePosition(4, 5, 7.5, True), []]

    tileArray[0][5][2][3] = [[0, 5, 1], [0, 5, 2]]
    tileArray[0][4][13][3] = [[0, 4, 14], [0, 5, 14]]
    tileArray[2][4][8][3] = [[3, 4, 8], [3, 5, 8]]
    tileArray[2][4][7][3] = [[3, 4, 7], [3, 5, 8]]
    tileArray[2][5][7][3] = [[3, 5, 7], [3, 5, 8]]

def ArrangeTiles(version):
    if(version=='standard'):
        StandardArrangement()
    else:
        StandardArrangement()

def RenderPieces(screen):
    for level in range(0,5):
        for line in range(0,9):
            for column in range(0, 16):
                if tileArray[level][line][column][0] == True:
                    screen.blit(pieceImages[tileArray[level][line][column][1]], tileArray[level][line][column][2])

def InitPieceArrangement(gameVersion):
    LoadPieceImages()
    CreateTileArray()
    ArrangeTiles(gameVersion)
