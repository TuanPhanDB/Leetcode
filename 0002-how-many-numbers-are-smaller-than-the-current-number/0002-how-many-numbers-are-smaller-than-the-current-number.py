class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortNums = sorted(nums)
        d = {}

        for i in range(len(sortNums)):
            if sortNums[i] not in d:
                d[sortNums[i]] = i

        res = []
        for n in nums:
            res.append(d.get(n))

        return res
