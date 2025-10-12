'''
You are given an n x n grid representing a field of cherries, each cell is one of three possible integers.

0 means the cell is empty, so you can pass through,
1 means the cell contains a cherry that you can pick up and pass through, or
-1 means the cell contains a thorn that blocks your way.
Return the maximum number of cherries you can collect by following the rules below:

Starting at the position (0, 0) and reaching (n - 1, n - 1) by moving right or down through valid path cells (cells with value 0 or 1).
After reaching (n - 1, n - 1), returning to (0, 0) by moving left or up through valid path cells.
When passing through a path cell containing a cherry, you pick it up, and the cell becomes an empty cell 0.
If there is no valid path between (0, 0) and (n - 1, n - 1), then no cherries can be collected.
'''

from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        '''
        Notice after t steps, each position (r, c) we could be, is on the line r + c = t. 
        So if we have two people at positions (r1, c1) and (r2, c2), 
        then r2 = r1 + c1 - c2. That means the variables r1, c1, c2 uniquely determine 2 
        people who have walked the same r1 + c1 number of steps. This sets us up for 
        dynamic programming quite nicely.

        It corresponds to the 4 possibilities for persons 1 and 2 moving down and right:

Person 1 down and person 2 down: dp[r1 + 1][c1][c2];
Person 1 right and person 2 down: dp[r1][c1 + 1][c2];
Person 1 down and person 2 right: dp[r1 + 1][c1][c2 + 1];
Person 1 right and person 2 right: dp[r1][c1 + 1][c2 + 1];

        '''
        n = len(grid)
        memo = [[[None] * n for _ in range(n)] for _ in range(n)]

        def dp(r1, c1, c2):
            r2 = r1 + c1 - c2
            if r1 == n or r2 == n or c1 == n or c2 == n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            if r1 == r2 == c1 == c2 == n-1:
                return grid[r1][c1]
            if memo[r1][c1][c2] is not None:
                return memo[r1][c1][c2]
            
            ans = grid[r1][c1] + (c1 != c2) * grid[r2][c2]
            ans += max(dp(r1 + 1, c1, c2), 
                        dp(r1, c1 + 1, c2),
                        dp(r1 + 1, c1, c2 + 1),
                        dp(r1, c1 + 1, c2 + 1))
            
            memo[r1][c1][c2] = ans
            return ans

        return max(0, dp(0, 0, 0))

if __name__ == "__main__":
    # Patch List for the Solution class
    Solution.__annotations__ = {'grid': list}

    # Example test cases
    test_cases = [
        (
            [[0,1,-1],[1,0,-1],[1,1,1]],
            5
        ),
        (
            [[1,1,-1],[1,-1,1],[-1,1,1]],
            0
        ),
        (
            [[1,1,1],[1,-1,1],[1,1,1]],
            8
        ),
    ]
    sol = Solution()
    for i, (grid, expected) in enumerate(test_cases):
        result = sol.cherryPickup([row[:] for row in grid])
        print(f"Test case {i+1}: result={result}, expected={expected}, pass={result==expected}")