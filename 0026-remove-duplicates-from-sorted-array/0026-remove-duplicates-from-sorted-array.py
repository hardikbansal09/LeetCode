class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a=set(nums)
        nums[:] = sorted(a)
        return len(nums)
        