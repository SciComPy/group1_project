import matplotlib.pyplot as plt
import random
from SimpleVirus import SimpleVirus   
from simplePatient import SimplePatient

def part2():
    maxPop = 1000
    time = []
    pop = []
    viruses = []
    for i in range (0,500):
        a = SimpleVirus(.6,0.5)
        viruses.append(a)
    aPatient = SimplePatient(viruses, maxPop)
    for i in range (0,300):
        pop.append(aPatient.update())
        time.append(i)

    #print pop
    plt.plot(time,pop)
    plt.show()

if __name__ == '__main__':
    part2()
