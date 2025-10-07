class Solution:
    def minCostConnectPoints(self, P: List[List[int]]) -> int:
        n = len(P)
        seen = set()

        h = [[0, P[0]]]
        heapify(h)

        res = 0

        while len(seen) < n:

            cost, (x, y) = heappop(h)

            if (x, y) in seen:
                continue
            else:
                seen.add((x, y))
                res += cost

            for (u, v) in P:
                c = abs(x - u) + abs(y - v)
                heappush(h, (c, (u, v)))

        return res
