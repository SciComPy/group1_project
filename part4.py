import matplotlib.pyplot as plt
import random
from ResistantVirus import ResistantVirus   
from Patient import Patient

def part4():
    maxPop = 1000
    time = []
    pop = []
    viruses = []
    gutResPop = []
    resistances = {'guttagonol':False}
    for i in range (0,100):
        a = ResistantVirus(.1,0.5,resistances,0.005)
        viruses.append(a)
    aPatient = Patient(viruses, maxPop)
    for i in range (0,300):
        if i == 149:
            aPatient.addPrescription('guttagonol')
            
        pop.append(aPatient.update())
        time.append(i)
        
        gutRes = []
        
        for v in aPatient.viruses:
            if (v != None):
                if(v.getResistance('guttagonol')):
                   gutRes.append(v)
                   
        gutResPop.append(len(gutRes))
        
    plt.figure('Time - Total Population')
    plt.plot(time,pop)
    plt.figure('Time - Guttagonol-Resistant')
    plt.plot(time,gutResPop)
    plt.show()
if __name__ == '__main__':
    part4()
