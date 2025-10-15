'''
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

 

Example 1:

Input: n = 12
Output: 21
Example 2:

Input: n = 21
Output: -1
 

Constraints:

1 <= n <= 231 - 1
'''

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n_list = list(str(n))  # Convert the integer to a list of its digits
        i = len(n_list) - 2    # Start from the second-last digit

        # Step 1: Find the first digit that is smaller than the digit to its right (from right to left)
        while i >= 0 and n_list[i] >= n_list[i + 1]:
            i -= 1

        # If no such digit exists, the digits are sorted in descending order, so there's no greater permutation
        if i < 0:
            return -1
        
        # Step 2: Find the smallest digit on the right side of i that is greater than n_list[i]
        j = len(n_list) - 1
        while j >= 0 and n_list[j] <= n_list[i]:
            j -= 1
        
        # Step 3: Swap the found digits
        n_list[i], n_list[j] = n_list[j], n_list[i]

        # Step 4: Reverse the order of the digits to the right of position i (to get the smallest lexicographic order)
        left, right = i + 1, len(n_list) - 1
        while left < right:
            n_list[left], n_list[right] = n_list[right], n_list[left] 
            left += 1
            right -=1

        # Step 5: Convert list back to integer, return result if in 32-bit range, else -1
        ans = int("".join(n_list))
        return ans if ans <= 2**31 - 1 else -1 