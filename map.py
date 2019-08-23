import time
mapWidth = 10
mapHeight = 20
class Map:
    def __init__(self):
        self.blockX = 1
        self.blockY = 2
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

    def update(self):
        def canExist(bx, by, x, y):
            try:
                mapTileIsFree = self.map[y][x] == ''
                pass
            finally:
                pass
            return mapTileIsFree

        def removeTile(bx, by, x, y):
            self.map[y][x] = ''

        def placeTile(bx, by, x, y):
            self.map[y][x] = self.block[by][bx]


        self.forTileInBlock(removeTile)
        self.blockY += 1
        self.forTileInBlock(placeTile)


    def forTileInBlock(self, run):
        returnValues = []
        for by in range(len(self.block)):
            for bx in range(len(self.block[by])):
                if self.block[by][bx] != '':
                    x = self.blockX + bx
                    y = self.blockY + by
                    returnValue = run(bx, by, x, y)
                    returnValues.append(returnValue)
        



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
