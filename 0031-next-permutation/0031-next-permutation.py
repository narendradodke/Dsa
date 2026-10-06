class Solution:
    def nextPermutation(self, nums):
        n = len(nums)

        # 1. Find the first decreasing element from right
        i = n - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 2. Find the smallest element greater than nums[i]
        if i >= 0:
            j = n - 1

            while nums[j] <= nums[i]:
                j -= 1

            # 3. Swap
            nums[i], nums[j] = nums[j], nums[i]

        # 4. Reverse the suffix
        left = i + 1
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1