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
