'''
https://leetcode.com/problems/count-nodes-with-the-highest-score/description/

There is a binary tree rooted at 0 consisting of n nodes. The nodes are labeled from 0 to n - 1. You are given a 0-indexed integer array parents representing the tree, where parents[i] is the parent of node i. Since node 0 is the root, parents[0] == -1.

Each node has a score. To find the score of a node, consider if the node and the edges connected to it were removed. The tree would become one or more non-empty subtrees. The size of a subtree is the number of the nodes in it. The score of the node is the product of the sizes of all those subtrees.

Return the number of nodes that have the highest score.
'''

from typing import List
import collections
from collections import Counter


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        # build graph
        graph = collections.defaultdict(list)

        for i, parent in enumerate(parents):
            graph[parent].append(i)
        
        n = len(parents)
        memo = Counter()

        def count_nodes(node):
            prod, sum = 1, 0
            for child in graph[node]:
                num = count_nodes(child) # count the # of nodes in each child
                prod *= num
                sum += num
            
            prod *= max(1, n - 1 - sum)
            memo[prod] += 1 #
            return sum + 1

        count_nodes(0)

        return memo[max(memo.keys())]