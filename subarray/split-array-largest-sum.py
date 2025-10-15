'''
410. Split Array Largest Sum

Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.

 
'''
from typing import List

class Solution:
    # Time: O(n^2k)
    # Space: O(nk)
    def splitArrayRecursionWithMemo(self, nums: List[int], k: int) -> int:
        # Top-down dynamic programming
        n = len(nums)   
        memo = {}
        def recurse(i, k):
            if (i, k) in memo:
                return memo[(i, k)]
            if k == 1:
                return sum(nums[i:])
            if i == n:
                return float('inf')
            res = float('inf')
            for j in range(i, n):
                res = min(res, max(sum(nums[i:j]), recurse(j, k-1)))
            memo[(i, k)] = res
            return res
        return recurse(0, k)

    # Time: O(n^2k)
    # Space: O(nk)
    def splitArrayBottomUp(self, nums: List[int], k: int) -> int:
        # Bottom-up dynamic programming
        n = len(nums)
        dp = [[float('inf')] * (k+1) for _ in range(n+1)]  # dp[start_idx][groups_left]
        dp[n][0] = 0
        for start_idx in range(n-1, -1, -1):
            for groups_left in range(1, k+1):
                for split_point in range(start_idx, n):
                    left_sum = sum(nums[start_idx:split_point])
                    right_min_largest = dp[split_point][groups_left-1]
                    dp[start_idx][groups_left] = min(dp[start_idx][groups_left], max(left_sum, right_min_largest))
        return dp[0][k]

    # Time: O(nlog(sum(nums)))
    # Space: O(1)
    def splitArrayBinarySearch(self, nums: List[int], k: int) -> int:
        # Binary search
        n = len(nums)
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if self.canSplit(nums, k, mid):
                right = mid
            else:
                left = mid + 1
        return left

    def canSplit(self, nums: List[int], k: int, mid: int) -> bool:
        count = 0
        currSum = 0
        for num in nums:
            currSum += num
            if currSum > mid:
                count += 1
                currSum = num
        return count + 1 <= k