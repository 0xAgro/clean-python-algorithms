class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        k = 1

        rank = [ord(c) for c in s]
        tmp = [0] * n
        sa = list(range(n))
        
        while True:
            sa.sort(key=lambda x: (rank[x], rank[x + k] if x + k < n else -1))
            
            tmp[sa[0]] = 0
            for i in range(1, n):
                prev = sa[i-1]
                curr = sa[i]
                tmp[curr] = tmp[prev] + (rank[curr] != rank[prev] or
                                        (rank[curr + k] if curr + k < n else -1) != (rank[prev + k] if prev + k < n else -1))
            rank[:] = tmp[:]
            
            if max(rank) == n - 1:
                break
            k <<= 1 
        
        return s[sa[-1]:]
