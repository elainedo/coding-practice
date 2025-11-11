'''
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

'''
from collections import deque
from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q = deque()
        m, n = len(rooms), len(rooms[0])
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))

        dirs = [[0,1], [1,0], [0,-1], [-1,0]]

        while q:
            x, y = q.popleft()
            d = rooms[x][y]

            for dx, dy in dirs:
                nx, ny = dx + x, dy + y
                if 0 <= nx < m and 0 <= ny < n and rooms[nx][ny] == 2147483647:
                    q.append((nx, ny))
                    rooms[nx][ny] = d + 1