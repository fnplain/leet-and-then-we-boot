class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        longestrun = {}
        for x in nums:
            longestrun[x+1] = longestrun.get(x,0) + 1
            longestrun[x] = longestrun.get(x-1,0) + 1
        
        return max(longestrun.values())
