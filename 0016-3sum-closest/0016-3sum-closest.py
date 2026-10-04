class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:

        nums.sort()

        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):

            left = i + 1
            right = len(nums) - 1

            while left < right:

                current_sum = nums[i] + nums[left] + nums[right]

                # Check if current sum is closer
                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum

                # Perfect match
                if current_sum == target:
                    return current_sum

                # Need a bigger sum
                elif current_sum < target:
                    left += 1

                # Need a smaller sum
                else:
                    right -= 1

        return closest