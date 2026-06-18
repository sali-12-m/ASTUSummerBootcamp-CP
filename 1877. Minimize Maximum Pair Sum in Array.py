class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        li=[]
        nums.sort()
        while l<r:
            li.append(nums[l]+nums[r])
            l+=1
            r-=1
        return max(li)
