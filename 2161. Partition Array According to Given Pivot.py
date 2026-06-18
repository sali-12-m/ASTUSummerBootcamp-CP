class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less=[]
        equal=[]
        gret=[]
        for i in nums:
            if i<pivot:
                less.append(i)
            elif i==pivot:
                equal.append(i)
            else:
                gret.append(i)
        return less+equal+gret
