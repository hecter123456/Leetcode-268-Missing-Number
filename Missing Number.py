import unittest

class unitest(unittest.TestCase):
    def testNone(self):
        Input = []
        Output = 0
        self.assertEqual(Solution().missingNumber(Input),Output)

class Solution():
    def missingNumber(self, nums):
        if nums == []:
            return 0

if __name__ == '__main__':
    unittest.main()
