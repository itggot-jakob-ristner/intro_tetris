from map import *
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
        self.gamemap = Map()
        self.tick = 0
        self.colordict = {
                "r" : (255, 0, 0),
                "g" : (0, 255, 0),
                "b" : (0, 0, 255)
                }

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
        self.tick += 1
        if self.tick > 120:
            self.gamemap.update()
            self.tick = 0

    def events(self):
        #TODO Keybinds for blocks rotating
        for event in pg.event.get():
            
            # check for closing window
            if event.type == pg.QUIT and self.playing:
                self.playing = False
            
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE and self.playing:
                    self.playing = False
                if event.key == pg.K_s:
                    self.gamemap.tryMoveDown()
                    
    def draw(self):
        # drawing the screen
        self.screen.fill((0, 0, 0))
        self.debug_lines(self.screen)
        self.draw_frame(self.screen)
        #self.fillcoord(self.screen, (9,19), (255, 0, 0))
        self.drawmap(self.screen)

    def debug_lines(self, screen):
        for x in range((self.width - 100) // self.tilesize + 1):
            pg.draw.line(screen, (255, 255, 255), (x * 40 + 50, 0), (x * 40 + 50, self.height), 1)
        for y in range((self.height - 100) // self.tilesize + 1):
           pg.draw.line(screen, (255, 255, 255), (0, y * 40 + 50), (self.width, y * 40 + 50), 1)
    
    def draw_frame(self, screen):
        #top frame
        pg.draw.line(screen, (255, 255, 255), (50, 50), (self.width - 50, 50), 4)
        pg.draw.line(screen, (255, 255, 255), (50, self.height - 50), (self.width - 50, self.height - 50), 4)

        pg.draw.line(screen, (255, 255, 255), (50, 50), (50, self.height - 50), 4)
        pg.draw.line(screen, (255, 255, 255), (self.width - 50, 50), (self.width - 50, self.height - 50), 4)

    def coordtoscreen(self, coord):
        # y coord to top left coord
        x = 10 + 40 * (coord[0] + 1)
        y = 10 + 40 * (coord[1] + 1)

        return (x, y)
    
    def fillcoord(self, screen, coord, color):
        coord = self.coordtoscreen(coord)
        x = coord[0]
        y = coord[1] 
        pg.draw.rect(screen, color, (x, y, 40, 40))

    def drawmap(self, screen):
        for y in range(len(self.gamemap.getMap())):
            for x in range(len(self.gamemap.getMap()[y])):
                colorstring = self.gamemap.getMap()[y][x]
                if colorstring == '':
                    continue
                color = self.colordict[colorstring]
                self.fillcoord(screen, (x,y), color)
                #print(coords)
               
                














