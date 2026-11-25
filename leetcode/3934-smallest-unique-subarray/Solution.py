class Solution:
    def smallestUniqueSubarray(self, nums):
        n = len(nums)
        M = (1 << 61) - 1
        base = random.randint(10**7, 10**8)

        def exists_unique(L):
            top = pow(base, L - 1, M)
            h = 0
            for x in nums[:L]:
                h = (h * base + x) % M

            counts = {h: 1}

            for i in range(1, n - L + 1):
                h = ((h - nums[i-1] * top) * base + nums[i+L-1]) % M
                counts[h] = counts.get(h, 0) + 1

            return 1 in counts.values()

        lo, hi, best = 1, n, None
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if exists_unique(mid):
                best = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return best
