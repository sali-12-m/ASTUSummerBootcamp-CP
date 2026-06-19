class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans=1
        l=1
        for i in range(1,len(prices)):
            if prices[i]==prices[i-1]-1:
                l+=1
            else:
                l=1
            ans+=l
        return ans
