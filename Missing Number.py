import unittest

class unitest(unittest.TestCase):
    def testNone(self):
        Input = []
        Output = 0
        self.assertEqual(Solution().missingNumber(Input),Output)
    def testSample(self):
        Input = [3,0,1]
        Output = 2
        self.assertEqual(Solution().missingNumber(Input),Output)

class Solution():
    def missingNumber(self, nums):
        if nums == []:
            return 0
        total = (1 + len(nums)) * len(nums) / 2
        return int(total) - sum(nums)

if __name__ == '__main__':
    unittest.main()
