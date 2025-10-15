'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 '''

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i in range(len(nums)):
            if i > reach:
                return False
            reach = max(reach, i+nums[i])
        return True

'''
You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        curr = 0 # the farthest position reachable at the current step or WIHTIN the CURRENT jump
        farthest = 0  # tracks the end of the current jump range

        for i in range(len(nums) - 1):
            curr = max(curr, i + nums[i]) # calculates the farthest point reachable at each step
            
            if i == farthest: # the current jump range is exhausted,
                count += 1
                farthest = max(farthest, curr)
            print(curr, farthest, count)

        return count
