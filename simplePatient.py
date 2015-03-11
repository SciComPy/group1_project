class SimplePatient(object):

    def __init__(self, viruses, maxPop):
        self.viruses = viruses
        self.maxPop = maxPop
        self.population = 0


    def getTotalPop(self):
        self.population = len(self.viruses)
        return self.population

    def update(self):
        self.ref = self.viruses[:]
        for v in self.ref:
            if (v.doesClear()):
                self.viruses.remove(v)
        self.ref = self.viruses[:]
        self.population = len(self.viruses)
        for v in self.ref:
            if (v.reproduce(self.population)!=None and len(self.viruses)<self.maxPop):
                self.viruses.append(v)

        self.population = len(self.viruses)
        return len(self.viruses)
