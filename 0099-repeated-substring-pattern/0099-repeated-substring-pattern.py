class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, len(s), 1):
            if n % i == 0:
                subStr = s[:i]
                if subStr * (n // i) == s:
                    return True
                
        return False
        