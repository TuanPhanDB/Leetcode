class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        freq = [[] * i for i in range(len(nums) + 1)]
        res = []

        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1

        for n in d:
            freq[d[n]].append(n)

        for f in range(len(freq) - 1, 0, -1):
            for num in freq[f]:
                res.append(num)
                if len(res) == k:
                    return res

        