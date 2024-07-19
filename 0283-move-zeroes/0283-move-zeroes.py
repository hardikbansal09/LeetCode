class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_zero = 0
        for current in range(len(nums)):
            if nums[current] != 0:
                nums[last_zero], nums[current] = nums[current], nums[last_zero]
                last_zero += 1
        