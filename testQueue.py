import unittest
import random

from Queue import Queue

class queueTest(unittest.TestCase):

    def test_1(self):
        qu = Queue()
        count = random.randint(100,500)
        for i in range(count):
            qu.enqueue(i)
        for i in range(count):
            qu.dequeue()
        self.assertEqual(qu.size(), 0)

    def test_2(self):
        qu = Queue()
        count1 = random.randint(3000,5000)
        count2 = random.randint(1000,3000)
        for i in range(count1):
            qu.enqueue(i)
        for i in range(count2):
            qu.dequeue()
        self.assertEqual(qu.size(), count1 -count2)
    def test_3(self):
        qu3 = Queue()
        count = 0
        for i in range(100):
            count1 = random.randint(1,500)
            count2 = random.randint(1,500)
            count = count + count1 - count2
            if count < 0: count = 0
            for i in range(count1):
                qu3.enqueue(i)
            for i in range(count2):
                qu3.dequeue()
        self.assertEqual(qu3.size(), count)

if __name__ == '__main__':
    unittest.main()
