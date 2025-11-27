class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # res = [[] * i for i in range(len(nums))]
        # dup = 0

        # for i in range(len(nums)):
        #     if not res[nums[i] - 1]:
        #         res[nums[i] - 1] = nums[i]
        #     else:
        #         dup = nums[i]

        # for i in range(len(res)):
        #     if not res[i]:
        #         return [dup, i + 1]

        # return []

        n, numsS, setS = len(nums), sum(nums), sum(set(nums))

        actualS = n * (n+1) // 2

        return [numsS - setS, actualS - setS]


        
