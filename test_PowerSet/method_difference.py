import unittest

from PowerSet import PowerSet

Pw = PowerSet()
for i in range(10000,20000):
    Pw.put(str(i))

class PowerSet(unittest.TestCase):
    

    def test_1(self):
        s = []
        for i in range(15000):
            s.append(str(i))
        S = set(s)
        per = len(Pw.difference(S))
        self.assertEqual(per,5000)


    def test_2(self):
        s = []
        for i in range(7000,21000):
            s.append(str(i))
        S = set(s)
        per = len(Pw.difference(S))
        self.assertEqual(per,0)


if __name__ == '__main__':
    unittest.main()
