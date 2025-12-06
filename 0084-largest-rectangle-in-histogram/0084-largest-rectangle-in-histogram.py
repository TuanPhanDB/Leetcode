class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        mx = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                mn = min(heights[i:j+1])
                area = mn * len(heights[i:j+1])
                mx = max(mx, area)

        return mx