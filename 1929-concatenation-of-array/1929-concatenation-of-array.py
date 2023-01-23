class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = list()
        n = len(nums)
        for i, num in enumerate(nums) : 
            ans.insert(i, num)
            ans.insert(i + n,  num)
        return ans