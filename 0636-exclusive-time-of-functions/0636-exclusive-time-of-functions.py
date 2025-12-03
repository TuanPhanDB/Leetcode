class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        s = []
        res = [0 * i for i in range(n)]

        for log in logs:
            cur = log.split(":")
            cur[0], cur[2] = int(cur[0]), int(cur[2])
            if s and cur[1] == "start":
                prev = s[-1]
                s.append(cur)
                res[prev[0]] += (cur[2] - prev[2])
            elif s and cur[1] == "end":
                start = s.pop()
                res[start[0]] += (cur[2] - start[2] + 1)
                if s:
                    #Change last value timestamp to cur timestamp
                    s[-1][2] = cur[2] + 1
            else:
                s.append(cur)
        
        return res