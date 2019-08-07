from ..Engine import *
from .Scene import *


class SceneWelcome(Scene):
    def refreshPressStartText(self):
        self.pressStartText = Engine.createText("Press space to start", self.pressStartFonts[self.pressStartFontIndex])


    def __init__(self):
        super().__init__()

        sceneType = SceneType.Welcome

        self.setResource("background", Engine.loadImage("welcome.png"))

        self.pressStartFonts = []
        self.pressStartFonts.append(Engine.createFont("calibri", 40, False, True, (255,0,0)))
        self.pressStartFonts.append(Engine.createFont("calibri", 40, False, True, (0,255,0)))
        self.pressStartFonts.append(Engine.createFont("calibri", 40, False, True, (0,0,255)))
        self.pressStartFontIndex = 0
        self.refreshPressStartText()
        self.pressStartColorChangeInterval = 500
        self.lastPressStartColorChangeTick = Engine.getTick()


    def handleEvent(self, event, currentTick):
        lastPressStartColorChangeDuration = currentTick - self.lastPressStartColorChangeTick
        if (lastPressStartColorChangeDuration > self.pressStartColorChangeInterval):
            self.pressStartFontIndex = (self.pressStartFontIndex + 1) % 3
            self.refreshPressStartText()
            self.lastPressStartColorChangeTick = currentTick


    def draw(self):
        Engine.draw(self.resources["background"], (0,0))
        Engine.draw(self.pressStartText, (230,360))
    