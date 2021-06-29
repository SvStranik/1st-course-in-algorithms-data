import unittest

from PowerSet import PowerSet

Pw = PowerSet()
for i in range(10000,20000):
    Pw.put(str(i))

class PowerSet(unittest.TestCase):
    

    def test_1(self):
        s = []
        for i in range(13000,15000):
            s.append(str(i))
        S = set(s)
        self.assertEqual(Pw.issubset(S),True)


    def test_2(self):
        s = []
        for i in range(10000,20000):
            s.append(str(i))
        S = set(s)
        self.assertEqual(Pw.issubset(S),True)

    def test_3(self):
        s = []
        for i in range(8000,15000):
            s.append(str(i))
        S = set(s)
        self.assertEqual(Pw.issubset(S),False)

if __name__ == '__main__':
    unittest.main()
