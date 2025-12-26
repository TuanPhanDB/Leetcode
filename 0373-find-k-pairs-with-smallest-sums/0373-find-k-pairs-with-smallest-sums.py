class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []

        for n1 in nums1:
            for n2 in nums2:
                res.append((n1 + n2, [n1, n2]))

        heapq.heapify(res)

        return [heapq.heappop(res)[1] for _ in range(k)]