from .Engine import Engine
from .ResourceContainer import *
from .scene.Scene import Scene
from .scene.SceneWelcome import SceneWelcome


class Game(ResourceContainer):
    def __init__(self):
        super().__init__()
        self.scene = SceneWelcome()
        self.fps = 20
        self.lastFlushedTick = Engine.getTick()


    def handleEvent(self, event):
        currentTick = Engine.getTick()
        tickTnterval = currentTick - self.lastFlushedTick

        self.scene.handleEvent(event, currentTick)

        if (tickTnterval > (1 / self.fps * 1000)):
            self.scene.draw()
            self.lastFlushedTick = currentTick
            Engine.flushDisplay()
