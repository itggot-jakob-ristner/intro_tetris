import time
import random
import math
import Blocks
mapWidth = 10
mapHeight = 20
class Map:
    def __init__(self):
        self.blockR = 0
        self.blockX = 4
        self.blockY = 4
        self.block = [
                            ['', 'r'],
                            ['', 'r'],
                            ['r', 'r'],
                            ]

        self.map = []
        for y in range(mapHeight):
            line = []
            for x in range(mapWidth):
                line.append('')
            self.map.append(line)

    def forTileInBlock(self, myMap, run):
        returnValues = []
        height = len(self.block)
        width = len(self.block[0])
        midX = math.floor(width/2)
        midY = math.floor(height/2)
        for by in range(height):
            for bx in range(width):
                if self.block[by][bx] == '':
                    continue
                dx = bx - midX
                dy = by - midY
                if self.blockR == 0:
                    rx = dx
                    ry = dy
                elif self.blockR == 1:
                    rx = -dy
                    ry = dx
                elif self.blockR == 2:
                    rx = -dx
                    ry = -dy
                elif self.blockR == 3:
                    rx = dy
                    ry = -dx
                x = self.blockX + rx + midX
                y = self.blockY + ry + midY
                returnValue = run(myMap, bx, by, x, y)
                returnValues.append(returnValue)
        return returnValues

    def canExist(self, myMap, bx, by, x, y):
        if x < 0 or y < 0:
            return False
        mapTileIsFree = False
        try:
            mapTileIsFree = myMap[y][x] == ''
            pass
        except:
            pass
        return mapTileIsFree

    def removeTile(self, myMap, bx, by, x, y):
        myMap[y][x] = ''

    def placeTile(self, myMap, bx, by, x, y):
        myMap[y][x] = self.block[by][bx]

    def tryMoveDown(self):
        self.blockY += 1
        if not all(self.forTileInBlock(self.map, self.canExist)):
            self.blockY -= 1

    def tryMoveRight(self):
        self.blockX += 1
        if not all(self.forTileInBlock(self.map, self.canExist)):
            self.blockX -= 1

    def tryMoveLeft(self):
        self.blockX -= 1
        if not all(self.forTileInBlock(self.map, self.canExist)):
            self.blockX += 1

    def tryRotateRight(self):
        self.blockR += 1
        self.blockR %= 4
        if not all(self.forTileInBlock(self.map, self.canExist)):
            self.blockR -= 1
            self.blockR %= 4

    def tryRotateLeft(self):
        self.blockR -= 1
        self.blockR %= 4
        if not all(self.forTileInBlock(self.map, self.canExist)):
            self.blockR += 1
            self.blockR %= 4

    def getMap(self):
        returnMap = []
        for line in self.map:
            returnMap.append(list(line))
        self.forTileInBlock(returnMap, self.placeTile)
        return returnMap

    def update(self):
        self.tryRotateRight()
        #self.tryMoveDown()
        
    def prettyPrint(self):
        mapToPrint = self.getMap()
        print()
        for line in mapToPrint:
            for tile in line:
                if tile == '':
                    print('.', end='')
                    continue
                print(tile, end='')
            print()
        print()

if __name__ == "__main__":
    m = Map()
    m.prettyPrint()
    m.tryMoveDown()
    while(True):
        m.update()
        m.prettyPrint()
        time.sleep(1)
