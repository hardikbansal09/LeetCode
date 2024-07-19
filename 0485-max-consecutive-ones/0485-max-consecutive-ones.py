class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a=b=0
        for num in nums:
            if num==1:
                a+=1
                b=max(b,a)
            else:
                a=0
        return b
        