class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []

        for i in range(len(prices)):
            dc = 0 
            for j in range(i+1, len(prices)):
                if prices[j] > prices[i]:
                    dc = 0
                else:
                    dc = prices[j]
                    break
                
            res.append(prices[i] - dc)

        return res

        