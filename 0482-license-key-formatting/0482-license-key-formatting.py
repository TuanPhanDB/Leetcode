class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = "".join(s.upper().split("-"))
        
        head = len(s) % k
        res = []
        
        if head:
            res.append(s[:head])
        
        for i in range(head, len(s), k):
            res.append(s[i: i+k])

        return "-".join(res)