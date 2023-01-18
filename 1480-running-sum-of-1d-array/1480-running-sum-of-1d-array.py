class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i,n in enumerate(nums) :
            if 0 < i < len(nums) :
                nums[i] = n + nums[i-1]
        return nums
    