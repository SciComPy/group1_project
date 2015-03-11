from simplePatient import SimplePatient
class Patient(SimplePatient):
    
    def __init__ (self, viruses, maxPop):
        self.viruses = viruses
        self.maxPop = maxPop
        self.prescriptions = []
    def addPrescription(self, newDrug):
        if (not(newDrug in self.prescriptions)):
            self.prescriptions.append(newDrug)

    def getPrescriptions(self):
        return self.prescriptions

    def getResistPop(self, drugResist):
        self.resistant = 0
        for v in viruses:
            for d in drugResist:
                if (v.getResistance(d)):
                    resistant+=1

        return self.resistant

    def update(self):
        for i in range (0,len(self.viruses)-1):
            if(self.viruses[i] != None):
                if (self.viruses[i].doesClear()):
                    self.viruses[i] = None
        self.population = len(filter(None,self.viruses))
                        
        for i in range (0,len(self.viruses)-1):
            if (self.viruses[i]!=None):
                aVirus = self.viruses[i].reproduce(self.population,self.prescriptions)
                if (aVirus!=None and len(filter(None,self.viruses))<self.maxPop):
                    self.viruses.append(aVirus)
        self.population = len(filter(None,self.viruses))
        return len(filter(None,self.viruses))
    
    
