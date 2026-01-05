class Solution:
    def maskPII(self, s: str) -> str:
        def maskEmail(s):
            name, domain = s.split('@')
            res = name[0] + '*****' + name[-1] + '@' + domain
            return res

        def maskPhone(s):
            phone = ''.join(c for c in s if ord('0') <= ord(c) <= ord('9'))
            countryLen = len(phone) - 10
            res = "***-***-" + phone[-4:]
            if countryLen == 0:
                return res
        
            return "+" + "*" * countryLen + "-" + res
        
        if '@' in s:
            return maskEmail(s).lower()
        return maskPhone(s).lower()