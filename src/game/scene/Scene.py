from enum import Enum, unique
from ..ResourceContainer import ResourceContainer


@unique
class SceneType(Enum):
    Welcome = 0
    Playing = 1


class Scene(ResourceContainer):
    sceneType = None


    def __init__(self):
        super().__init__()


    def handleEvent(self, event, currentTick):
        print("Scene.handleEvent")


    def draw(self):
        print("Scene.draw")