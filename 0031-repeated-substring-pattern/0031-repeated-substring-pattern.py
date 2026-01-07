class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        i, j = 0, 1
        subStr = []
        while i < len(s) and j < len(s):
            curLen = j - i + 1
            n = curLen // 2
            if s[i:n] == s[n:j+1]:
                subStr = s[i:n]
                break
            j += 1

        step = len(subStr)
        if step < 1:
            return False

        for i in range(step, len(s), step):
            if s[i:i+step] != subStr:
                return False
        
        return True
        