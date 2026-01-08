class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # for i in range(len(s)):
        #     if s[i] == goal[0]:
        #         swap = s[i:] + s[:i]
        #         if swap == goal:
        #             return True
    
        # return False
        if len(goal) != len(s):
            return False
        
        return goal in s + s
        