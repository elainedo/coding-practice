from collections import defaultdict


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        indegree = [0 for _ in range(n)]
        max_duration = [0 for _ in range(n)]
        for c1, c2 in relations:
            graph[c1-1].append(c2-1)
            indegree[c2-1] += 1
        queue = deque()
        for vertex in range(n):
            if indegree[vertex] == 0:
                queue.append(vertex)
                max_duration[vertex] = time[vertex]

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                max_duration[neighbor] = max(max_duration[neighbor], max_duration[node] + time[neighbor])
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return max(max_duration)
