'''
A DashMart is a warehouse run by DoorDash that houses items found in
convenience stores, grocery stores, and restaurants. We have a city with open
roads, blocked-off roads, and DashMarts.

City planners want you to identify how far a location is from its closest
DashMart.

You can only travel over open roads (up, down, left, right).

Locations are given in [row, col] format.

Example:

[
# 0 1 2 3 4 5 6 7 8
['X', ' ', ' ', 'D', ' ', ' ', 'X', ' ', 'X'], # 0
['X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', 'X'], # 1
[' ', ' ', ' ', 'D', 'X', 'X', ' ', 'X', ' '], # 2
[' ', ' ', ' ', 'D', ' ', 'X', ' ', ' ', ' '], # 3
[' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X'], # 4
[' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X', 'X'] # 5
]

' ' represents an open road that you can travel over in any direction (up, down, left, or right).
'X' represents an blocked road that you cannot travel through.
'D' represents a DashMart.

# list of pairs [row, col]
locations = [
[2, 2],
[4, 0],
[0, 4],
[2, 6],
]

answer = [1, 4, 1, 5]

Implement Function:
- get_closest_dashmart(city, locations)

Provided:
- city: List[str]
- locations: List[List[int]]

Return:
- answer: List[int]
'''

from typing import List

class Solution:
    def get_closest_dashmart(self, city: List[List[str]], locations: List[List[int]]) -> List[int]:
        from collections import deque
        ROWS, COLS = len(city), len(city[0])
        queue = deque()
        dist = [[-1 for _ in range(COLS)] for _ in range(ROWS)]

        # Enqueue all DashMart locations, set their distance to 0
        for r in range(ROWS):
            for c in range(COLS):
                if city[r][c] == 'D':
                    queue.append((r, c))
                    dist[r][c] = 0

        # BFS explores only from open roads or DashMarts, never through 'X'
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        while queue:
            r, c = queue.popleft()
            if city[r][c] == 'X':
                continue
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                # Can only enter open road cells, and those not yet visited
                if 0 <= nr < ROWS and 0 <= nc < COLS and dist[nr][nc] == -1:
                    queue.append((nr, nc))
                    dist[nr][nc] = dist[r][c] + 1

        # For each query, return distance or 0 if it's a DashMart itself
        result = []
        for r, c in locations:
            if city[r][c] == 'D':
                result.append(0)
            else:
                result.append(dist[r][c])
        return result


if __name__ == "__main__":
    solution = Solution()
    city = [
        ['X', ' ', ' ', 'D', ' ', ' ', 'X', ' ', 'X'],
        ['X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', 'X'],
        [' ', ' ', ' ', 'D', 'X', 'X', ' ', 'X', ' '],
        [' ', ' ', ' ', 'D', ' ', 'X', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X'],
        [' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X', 'X']
    ]
    locations = [[2, 2], [4, 0], [0, 4], [2, 6], [1, 8]]
    print(solution.get_closest_dashmart(city, locations))
    assert solution.get_closest_dashmart(city, locations) == [1, 4, 1, 5, 6]