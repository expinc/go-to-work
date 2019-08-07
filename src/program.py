import sys
import os
sys.path.append(os.path.dirname(__file__) + os.sep + '../')

import pygame.locals
from environment.Environment import *
from game import Game


Environment.init()
mygame = Game.Game()
while True:
    event = Environment.getEvent()
    if event.type == pygame.locals.QUIT:
        sys.exit()
    mygame.handleEvent(event)
