from environment.Environment import *


class Font:
    def __init__(self, font, size, bold = False, italic = False, color = (0,0,0)):
        bold = (0 if False == bold else 1)
        italic = (0 if False == italic else 1)
        self.internalFont = pygame.font.SysFont(font, size, bold, italic)
        self.color = color


class Text:
    def __init__(self, font, surface):
        self.font = font
        self.surface = surface


class Engine:
    @staticmethod
    def loadImage(file):
        return pygame.image.load(Environment.resourceDir + file)


    @staticmethod
    def createFont(font, size, bold = False, italic = False, color = (0,0,0)):
        return Font(font, size, bold, italic, color)


    @staticmethod
    def createText(content, font):
        return Text(font, font.internalFont.render(content, True, font.color))


    @staticmethod
    def getTick():
        return pygame.time.get_ticks()


    @staticmethod
    def flushDisplay():
        Environment.flushDisplay()


    @staticmethod
    def draw(content, position):
        if type(content) is Text:
            content = content.surface
        Environment.screen.blit(content, position)