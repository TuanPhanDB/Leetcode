class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        checkNum = [[] * i for i in range(len(nums))]
        res = []

        for n in nums:
            checkNum[n - 1] = 1

        for i in range(len(checkNum)):
            if not checkNum[i]:
                res.append(i+1)

        return res