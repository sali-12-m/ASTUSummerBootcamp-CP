class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if sum(nums)<k:
            return sum(nums)
        else:
            count=0
            s=sum(nums)
            while s%k!=0:
                s-=1
                count+=1
            return count 
