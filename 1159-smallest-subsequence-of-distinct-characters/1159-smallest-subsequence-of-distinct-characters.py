class Solution:
    def smallestSubsequence(self, s: str) -> str:
        d = dict()
        visited = set()
        stack = []

        #Initialize counter dict
        for c in s:
            if c not in d:
                d[c] = 0
            d[c] += 1
            
        for i in range(len(s)):
            d[s[i]] -= 1
            if s[i] not in visited:
                while stack and stack[-1] > s[i] and d[stack[-1]]:
                    visited.remove(stack[-1])
                    stack.pop()
                visited.add(s[i])
                stack.append(s[i])

        return "".join(stack)