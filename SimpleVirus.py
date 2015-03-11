from random import uniform
class NoChildException(Exception):
    print ('No child created!')
    pass

class SimpleVirus(object):
    def __init__ (self, maxBirthProb, clearProb):
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
    
    def doesClear(self):
        self.prob =  uniform(0,1)
        self.isClear = True
        if(self.prob >= self.clearProb):
            self.isClear = False
        
        return self.isClear
    
    def reproduce(self, popDensity):
        self.prob = uniform(0,popDensity)
        self.probBase = self.maxBirthProb * (1 - popDensity)
        if(self.prob >= self.probBase):        
	    return SimpleVirus(self.maxBirthProb, self.clearProb)
        else:
            raise NoChildException
