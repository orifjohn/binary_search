class Solution:
    def solve(self, nums):
        if not nums:
            return []
        minSoFar, prev = nums[0], nums[0]
        for i in range(1, len(nums)):
            minSoFar = min(minSoFar, prev)
            prev = nums[i]
            nums[i] = minSoFar

        nums[0] = 0
        return nums

