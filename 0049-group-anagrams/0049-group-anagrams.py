class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) < 2:
            return [strs]
        
        d = dict()
        for str in strs:
            count = [0] * 26
            for c in str:
                count[ord(c) - ord('a')] += 1
            count = tuple(count)
            if count not in d:
                d[count] = []
            d[count].append(str)

        return d.values()

        
        