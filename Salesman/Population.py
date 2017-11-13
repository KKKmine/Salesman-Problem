import random as r
from Individual import Individual

class Population:
    isKeepElitim = True

    def __init__(self, popSize = 0, selSize = 0, mutRate = 0):
        self.generation = 0
        self.individuals = []
        self.selectionSize = selSize
        self.mutationRate = mutRate

        for i in range(popSize):
            self.individuals += [Individual()]

    def GetFittest(self):
        fittest = self.individuals[0]
        for indi in self.individuals:
            if(fittest.GetDistance() > indi.GetDistance()):
                fittest = indi
        return fittest

    def Evolve(self):
        self.generation += 1
        newIndividuals = []
        if(self.isKeepElitim):
            newIndividuals += [self.GetFittest()]
        while(len(newIndividuals) < len(self.individuals)):
            parent1 = self.ParentSelect()
            parent2 = self.ParentSelect()
            newIndividuals += [Individual(parent1, parent2, self.mutationRate)]
        self.individuals = newIndividuals

    def ParentSelect(self):
        selection = Population()
        for i in range(self.selectionSize):
            selection.individuals += [self.individuals[r.randint(0, len(self.individuals)-1)]]
        return selection.GetFittest()