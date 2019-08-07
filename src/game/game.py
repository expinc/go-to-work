from enum import Enum
from enum import unique
from .engine import Engine
from .gameEntity import *


@unique
class CockpitType(Enum):
    Welcome = 0
    Playing = 1


class Game(GameEntity):
    def __init__(self):
        super().__init__()
        self.cockpitType = CockpitType.Welcome
        self.setResource("background", Engine.loadImage("welcome.png"))

        self.pressStartColors = []
        self.pressStartColors.append(Engine.createFont("calibri", 40, False, True, (255,0,0)))
        self.pressStartColors.append(Engine.createFont("calibri", 40, False, True, (0,255,0)))
        self.pressStartColors.append(Engine.createFont("calibri", 40, False, True, (0,0,255)))
        self.pressStartColorIndex = 0
        self.pressStartColorChangeInterval = 500

        self.fps = 20
        self.lastTick = Engine.getTick()


    def idle(self):
        currentTick = Engine.getTick()
        tickTnterval = currentTick - self.lastTick
        refreshTick = False

        Engine.draw(self.resources["background"], (0,0))

        pressStartText = Engine.createText("Press space to start", self.pressStartColors[self.pressStartColorIndex])
        Engine.draw(pressStartText, (230,360))
        if (tickTnterval > self.pressStartColorChangeInterval):
            self.pressStartColorIndex = (self.pressStartColorIndex + 1) % 3
            refreshTick = True

        if True == refreshTick:
            self.lastTick = currentTick
        Engine.flushDisplay()
