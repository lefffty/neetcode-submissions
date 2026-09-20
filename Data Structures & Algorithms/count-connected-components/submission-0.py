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


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        disjoint_set = DisjointSet(n)
        for x, y in edges:
            disjoint_set.union(x, y)
        return disjoint_set._sets_count