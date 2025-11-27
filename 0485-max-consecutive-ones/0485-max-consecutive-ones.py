class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        cnt = 0
        maxCnt = 0
        while i < len(nums):
            if nums[i] == 1:
                cnt += 1
                maxCnt = max(maxCnt, cnt)
            else:
                cnt = 0
            i += 1

        return maxCnt