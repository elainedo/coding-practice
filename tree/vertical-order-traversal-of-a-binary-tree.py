'''
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

'''

from collections import defaultdict, deque
from typing import List, Optional
from tree_utils import TreeNode, build_tree

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        min_col, max_col = 0, 0
        q = deque()
        q.append((root, 0)) # node, col 
        dct = defaultdict(list)

        while q:
            n = len(q)
            level = defaultdict(list)

            for i in range(n):
                node, col = q.popleft()
                level[col].append(node.val)

                min_col = min(col, min_col)
                max_col = max(col, max_col)

                if node.left:
                    q.append((node.left, col - 1))
                if node.right:
                    q.append((node.right, col + 1))

            for k in level.keys():
                level[k].sort() # sort by values
                dct[k].extend(level[k])

        ans = []
        
        for i in range(min_col, max_col + 1): #
            ans.append(dct[i])
        
        return ans

if __name__ == "__main__":
    # Test 1: Basic Tree
    root = build_tree([3,9,20,None,None,15,7])
    res = Solution().verticalTraversal(root)
    print("Test 1:", res)
    assert res == [[9],[3,15],[20],[7]]

    # Test 2: Two nodes at same (row, col), test sorting
    root = build_tree([1,2,3,4,5,6,7])
    res = Solution().verticalTraversal(root)
    print("Test 2:", res)
    assert res == [[4],[2],[1,5,6],[3],[7]]

    # Test 3: Empty tree
    root = build_tree([])
    res = Solution().verticalTraversal(root)
    print("Test 3:", res)
    assert res == []

    # Test 4: Left-skewed tree
    root = build_tree([1,2,None,3,None,4,None])
    res = Solution().verticalTraversal(root)
    print("Test 4:", res)
    assert res == [[4],[3],[2],[1]]

    # Test 5: Right-skewed tree
    root = build_tree([1,None,2,None,3,None,4])
    res = Solution().verticalTraversal(root)
    print("Test 5:", res)
    assert res == [[1],[2],[3],[4]]
