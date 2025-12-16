class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            if not max_heap:
                return 0
            
            first, second = -heapq.heappop(max_heap), -heapq.heappop(max_heap)
            heapq.heappush(max_heap, -(first - second))

        return -max_heap[0]
            
        