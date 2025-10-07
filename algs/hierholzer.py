def findItinerary(self, T: List[List[str]]) -> List[str]:
        g = defaultdict(list)

        for f, t in T:
            heappush(g[f], t)

        stack = ["JFK"]
        res = []

        while stack:

            while g[stack[-1]]:
                adj = heappop(g[stack[-1]])
                stack.append(adj)

            res.append(stack.pop())

        return res[::-1]
