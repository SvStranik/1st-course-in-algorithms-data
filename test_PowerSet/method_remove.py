import unittest

from PowerSet import PowerSet

Pw = PowerSet()
for i in range(10000,50000):
            Pw.put(str(i))
class PowerSet(unittest.TestCase):
    

    def test_1(self):
        for i in range(10000,30000):
            Pw.remove(str(i))
        for j in range(10000):
            Pw.remove(str(j))
        self.assertEqual(Pw.size(),20000)

    def test_2(self):
        for i in range(15000,30000):
            Pw.remove(str(i))
        for j in range(5000):
            Pw.remove(str(j))
        self.assertEqual(Pw.size(),20000)


if __name__ == '__main__':
    unittest.main()