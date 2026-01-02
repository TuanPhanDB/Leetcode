class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        def isWord(word):
            return ord('A') <= ord(word) <= ord('Z') or ord('a') <= ord(word) <= ord('z') or ord('0') <= ord(word) <= ord('9')

        n = sum(isWord(w) for w in s)

        if (n+k)%2 == 0:
            dash = n//k - 1
        else:
            dash = n//k
            
        cnt = k
        res = ''
        for i in reversed(range(len(s))):
            if isWord(s[i]):
                res = s[i].upper() + res
                cnt -= 1
            if cnt == 0 and dash > 0:
                cnt = k
                res = '-' + res
                dash -= 1

        return res