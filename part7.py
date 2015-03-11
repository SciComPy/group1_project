import matplotlib.pyplot as plt
from ResistantVirus import ResistantVirus   
from Patient import Patient


def part7 ():
    maxPop = 1000
    viruses = []
    time = []
    pop = []
    gutResPop = []
    grimResPop = []
    bothResPop = []
    resistances = {'guttagonol':False, 'grimpex':False}
    for i in range (0,1000):
        r = ResistantVirus(0.1, 0.5, resistances, 0.005)
        viruses.append(r)
    aPatient = Patient (viruses, maxPop)

    for i in range (0,600):
        if i == 149:
            aPatient.addPrescription('guttagonol')

        if i == 449:
            aPatient.addPrescription('grimpex')

        pop.append(aPatient.update())

        gutRes = []
        grimRes = []
        bothRes = []

        for v in aPatient.viruses:
            if (v != None):
                if(v.getResistance('guttagonol') and (not(v.getResistance('grimpex')))):
                   gutRes.append(v)
                elif(v.getResistance('grimpex') and (not(v.getResistance('guttagonol')))):
                   grimRes.append(v)
                elif(v.getResistance('guttagonol') and (v.getResistance('grimpex'))):
                   bothRes.append(v)
        gutResPop.append(len(gutRes))
        grimResPop.append(len(grimRes))
        bothResPop.append(len(bothRes))
        time.append(i)


    plt.figure('First Patient: Time - Total population')
    plt.plot(time,pop)
    plt.figure('First Patient: Time - Guttagonol resistant viruses')
    plt.plot(time,gutResPop)
    plt.figure('First Patient: Time - Grimpex resistant viruses')
    plt.plot(time,grimResPop)
    plt.figure('First PatientTime - Resistant to 2 drugs')
    plt.plot(time,bothResPop)

    gutResPop2 = []
    grimResPop2 = []
    bothResPop2 = []
    viruses = []
    for i in range (0,1000):
        r = ResistantVirus(0.1, 0.5, resistances, 0.0005)
        viruses.append(r)
    aPatient2 = Patient (viruses, maxPop)

    pop2 = []
    time2 = []
    for i in range (0,300):
        if i == 149:
            aPatient2.addPrescription('guttagonol')
            aPatient2.addPrescription('grimpex')
        pop2.append(aPatient2.update())
        gutRes2 = []
        grimRes2 = []
        bothRes2 = []

        for v in aPatient2.viruses:
            if (v != None):
                if(v.getResistance('guttagonol') and (not(v.getResistance('grimpex')))):
                   gutRes2.append(v)
                elif(v.getResistance('grimpex') and (not(v.getResistance('guttagonol')))):
                   grimRes2.append(v)
                elif(v.getResistance('guttagonol') and (v.getResistance('grimpex'))):
                   bothRes2.append(v)
        gutResPop2.append(len(gutRes2))
        grimResPop2.append(len(grimRes2))
        bothResPop2.append(len(bothRes2))
        time2.append(i)

    plt.figure('Second Patient: Time - Total population')
    plt.plot(time2,pop2)
    plt.figure('Second Patient: Time - Guttagonol resistant viruses')
    plt.plot(time2,gutResPop2)
    plt.figure('Second Patient: Time - Grimpex resistant viruses')
    plt.plot(time2,grimResPop2)
    plt.figure('Second PatientTime - Resistant to 2 drugs')
    plt.plot(time2,bothResPop2)
    plt.show()

       
if __name__ == '__main__':
    part7()
