import math
import random as r

class Individual:
    map = 0
    pointSize = 0
    mutationRate = 0.03

    def __init__(self, parent1 = None, parent2 = None, mutationRate = 0):
        self.path = []
        self.dist = -1
        if(parent1 == None and parent2 == None):
            self.path = list(range(self.pointSize))
            r.shuffle(self.path)
        else:
            #Cross Over
            start = r.randint(0, self.pointSize-1)
            end = r.randint(0, self.pointSize-1)
            if(start > end):
                start, end = end, start
            parentPath = parent1.path[start:end+1]
            for i in range(self.pointSize):
                if(not parent2.path[i] in parentPath):
                    self.path += [parent2.path[i]]
            for i in range(len(parentPath)):
                self.path.insert(start+i, parentPath[i])
            #Mutation
            for i in range(self.pointSize):
                if(r.random() < mutationRate):
                    rand = r.randint(0, self.pointSize-1)
                    self.path[i], self.path[rand] = self.path[rand], self.path[i]
        if(not len(self.path) == self.pointSize):
            print("Error Individual Create!")

    def GetDistance(self):
        if self.dist < 0:
            self.dist = 0
            for i in range(self.pointSize):
                p1 = self.path[i]
                p2 = self.path[(i+1)%self.pointSize]
                self.dist += math.sqrt((self.map.pointX[p1] - self.map.pointX[p2])**2 + (self.map.pointY[p1] - self.map.pointY[p2])**2)
        return self.dist

    def GetPathPos(self):
        pathX = []
        pathY = []
        for i in range(self.pointSize):
            pathX += [self.map.pointX[self.path[i]]]
            pathY += [self.map.pointY[self.path[i]]]
        pathX += [self.map.pointX[self.path[0]]]
        pathY += [self.map.pointY[self.path[0]]]
        return pathX, pathY

    def PrintPath(self):
        print("Individual Path:", end = " ")
        for i in range(self.pointSize):
            print(str(self.path[i]), end = " ")
        print()