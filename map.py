import time
import random
mapWidth = 10
mapHeight = 20
class Map:
    def __init__(self):
        self.blockX = 1
        self.blockY = 15
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

    def forTileInBlock(self, run):
        returnValues = []
        for by in range(len(self.block)):
            for bx in range(len(self.block[by])):
                if self.block[by][bx] != '':
                    x = self.blockX + bx
                    y = self.blockY + by
                    returnValue = run(bx, by, x, y)
                    returnValues.append(returnValue)
        return returnValues

    def canExist(self, bx, by, x, y):
        if x < 0 or y < 0:
            return False
        mapTileIsFree = False
        try:
            mapTileIsFree = self.map[y][x] == ''
            pass
        except:
            pass
        return mapTileIsFree

    def removeTile(self, bx, by, x, y):
        self.map[y][x] = ''

    def placeTile(self, bx, by, x, y):
        self.map[y][x] = self.block[by][bx]

    def tryMove(self, moveFunction, unmoveFunction):
        self.forTileInBlock(self.removeTile)
        moveFunction()
        if not all(self.forTileInBlock(self.canExist)):
            unmoveFunction()
        self.forTileInBlock(self.placeTile)

    def tryMoveDown(self):
        self.forTileInBlock(self.removeTile)
        self.blockY += 1
        if not all(self.forTileInBlock(self.canExist)):
            self.blockY -= 1
        self.forTileInBlock(self.placeTile)

    def tryMoveRight(self):
        self.forTileInBlock(self.removeTile)
        self.blockX += 1
        if not all(self.forTileInBlock(self.canExist)):
            self.blockX -= 1
        self.forTileInBlock(self.placeTile)

    def tryMoveLeft(self):
        self.forTileInBlock(self.removeTile)
        self.blockX -= 1
        if not all(self.forTileInBlock(self.canExist)):
            self.blockX += 1
        self.forTileInBlock(self.placeTile)

    def update(self):
        if random.random()>0.5:
            if random.random()>0.9:
                self.tryMoveRight()
            else:
                self.tryMoveLeft()

        self.tryMoveDown()
        
    def prettyPrint(self):
        print()
        for line in self.map:
            for tile in line:
                if tile == '':
                    print('.', end='')
                    continue
                print(tile, end='')
            print()
        print()

m = Map()
m.prettyPrint()
while(True):
    m.update()
    m.prettyPrint()
    time.sleep(1)
