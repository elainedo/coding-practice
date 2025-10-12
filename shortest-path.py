from collections import deque

def shortest_path_to_end(matrix):
    m, n = len(matrix), len(matrix[0])
    DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Directions: right, left, down, up

    # Queue for BFS and parent tracking
    queue = deque()
    parent = [[None for _ in range(n)] for _ in range(m)]

    # Add all valid points in the first row to the queue
    for j in range(n):
        if matrix[0][j] == '1':
            queue.append((0, j))  # (row, column)
            parent[0][j] = (-1, -1)  # Mark as visited and track parent

    # Perform BFS
    end_point = None
    while queue:
        x, y = queue.popleft()

        # Check if we reached the last row
        if x == m - 1:
            end_point = (x, y)
            break

        # Explore neighbors
        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] == '1' and parent[nx][ny] is None:
                parent[nx][ny] = (x, y)  # Track the parent
                queue.append((nx, ny))

    # If no path exists, return None or an empty matrix
    if end_point is None:
        return [[0] * n for _ in range(m)]

    result_matrix = [[0 for _ in range(n)] for _ in range(m)]

    # Backtrack to mark the shortest path
    x, y = end_point
    while (x, y) != (-1, -1):
        result_matrix[x][y] = '1'  # Mark the path
        x, y = parent[x][y]

    return result_matrix


# Example usage
matrix = [
    ['1', '0', '0', '1', '0'],
    ['1', '0', '1', '1', '0'],
    ['0', '1', '1', '0', '0'],
    ['0', '1', '1', '0', '0']
]

result = shortest_path_to_end(matrix)
for row in result:
    print(row)