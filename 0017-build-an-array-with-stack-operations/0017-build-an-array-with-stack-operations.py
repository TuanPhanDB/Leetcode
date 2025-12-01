class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        s = []
        i, idx = 1, 0

        while i <= n and idx < len(target):
            s.append("Push")
            if i == target[idx]:
                idx += 1
            else:
                s.append("Pop")
            i += 1

        return s
            






                
                


        