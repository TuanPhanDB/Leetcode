class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        i = 0
        res = []
        while i < len(nums):
            cnt = 0
            cur = nums[i]
            for j in range(len(nums)):
                if nums[j] < cur:
                    cnt += 1

            res.append(cnt)
            i += 1
        
        return res
            