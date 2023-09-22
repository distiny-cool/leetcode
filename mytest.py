import unittest
from now import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_distMoney(self):
        self.assertEqual(self.s.distMoney(10, 3), 1)
        self.assertEqual(self.s.distMoney(20, 5), 2)
        self.assertEqual(self.s.distMoney(100, 10), 9)
        self.assertEqual(self.s.distMoney(10, 20), -1)
        self.assertEqual(self.s.distMoney(100, 1), 0)
        self.assertEqual(self.s.distMoney(100, 14), 12)

if __name__ == '__main__':
    unittest.main()