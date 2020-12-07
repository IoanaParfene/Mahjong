import pygame

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
        ''' Initialize button attributes '''
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
        ''' On-click button action function'''
        if event.button == 1:
            if self.icon_rect.collidepoint(event.pos):
                function_name = str(self.button_type) + '_button_action'
                eval(function_name)(self)


def MusicOn_button_action(button):
    '''Turn music volume on and off'''
    if(button.varg[0]==False):
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
