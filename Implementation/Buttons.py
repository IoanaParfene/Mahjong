import pygame
import GameModel

volumeOn = True

class Button:

    pixels = 60
    buttonIconType = 2
    iconPref = 'Scroll'
    popUpPref = 'PopUp'

    def __init__(self, buttonType, iconPosition, popUpPositionAdd, screen, *varg):

        self.buttonType = buttonType

        self.iconPosition = iconPosition
        self.image = pygame.image.load('Icons/' + str(self.iconPref) + str(self.buttonIconType) + buttonType + '.png')
        self.image = pygame.transform.scale(self.image, (self.pixels, self.pixels))
        self.iconRect = self.image.get_rect(topleft=self.iconPosition)

        self.popUpPosition = ([list(self.iconPosition)[0] + popUpPositionAdd[0], list(self.iconPosition)[1] + popUpPositionAdd[1]])
        self.popUpImage = pygame.image.load('Icons/' + str(self.popUpPref) + buttonType + '.png')
        self.popUpImage = pygame.transform.scale(self.popUpImage, (self.pixels, self.pixels))
        self.popUpRect = self.popUpImage.get_rect(topleft=self.popUpPosition)

        self.screen = screen

        self.varg = list(varg)

    def on_click(self, event):
        if event.button == 1:
            if self.iconRect.collidepoint(event.pos):
                functionName = str(self.buttonType) + 'ButtonAction'
                eval(functionName)(self)

def SoundOnButtonAction(button):
    if(button.varg[0]==False):
        button.image = pygame.image.load('Icons/' + str(button.iconPref) + str(button.buttonIconType) + 'SoundOn' + '.png')
        button.image = pygame.transform.scale(button.image, (button.pixels, button.pixels))
        button.screen.blit(button.image, button.iconRect)
        button.varg[0] = True
        button.varg[1].set_volume(0.1)
    else:
        button.image = pygame.image.load('Icons/' + str(button.iconPref) + str(button.buttonIconType) + 'SoundOff' + '.png')
        button.image = pygame.transform.scale(button.image, (button.pixels, button.pixels))
        button.screen.blit(button.image, button.iconRect)
        button.varg[0] = False
        button.varg[1].set_volume(0.0)

def NewGameButtonAction(button):
    GameModel.InitPieceArrangement(button.varg[0])