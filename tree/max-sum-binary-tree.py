'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
'''

import math
from typing import Optional
from tree_utils import TreeNode

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -math.inf
        
        def helper(node): 
            nonlocal ans
            if not node:
                return 0

            left = max(0, helper(node.left)) # max(0, ...) is to handle the case where the left or right subtree is negative
            right = max(0, helper(node.right)) # max(0, ...) is to handle the case where the left or right subtree is negative

            ans = max(ans, left + right + node.val) # global variable

            # path that starts at the current node and extends to one of its subtrees
            return node.val + max(left, right) 

        helper(root)
        return ans