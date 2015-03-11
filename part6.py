import matplotlib.pyplot as plt
import random
from ResistantVirus import ResistantVirus   
from Patient import Patient

def part6():
    maxPop = 1000

    finalValuesFirst = []
    finalValuesSecnd = []
    finalValuesThird = []
    finalValuesFourt = []
    resistances = {'guttagonol':False, 'grimpex':False}
    for q in range (0,5):
        #FIRST
        time = []
        pop = []
        viruses = []
        for i in range (0,100):
            a = ResistantVirus(.1,0.5,resistances,0.005)
            viruses.append(a)
        aPatient1 = Patient(viruses, maxPop)


        aPatient4 = Patient(viruses, maxPop)
        
        for i in range (0,600):
            if i == (150):
                aPatient1.addPrescription('guttagonol')
            if i == 450:
                aPatient1.addPrescription('grimpex')
            pop.append(aPatient1.update())
            time.append(i)

        finalValuesFirst.append(len(filter(None,aPatient1.viruses)))
        #END OF FIRST
                   
        #SECOND           
        pop = []
        time = []
        viruses = []

        for i in range (0,100):
            a = ResistantVirus(.1,0.5,resistances,0.005)
            viruses.append(a)

        aPatient2 = Patient(viruses, maxPop)

        for i in range (0,450):
            if i == (150):
                aPatient2.addPrescription('guttagonol')

            if i == 300:
                aPatient2.addPrescription('grimpex')
                
            pop.append(aPatient2.update())
            time.append(i)	
        finalValuesSecnd.append(len(filter(None,aPatient2.viruses)))
        #END OF SECOND


        #THIRD
        pop = []
        time = []
        viruses = []

        for i in range (0,100):
            a = ResistantVirus(.1,0.5,resistances,0.005)
            viruses.append(a)
        
        aPatient3 = Patient(viruses, maxPop)
        for i in range (0,375):
            if i == (75):
                aPatient3.addPrescription('grimpex')
            
            if i == (150):
                aPatient3.addPrescription('guttagonol')
            pop.append(aPatient3.update())
            time.append(i)

        finalValuesThird.append(len(filter(None,aPatient3.viruses)))
        #END OF THIRD

        #FOURTH
        pop = []
        time = []
        viruses = []
        for i in range (0,100):
            a = ResistantVirus(.1,0.5,resistances,0.005)
            viruses.append(a)

        aPatient2 = Patient(viruses, maxPop)
        
        for i in range (0,300):
            if i == (150):
                aPatient4.addPrescription('guttagonol')
            if i == 0:
                aPatient4.addPrescription('grimpex')
            pop.append(aPatient4.update())
            time.append(i)
        finalValuesFourt.append(len(filter(None,aPatient4.viruses)))
        #END OF FOURTH
    
    plt.figure('Drug treatment at 300')
    plt.hist(finalValuesFirst)
    plt.figure('Drug treatment at 150')
    plt.hist(finalValuesSecnd)
    plt.figure('Drug treatment at 75')
    plt.hist(finalValuesThird)
    plt.figure('Drug treatment at 0')
    plt.hist(finalValuesFourt)
    plt.show()

if __name__ == '__main__':
    part6()
