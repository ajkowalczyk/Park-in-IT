"""
GameEngine module.

Handles low-level engine responsibilities using the selected backend (e.g. pygame).

This includes:
- initializing the game library (pygame.init)
- creating and managing the game window
- handling raw input/events from the system
- managing frame timing (FPS / clock)
- delegating rendering to the Renderer

GameEngine does NOT contain gameplay logic.
It only provides the technical layer required to run the game.
"""

# TODO:
# - initialize pygame
# - create window/screen
# - implement event polling (get_events)
# - detect quit events
# - integrate Renderer
# - implement frame timing (tick)

import src.core.config as cfg
import pygame as pg
from src.core.renderer import Renderer

class GameEngine:
    def __init__(self):
        print(f"GameEngine starting!")
        self.screensize = (cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT)
        self.fps = cfg.FPS
        self.clock = pg.time.Clock()
        pg.init()
        self.gamescreen = pg.display.set_mode(self.screensize)
        self.renderer = Renderer(self.gamescreen)
        print(f"GameEngine initialized!")