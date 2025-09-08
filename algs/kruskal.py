def minCostConnectPoints(self, P: List[List[int]]) -> int:
        g = []
        seen = set()
        dsu = DSU(len(P))
        res = []

        idx_map = {(x, y):idx for idx, (x, y) in enumerate(P)}

        for x, y in P:
            for u, v in P:
                if x == u and y == v:
                    continue
                g.append((abs(x - u) + abs(y - v), (x, y), (u, v)))

        g.sort(reverse=True)
        
        while len(res) < len(P) - 1:
            d, p1, p2 = g.pop()

            if dsu.find(idx_map[p1]) != dsu.find(idx_map[p2]):
                res.append(d)
                dsu.union(idx_map[p1], idx_map[p2])

        return sum(res)



class DSU:

    def __init__(self, size):
        self.parents = [idx for idx in range(size)]
        self.rank = [0 for _ in range(size)]
        
    def find(self, i):
        p = self.parents[i]
        while p != self.parents[p]:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
            
        return self.parents[p]
    
    def union(self, i, j):
        i, j = self.find(i), self.find(j)
        
        if i == j: return False
        
        if self.rank[i] > self.rank[j]:
            self.parents[j] = i
            self.rank[i] += self.rank[j]
        else:
            self.parents[i] = j
            self.rank[j] += self.rank[i]
            
        return True
