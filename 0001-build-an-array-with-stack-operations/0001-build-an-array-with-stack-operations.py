class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        s = []

        stream = [i for i in range(1, n+1)]

        i = 0

        while i < len(target):
            cur = target[i]
            if stream:
                num = stream.pop(0)
                s.append("Push")
            
            if cur == num:
                i += 1
            else:
                s.append("Pop")

        return s
            






                
                


        