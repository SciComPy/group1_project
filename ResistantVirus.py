from SimpleVirus import SimpleVirus
from SimpleVirus import NoChildException
from random import uniform
class ResistantVirus(SimpleVirus):
    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        self.resistances = resistances
        self.mutProb = mutProb

    def getResistance(self, drug):
        return self.resistances[drug]

    def reproduce(self, popDensity, activeDrugs):
        self.probRepro = uniform(0,popDensity)
        self.probBaseRepro = self.maxBirthProb * (1 - popDensity)
        if(self.probRepro >= self.probBaseRepro):
            self.newResist = {}

            for d in self.resistances.keys():
                probMut = uniform(0,1)
                if(probMut >= self.mutProb):
                    self.newResist[d] = self.resistances[d]
                else:
                    self.newResist[d] = (not (self.resistances[d]))

            vir = ResistantVirus(self.maxBirthProb, self.clearProb, self.newResist, self.mutProb)
            return vir
        else:
            raise NoChildException
                
