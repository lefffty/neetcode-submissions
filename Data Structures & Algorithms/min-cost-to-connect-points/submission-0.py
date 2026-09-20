from collections import deque


class DisjointSet:
    def __init__(self, n: int):
        self._parent = list(range(n))
        self._rank = [0] * n
        self._sets_count = n

    def _find(self, x):
        if self._parent[x] != x:
            self._parent[x] = self._find(self._parent[x])
        return self._parent[x]

    def union(self, x: int, y: int):
        x_root = self._find(x)
        y_root = self._find(y)

        if x_root == y_root:
            return False

        if self._rank[x_root] < self._rank[y_root]:
            self._parent[x_root] = y_root
        elif self._rank[y_root] < self._rank[x_root]:
            self._parent[y_root] = x_root
        else:
            self._parent[x_root] = y_root
            self._rank[y_root] += 1

        self._sets_count -= 1
        return True

    def is_connected(self, x, y):
        return self._find(x) == self._find(y)


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = [
            (i, j, (abs(points[i][0] - points[j][0])) + abs(points[i][1] - points[j][1]))
            for i in range(len(points) - 1)
            for j in range(i + 1, len(points))
        ]
        edges.sort(key=lambda x: x[2])

        mst_edges = deque()
        min_cost = 0
        disjoint_set = DisjointSet(len(points))
        for u, v, weight in edges:
            if disjoint_set.union(u, v):
                mst_edges.append((u, v, weight))
                min_cost += weight

                if len(mst_edges) == len(points) - 1:
                    break

        return min_cost
