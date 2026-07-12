class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans = 0
        n = len(nums)

        for i in range(n):
            if nums[i] % 2 == 1 or nums[i] > threshold:
                continue

            length = 1
            j = i + 1

            while j < n:
                if nums[j] > threshold:
                    break
                if nums[j] % 2 == nums[j - 1] % 2:
                    break
                length += 1
                j += 1

            ans = max(ans, length)

        return ans