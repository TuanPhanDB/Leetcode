class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeat = len(b) // len(a)
        cnt = 1

        while cnt <= repeat + 2:
            if b in a*cnt:
                return cnt
            else:
                cnt += 1
        
        return -1


        