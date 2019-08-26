import time
import random
mapWidth = 10
mapHeight = 20
class Map:
    def __init__(self):
        self.blockR = 0
        self.blockX = 4
        self.blockY = 1
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
                if self.blockR == 0:
                    dx = bx
                    dy = by
                    pass
                elif self.blockR == 1:
                    dx = -by
                    dy = bx
                    pass
                elif self.blockR == 2:
                    dx = -bx
                    dy = -by
                    pass
                elif self.blockR == 3:
                    dx = by
                    dy = -bx
                    pass
                if self.block[by][bx] != '':
                    x = self.blockX + dx
                    y = self.blockY + dy
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

    def tryRotateRight(self):
        self.forTileInBlock(self.removeTile)
        self.blockR += 1
        self.blockR %= 4
        if not all(self.forTileInBlock(self.canExist)):
            self.blockR -= 1
            self.blockR %= 4
        self.forTileInBlock(self.placeTile)

    def tryRotateLeft(self):
        self.forTileInBlock(self.removeTile)
        self.blockR -= 1
        self.blockR %= 4
        if not all(self.forTileInBlock(self.canExist)):
            self.blockR += 1
            self.blockR %= 4
        self.forTileInBlock(self.placeTile)


    def update(self):
        self.tryMoveDown()
        self.tryRotateRight()
        
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

if __name__ == "__main__":
    m = Map()
    m.prettyPrint()
    while(True):
        m.update()
        m.prettyPrint()
        time.sleep(1)
