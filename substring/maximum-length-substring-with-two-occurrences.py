'''
3090. Maximum Length Substring With Two Occurrences

Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.
 

Example 1:

Input: s = "bcbbbcba"

Output: 4

Explanation:

The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
Example 2:

Input: s = "aaaa"

Output: 2

Explanation:

The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".
 

Constraints:

2 <= s.length <= 100
s consists only of lowercase English letters.
'''

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left, right = 0, 0
        n = len(s)
        count = defaultdict(int)
        max_len = 0

        while right < n:
            count[s[right]] += 1
            while left < n and count[s[right]] > 2:
                count[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len
