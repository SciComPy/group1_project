import unittest
from SimpleVirus import SimpleVirus
from ResistantVirus import ResistantVirus

class Tester(unittest.TestCase):
    def test_noBirth_noClear_hasPop(self):
        SimpleVirus(0,0).reproduce(500)
    
    def test_noBirth_Clear_hasPop(self):
        SimpleVirus(0,1).reproduce(500)

    def test_birth_noClear_hasPop(self):
        SimpleVirus(1,0).reproduce(500)

    def test_birth_clear_hasPop(self):
        SimpleVirus(1,1).reproduce(500)

    def test_noBirth_noClear_noPop(self):
        SimpleVirus(0,0).reproduce(0)
    
    def test_noBirth_Clear_noPop(self):
        SimpleVirus(0,1).reproduce(0)

    def test_birth_noClear_noPop(self):
        SimpleVirus(1,0).reproduce(0)

    def test_birth_clear_noPop(self):
        SimpleVirus(1,1).reproduce(0)

    def test_noValues(self):
        ResistantVirus(0,0,{},0).reproduce(0,[])

    def test_hasValues(self):
        ResistantVirus(.5,.5,{'testDrug':True},.5).reproduce(100,['testDrug'])

if __name__ == '__main__':
    unittest.main()
