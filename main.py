import pygame as pg
import sys
from settings import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()

    def new_game(self):
        pass

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.fill('black')

    def run(self):
        while True:
            self.update()
            self.draw()