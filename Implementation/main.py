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
screen = pygame.display.set_mode((1200, 770))
bg = pygame.image.load('Pictures/bk.png')
table = pygame.image.load('Pictures/WoodTable.jpg')
table = pygame.transform.scale(table, (1500, 800))

# Music and Sound
background_music = pygame.mixer.Sound('Sound/bkmusic.wav')
background_music.play(-1)
background_music.set_volume(0.1)
volumeOn = True

# Time
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
start_time = time.time()


def game_over_variables():
    """ Initializing the game over variables """
    # Losing message
    lost = False
    lost_message = pygame.image.load('Icons/Loss.png')
    lost_message = pygame.transform.scale(lost_message, (500, 300))
    # Winning message
    won = False
    won_message = pygame.image.load('Icons/Win.png')
    won_message = pygame.transform.scale(won_message, (500, 300))
    # Auto-shuffling message
    shuffle_message = pygame.image.load('Icons/NoMoves.png')
    shuffle_message = pygame.transform.scale(shuffle_message, (500, 130))
    return lost, won, won_message, lost_message, shuffle_message


def main():
    """ Initialize game elements and run main loop """

    # Initialize Buttons and Pieces
    ControlManagement.create_buttons(screen, background_music, volumeOn)
    TileArrangement.init_piece_arrangement()

    # Winning Conditions
    lost, won, won_message, lost_message, shuffle_message = game_over_variables()

    # Score and time
    game_time_not_lost = "0"
    game_score = "0"

    # Run game loop by frame
    running = True
    while running:
        # Render screen, buttons, check if button hover occurs
        screen.blit(table, (0, 0))
        screen.blit(bg, (0, 0))
        TileArrangement.render_pieces(screen)
        ControlManagement.render_buttons(screen)

        # Check if the game is over
        if lost:
            # Auto-shuffle if any shuffle uses remain
            if ControlManagement.try_shuffling(ControlManagement.buttons[1]) > 0:
                lost = False
                screen.blit(shuffle_message, (335, 80))
                pygame.display.update()
                time.sleep(2)
            else:
                screen.blit(lost_message, (335, 160))
        if won:
            screen.blit(won_message, (335, 160))

        # Render button hover messages
        ControlManagement.hover_buttons(screen)

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if lost is False and won is False:
                if TileArrangement.check_win() == "Lost":
                    lost = True
                elif TileArrangement.check_win() == "Won":
                    won = True
            if lost is False and won is False:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Action if a certain button was clicked
                    for button in ControlManagement.buttons:
                        button.on_click(event)
                    # Action if a certain game tile was clicked
                    for piece in TileArrangement.pieces:
                        piece.on_click(event)
                # Get the score and time when the game is not over
                game_time_not_lost = str(int((time.time() - TileArrangement.start_time)))
                game_score = str(len(TileArrangement.executed_moves))
            if lost is True or won is True:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Quitting during won/loss messages
                    if pygame.Rect((617, 330), (90, 40)).collidepoint(event.pos):
                        running = False
                    # Replay during won/loss messages
                    if pygame.Rect((450, 330), (95, 40)).collidepoint(event.pos):
                        won = False
                        lost = False
                        ControlManagement.restart_game(ControlManagement.buttons[3])
        # General game time
        game_time = str(int((time.time() - TileArrangement.start_time)))
        # Display the score and time
        if lost is True or won is True:
            game_time_text = myfont.render('Time: ' + game_time_not_lost, False, (0, 0, 0))
        else:
            game_time_text = myfont.render('Time: ' + game_time, False, (0, 0, 0))
        screen.blit(game_time_text, (940, 100))
        game_score_text = myfont.render('Score: ' + game_score, False, (0, 0, 0))
        screen.blit(game_score_text, (940, 135))
        # Display the screen
        pygame.display.update()


main()
