
import pygame as pg
import math

class Game:
    def __init__(self):
        #init game window and clock etc.
        self.width = 500
        self.height = 900
        self.tilesize = 40
        pg.init()
        self.screen = pg.display.set_mode((self.width, self.height))
        self.clock = pg.time.Clock()
        self.rect = self.screen.get_rect()
        self.running = True

    def new(self):
        #start a new game
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(120)
            #after drawing everything we flip the display
            pg.display.flip()

    def update(self):
        #TODO Blocks falling
        pass

    def events(self):
        #TODO Keybinds for blocks rotating
        for event in pg.event.get():
            
            # check for closing window
            if event.type == pg.QUIT and self.playing:
                self.playing = False
            
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE and self.playing:
                    self.playing = False
    def draw(self):
        # drawing the screen
        self.screen.fill((0, 0, 0))
        self.debug_lines(self.screen)
        self.draw_frame(self.screen)

    def debug_lines(self, screen):
        for x in range((self.width - 100) // self.tilesize + 1):
            pg.draw.line(screen, (255, 255, 255), (x * 40 + 50, 0), (x * 40 + 50, self.height), 1)
        for y in range((self.height - 100) // self.tilesize + 1):
           pg.draw.line(screen, (255, 255, 255), (0, y * 40 + 50), (self.width, y * 40 + 50), 1)
    
    def draw_frame(self, screen):
        #top frame
        pg.draw.line(screen, (255, 255, 255), (50, 50), (self.width - 50, 50), 4)

