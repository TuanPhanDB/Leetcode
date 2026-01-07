class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        sub = []
        n = len(s) // 2
        for i in range(len(s)):
            for j in range(i, len(s)):
                if len(s[i:j+1]) <= n:
                    sub.append(s[i:j+1])
            break
        
        for subStr in sub:
            if subStr * (len(s) // len(subStr)) == s:
                return True
                
        return False
        