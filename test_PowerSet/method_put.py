import unittest

from PowerSet import PowerSet

Pw = PowerSet()
class PowerSet(unittest.TestCase):
    

    def test_1(self):
        counter = 20000
        for i in range(10000,30000):
            Pw.put(str(i))
        for j in range(10000):
            Pw.put(str(j))
        self.assertEqual(Pw.size(),30000)

    def test_2(self):
        for i in range(25000,30000):
            Pw.put(str(i))
        for j in range(5000):
            Pw.put(str(j))
        self.assertEqual(Pw.size(),30000)


if __name__ == '__main__':
    unittest.main()