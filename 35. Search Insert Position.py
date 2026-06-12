class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        found = False
        for i in range(len(nums)):
            if nums[i]==target:
                found=True
                break
            elif nums[i]>target:
                found= True
                break
        if found:
            return i
        else:
            return i+1
