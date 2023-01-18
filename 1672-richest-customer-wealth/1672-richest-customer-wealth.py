class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        a = list()
        for c in accounts :
            m = sum(c)
            a.append(m)
        return max(a)
        