class Solution:
    def maskPII(self, s: str) -> str:
        def maskEmail(s):
            name = ''
            i = 0
            while s[i] != '@':
                i += 1
            
            name = s[:i]
            res = name[0].lower() + '*****' + name[-1].lower() + s[i:].lower()
            return res

        def maskPhone(s):
            phone = ''.join(c for c in s if ord('0') <= ord(c) <= ord('9'))
            if len(phone) == 10:
                res = "***-***-" + phone[len(phone) - 4:]
            if len(phone) == 11:
                res = "+*-***-***-" + phone[len(phone) - 4:]
            if len(phone) == 12:
                res = "+**-***-***-" + phone[len(phone) - 4:]
            if len(phone) == 13:
                res = "+***-***-***-" + phone[len(phone) - 4:]
            return res
        
        if '@' in s:
            mask = maskEmail(s)
        else:
            mask = maskPhone(s)

        return mask