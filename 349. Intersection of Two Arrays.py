class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        li=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] in nums2 and nums1[i] not in li:
                    li.append(nums1[i])
        return li 
