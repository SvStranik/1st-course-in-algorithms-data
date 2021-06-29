import unittest

from PowerSet import PowerSet

Pw = PowerSet()
for i in range(5000,20000):
    Pw.put(str(i))

class PowerSet(unittest.TestCase):
    

    def test_1(self):
        s = []
        for i in range(10000,15000):
            s.append(str(i))
        S = set(s)
        per = len(Pw.intersection(S))
        self.assertEqual(per,5000)


    def test_2(self):
        s = {}
        per = Pw.intersection(s)
        self.assertEqual(per,None)


    def test_3(self):
        for i in range(5000,20000):
            Pw.remove(str(i))
        s = []
        for i in range(10000,15000):
            s.append(str(i))
        S = set(s)
        per = Pw.intersection(S)
        self.assertEqual(per,None)

    
    def test_4(self):
        for i in range(5000,20000):
            Pw.put(str(i))
        s = []
        for i in range(10000):
            s.append(str(i))
        for i in range(15000,25000):
            s.append(str(i))
        for i in range(7000):
            s.append(str(i))
        S = set(s)
        per = len(Pw.intersection(S))
        self.assertEqual(per,10000)


if __name__ == '__main__':
    unittest.main()
