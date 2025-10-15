from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(nodes):
    """
    Build a binary tree from a list of values (level-order traversal).
    None values denote missing nodes.
    Returns the root TreeNode.
    """
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    q = deque([root])
    idx = 1
    while q and idx < len(nodes):
        node = q.popleft()
        if idx < len(nodes) and nodes[idx] is not None:
            node.left = TreeNode(nodes[idx])
            q.append(node.left)
        idx += 1
        if idx < len(nodes) and nodes[idx] is not None:
            node.right = TreeNode(nodes[idx])
            q.append(node.right)
        idx += 1
    return root
