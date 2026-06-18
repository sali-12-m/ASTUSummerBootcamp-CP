class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq=Counter(nums)
        count=0
        for i in freq:
            if i+1 in freq:
                count=max(count,freq[i]+freq[i+1])
        return count
