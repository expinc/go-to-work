import sys
import os
sys.path.append(os.path.dirname(__file__) + os.sep + '../')

import pygame.locals
from environment.environment import *
from game import game


Environment.init()
mygame = game.Game()
while True:
    event = Environment.getEvent()
    if event.type == pygame.locals.QUIT:
        sys.exit()
    mygame.idle()
