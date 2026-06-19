class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_window=sum(nums[:k])
        max_window=current_window
        l,r=0,k
        while r<len(nums):
            current_window=current_window- nums[l]+nums[r]
            max_window=max(max_window,current_window)
            r+=1
            l+=1
        return max_window/k
