class Solution:
    def maxLength(self, nums: list[int]) -> int:
        best = 0
        n = len(nums)
        for i in range(n):
            prod, l, g = 1, 1, 0
            for j in range(i, n):
                x = nums[j]
                prod *= x
                l = lcm(l, x)
                g = gcd(g, x)
                if prod == l * g:
                    best = max(best, j - i + 1)
        return best
