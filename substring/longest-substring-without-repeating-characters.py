from collections import defaultdict

class Solution:
    '''
    Given a string s, find the length of the longest substring without repeating characters.

    Example 1:

    Input: s = "abcabcbb"
    Output: 3

    Example 2:

    Input: s = "bbbbb"
    Output: 1
    '''

    # Two pointers
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = defaultdict(int)
        max_len = 0
        left = 0
        for right, character in enumerate(s):
            if character in last_seen:
                left = max(left, last_seen[character]+1)
            max_len = max(max_len, right-left+1)
            last_seen[character] = right
        return max_len

if __name__ == "__main__":
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))
