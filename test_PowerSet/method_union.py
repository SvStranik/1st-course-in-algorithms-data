import unittest

from PowerSet import PowerSet

Pw = PowerSet()
for i in range(10000,20000):
            Pw.put(str(i))
class PowerSet(unittest.TestCase):
    

    def test_1(self):
        per = []
        for i in range(10000):
            per.append(str(i))
        size = len(Pw.union(set(per)))
        self.assertEqual(size,20000)

    def test_2(self):
        per = []
        for i in range(5000,15000):
            per.append(str(i))
        size = len(Pw.union(set(per)))
        self.assertEqual(size,15000)
    
    def test_3(self):
        per = set
        self.assertEqual(len(Pw.union(per)),10000)

    def test_4(self):
        for i in range(10000,20000):
            Pw.remove(str(i))
        per = {'1'}
        self.assertEqual(Pw.union(per),['1'])

if __name__ == '__main__':
    unittest.main()