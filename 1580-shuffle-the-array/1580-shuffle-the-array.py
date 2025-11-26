class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first, second = 0, n
        maxVal = 10000

        for i in range(2*n):
            if i % 2 == 0:
                nums[i] = (nums[first] % maxVal) *  maxVal + nums[i]
                first += 1
            else:
                nums[i] = (nums[second] % maxVal) * maxVal + nums[i]
                second += 1

        for i in range(2*n):
            nums[i] = nums[i] // maxVal
        
        return nums

        