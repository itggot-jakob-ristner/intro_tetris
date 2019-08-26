import random

class Blocks:
    def __init__(self):

        self.I = ['t', 't', 't', 't']
        self.L = [
                ['1', '2'],
                ['3', '4'],
                ['5', '6'] 
                ]
        self.T = [
                ['p', ''],
                ['p', 'p'],
                ['p', ''] 
                ]
        self.J = [
                ['o', 'o'],
                ['o', ''],
                ['o', ''] 
                ]
        self.S = [
                ['g', ''],
                ['g', 'g'],
                ['', 'g'] 
                ]
        self.Z = [
                ['', 'r'],
                ['r', 'r'],
                ['r', ''] 
                ]
        self.O = [
                ['y', 'y'],
                ['y', 'y'] 
                ]
        
        self.Blocks = [self.I, self.L, self.T, self.J, self.S, self.Z, self.O]

    def getRandomBlock(self):
        return self.Blocks[random.randrange(7)]


